"""Testes dos scripts partilhados. Correm sem rede, sobre as fixtures."""

import importlib.util
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SCRIPTS = RAIZ / 'partilhado' / 'scripts'
FIXTURES = Path(__file__).resolve().parent / 'fixtures'


def carregar(nome):
    especificacao = importlib.util.spec_from_file_location(nome, SCRIPTS / f'{nome}.py')
    modulo = importlib.util.module_from_spec(especificacao)
    especificacao.loader.exec_module(modulo)
    return modulo


def correr(script, *argumentos):
    processo = subprocess.run(
        [sys.executable, str(SCRIPTS / script), *argumentos],
        capture_output=True, text=True, check=False,
    )
    return processo.returncode, processo.stdout


class ExtrairSinaisPagina(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        modulo = carregar('extrair_sinais_pagina')
        html = (FIXTURES / 'viatura.html').read_text(encoding='utf-8')
        cls.r = modulo.analisar_html(html, 'https://stand-exemplo.pt/viaturas/peugeot-308-sw-2021?ref=x')

    def test_cabeca(self):
        self.assertTrue(self.r['titulo'].startswith('Peugeot 308 SW'))
        self.assertEqual(self.r['idioma'], 'pt-PT')
        self.assertEqual(self.r['meta_robots'], 'index, follow')
        self.assertEqual(self.r['canonico'], 'https://stand-exemplo.pt/viaturas/peugeot-308-sw-2021')
        self.assertEqual([h['idioma'] for h in self.r['hreflang']], ['pt-PT', 'en'])
        self.assertEqual(self.r['h1'], ['Peugeot 308 SW 1.5 BlueHDi'])
        self.assertEqual(self.r['open_graph']['title'], 'Peugeot 308 SW 2021')

    def test_json_ld_resume_viatura_e_stand(self):
        por_tipo = {tuple(n['tipo']): n['campos'] for n in self.r['json_ld']}
        carro = por_tipo[('Car', 'Product')]
        self.assertEqual(carro['brand'], 'Peugeot')
        self.assertEqual(carro['mileageFromOdometer'], {'value': 62000, 'unitCode': 'KMT'})
        self.assertEqual(carro['offers']['priceCurrency'], 'EUR')
        self.assertEqual(por_tipo[('AutoDealer',)]['address']['addressLocality'], 'Leiria')
        self.assertIn('chaves', por_tipo[('BreadcrumbList',)])
        self.assertTrue(any('JSON-LD inválido' in a for a in self.r['avisos']))

    def test_etiquetas(self):
        e = self.r['etiquetas']
        self.assertEqual(e['ga4'], ['G-ABC123DEF4'])
        self.assertEqual(e['gtm'], ['GTM-AB12CD'])
        self.assertEqual(e['google_ads'], ['AW-123456789'])
        self.assertTrue(e['consent_mode'])
        self.assertEqual(e['cmp'], ['Cookiebot'])
        self.assertIn('Botão WhatsApp', e['chat'])

    def test_contactos_formularios_imagens(self):
        self.assertEqual(self.r['contactos']['telefones'], ['+351244000000'])
        self.assertEqual(self.r['contactos']['emails'], ['vendas@stand-exemplo.pt'])
        self.assertEqual(len(self.r['contactos']['whatsapp']), 1)
        formulario = self.r['formularios'][0]
        self.assertEqual(formulario['accao'], 'https://stand-exemplo.pt/contacto')
        self.assertEqual([c['nome'] for c in formulario['campos']], ['nome', 'telefone', 'mensagem', 'marketing'])
        self.assertEqual(formulario['caixas_pre_seleccionadas'], ['marketing'])
        self.assertEqual(self.r['imagens'], {'total': 3, 'sem_alt': 1, 'alt_vazio': 1})

    def test_terceiros_exclui_o_proprio_dominio(self):
        self.assertEqual(self.r['scripts_terceiros'], ['consent.cookiebot.com', 'googletagmanager.com'])

    def test_linha_de_comandos_com_ficheiro(self):
        codigo, saida = correr('extrair_sinais_pagina.py', str(FIXTURES / 'viatura.html'))
        self.assertEqual(codigo, 0)
        self.assertEqual(json.loads(saida)['h1'], ['Peugeot 308 SW 1.5 BlueHDi'])


class VerificarBotsIa(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = carregar('verificar_bots_ia')
        cls.texto = (FIXTURES / 'robots.txt').read_text(encoding='utf-8')

    def estado(self, agente, caminho):
        bots, _ = self.m.avaliar(self.texto, [caminho])
        bot = next(b for b in bots if b['agente'] == agente)
        return bot['caminhos'][caminho], bot['regra_aplicada'][caminho]

    def test_grupo_proprio_ganha_ao_geral(self):
        self.assertEqual(self.estado('GPTBot', '/viaturas'), ('bloqueado', 'Disallow: /'))
        self.assertEqual(self.estado('OAI-SearchBot', '/viaturas'), ('permitido', 'sem regra'))

    def test_varios_agentes_no_mesmo_grupo(self):
        self.assertEqual(self.estado('Google-Extended', '/')[0], 'bloqueado')
        self.assertEqual(self.estado('CCBot', '/')[0], 'bloqueado')

    def test_regra_mais_longa_e_crawl_delay_nao_fecha_o_grupo(self):
        self.assertEqual(self.estado('ClaudeBot', '/admin/x'), ('bloqueado', 'Disallow: /admin'))
        self.assertEqual(self.estado('ClaudeBot', '/admin/publico/a'), ('permitido', 'Allow: /admin/publico'))

    def test_curingas(self):
        self.assertEqual(self.estado('PerplexityBot', '/viaturas?filtro=diesel')[0], 'bloqueado')
        self.assertEqual(self.estado('PerplexityBot', '/ficha.pdf')[0], 'bloqueado')
        self.assertEqual(self.estado('PerplexityBot', '/ficha.pdf?v=2')[0], 'permitido')

    def test_empate_favorece_allow(self):
        self.assertEqual(self.m.decidir([('disallow', '/a'), ('allow', '/a')], '/a'), (True, 'Allow: /a'))

    def test_sitemaps(self):
        _, sitemaps = self.m.avaliar(self.texto, ['/'])
        self.assertEqual(sitemaps, ['https://stand-exemplo.pt/sitemap.xml'])

    def test_robots_vazio_permite_tudo(self):
        bots, _ = self.m.avaliar('', ['/'])
        self.assertTrue(all(b['caminhos']['/'] == 'permitido' for b in bots))

    def test_linha_de_comandos_com_robots_local(self):
        codigo, saida = correr('verificar_bots_ia.py', 'https://stand-exemplo.pt',
                               '--robots', str(FIXTURES / 'robots.txt'), '--caminho', '/viaturas')
        self.assertEqual(codigo, 0)
        resultado = json.loads(saida)
        self.assertEqual(resultado['robots']['interpretacao'], 'ficheiro local')
        self.assertNotIn('acesso', resultado)


class ValidarLlmsTxt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = carregar('validar_llms_txt')

    def test_ficheiro_valido(self):
        r = self.m.validar_texto((FIXTURES / 'llms-valido.txt').read_text(encoding='utf-8'))
        self.assertTrue(r['valido'], r['erros'])
        self.assertEqual(r['titulo'], 'Stand Exemplo')
        self.assertEqual(r['total_links'], 10)
        self.assertEqual(r['avisos'], [])

    def test_ficheiro_invalido(self):
        r = self.m.validar_texto((FIXTURES / 'llms-invalido.txt').read_text(encoding='utf-8'))
        self.assertFalse(r['valido'])
        erros = ' '.join(r['erros'])
        self.assertIn('primeira linha', erros)
        self.assertIn('2 H1', erros)
        self.assertIn('não absoluto', erros)
        avisos = ' '.join(r['avisos'])
        for esperado in ('item sem ligação', 'citação de resumo', 'parâmetros de campanha', 'sem descrição', 'repetido', '"Vazia"'):
            self.assertIn(esperado, avisos)

    def test_linha_de_comandos_devolve_1_se_invalido(self):
        codigo, _ = correr('validar_llms_txt.py', str(FIXTURES / 'llms-invalido.txt'))
        self.assertEqual(codigo, 1)


class ClassificarReferenciasIa(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = carregar('classificar_referencias_ia')

    def test_agrupa_motores_e_ignora_taxas(self):
        r = self.m.analisar((FIXTURES / 'ga4.csv').read_text(encoding='utf-8'))
        self.assertEqual(r['coluna_origem'], 'Origem da sessão')
        self.assertEqual(r['metricas'], ['Sessões', 'Sessões envolvidas', 'Eventos-chave'])
        self.assertEqual([m['motor'] for m in r['motores']], ['ChatGPT', 'Perplexity', 'Gemini', 'Copilot'])
        self.assertEqual(r['motores'][0]['metricas']['Sessões'], 30)
        self.assertEqual(r['nao_classificadas_amostra'][0]['origem'], 'google')

    def test_classificar(self):
        self.assertEqual(self.m.classificar('chat.openai.com / referral'), 'ChatGPT')
        self.assertEqual(self.m.classificar('m.facebook.com'), None)
        self.assertEqual(self.m.classificar('meta.ai'), 'Meta AI')
        self.assertEqual(self.m.classificar('cometa.ai'), None)

    def test_regex_apanha_os_motores(self):
        padrao = re.compile(self.m.regex_ga4())
        for origem in ('chatgpt.com', 'perplexity.ai', 'gemini.google.com', 'claude.ai', 'copilot.microsoft.com'):
            self.assertRegex(origem, padrao)
        self.assertNotRegex('google', padrao)

    def test_coluna_inexistente(self):
        with self.assertRaises(ValueError):
            self.m.analisar('Página,Vistas\n/,10\n')


if __name__ == '__main__':
    unittest.main()
