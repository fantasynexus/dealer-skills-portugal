#!/usr/bin/env python3
"""Valida um llms.txt contra o formato de llmstxt.org e as regras das skills.

Uso:
  python3 validar_llms_txt.py https://stand-exemplo.pt/llms.txt
  python3 validar_llms_txt.py llms.txt
  python3 validar_llms_txt.py https://stand-exemplo.pt/llms.txt --verificar-links

Verifica o H1, a citação de resumo, as secções H2, o formato das linhas de
ligação (`- [nome](url): descrição`), URLs absolutos, duplicados, parâmetros
de campanha, o número de ligações e, quando lê do site, o estado HTTP e o
content-type. Com --verificar-links pede cada ligação e aponta as que não
respondem 200 ou redireccionam.

Um llms.txt válido ajuda a descoberta; não garante citações nem indexação.
Só biblioteca padrão.
"""

import argparse
import json
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen

UA = 'Mozilla/5.0 (compatible; dealer-skills-portugal)'
LINHA_LIGACAO = re.compile(r'^\s*[-*]\s+\[([^\]]+)\]\(([^)\s]+)\)\s*(?::\s*(.*))?$')
PARAMETROS_CAMPANHA = ('utm_', 'gclid', 'fbclid', 'msclkid', 'mc_cid')
MINIMO_LIGACOES, MAXIMO_LIGACOES = 10, 30


def validar_texto(texto):
    erros, avisos = [], []
    linhas = texto.splitlines()
    conteudo = [(n, l) for n, l in enumerate(linhas, start=1) if l.strip()]

    titulo, resumo = None, None
    h1 = [(n, l) for n, l in conteudo if re.match(r'^#\s+\S', l)]
    if not conteudo or not re.match(r'^#\s+\S', conteudo[0][1]):
        erros.append('A primeira linha com conteúdo tem de ser o H1 com o nome do stand.')
    if h1:
        titulo = h1[0][1].lstrip('#').strip()
    if len(h1) > 1:
        erros.append(f'Há {len(h1)} H1; o formato só admite um (linhas {", ".join(str(n) for n, _ in h1)}).')

    citacao = [l for _, l in conteudo if l.lstrip().startswith('>')]
    if citacao:
        resumo = ' '.join(l.lstrip()[1:].strip() for l in citacao)
    else:
        avisos.append('Falta a citação de resumo (> uma frase factual sobre o stand).')

    seccoes, actual = [], None
    vistos, total = {}, 0
    for numero, linha in conteudo:
        if re.match(r'^##\s+\S', linha):
            actual = {'titulo': linha.lstrip('#').strip(), 'links': 0}
            seccoes.append(actual)
            continue
        if actual is None or not re.match(r'^\s*[-*]\s+', linha):
            continue
        procura = LINHA_LIGACAO.match(linha)
        if not procura:
            # O formato pede ligações nas listas das secções H2; os leitores saltam o resto.
            avisos.append(f'Linha {numero}: item sem ligação numa secção H2; o formato espera `- [nome](url): descrição`.')
            continue
        nome, url, descricao = procura.groups()
        total += 1
        actual['links'] += 1
        partes = urlparse(url)
        if partes.scheme not in ('http', 'https') or not partes.netloc:
            erros.append(f'Linha {numero}: URL não absoluto ({url}).')
        elif partes.scheme == 'http':
            avisos.append(f'Linha {numero}: URL em http, não https ({url}).')
        if any(p.startswith(PARAMETROS_CAMPANHA) for p in parse_qs(partes.query)):
            avisos.append(f'Linha {numero}: URL com parâmetros de campanha ({url}).')
        if not (descricao or '').strip():
            avisos.append(f'Linha {numero}: ligação "{nome}" sem descrição.')
        chave = url.rstrip('/')
        if chave in vistos:
            avisos.append(f'Linha {numero}: URL repetido (já na linha {vistos[chave]}).')
        else:
            vistos[chave] = numero

    if not seccoes:
        erros.append('Não há secções H2 com ligações.')
    for seccao in seccoes:
        if not seccao['links']:
            avisos.append(f'A secção "{seccao["titulo"]}" não tem ligações.')
    if total and not MINIMO_LIGACOES <= total <= MAXIMO_LIGACOES:
        avisos.append(f'{total} ligações; as skills recomendam entre {MINIMO_LIGACOES} e {MAXIMO_LIGACOES} de alto valor.')

    dominios = {urlparse(u).hostname for u in vistos}
    if len(dominios) > 1:
        avisos.append(f'Ligações para {len(dominios)} domínios: confirmar que os externos são do stand ou oficiais.')

    return {
        'valido': not erros,
        'erros': erros,
        'avisos': avisos,
        'titulo': titulo,
        'resumo': resumo,
        'seccoes': seccoes,
        'total_links': total,
        'urls': list(vistos),
    }


def _estado(url):
    for metodo in ('HEAD', 'GET'):
        try:
            resposta = urlopen(Request(url, method=metodo, headers={'User-Agent': UA}), timeout=15)
            return resposta.getcode(), resposta.geturl()
        except HTTPError as erro:
            if metodo == 'HEAD' and erro.getcode() in (403, 405, 501):
                continue
            return erro.getcode(), url
    return None, url


def verificar_links(urls):
    problemas = []
    for url in urls:
        try:
            estado, final = _estado(url)
        except (URLError, OSError) as erro:
            problemas.append({'url': url, 'motivo': str(erro)})
            continue
        if estado != 200:
            problemas.append({'url': url, 'estado_http': estado})
        elif final.rstrip('/') != url.rstrip('/'):
            problemas.append({'url': url, 'estado_http': estado, 'motivo': f'redirecciona para {final}'})
    return problemas


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('alvo', help='URL do llms.txt ou caminho de um ficheiro')
    parser.add_argument('--verificar-links', action='store_true', help='pedir cada ligação e apontar as que falham')
    args = parser.parse_args(argv)

    origem = {}
    if re.match(r'https?://', args.alvo, re.I):
        try:
            resposta = urlopen(Request(args.alvo, headers={'User-Agent': UA}), timeout=15)
        except HTTPError as erro:
            print(json.dumps({'alvo': args.alvo, 'valido': False, 'estado_http': erro.getcode(),
                              'erros': [f'O llms.txt respondeu {erro.getcode()}.']}, ensure_ascii=False, indent=2))
            return 1
        except (URLError, OSError) as erro:
            print(json.dumps({'alvo': args.alvo, 'erro': str(erro)}, ensure_ascii=False, indent=2))
            return 1
        tipo = resposta.headers.get('content-type', '')
        origem = {'estado_http': resposta.getcode(), 'content_type': tipo, 'url_final': resposta.geturl()}
        texto = resposta.read(1_000_000).decode('utf-8', 'replace')
    else:
        with open(args.alvo, encoding='utf-8', errors='replace') as ficheiro:
            texto = ficheiro.read()

    resultado = {'alvo': args.alvo, **origem, **validar_texto(texto)}
    tipo = origem.get('content_type', '')
    if tipo and not tipo.startswith(('text/plain', 'text/markdown')):
        resultado['avisos'].append(f'Content-type {tipo}; esperado text/plain ou text/markdown.')
    if args.verificar_links:
        resultado['links_com_problema'] = verificar_links(resultado['urls'])
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 0 if resultado['valido'] else 1


if __name__ == '__main__':
    sys.exit(main())
