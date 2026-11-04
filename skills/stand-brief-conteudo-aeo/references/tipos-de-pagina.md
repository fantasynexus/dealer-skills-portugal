# Tipos de página

## Escolher

| A pergunta soa a | Tipo |
|---|---|
| "aceitam X?", "como funciona X no stand?" | Página de serviço |
| "o que verificar ao comprar X?", "vale a pena X?" | Guia de compra |
| "[modelo] usado: versões, consumos, o que ver" | Guia de modelo |
| "X ou Y?" (modelos, combustíveis, crédito ou renting) | Comparação |
| "quanto custa / quando se paga / de quanto em quanto tempo" (IUC, inspecção, ISV) | Explicação de uma regra |
| "stand em [concelho]" | Página local, só com razão real |
| muitas perguntas curtas sobre o mesmo tema | Perguntas frequentes |
| algo novo e com data (Orçamento do Estado, novo aviso de apoios) | Artigo datado |

Comparar o stand com um concorrente nomeado é trabalho de
`stand-pagina-comparacao`. O texto de um anúncio de viatura é de
`stand-escrever-anuncio`.

Antes de propor uma página nova, decide:

1. Já existe uma página sobre isto? Reescrever é melhor do que duplicar.
2. A pergunta cabe numa secção de uma página existente? Muitas perguntas de
   retoma ou garantia ficam melhor como perguntas e respostas na página do
   serviço do que como artigo à parte.
3. A resposta é só uma regra oficial? Então a página diz o que o stand faz
   por si e liga à fonte, em vez de reescrever a lei.

## 1. Página de serviço (retoma, financiamento, garantia, entrega, oficina)

- **Estrutura:** abertura com o que o stand faz e como pedir; como funciona,
  em passos; o que é preciso (documentos, condições); prazos e custos, só os
  medidos ou confirmados; perguntas e respostas; próximo passo.
- **Provas do stand:** condições escritas, lista de documentos, prazos medidos.
- **Fontes:** a regra que se aplica (Banco de Portugal, Decreto-Lei n.º 84/2021, IRN).
- **Dados estruturados:** `FAQPage` se as perguntas estão visíveis; o stand como
  `publisher` ou `provider`, pelo `@id` do `AutoDealer`.
- **CTA:** pedir simulação, avaliação da retoma, marcação.
- **Armadilhas:** prometer aprovação de crédito, valores de retoma, prazos não medidos.

## 2. Guia de compra

- **Estrutura:** resposta directa; o que verificar (lista); documentos; erros
  frequentes; o que o stand faz nesse ponto (com prova); perguntas; ligação
  ao stock.
- **Dados estruturados:** `Article`, mais `FAQPage` se houver perguntas visíveis.
- **Armadilhas:** texto genérico que podia estar em qualquer site. Cada secção
  liga o conselho ao que o stand faz e consegue provar.

## 3. Guia de modelo

- **Estrutura:** para quem é o modelo e que versões o stand costuma ter (só
  com dados do stock); motores e versões (fonte: fabricante); consumos ou
  autonomia (WLTP, com fonte); o que verificar num usado deste modelo;
  segurança (Euro NCAP, com o ano do teste); perguntas; viaturas deste modelo
  em stock.
- **Dados estruturados:** `Article`. `Car` e `Offer` ficam só nas fichas.
- **Armadilhas:** especificações de memória; "fiável" ou "problemas
  conhecidos" sem fonte; preços de mercado sem data.

## 4. Comparação

- **Estrutura:** a resposta (qual, para que uso) logo no início; tabela lado a
  lado com a fonte de cada linha; quando ganha A; quando ganha B; o que decide;
  perguntas; ver os dois no stand.
- **Dados estruturados:** `Article`.
- **Armadilhas:** um texto equilibrado que não responde; tabela sem fontes.

## 5. Explicação de uma regra (IUC, inspecção, ISV, garantia legal, documentos)

- **Estrutura:** resposta com data e fonte ("segundo o Portal das Finanças,
  consultado em [data]"); como funciona; casos frequentes; o que o stand faz
  por si; lista de fontes oficiais; data da última revisão visível.
- **Dados estruturados:** `Article` com `dateModified`.
- **Armadilhas:** valores de memória; texto sem data; não actualizar depois
  de cada Orçamento do Estado ou mudança de lei.
- **Revisão:** obrigatória quando a regra muda; nos impostos, pelo menos uma
  vez por ano.

## 6. Página local

Só quando há razão real: o stand está nesse concelho, entrega lá com
regularidade, ou tem clientes de lá que o gestor confirma.

- **Estrutura:** quem é o stand e onde fica em relação a esse concelho; o que
  os clientes de lá procuram (só com dados do stand); como chegar ou como
  funciona a entrega; perguntas; contacto.
- **Dados estruturados:** o `AutoDealer` vive na página de contactos; a
  página local refere-o pelo `@id`.
- **Armadilhas:** páginas iguais com o nome do concelho trocado (as políticas
  de spam da Google tratam-nas como páginas de entrada, ou doorway); inventar
  "os nossos clientes de X".

## 7. Perguntas frequentes

- **Quando:** muitas perguntas curtas sobre o mesmo tema. Cada resposta tem
  uma a três frases e liga à página que desenvolve.
- **Dados estruturados:** `FAQPage` com as perguntas visíveis, texto igual.
  Desde 2023 a Google só mostra resultados enriquecidos de FAQ a sites
  governamentais e de saúde (confirma); a marcação descreve, não destaca.
- **Armadilhas:** respostas vagas; repetir as páginas de serviço palavra a palavra.

## 8. Artigo datado

- **Quando:** novidade com data (mudança no IUC, novo aviso de apoios).
- **Dados estruturados:** `Article` com `datePublished`.
- **Armadilhas:** deixá-lo no ar depois de caducar. Actualiza ou marca como
  desactualizado, com a data.

## Fase de compra e CTA

Um CTA principal por página, coerente com a fase:

| Fase | O comprador quer | CTA principal | CTA secundário |
|---|---|---|---|
| Pesquisa | perceber | Ver viaturas | Ler o guia relacionado |
| Comparação | escolher | Marcar test drive | Ver as duas viaturas |
| Decisão | avançar | Pedir simulação ou avaliação da retoma | Falar por WhatsApp |
| Pós-venda | manter | Marcar revisão | Contactos da oficina |

Nunca "Compre já" num guia ou numa explicação de regra.

## Dados estruturados: resumo

| Tipo | Onde | Campos que o brief indica |
|---|---|---|
| `Article` | guias, explicações, artigos | `headline`, `datePublished`, `dateModified`, `author` (pessoa real com função, ou o stand), `publisher` (o `@id` do `AutoDealer`) |
| `FAQPage` | só com perguntas visíveis | cada pergunta e resposta com o texto da página |
| `AutoDealer` | contactos (e página inicial) | nome, morada, telefone, horário, `sameAs` |
| `Car` com `Offer` | só fichas de viaturas | marca, modelo, quilómetros, preço em EUR, disponibilidade |

Exemplos completos de JSON-LD para `AutoDealer` e `Car` estão na skill
`stand-auditoria-aeo`. Os dados estruturados dizem o que a página já diz:
nunca acrescentam factos que não estão visíveis.

## Regras para todos os tipos

- Abertura de 60 a 100 palavras que responde à pergunta sem rodeios.
- Comprimento: o que a lista de perguntas obrigatórias pede. Não há número
  de palavras certo para aparecer em respostas de IA; não inventes um.
- PT-PT, euros, quilómetros. Datas em tudo o que muda (preços, regras, apoios).
- Uma pergunta, uma página. Nada de gerar dezenas de páginas parecidas com IA:
  as políticas de spam da Google visam conteúdo em escala feito para motores.
