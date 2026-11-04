# llms.txt de [nome do stand]

| Campo | Valor |
|---|---|
| Site | [URL canónico] |
| Data | [AAAA-MM-DD] |
| Modo | [criar de raiz / rever o existente] |
| Acesso à web | [sim: URLs abertos um a um / não: URLs dados pelo gestor, por confirmar] |
| Responsável pelo ficheiro | [nome ou função] |

## 1. A resolver antes de publicar

[Primeiro os bloqueios: agentes de pesquisa ou de pedido do utilizador
bloqueados no robots.txt, robots.txt em erro, `/llms.txt` bloqueado. Depois
os URLs com problema.]

| URL ou regra | Problema | O que fazer | Quem |
|---|---|---|---|
| | | | |

**Por confirmar pelo gestor:** [factos do resumo e das descrições que não
foram verificados no site; URLs dados sem acesso à web]

## 2. Páginas consideradas

| URL | Estado HTTP | Decisão (dentro / Optional / fora) | Motivo |
|---|---|---|---|
| | | | |

Páginas que fazem falta no site: [por exemplo, retoma sem página própria;
fica a sugestão, nunca um URL inventado]

## 3. O ficheiro

```markdown
[o llms.txt completo, sem comentários dentro do ficheiro]
```

Validação do rascunho (`validar_llms_txt.py --verificar-links`): [valido,
n.º de erros, avisos mantidos e porquê, ligações com problema]

## 4. Publicar

- Caminho: `[URL canónico]/llms.txt`
- Resposta esperada: 200, `content-type` `text/plain` ou `text/markdown`, `charset=utf-8`
- Como, nesta plataforma: [painel de alojamento ou FTP / pedido por escrito ao fornecedor do site / limitação do construtor de sites]
- Não é preciso declarar no robots.txt nem no sitemap.

## 5. Verificar depois de publicar

```text
python3 scripts/validar_llms_txt.py [URL]/llms.txt --verificar-links
python3 scripts/verificar_bots_ia.py [URL]/llms.txt --caminho /llms.txt --testar-acesso
```

- [ ] responde 200 com o content-type certo
- [ ] acentos legíveis no navegador
- [ ] nenhuma ligação em `links_com_problema`
- [ ] `/llms.txt` permitido aos agentes de pesquisa e de pedido do utilizador

## 6. Manutenção

Rever quando mudar um URL da lista, abrir ou fechar um serviço, mudar o
nome, a morada ou o telefone, ou o site mudar de plataforma. Verificar as
ligações de três em três meses.

Próxima revisão: [AAAA-MM-DD]

## 7. O que este ficheiro não faz

Não garante citações nem indexação, e nenhum grande motor documentou que o
usa para escolher fontes. Não substitui o robots.txt, o sitemap, os dados
estruturados nem o texto das páginas.
