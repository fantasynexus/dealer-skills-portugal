#!/usr/bin/env python3
"""Extrai de uma página os sinais que as auditorias de um stand precisam.

Uso:
  python3 extrair_sinais_pagina.py https://stand-exemplo.pt/viaturas/123
  python3 extrair_sinais_pagina.py pagina.html

Escreve JSON no stdout: título, descrição, robots, canónico, hreflang, H1,
JSON-LD resumido, Open Graph, contactos, formulários, imagens sem alt,
etiquetas de medição e consentimento, scripts de terceiros.

Não executa JavaScript. O que o site injecta depois de carregar (muitos
widgets de chat, tags disparadas pelo GTM, JSON-LD montado no browser) não
aparece aqui: a ausência de um sinal é "não visto no HTML", não "não existe".
Só biblioteca padrão. Não envia nada a terceiros além do pedido à página.
"""

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

UA_OMISSAO = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/130.0 Safari/537.36 dealer-skills-portugal'
)
LIMITE_BYTES = 5_000_000

# Tipos de JSON-LD que interessam a um stand e os campos que se resumem.
TIPOS_RESUMIDOS = {
    'car', 'vehicle', 'motorizedbicycle', 'product', 'offer', 'aggregateoffer',
    'autodealer', 'autorepair', 'localbusiness', 'organization', 'store',
}

CMPS = {
    'Cookiebot': r'consent\.cookiebot\.(com|eu)|cookiebot',
    'OneTrust': r'cdn\.cookielaw\.org|otSDKStub|onetrust',
    'CookieYes': r'cdn-cookieyes\.com|cookieyes',
    'Didomi': r'sdk\.privacy-center\.org|didomi',
    'Complianz': r'complianz',
    'iubenda': r'iubenda\.com',
    'Usercentrics': r'usercentrics\.(eu|com)',
    'Termly': r'termly\.io',
    'Axeptio': r'axeptio',
    'CookieFirst': r'cookiefirst\.com',
    'Cookie Script': r'cookie-script\.com',
    'CookieHub': r'cookiehub\.(net|eu)',
    'Borlabs Cookie': r'borlabs-cookie',
    'Klaro': r'klaro(\.min)?\.js',
}

RASTREIO_CHAMADAS = {
    'CallRail': r'cdn\.callrail\.com|callrail',
    'CallTrackingMetrics': r'tctm\.co|calltrackingmetrics',
    'Invoca': r'invoca\.net|invocacdn',
}

CHAT = {
    'Tawk.to': r'embed\.tawk\.to',
    'Intercom': r'widget\.intercom\.io|intercomcdn',
    'Crisp': r'client\.crisp\.chat',
    'Zendesk': r'static\.zdassets\.com|zopim',
    'HubSpot': r'js\.hs-scripts\.com|js\.usemessages\.com',
    'Tidio': r'code\.tidio\.co',
    'LiveChat': r'cdn\.livechatinc\.com',
    'Smartsupp': r'smartsuppchat\.com',
    'Botão WhatsApp': r'wa\.me/|api\.whatsapp\.com/send|whatsapp://send',
}


class Recolha(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.idioma = None
        self.titulo = ''
        self._no_titulo = False
        self.meta = {}
        self.open_graph = {}
        self.canonico = None
        self.hreflang = []
        self.h1 = []
        self._h1_profundidade = 0
        self._h1_texto = []
        self.json_ld = []
        self._no_json_ld = False
        self._json_ld_texto = []
        self.scripts_src = []
        self.scripts_texto = []
        self._no_script = False
        self.ligacoes = []
        self.formularios = []
        self._form = None
        self.imagens_total = 0
        self.imagens_sem_alt = 0
        self.imagens_alt_vazio = 0

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or '') for k, v in attrs}
        if tag == 'html' and a.get('lang'):
            self.idioma = a['lang']
        elif tag == 'title':
            self._no_titulo = True
        elif tag == 'meta':
            nome = (a.get('name') or '').lower()
            propriedade = (a.get('property') or '').lower()
            if nome:
                self.meta[nome] = a.get('content', '')
            if propriedade.startswith('og:'):
                self.open_graph[propriedade[3:]] = a.get('content', '')
        elif tag == 'link':
            rel = (a.get('rel') or '').lower().split()
            if 'canonical' in rel:
                self.canonico = a.get('href')
            if 'alternate' in rel and a.get('hreflang'):
                self.hreflang.append({'idioma': a['hreflang'], 'url': a.get('href')})
        elif tag == 'h1':
            self._h1_profundidade += 1
        elif tag == 'br' and self._h1_profundidade:
            self._h1_texto.append(' ')
        elif tag == 'script':
            tipo = (a.get('type') or '').lower()
            if tipo == 'application/ld+json':
                self._no_json_ld = True
                self._json_ld_texto = []
            else:
                self._no_script = True
                if a.get('src'):
                    self.scripts_src.append(a['src'])
        elif tag == 'a' and a.get('href'):
            self.ligacoes.append(a['href'])
        elif tag == 'form':
            self._form = {
                'accao': a.get('action', ''),
                'metodo': (a.get('method') or 'get').lower(),
                'campos': [],
                'caixas_pre_seleccionadas': [],
            }
        elif tag in ('input', 'select', 'textarea') and self._form is not None:
            tipo = (a.get('type') or ('text' if tag == 'input' else tag)).lower()
            if tipo in ('hidden', 'submit', 'button', 'image', 'reset'):
                return
            campo = {
                'nome': a.get('name') or a.get('id') or '',
                'tipo': tipo,
                'obrigatorio': 'required' in a or a.get('aria-required') == 'true',
            }
            self._form['campos'].append(campo)
            if tipo == 'checkbox' and 'checked' in a:
                self._form['caixas_pre_seleccionadas'].append(campo['nome'])
        elif tag == 'img':
            self.imagens_total += 1
            if 'alt' not in a:
                self.imagens_sem_alt += 1
            elif not a['alt'].strip():
                self.imagens_alt_vazio += 1

    def handle_endtag(self, tag):
        if tag == 'title':
            self._no_titulo = False
        elif tag == 'h1' and self._h1_profundidade:
            self._h1_profundidade -= 1
            if not self._h1_profundidade:
                self.h1.append(' '.join(''.join(self._h1_texto).split()))
                self._h1_texto = []
        elif tag == 'script':
            if self._no_json_ld:
                self.json_ld.append(''.join(self._json_ld_texto))
            self._no_json_ld = False
            self._no_script = False
        elif tag == 'form' and self._form is not None:
            self.formularios.append(self._form)
            self._form = None

    def handle_data(self, data):
        if self._no_titulo:
            self.titulo += data
        if self._h1_profundidade:
            self._h1_texto.append(data)
        if self._no_json_ld:
            self._json_ld_texto.append(data)
        elif self._no_script:
            self.scripts_texto.append(data)


def _tipos(no):
    tipo = no.get('@type')
    if isinstance(tipo, list):
        return [str(t) for t in tipo]
    return [str(tipo)] if tipo else []


def _nos(dados):
    """Aplana listas e @graph num iterável de objectos JSON-LD."""
    if isinstance(dados, list):
        for item in dados:
            yield from _nos(item)
    elif isinstance(dados, dict):
        if '@graph' in dados:
            yield from _nos(dados['@graph'])
        if '@type' in dados:
            yield dados


def _texto(valor):
    if isinstance(valor, dict):
        return valor.get('name') or valor.get('@id') or valor.get('value')
    if isinstance(valor, list):
        return [_texto(v) for v in valor]
    return valor


def _resumir_oferta(oferta):
    if isinstance(oferta, list):
        return [_resumir_oferta(o) for o in oferta]
    if not isinstance(oferta, dict):
        return oferta
    return {k: oferta.get(k) for k in (
        '@type', 'price', 'lowPrice', 'highPrice', 'priceCurrency', 'availability', 'url',
    ) if oferta.get(k) is not None}


def resumir_no(no):
    campos = {}
    if any(t.lower() in TIPOS_RESUMIDOS for t in _tipos(no)):
        for chave in (
            'name', 'brand', 'manufacturer', 'model', 'vehicleModelDate', 'modelDate',
            'productionDate', 'vehicleConfiguration', 'fuelType', 'vehicleTransmission',
            'bodyType', 'color', 'numberOfPreviousOwners', 'vehicleIdentificationNumber',
            'telephone', 'email', 'url', 'priceRange', 'sku',
        ):
            if no.get(chave) is not None:
                campos[chave] = _texto(no[chave])
        if isinstance(no.get('mileageFromOdometer'), dict):
            km = no['mileageFromOdometer']
            campos['mileageFromOdometer'] = {'value': km.get('value'), 'unitCode': km.get('unitCode')}
        if no.get('offers') is not None:
            campos['offers'] = _resumir_oferta(no['offers'])
        if isinstance(no.get('address'), dict):
            morada = no['address']
            campos['address'] = {k: morada.get(k) for k in (
                'streetAddress', 'postalCode', 'addressLocality', 'addressRegion', 'addressCountry',
            ) if morada.get(k)}
        if no.get('aggregateRating') is not None:
            campos['aggregateRating'] = no['aggregateRating']
    else:
        campos['chaves'] = sorted(k for k in no if not k.startswith('@'))
    return {'tipo': _tipos(no), 'campos': campos}


def _dominio(url):
    host = (urlparse(url).hostname or '').lower()
    return host[4:] if host.startswith('www.') else host


def _encontrar(padroes, texto):
    return sorted(nome for nome, padrao in padroes.items() if re.search(padrao, texto, re.I))


def analisar_html(html, url_base=None):
    recolha = Recolha()
    recolha.feed(html)
    recolha.close()
    avisos = []

    json_ld = []
    for indice, bloco in enumerate(recolha.json_ld, start=1):
        try:
            dados = json.loads(bloco)
        except ValueError:
            avisos.append(f'JSON-LD inválido no bloco {indice}: o Google ignora-o inteiro.')
            continue
        json_ld.extend(resumir_no(no) for no in _nos(dados))

    scripts = '\n'.join(recolha.scripts_texto + recolha.scripts_src)
    etiquetas = {
        'ga4': sorted(set(re.findall(r'\bG-[A-Z0-9]{8,12}\b', scripts))),
        'gtm': sorted(set(re.findall(r'\bGTM-[A-Z0-9]{5,8}\b', scripts))),
        'google_ads': sorted(set(re.findall(r'\bAW-\d{6,12}\b', scripts))),
        'meta_pixel': sorted(set(re.findall(r"fbq\(\s*['\"]init['\"]\s*,\s*['\"](\d{8,20})", scripts))),
        'consent_mode': bool(re.search(r"gtag\(\s*['\"]consent['\"]", scripts)),
        'cmp': _encontrar(CMPS, scripts),
        'rastreio_chamadas': _encontrar(RASTREIO_CHAMADAS, scripts),
        'chat': _encontrar(CHAT, scripts + '\n' + '\n'.join(recolha.ligacoes)),
    }
    if 'connect.facebook.net' in scripts and not etiquetas['meta_pixel']:
        avisos.append('Script da Meta presente sem ID de pixel visível no HTML.')

    telefones, emails, whatsapp = set(), set(), set()
    for href in recolha.ligacoes:
        baixo = href.lower()
        if baixo.startswith('tel:'):
            telefones.add(href[4:].strip())
        elif baixo.startswith('mailto:'):
            emails.add(href[7:].split('?')[0].strip())
        elif re.search(r'wa\.me/|api\.whatsapp\.com/send|whatsapp://', baixo):
            whatsapp.add(href)

    dominio_pagina = _dominio(url_base) if url_base else ''
    terceiros = set()
    for src in recolha.scripts_src:
        absoluto = urljoin(url_base or '', src)
        dominio = _dominio(absoluto)
        if dominio and dominio != dominio_pagina and not dominio.endswith('.' + dominio_pagina):
            terceiros.add(dominio)

    for formulario in recolha.formularios:
        if url_base and formulario['accao']:
            formulario['accao'] = urljoin(url_base, formulario['accao'])
        if formulario['caixas_pre_seleccionadas']:
            avisos.append('Formulário com caixas pré-seleccionadas: confirmar se alguma é consentimento.')

    if not recolha.titulo.strip():
        avisos.append('Sem <title>.')
    if len(recolha.h1) != 1:
        avisos.append(f'{len(recolha.h1)} H1 na página.')
    if not recolha.canonico:
        avisos.append('Sem link canónico.')

    return {
        'titulo': ' '.join(recolha.titulo.split()),
        'meta_descricao': recolha.meta.get('description'),
        'meta_robots': recolha.meta.get('robots'),
        'canonico': urljoin(url_base, recolha.canonico) if url_base and recolha.canonico else recolha.canonico,
        'idioma': recolha.idioma,
        'hreflang': recolha.hreflang,
        'h1': recolha.h1,
        'json_ld': json_ld,
        'open_graph': recolha.open_graph,
        'contactos': {
            'telefones': sorted(telefones),
            'emails': sorted(emails),
            'whatsapp': sorted(whatsapp),
        },
        'formularios': recolha.formularios,
        'imagens': {
            'total': recolha.imagens_total,
            'sem_alt': recolha.imagens_sem_alt,
            'alt_vazio': recolha.imagens_alt_vazio,
        },
        'etiquetas': etiquetas,
        'scripts_terceiros': sorted(terceiros),
        'avisos': avisos,
    }


def _descodificar(corpo, content_type=''):
    procura = re.search(r'charset=([\w-]+)', content_type or '', re.I)
    codificacao = procura.group(1) if procura else 'utf-8'
    if not procura:
        no_html = re.search(rb'<meta[^>]+charset=["\']?([\w-]+)', corpo[:4096], re.I)
        if no_html:
            codificacao = no_html.group(1).decode('ascii', 'ignore')
    try:
        return corpo.decode(codificacao, errors='replace')
    except LookupError:
        return corpo.decode('utf-8', errors='replace')


def obter(alvo, user_agent):
    if not re.match(r'https?://', alvo, re.I):
        with open(alvo, 'rb') as ficheiro:
            return {'url': None, 'estado_http': None, 'cabecalhos': {}}, _descodificar(ficheiro.read())
    pedido = Request(alvo, headers={
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'pt-PT,pt;q=0.9,en;q=0.5',
    })
    try:
        resposta = urlopen(pedido, timeout=20)
    except HTTPError as erro:
        resposta = erro
    cabecalhos = {
        chave: resposta.headers.get(chave)
        for chave in ('content-type', 'x-robots-tag', 'cache-control', 'server', 'content-language')
        if resposta.headers.get(chave)
    }
    corpo = resposta.read(LIMITE_BYTES)
    meta = {'url': resposta.geturl(), 'estado_http': resposta.getcode(), 'cabecalhos': cabecalhos}
    return meta, _descodificar(corpo, cabecalhos.get('content-type', ''))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('alvo', help='URL da página ou caminho de um ficheiro HTML')
    parser.add_argument('--user-agent', default=UA_OMISSAO, help='user agent do pedido')
    args = parser.parse_args(argv)
    try:
        meta, html = obter(args.alvo, args.user_agent)
    except (URLError, OSError, ValueError) as erro:
        print(json.dumps({'alvo': args.alvo, 'erro': str(erro)}, ensure_ascii=False, indent=2))
        return 1
    resultado = {**meta, **analisar_html(html, meta['url'] or None)}
    if meta['estado_http'] and meta['estado_http'] >= 400:
        resultado['avisos'].insert(0, f"A página respondeu {meta['estado_http']}.")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
