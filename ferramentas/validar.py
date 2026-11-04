#!/usr/bin/env python3
"""Valida a biblioteca: estrutura das skills, ligações, copy e cópias dos scripts.

Uso:
  python3 ferramentas/validar.py

Sai com 1 e a lista de problemas (ficheiro:linha) quando alguma regra falha.
As regras estão no AGENTS.md; cada verificação abaixo diz qual guarda.
"""

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SKILLS = RAIZ / 'skills'
PARTILHADO = RAIZ / 'partilhado' / 'scripts'
ROUTER = 'stand-por-onde-comecar'
MAX_LINHAS_SKILL = 200
EXTENSOES_TEXTO = {'.md', '.yaml', '.yml', '.json', '.py', '.txt', '.csv', '.html'}
EXCLUIDOS = {'THIRD_PARTY_NOTICES.md', 'LICENSE'}
TRAVESSAO = '\u2014'

# Formas do Acordo de 1990 ou do português do Brasil que a casa escreve de outra
# maneira. Palavras inteiras, para "informação" não cair em "ação".
PALAVRAS_PROIBIDAS = {
    r'aç(ão|ões)': 'acção',
    r'atua(l|is|lmente)': 'actual',
    r'atualiz\w*': 'actualizar',
    r'atua(r|m|ção|ções|do|da)': 'actuar',
    r'ativ(o|a|os|as|ar|ação|ado|ada|amente|idade|idades)': 'activo',
    r'objetiv\w*': 'objectivo',
    r'elétric\w*|eletrific\w*': 'eléctrico',
    r'proteç(ão|ões)': 'protecção',
    r'corret(o|a|os|as|amente)|correç(ão|ões)': 'correcto',
    r'exat(o|a|os|as|amente|idão)': 'exacto',
    r'direç(ão|ões)|diret(o|a|os|as|amente|or|ora|ores|ório|órios)': 'direcção',
    r'seleç(ão|ões)|coleç(ão|ões)': 'selecção',
    r'adot\w*|adoç(ão|ões)': 'adoptar',
    r'efetiv\w*': 'efectivo',
    r'ótim(o|a|os|as)|otimiz\w*|ótic\w*': 'óptimo',
    r'projet\w*': 'projecto',
    r'receç(ão|ões)': 'recepção',
    r'perspetiv\w*': 'perspectiva',
    r'infraç(ão|ões)|reaç(ão|ões)|transaç(ão|ões)|interaç(ão|ões)|inspeç(ão|ões)|redaç(ão|ões)': 'acção',
    r'deteç(ão|ões)|detet\w*': 'detectar',
    r'fatur\w*': 'factura',
    r'setor(es)?': 'sector',
    r'contat\w*': 'contacto',
    r'usuári\w*': 'utilizador',
    r'registr(o|os|ar|ado|ada|ados|adas)': 'registo',
    r'equipe(s)?': 'equipa',
    r'celular(es)?': 'telemóvel',
    r'planilha\w*': 'folha de cálculo',
    r'cadastr\w*': 'registo',
}
GRAFIA = re.compile(r'\b(' + '|'.join(PALAVRAS_PROIBIDAS) + r')\b', re.I)


class Relatorio:
    def __init__(self):
        self.problemas = []

    def erro(self, caminho, mensagem, linha=None):
        relativo = caminho.relative_to(RAIZ) if isinstance(caminho, Path) else caminho
        sitio = f'{relativo}:{linha}' if linha else str(relativo)
        self.problemas.append(f'{sitio}: {mensagem}')


def ler_frontmatter(texto):
    if not texto.startswith('---\n'):
        return None, texto
    fim = texto.find('\n---', 4)
    if fim == -1:
        return None, texto
    campos, chave = {}, None
    for linha in texto[4:fim].splitlines():
        procura = re.match(r'^([a-z_-]+):\s*(.*)$', linha)
        if procura:
            chave, valor = procura.groups()
            campos[chave] = '' if valor in ('>', '|', '>-', '|-') else valor.strip().strip('"\'')
        elif chave and linha.startswith((' ', '\t')):
            campos[chave] = (campos[chave] + ' ' + linha.strip()).strip()
    return campos, texto[fim + 4:]


def ficheiros_texto():
    for caminho in sorted(RAIZ.rglob('*')):
        partes = caminho.relative_to(RAIZ).parts
        if caminho.is_file() and partes[0] != '.git' and '__pycache__' not in partes \
                and caminho.suffix in EXTENSOES_TEXTO and caminho.name not in EXCLUIDOS:
            yield caminho


def validar_skill(pasta, nomes, r):
    skill_md = pasta / 'SKILL.md'
    if not skill_md.exists():
        r.erro(pasta, 'falta SKILL.md')
        return
    texto = skill_md.read_text(encoding='utf-8')
    campos, corpo = ler_frontmatter(texto)
    if campos is None:
        r.erro(skill_md, 'falta o frontmatter entre linhas ---')
        return
    nome, descricao = campos.get('name', ''), campos.get('description', '')
    if nome != pasta.name:
        r.erro(skill_md, f'name "{nome}" diferente da pasta "{pasta.name}"')
    if not re.fullmatch(r'stand-[a-z0-9]+(-[a-z0-9]+)*', nome) or len(nome) > 64:
        r.erro(skill_md, 'name tem de começar por stand-, em minúsculas e hífens, até 64 caracteres')
    if not descricao:
        r.erro(skill_md, 'description vazia')
    elif len(descricao) > 1024:
        r.erro(skill_md, f'description com {len(descricao)} caracteres; máximo 1024')
    if '<' in descricao or '>' in descricao:
        r.erro(skill_md, 'description não pode ter < nem >')
    linhas = corpo.count('\n')
    if linhas > MAX_LINHAS_SKILL:
        r.erro(skill_md, f'{linhas} linhas no corpo; máximo {MAX_LINHAS_SKILL}, o detalhe vai para references/')

    yaml = pasta / 'agents' / 'openai.yaml'
    if not yaml.exists():
        r.erro(pasta, 'falta agents/openai.yaml')
    else:
        conteudo = yaml.read_text(encoding='utf-8')
        for chave in ('display_name', 'short_description', 'default_prompt'):
            if not re.search(rf'^\s+{chave}:\s*\S', conteudo, re.M):
                r.erro(yaml, f'falta {chave}')
        if f'${pasta.name}' not in conteudo:
            r.erro(yaml, f'default_prompt tem de invocar ${pasta.name}')

    for md in sorted(pasta.rglob('*.md')):
        em_bloco = False
        for numero, linha in enumerate(md.read_text(encoding='utf-8').splitlines(), start=1):
            if linha.lstrip().startswith('```'):
                em_bloco = not em_bloco
            # Exemplos em código (`- [nome](url)`, blocos de llms.txt) não são ligações deste repo.
            prosa = '' if em_bloco else re.sub(r'`[^`]*`', '', linha)
            for alvo in re.findall(r'\]\(([^)\s]+)\)', prosa):
                if re.match(r'(https?:|mailto:|tel:|#)', alvo):
                    continue
                if not (md.parent / alvo.split('#')[0]).exists():
                    r.erro(md, f'ligação para {alvo}, que não existe', numero)
            for script in re.findall(r'\bscripts/([a-z0-9_]+\.py)', linha):
                if not (pasta / 'scripts' / script).exists():
                    r.erro(md, f'cita scripts/{script}, que esta skill não tem', numero)
            for citado in re.findall(r'`\$?(stand-[a-z0-9-]+)`', linha) + re.findall(r'\$(stand-[a-z0-9-]+)', linha):
                if citado not in nomes:
                    r.erro(md, f'cita a skill {citado}, que não existe', numero)


def validar_scripts(nomes, r):
    destinos_json = RAIZ / 'partilhado' / 'destinos.json'
    destinos = json.loads(destinos_json.read_text(encoding='utf-8'))
    esperados = set()
    for script, skills in destinos.items():
        fonte = PARTILHADO / script
        if not fonte.exists():
            r.erro(destinos_json, f'{script} não existe em partilhado/scripts')
            continue
        for skill in skills:
            if skill not in nomes:
                r.erro(destinos_json, f'destino {skill} não é uma skill')
                continue
            copia = SKILLS / skill / 'scripts' / script
            esperados.add(copia)
            if not copia.exists() or copia.read_bytes() != fonte.read_bytes():
                r.erro(copia, 'cópia em falta ou diferente da fonte; correr ferramentas/sincronizar.py')
    for copia in SKILLS.glob('*/scripts/*'):
        if copia.is_file() and copia not in esperados:
            r.erro(copia, 'script fora de partilhado/destinos.json')


def validar_router(nomes, r):
    pasta = SKILLS / ROUTER
    if not pasta.exists():
        r.erro(SKILLS, f'falta a skill {ROUTER}')
        return
    texto = '\n'.join(p.read_text(encoding='utf-8') for p in pasta.rglob('*.md'))
    for nome in sorted(nomes - {ROUTER}):
        if f'`{nome}`' not in texto:
            r.erro(pasta, f'não encaminha para `{nome}`')


def validar_copy(r):
    for caminho in ficheiros_texto():
        for numero, linha in enumerate(caminho.read_text(encoding='utf-8').splitlines(), start=1):
            if TRAVESSAO in linha:
                r.erro(caminho, 'travessão (U+2014): usar dois pontos, vírgula ou parênteses', numero)
            if caminho.suffix == '.py' or caminho.parent.name == 'fixtures':
                continue
            # Dentro de `código` a palavra é citada, não escrita (listas "evitar: `contato`").
            for achado in GRAFIA.finditer(re.sub(r'`[^`]*`', '', linha)):
                r.erro(caminho, f'grafia "{achado.group(1)}": a casa escreve pré-Acordo e PT-PT', numero)


def validar_raiz(nomes, r):
    readme = RAIZ / 'README.md'
    for numero, linha in enumerate(readme.read_text(encoding='utf-8').splitlines(), start=1):
        for contagem in re.findall(r'\b(\d+) skills\b', linha):
            if int(contagem) != len(nomes):
                r.erro(readme, f'diz {contagem} skills; há {len(nomes)}', numero)
    for nome in ('marketplace.json', 'plugin.json'):
        caminho = RAIZ / '.claude-plugin' / nome
        try:
            json.loads(caminho.read_text(encoding='utf-8'))
        except (OSError, ValueError) as erro:
            r.erro(caminho, f'JSON inválido ou em falta: {erro}')


def validar_catalogo(nomes, r):
    sys.path.insert(0, str(RAIZ / 'ferramentas'))
    import catalogo

    listados = catalogo.todos_os_nomes()
    antes = len(r.problemas)
    for nome in sorted(nomes - set(listados)):
        r.erro(RAIZ / 'ferramentas' / 'catalogo.py', f'{nome} não está em CATEGORIAS')
    for nome in sorted(set(listados) - nomes):
        r.erro(RAIZ / 'ferramentas' / 'catalogo.py', f'{nome} está em CATEGORIAS mas não existe')
    for nome in sorted({n for n in listados if listados.count(n) > 1}):
        r.erro(RAIZ / 'ferramentas' / 'catalogo.py', f'{nome} aparece em mais de uma categoria')
    if len(r.problemas) > antes:
        return
    try:
        if catalogo.README.read_text(encoding='utf-8') != catalogo.readme_gerado():
            r.erro(catalogo.README, 'catálogo desactualizado; correr ferramentas/catalogo.py')
        if not catalogo.CATALOGO_ROUTER.exists() or \
                catalogo.CATALOGO_ROUTER.read_text(encoding='utf-8') != catalogo.catalogo_router():
            r.erro(catalogo.CATALOGO_ROUTER, 'catálogo desactualizado; correr ferramentas/catalogo.py')
    except (OSError, ValueError, AttributeError) as erro:
        r.erro(catalogo.README, f'não consegui gerar o catálogo: {erro}')


def main():
    r = Relatorio()
    pastas = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    nomes = {p.name for p in pastas}
    for pasta in pastas:
        validar_skill(pasta, nomes, r)
    validar_scripts(nomes, r)
    validar_router(nomes, r)
    validar_copy(r)
    validar_raiz(nomes, r)
    validar_catalogo(nomes, r)
    if r.problemas:
        print('\n'.join(r.problemas))
        print(f'\n{len(r.problemas)} problema(s) em {len(nomes)} skills.')
        return 1
    print(f'{len(nomes)} skills válidas.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
