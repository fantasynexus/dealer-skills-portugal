#!/usr/bin/env python3
"""Agrupa por motor de IA as origens de tráfego de uma exportação do GA4.

Uso:
  python3 classificar_referencias_ia.py exportacao.csv
  python3 classificar_referencias_ia.py exportacao.csv --coluna-origem "Origem da sessão"
  python3 classificar_referencias_ia.py exportacao.csv --metricas "Sessões,Eventos-chave"
  python3 classificar_referencias_ia.py --regex

Lê o CSV que o GA4 exporta (ignora as linhas de comentário com `#` no topo),
encontra a coluna de origem ou de referenciador, classifica cada linha num
motor de IA e soma as métricas numéricas. Mostra as maiores origens que não
classificou, para apanhar motores novos. Com --regex escreve a expressão para
um grupo de canais personalizado no GA4.

O que isto não vê: visitas de IA que chegam sem referenciador (contam como
directo), AI Overviews e AI Mode da Google (chegam como google / organic) e
crawlers, que não executam o JavaScript do GA4. Só biblioteca padrão.
"""

import argparse
import csv
import io
import json
import re
import sys

LISTA_REVISTA_EM = '2026-11'

# Domínios (ou tokens de utm_source) por motor. Casam como sufixo de host:
# `meta.ai` apanha `www.meta.ai` mas não `cometa.ai`.
MOTORES = [
    ('ChatGPT', ['chatgpt.com', 'chat.openai.com', 'chatgpt']),
    ('Perplexity', ['perplexity.ai', 'perplexity']),
    ('Gemini', ['gemini.google.com', 'bard.google.com']),
    ('Copilot', ['copilot.microsoft.com', 'copilot.cloud.microsoft', 'edgeservices.bing.com']),
    ('Claude', ['claude.ai']),
    ('Mistral', ['chat.mistral.ai']),
    ('DeepSeek', ['chat.deepseek.com', 'deepseek.com']),
    ('Meta AI', ['meta.ai']),
    ('Grok', ['grok.com']),
    ('You.com', ['you.com']),
]

COLUNAS_ORIGEM = [
    'origem da sessão', 'session source', 'origem/meio da sessão', 'session source / medium',
    'referenciador da página', 'page referrer', 'origem', 'source', 'origem/meio', 'source / medium',
    'primeira origem do utilizador', 'first user source',
]


def regex_ga4():
    dominios = [re.escape(d) for _, lista in MOTORES for d in lista]
    return '.*(' + '|'.join(dominios) + ').*'


def classificar(origem):
    texto = (origem or '').strip().lower()
    for motor, dominios in MOTORES:
        if any(re.search(r'(^|[^a-z0-9-])' + re.escape(d) + r'($|[^a-z0-9-])', texto) for d in dominios):
            return motor
    return None


def _numero(valor):
    texto = (valor or '').strip().replace('\u00a0', '').replace(' ', '').replace('%', '')
    if not texto:
        return None
    if ',' in texto and '.' in texto:
        texto = texto.replace('.', '').replace(',', '.') if texto.rfind(',') > texto.rfind('.') else texto.replace(',', '')
    elif ',' in texto:
        texto = texto.replace(',', '.')
    try:
        return float(texto)
    except ValueError:
        return None


# Taxas, médias e durações não se somam: ficam de fora das métricas automáticas.
NAO_SOMAVEL = re.compile(r'taxa|rate|média|media|average|duração|duration|por sessão|per session|%', re.I)


def _somavel(coluna, linhas):
    if NAO_SOMAVEL.search(coluna):
        return False
    valores = [(l.get(coluna) or '').strip() for l in linhas]
    if any('%' in v or ':' in v for v in valores):
        return False
    numeros = [_numero(v) for v in valores if v]
    return bool(numeros) and None not in numeros


def ler_csv(texto):
    linhas = [l for l in texto.splitlines() if l.strip() and not l.lstrip().startswith('#')]
    if not linhas:
        return [], []
    amostra = '\n'.join(linhas[:5])
    try:
        dialecto = csv.Sniffer().sniff(amostra, delimiters=',;\t')
    except csv.Error:
        dialecto = csv.excel
    leitor = csv.DictReader(io.StringIO('\n'.join(linhas)), dialect=dialecto)
    return leitor.fieldnames or [], list(leitor)


def analisar(texto, coluna_origem=None, metricas=None):
    colunas, linhas = ler_csv(texto)
    if not colunas:
        raise ValueError('CSV vazio.')
    if coluna_origem is None:
        por_nome = {c.strip().lower(): c for c in colunas}
        coluna_origem = next((por_nome[c] for c in COLUNAS_ORIGEM if c in por_nome), None)
    if coluna_origem not in colunas:
        raise ValueError(f'Não encontrei a coluna de origem. Colunas: {", ".join(colunas)}. Usa --coluna-origem.')
    if metricas is None:
        metricas = [c for c in colunas if c != coluna_origem and _somavel(c, linhas)]

    motores, outras = {}, {}
    totais = {m: 0.0 for m in metricas}
    for linha in linhas:
        origem = linha.get(coluna_origem, '')
        valores = {m: _numero(linha.get(m)) or 0.0 for m in metricas}
        for m in metricas:
            totais[m] += valores[m]
        motor = classificar(origem)
        if motor is None:
            somas = outras.setdefault(origem, {m: 0.0 for m in metricas})
        else:
            grupo = motores.setdefault(motor, {'motor': motor, 'origens': set(), 'linhas': 0,
                                               'metricas': {m: 0.0 for m in metricas}})
            grupo['origens'].add(origem)
            grupo['linhas'] += 1
            somas = grupo['metricas']
        for m in metricas:
            somas[m] += valores[m]

    principal = metricas[0] if metricas else None
    resultado_motores = sorted(motores.values(), key=lambda g: -(g['metricas'].get(principal, 0) if principal else g['linhas']))
    for grupo in resultado_motores:
        grupo['origens'] = sorted(grupo['origens'])
        if principal and totais[principal]:
            grupo['quota_' + principal] = round(grupo['metricas'][principal] / totais[principal], 4)
    nao_classificadas = sorted(outras.items(), key=lambda par: -(par[1].get(principal, 0) if principal else 0))[:15]
    return {
        'coluna_origem': coluna_origem,
        'metricas': metricas,
        'linhas_lidas': len(linhas),
        'totais': totais,
        'motores': resultado_motores,
        'nao_classificadas_amostra': [{'origem': o, 'metricas': v} for o, v in nao_classificadas],
        'regex_ga4': regex_ga4(),
        'lista_revista_em': LISTA_REVISTA_EM,
        'limites': [
            'Visitas sem referenciador contam como directo e não aparecem aqui.',
            'AI Overviews e AI Mode da Google chegam como google / organic.',
            'Crawlers não executam o GA4: para eles, usar os logs do servidor ou da CDN.',
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('csv', nargs='?', help='exportação CSV do GA4')
    parser.add_argument('--coluna-origem', help='nome exacto da coluna de origem ou referenciador')
    parser.add_argument('--metricas', help='colunas a somar, separadas por vírgula (omissão: todas as numéricas)')
    parser.add_argument('--regex', action='store_true', help='escrever só a regex para o grupo de canais do GA4')
    args = parser.parse_args(argv)

    if args.regex and not args.csv:
        print(regex_ga4())
        return 0
    if not args.csv:
        parser.error('indica o ficheiro CSV ou usa --regex')
    with open(args.csv, encoding='utf-8-sig', errors='replace') as ficheiro:
        texto = ficheiro.read()
    metricas = [m.strip() for m in args.metricas.split(',')] if args.metricas else None
    try:
        resultado = analisar(texto, args.coluna_origem, metricas)
    except ValueError as erro:
        print(json.dumps({'erro': str(erro)}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
