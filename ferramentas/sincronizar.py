#!/usr/bin/env python3
"""Copia os scripts de partilhado/scripts para as skills que os usam.

Uso:
  python3 ferramentas/sincronizar.py

Os destinos estão em partilhado/destinos.json. Cada skill leva a sua cópia
porque tem de funcionar instalada sozinha; ferramentas/validar.py falha se
uma cópia divergir da fonte.
"""

import json
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def main():
    destinos = json.loads((RAIZ / 'partilhado' / 'destinos.json').read_text(encoding='utf-8'))
    copiados = 0
    for script, skills in destinos.items():
        fonte = RAIZ / 'partilhado' / 'scripts' / script
        conteudo = fonte.read_bytes()
        for skill in skills:
            pasta = RAIZ / 'skills' / skill
            if not pasta.is_dir():
                print(f'{skill}: a skill não existe', file=sys.stderr)
                return 1
            destino = pasta / 'scripts' / script
            destino.parent.mkdir(exist_ok=True)
            if not destino.exists() or destino.read_bytes() != conteudo:
                shutil.copy2(fonte, destino)
                copiados += 1
    print(f'{copiados} cópia(s) actualizada(s).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
