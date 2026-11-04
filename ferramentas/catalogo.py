#!/usr/bin/env python3
"""Gera o catálogo do README e o de stand-por-onde-comecar a partir das skills.

Uso:
  python3 ferramentas/catalogo.py

A ordem e as categorias vivem aqui, em CATEGORIAS, e em mais lado nenhum
deste repo (o hub tem as suas em shared/skills.ts). O resto vem de cada
skill: o frontmatter do SKILL.md, o agents/openai.yaml e o que a pasta tem.
ferramentas/validar.py falha se o que está escrito não for o que isto gera.
"""

import ast
import functools
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SKILLS = RAIZ / 'skills'
README = RAIZ / 'README.md'
CATALOGO_ROUTER = SKILLS / 'stand-por-onde-comecar' / 'references' / 'catalogo.md'

CATEGORIAS = [
    ('Dia-a-dia', [
        'stand-escrever-anuncio', 'stand-responder-leads', 'stand-responder-avaliacoes',
        'stand-publicar-redes-sociais',
    ]),
    ('Estratégia', [
        'stand-por-onde-comecar', 'stand-estrategia-pesquisa', 'stand-auditoria-prontidao-ia',
        'stand-posicionamento',
    ]),
    ('Pesquisa e IA', [
        'stand-auditoria-aeo', 'stand-visibilidade-ia', 'stand-monitorizar-reputacao-ia',
        'stand-analisar-trafego-ia', 'stand-gerar-llms-txt', 'stand-brief-conteudo-aeo',
    ]),
    ('SEO e presença local', [
        'stand-auditoria-seo', 'stand-auditoria-perfil-google', 'stand-seo-multilingue',
    ]),
    ('Site e conversão', [
        'stand-avaliar-site', 'stand-auditoria-cta', 'stand-rever-anuncios-viaturas',
        'stand-pagina-comparacao',
    ]),
    ('Medição e vendas', [
        'stand-auditoria-ga4-google-ads', 'stand-auditoria-rastreio-chamadas', 'stand-classificar-chamadas',
    ]),
    ('Clientes e reputação', [
        'stand-onboarding-cliente', 'stand-fluxos-email', 'stand-campanha-retoma', 'stand-analisar-avaliacoes',
    ]),
]

MARCAS = {
    'catalogo': ('<!-- catalogo:inicio -->', '<!-- catalogo:fim -->'),
    'scripts': ('<!-- scripts:inicio -->', '<!-- scripts:fim -->'),
}


def _yaml(texto, chave):
    procura = re.search(rf'^\s+{chave}:\s*"?(.*?)"?\s*$', texto, re.M)
    return procura.group(1) if procura else ''


@functools.lru_cache(maxsize=None)
def ler_skill(nome):
    pasta = SKILLS / nome
    texto = (pasta / 'SKILL.md').read_text(encoding='utf-8')
    descricao = re.search(r'^description:\s*(.*)$', texto, re.M).group(1).strip()
    yaml = (pasta / 'agents' / 'openai.yaml').read_text(encoding='utf-8')
    contar = lambda sub, padrao: len(list((pasta / sub).glob(padrao))) if (pasta / sub).is_dir() else 0
    return {
        'nome': nome,
        'titulo': _yaml(yaml, 'display_name'),
        'curta': _yaml(yaml, 'short_description'),
        'pedido': _yaml(yaml, 'default_prompt').replace(f'${nome}', f'`{nome}`'),
        'descricao': descricao,
        'referencias': contar('references', '*.md'),
        'modelos': contar('assets', '*'),
        'scripts': sorted(p.name for p in (pasta / 'scripts').glob('*.py')) if (pasta / 'scripts').is_dir() else [],
    }


def _plural(n, singular, plural):
    return f'{n} {singular if n == 1 else plural}'


def bloco_catalogo():
    linhas = []
    for categoria, nomes in CATEGORIAS:
        linhas += [f'### {categoria}', '', '| Skill | Para quê | Inclui |', '|---|---|---|']
        for skill in map(ler_skill, nomes):
            inclui = []
            if skill['referencias']:
                inclui.append(_plural(skill['referencias'], 'referência', 'referências'))
            if skill['modelos']:
                inclui.append(_plural(skill['modelos'], 'modelo', 'modelos'))
            if skill['scripts']:
                inclui.append(_plural(len(skill['scripts']), 'script', 'scripts'))
            linhas.append(
                f"| [{skill['titulo']}](skills/{skill['nome']}/SKILL.md)<br>`{skill['nome']}` "
                f"| {skill['curta']} | {' · '.join(inclui) or 'só SKILL.md'} |"
            )
        linhas.append('')
    return '\n'.join(linhas).rstrip()


def _primeira_linha_doc(caminho):
    modulo = ast.parse(caminho.read_text(encoding='utf-8'))
    return (ast.get_docstring(modulo) or '').split('\n')[0]


def bloco_scripts():
    destinos = json.loads((RAIZ / 'partilhado' / 'destinos.json').read_text(encoding='utf-8'))
    linhas = ['| Script | O que faz | Skills que o levam |', '|---|---|---|']
    for script, skills in destinos.items():
        resumo = _primeira_linha_doc(RAIZ / 'partilhado' / 'scripts' / script)
        linhas.append(f'| `{script}` | {resumo} | {len(skills)} |')
    return '\n'.join(linhas)


def catalogo_router():
    linhas = [
        '# Catálogo',
        '',
        'Todas as skills da biblioteca, por categoria, com o que fazem e o pedido de exemplo.',
        'Gerado por `ferramentas/catalogo.py` a partir de cada skill: não editar à mão.',
        '',
    ]
    for categoria, nomes in CATEGORIAS:
        linhas += [f'## {categoria}', '']
        for skill in map(ler_skill, nomes):
            linhas += [
                f"### {skill['titulo']} (`{skill['nome']}`)",
                '',
                skill['descricao'],
                '',
                f"Pedido de exemplo: {skill['pedido']}",
                '',
            ]
    return '\n'.join(linhas).rstrip() + '\n'


def substituir(texto, marca, conteudo):
    inicio, fim = MARCAS[marca]
    padrao = re.compile(re.escape(inicio) + r'.*?' + re.escape(fim), re.S)
    if not padrao.search(texto):
        raise ValueError(f'README sem as marcas {inicio} ... {fim}')
    return padrao.sub(lambda _: f'{inicio}\n{conteudo}\n{fim}', texto)


def readme_gerado():
    texto = README.read_text(encoding='utf-8')
    texto = substituir(texto, 'catalogo', bloco_catalogo())
    return substituir(texto, 'scripts', bloco_scripts())


def todos_os_nomes():
    return [nome for _, nomes in CATEGORIAS for nome in nomes]


def main():
    README.write_text(readme_gerado(), encoding='utf-8')
    CATALOGO_ROUTER.write_text(catalogo_router(), encoding='utf-8')
    print(f'Catálogo gerado com {len(todos_os_nomes())} skills.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
