# AGENTS.md

Biblioteca pública de skills para agentes de IA, para gestores e equipas de
stands de automóveis em Portugal. O catálogo humano está em
[onepilot.app/hub/skills](https://onepilot.app/hub/skills) e é mantido no repo
`fantasynexus/marketing-hub` (`shared/skills.ts`).

## Comandos

```bash
python3 ferramentas/validar.py          # estrutura, frontmatter, ligações, copy, cópias dos scripts
python3 ferramentas/sincronizar.py      # copia partilhado/scripts para as skills que os usam
python3 ferramentas/catalogo.py         # regenera o catálogo do README e do stand-por-onde-comecar
python3 -m unittest discover -s ferramentas/testes
```

Só biblioteca padrão de Python 3.9 ou mais recente. Nada para instalar.

## Como está arrumado

```
skills/<nome>/
  SKILL.md            instruções e limites; é o que o agente lê primeiro
  agents/openai.yaml  nome, descrição curta e pedido de exemplo
  references/         detalhe lido só quando é preciso (grelhas, contexto PT, exemplos)
  assets/             modelos de entrega que o agente preenche
  scripts/            cópias de partilhado/scripts; nunca se editam aqui
partilhado/scripts/   a fonte dos scripts; destinos.json diz que skills levam cada um
ferramentas/          validação, sincronização, catálogo e testes do próprio repo
.claude-plugin/       marketplace e plugin do Claude Code
```

Cada skill é autónoma: tem de funcionar instalada sozinha, sem as outras. É
por isso que um script usado por várias skills existe em várias cópias. A
fonte é `partilhado/scripts/`; `ferramentas/sincronizar.py` copia-a e
`ferramentas/validar.py` falha se uma cópia divergir.

## Escrever uma skill

### Frontmatter

- `name` igual ao nome da pasta, `stand-` no início, minúsculas e hífens.
- `description` até 1024 caracteres, em PT-PT: o que faz e quando usar. É o
  que decide se o agente a activa, por isso nomeia as situações e as palavras
  que um gestor usaria ("anúncio", "Standvirtual", "avaliação no Google").

### Corpo do `SKILL.md`

Curto o suficiente para ler de uma vez (60 a 130 linhas). O detalhe vai para
`references/`, com uma ligação relativa que diga quando o ler:
"Antes de pontuar, lê [references/grelha.md](references/grelha.md)."

Ordem habitual, adaptada ao trabalho:

1. Uma ou duas frases sobre o que a skill faz e o que não faz.
2. **Antes de começar:** o que perguntar, os modos (com acesso, público,
   documental) e o que fazer quando falta informação.
3. **Passos** numerados, cada um com um resultado verificável.
4. **Ferramentas:** scripts incluídos e ferramentas grátis do hub, quando
   servem.
5. **Entrega:** a estrutura do resultado, de preferência com um modelo em
   `assets/`.
6. **Limites:** o que a skill recusa fazer. É isto que a distingue de um
   prompt genérico.

### Regras de conteúdo

- **Português de Portugal, grafia anterior ao Acordo de 1990**, como no resto
  do repo: acção, actual, actualizar, activo, adoptar, colecção, contacto,
  correcto, direcção, efectivo, eléctrico, exacto, objectivo, óptimo,
  projecto, protecção, recepção, selecção.
- **Sem travessões (U+2014)**: usar dois pontos, vírgula ou parênteses. O
  validador falha.
- **Instruções no imperativo, a falar com o agente** ("Lê", "Pede",
  "Regista"). Os textos que o agente produz para clientes tratam por "você"
  ou de forma impessoal, salvo indicação do stand.
- **Nunca afirmar o que não se mediu.** O que não foi verificado diz `N/V`
  (não verificado) e sai do denominador da nota. Ausência de prova não é
  falha do stand.
- **Nunca inventar factos do stand ou da viatura**: garantias, inspecções,
  histórico, quilómetros, preços, volumes de pesquisa, posições, citações.
  Falta um dado: pergunta-se ou marca-se para confirmar no DMS/CRM.
- **Referências legais são listas de controlo, não pareceres.** Citar o
  diploma (RGPD, Lei n.º 41/2004, Decreto-Lei n.º 84/2021, Decreto-Lei
  n.º 81-C/2017, Regulamento (UE) 2024/1689) e mandar confirmar a versão em
  vigor. Na dúvida, encaminhar para o encarregado de protecção de dados ou
  para um jurista.
- **Minimizar dados pessoais**: não pedir bases de clientes, documentos de
  identificação ou matrículas quando não são precisos; não os repetir nos
  relatórios.
- **Nada sai sem autorização explícita**: publicar, enviar, alterar perfis,
  carregar audiências, mexer em GTM/GA4/Ads.
- **Contexto português**: euros, concelhos e distritos, Standvirtual, OLX e
  outros portais sem assumir que algum é obrigatório, WhatsApp como canal
  principal, Perfil de Empresa no Google, IVA no regime da margem nos usados.
- **Exemplos com stands fictícios**, assinalados como tal. Nunca usar o nome
  de um stand real.

### Ligações entre skills

Quando um trabalho pertence a outra skill, nomeia-a em código:
"Para medir citações ao vivo, usa `stand-visibilidade-ia`." O validador
confirma que o nome existe. Quem tiver só esta skill instalada continua a
perceber o que fazer.

### Ferramentas grátis do hub

Apontar para elas quando poupam trabalho real, nunca como publicidade:

| Ferramenta | URL | Serve para |
|---|---|---|
| Nota de visibilidade online | https://onepilot.app/hub/ferramentas/visibilidade | Perfil Google, avaliações, concorrentes da zona, velocidade do site, palavras-chave; nota 0 a 100 |
| Link de avaliações do Google | https://onepilot.app/hub/ferramentas/link-avaliacoes | Link directo para a caixa de avaliação, QR code e mensagens para pedir avaliações |
| Análise de stock | https://onepilot.app/hub/ferramentas/analise-stock | Preço pedido face a anúncios semelhantes no Standvirtual, dias anunciados, descidas de preço |
| Modelos de documentos | https://onepilot.app/hub/ferramentas/modelos-documentos | Contrato de compra e venda, declarações, termo de responsabilidade, requerimento de registo |

São opcionais: a skill tem de funcionar sem elas.

## Scripts

Ficam em `partilhado/scripts/`, com destinos em `partilhado/destinos.json`.
Regras: biblioteca padrão; aceitam um URL ou um ficheiro local (para testes e
para quando o agente já tem o HTML); escrevem JSON no stdout; ajuda em PT-PT
com `--help`; nunca enviam dados para terceiros. Cada script tem teste em
`ferramentas/testes/` que corre sem rede.

## Antes de abrir PR

`python3 ferramentas/validar.py` e os testes têm de passar.

Uma skill nova entra em `CATEGORIAS` de `ferramentas/catalogo.py` e no
catálogo do hub, no `marketing-hub` (`shared/skills.ts`). Uma mudança de fundo
num `SKILL.md` (passos, entrega ou limites) também pede actualização do hub.
