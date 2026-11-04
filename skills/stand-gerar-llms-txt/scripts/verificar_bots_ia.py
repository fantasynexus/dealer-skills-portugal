#!/usr/bin/env python3
"""Diz que agentes de IA o robots.txt de um site deixa entrar, e onde.

Uso:
  python3 verificar_bots_ia.py https://stand-exemplo.pt
  python3 verificar_bots_ia.py https://stand-exemplo.pt --caminho /viaturas --caminho /llms.txt
  python3 verificar_bots_ia.py https://stand-exemplo.pt --robots robots.txt
  python3 verificar_bots_ia.py https://stand-exemplo.pt --testar-acesso

Para cada agente conhecido devolve o fornecedor, a finalidade, se cada
caminho está permitido ou bloqueado e a regra que decidiu. Segue o RFC 9309
(a regra mais longa ganha, em empate ganha o Allow, `*` e `$` contam).

O robots.txt é declarativo: não prova que um bot o respeita nem que visita
o site. Com --testar-acesso pede a página com o user agent de cada bot, para
apanhar bloqueios de firewall ou CDN; um 403 pode querer dizer "bloqueia este
bot" ou "bloqueia quem se faz passar por ele" (o pedido não vem dos IP do
fornecedor). Só biblioteca padrão.
"""

import argparse
import functools
import json
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

LISTA_REVISTA_EM = '2026-11'

# token, fornecedor, finalidade, nota. `so_robots` são tokens sem crawler
# próprio: só existem para o robots.txt, não faz sentido testar o acesso.
BOTS = [
    ('GPTBot', 'OpenAI', 'treino', 'Recolhe conteúdo para treinar modelos.', False),
    ('OAI-SearchBot', 'OpenAI', 'pesquisa', 'Indexa para a pesquisa do ChatGPT. Bloquear tira o site das respostas com fontes.', False),
    ('ChatGPT-User', 'OpenAI', 'pedido do utilizador', 'Abre páginas quando alguém pede ao ChatGPT.', False),
    ('ClaudeBot', 'Anthropic', 'treino', 'Recolhe conteúdo para treinar modelos.', False),
    ('Claude-SearchBot', 'Anthropic', 'pesquisa', 'Indexa para a pesquisa do Claude.', False),
    ('Claude-User', 'Anthropic', 'pedido do utilizador', 'Abre páginas quando alguém pede ao Claude.', False),
    ('PerplexityBot', 'Perplexity', 'pesquisa', 'Indexa para as respostas do Perplexity.', False),
    ('Perplexity-User', 'Perplexity', 'pedido do utilizador', 'Abre páginas quando alguém pede ao Perplexity.', False),
    ('Googlebot', 'Google', 'pesquisa', 'Pesquisa Google, incluindo AI Overviews e AI Mode.', False),
    ('Google-Extended', 'Google', 'treino', 'Só robots.txt: uso no treino e nas respostas do Gemini. Não tira o site das AI Overviews.', True),
    ('Bingbot', 'Microsoft', 'pesquisa', 'Pesquisa Bing, que alimenta o Copilot e outros assistentes.', False),
    ('Applebot', 'Apple', 'pesquisa', 'Siri, Spotlight e Safari.', False),
    ('Applebot-Extended', 'Apple', 'treino', 'Só robots.txt: uso no treino dos modelos da Apple.', True),
    ('CCBot', 'Common Crawl', 'treino', 'Arquivo aberto usado por muitos modelos.', False),
    ('Meta-ExternalAgent', 'Meta', 'treino', 'Recolhe conteúdo para os modelos da Meta.', False),
    ('Meta-ExternalFetcher', 'Meta', 'pedido do utilizador', 'Abre páginas a pedido no Meta AI.', False),
    ('Amazonbot', 'Amazon', 'geral', 'Alexa e outros serviços da Amazon.', False),
    ('Bytespider', 'ByteDance', 'treino', 'Recolhe conteúdo para modelos da ByteDance.', False),
    ('DuckAssistBot', 'DuckDuckGo', 'pesquisa', 'Respostas do DuckAssist.', False),
    ('MistralAI-User', 'Mistral', 'pedido do utilizador', 'Abre páginas a pedido no Le Chat.', False),
]


def ler_grupos(texto):
    """Lê o robots.txt em grupos {agentes, regras}, mais a lista de sitemaps."""
    grupos, sitemaps = [], []
    actual, a_ler_agentes = None, False
    for linha in texto.splitlines():
        linha = linha.split('#', 1)[0].strip()
        if ':' not in linha:
            continue
        campo, valor = (parte.strip() for parte in linha.split(':', 1))
        campo = campo.lower()
        if campo == 'sitemap':
            sitemaps.append(valor)
        elif campo == 'user-agent':
            if not a_ler_agentes:
                actual = {'agentes': [], 'regras': []}
                grupos.append(actual)
            actual['agentes'].append(valor.lower())
            a_ler_agentes = True
        elif campo in ('allow', 'disallow') and actual is not None:
            a_ler_agentes = False
            if valor:
                actual['regras'].append((campo, valor))
        # Outros campos (Crawl-delay, Host...) ignoram-se sem fechar o grupo,
        # como faz o parser da Google.
    return grupos, sitemaps


def regras_para(grupos, token):
    """As regras que se aplicam a um token: o grupo com o nome dele, ou o `*`."""
    token = token.lower()
    proprias = [r for g in grupos if token in g['agentes'] for r in g['regras']]
    if any(token in g['agentes'] for g in grupos):
        return proprias, token
    gerais = [r for g in grupos if '*' in g['agentes'] for r in g['regras']]
    return gerais, '*' if any('*' in g['agentes'] for g in grupos) else None


@functools.lru_cache(maxsize=None)
def _padrao(caminho_regra):
    ancorado = caminho_regra.endswith('$')
    base = caminho_regra[:-1] if ancorado else caminho_regra
    expressao = '.*'.join(re.escape(parte) for parte in base.split('*'))
    return re.compile(expressao + ('$' if ancorado else ''))


def decidir(regras, caminho):
    """Devolve (permitido, regra) segundo o RFC 9309."""
    melhor = None
    for tipo, valor in regras:
        if _padrao(valor).match(caminho):
            chave = (len(valor), tipo == 'allow')
            if melhor is None or chave > melhor[0]:
                melhor = (chave, tipo, valor)
    if melhor is None:
        return True, None
    return melhor[1] == 'allow', f'{melhor[1].capitalize()}: {melhor[2]}'


def avaliar(texto, caminhos):
    grupos, sitemaps = ler_grupos(texto)
    bots = []
    for token, fornecedor, finalidade, nota, _ in BOTS:
        regras, grupo = regras_para(grupos, token)
        por_caminho, regra_aplicada = {}, {}
        for caminho in caminhos:
            permitido, regra = decidir(regras, caminho)
            por_caminho[caminho] = 'permitido' if permitido else 'bloqueado'
            regra_aplicada[caminho] = regra or 'sem regra'
        bots.append({
            'agente': token,
            'fornecedor': fornecedor,
            'finalidade': finalidade,
            'grupo': grupo or 'nenhum',
            'caminhos': por_caminho,
            'regra_aplicada': regra_aplicada,
            'nota': nota,
        })
    return bots, sitemaps


def _pedir(url, user_agent):
    pedido = Request(url, headers={'User-Agent': user_agent})
    try:
        resposta = urlopen(pedido, timeout=15)
    except HTTPError as erro:
        return erro.getcode(), erro.read(500_000).decode('utf-8', 'replace')
    return resposta.getcode(), resposta.read(500_000).decode('utf-8', 'replace')


def testar_acesso(url):
    resultados = []
    for token, fornecedor, _, _, so_robots in BOTS:
        if so_robots:
            continue
        try:
            estado, _ = _pedir(url, f'Mozilla/5.0 (compatible; {token}/1.0)')
        except (URLError, OSError) as erro:
            estado = f'erro: {erro}'
        resultados.append({'agente': token, 'fornecedor': fornecedor, 'estado_http': estado})
    return resultados


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('site', help='URL do site (o robots.txt é lido da raiz)')
    parser.add_argument('--caminho', action='append', help='caminho a verificar; repetir para vários (omissão: /)')
    parser.add_argument('--robots', help='ler o robots.txt de um ficheiro local em vez do site')
    parser.add_argument('--testar-acesso', action='store_true', help='pedir a página com o user agent de cada bot')
    args = parser.parse_args(argv)
    caminhos = args.caminho or ['/']

    url_robots = urljoin(args.site, '/robots.txt')
    robots = {'url': url_robots, 'estado_http': None, 'interpretacao': None}
    if args.robots:
        with open(args.robots, encoding='utf-8', errors='replace') as ficheiro:
            texto = ficheiro.read()
        robots['url'] = args.robots
        robots['interpretacao'] = 'ficheiro local'
    else:
        try:
            estado, texto = _pedir(url_robots, 'Mozilla/5.0 (compatible; dealer-skills-portugal)')
        except (URLError, OSError) as erro:
            estado, texto = None, ''
            robots['erro'] = str(erro)
        robots['estado_http'] = estado
        if estado == 200:
            robots['interpretacao'] = 'lido'
        elif isinstance(estado, int) and 400 <= estado < 500:
            texto = ''
            robots['interpretacao'] = 'inexistente: pelo RFC 9309 tudo está permitido'
        else:
            # Servidor em erro ou inalcançável: o RFC manda tratar como bloqueio total.
            texto = 'User-agent: *\nDisallow: /'
            robots['interpretacao'] = 'inacessível: pelo RFC 9309 os bots devem assumir bloqueio total'

    bots, sitemaps = avaliar(texto, caminhos)
    robots['sitemaps'] = sitemaps
    resultado = {'robots': robots, 'bots': bots, 'lista_revista_em': LISTA_REVISTA_EM}
    if args.testar_acesso:
        resultado['acesso'] = testar_acesso(args.site)
        resultado['nota_acesso'] = (
            'Um 403 ou 429 pode ser bloqueio deliberado do bot ou da imitação: '
            'confirmar na firewall/CDN antes de concluir.'
        )
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
