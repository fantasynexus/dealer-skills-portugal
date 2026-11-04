# Stock rotativo: viaturas vendidas, filtros e paginação

Lê isto antes de testar o stock e antes de propor regras ao fornecedor do site. Num stand, o stock roda todas as semanas: o site tem de deixar entrar no índice o que está à venda e sair o que já não está, sem perder a procura que essas páginas traziam.

## Princípios

1. **Uma viatura, um URL estável.** Identificador do stock mais marca e modelo. Não muda com o preço, as fotografias ou uma edição. Não leva preço nem "promoção".
2. **Uma fonte para o estado.** O estado da viatura vem do mesmo sítio que alimenta o site e os portais (DMS ou gestor de stock). Se o site e o portal discordam, o problema é a sincronização, não o SEO.
3. **Sem atalhos.** Nada de redireccionamentos temporários (302) que ficam para sempre; nada de mandar tudo para o início.
4. **O sitemap só lista o que deve estar no índice.**

## Estados de uma viatura

| Estado | O que a página mostra | HTTP | Índice | Sitemap | `Offer.availability` |
|---|---|---|---|---|---|
| Disponível | Tudo | 200 | Indexável | Sim | `InStock` |
| Reservada | "Reservada" visível, contacto para alternativas | 200 | Indexável | Sim | `Reserved` (confirma no validador) |
| Vendida, mantida com estado (opção A) | "Vendida" no topo, sem botão de compra nem reserva, viaturas semelhantes disponíveis | 200 | Indexável enquanto tiver valor | Sim, enquanto indexável | `SoldOut` |
| Vendida, redireccionada (opção B) | Não há página: o visitante cai na listagem equivalente | 301 | Sai | Não | Não se aplica |
| Vendida, removida (opção C) | Página de erro útil, com ligações para o stock e contactos | 410 ou 404 | Sai | Não | Não se aplica |
| Retirada (consignação terminada, devolvida) | Como vendida | | | | |
| Regressada (venda desfeita) | Volta a disponível no mesmo URL | 200 | Indexável | Sim | `InStock` |

## Viatura vendida: árvore de decisão

**Pergunta 1. A página tem valor próprio?** Basta um destes, no período que o stand definir:

- cliques ou impressões no Search Console;
- ligações externas (artigos, fóruns, redes sociais);
- partilhas que ainda trazem visitas (WhatsApp, Facebook);
- campanhas activas a apontar para ela.

Se sim: **opção A**, manter com estado, durante uma janela que o stand decide e fica escrita no relatório. No fim da janela, passa à pergunta 2. Se não: pergunta 2.

**Pergunta 2. Há uma página equivalente com stock?** Procura por esta ordem: listagem do mesmo modelo; da mesma marca e segmento; do mesmo combustível ou carroçaria.

Se sim: **opção B**, 301 para essa página, num só salto. Se não: **opção C**, 410 (ou 404).

### Porquê

- **Não redireccionar tudo para o início.** O Google tende a tratar redireccionamentos para páginas sem relação como páginas inexistentes (soft 404), e quem chega fica perdido.
- **404 e 410.** Para o Google acabam por ter o mesmo efeito: a página sai do índice. O 410 diz explicitamente que a remoção é definitiva. Usa o que a plataforma suportar de forma consistente. Em ambos, a página que o visitante vê tem ligações para o stock e contactos, sem mudar o código de estado.
- **Opção A exige conteúdo.** Uma página que fica só com "vendida", sem fotografias, dados nem semelhantes, passa a ser tratada como soft 404. As semelhantes têm de ser reais e disponíveis.
- **Risco legal.** Manter como disponível uma viatura vendida, no site ou no portal, pode configurar prática comercial enganosa (Decreto-Lei n.º 57/2008, na redacção em vigor). Lista de controlo, não parecer: confirma com jurista. Além disso, gera contactos frustrados.

## Testes a fazer na auditoria

| # | Teste | Como | Esperado |
|---|---|---|---|
| 1 | Viatura vendida há dias | URL pedido ao stand; `python3 scripts/extrair_sinais_pagina.py <url>` ou `curl -sI <url>` | Estado visível e regra A, B ou C aplicada |
| 2 | Viatura vendida há meses | URLs com 404 no Search Console, ou URL antigo pedido ao stand | 301 equivalente ou 410/404; fora do sitemap |
| 3 | Viatura reservada | Página no site | 200, estado visível, sem formulário de compra |
| 4 | Sitemap contra stock | Número de URLs de viatura no sitemap contra o número de viaturas à venda que o stand indica | Números próximos; nenhuma vendida antiga no sitemap |
| 5 | Filtro profundo | Combinação de três ou mais filtros, com preço ou cor | `noindex`, canónico para a listagem base, ou padrão bloqueado |
| 6 | Ordenação | `?ordem=` ou equivalente | Canónico para a versão sem ordenação |
| 7 | Página 2 de uma listagem | Ligação no fundo da página 1 | 200, canónico próprio, ligada com `<a href>` |
| 8 | Listagem vazia | Marca sem stock no momento | Ver "Listagem vazia" abaixo |

No relatório de páginas do Search Console, um stand tem sempre muitos URLs em "não encontrado (404)" ou "página com redireccionamento": é o stock a rodar e é normal. O problema é quando viaturas activas aparecem nesses motivos, ou quando as vendidas continuam no sitemap.

## Listagens e filtros

| Tipo de página | Exemplo | Indexar? | Como |
|---|---|---|---|
| Listagem geral | `/viaturas` | Sim | Canónico próprio, texto curto sobre o stand e a zona |
| Marca | `/viaturas/renault` | Sim, se há stock habitual e procura | Texto próprio; sem stock, ver "Listagem vazia" |
| Marca e modelo | `/viaturas/renault/clio` | Só com procura comprovada e stock recorrente | Senão, sem ligações rastreáveis ou com `noindex` |
| Combustível | `/viaturas/electricos` | Sim, se o stand tem esse stock | Explicação útil, sem dados de bateria inventados |
| Três ou mais filtros, intervalos de preço ou quilómetros, cor | `?preco_max=...&cor=...` | Não | Não gerar ligações rastreáveis para estas combinações, ou bloquear o padrão no robots.txt sem apanhar as listagens que se querem indexadas |
| Ordenação | `?ordem=preco` | Não | Canónico para a versão sem ordenação |
| Paginação | `?pagina=2` | Rastreável | Canónico próprio, ligação `<a href>`. O Google já não usa `rel="prev/next"`; não apontes o canónico para a página 1 |
| Pesquisa interna | `/pesquisa?q=...` | Não | `noindex` e fora do sitemap |

**robots.txt ou `noindex`, não os dois ao mesmo tempo.** Uma página bloqueada no robots.txt não é lida, por isso o Google não vê o `noindex` nem o canónico dela. Para limpar do índice o que já lá está, primeiro `noindex`; só depois de sair, se fizer falta, bloquear o rastreio.

**Listagem vazia.** Se a página costuma ter stock e tem procura (uma marca que o stand vende sempre), mantém 200 com texto, alternativas reais e forma de pedir aviso quando chegar. Se é uma combinação gerada sem procura, `noindex` ou 404. Uma página vazia com 200 e nada mais tende a ser classificada como soft 404.

## Dados estruturados de uma viatura

Exemplo com uma viatura fictícia. Num site real, cada campo vem do DMS; o que falta não se inventa.

```json
{
  "@context": "https://schema.org",
  "@type": "Car",
  "name": "Renault Clio 1.0 TCe",
  "brand": { "@type": "Brand", "name": "Renault" },
  "model": "Clio",
  "vehicleModelDate": "2021",
  "mileageFromOdometer": { "@type": "QuantitativeValue", "value": 48000, "unitCode": "KMT" },
  "fuelType": "Gasolina",
  "vehicleTransmission": "Manual",
  "itemCondition": "https://schema.org/UsedCondition",
  "offers": {
    "@type": "Offer",
    "price": 13900,
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock",
    "seller": { "@type": "AutoDealer", "name": "Stand Exemplo" }
  }
}
```

Regras:

- Tudo o que está nos dados estruturados tem de estar visível na página, com os mesmos valores.
- O nome do vendedor é o mesmo do Perfil de Empresa.
- Não ponhas a matrícula. O número de quadro (VIN) só se o stand decidir publicá-lo.
- Não copies as avaliações do Google para `aggregateRating` do próprio stand: a Google não mostra estrelas de avaliações que um negócio publica sobre si mesmo, e as avaliações pertencem à plataforma onde foram escritas.
- A Google tem resultados enriquecidos próprios para anúncios de viaturas, mas a disponibilidade varia por país. Confirma na documentação actual da Google se Portugal está incluído antes de prometer qualquer destaque no resultado.

## Portais e site

- Mesmo preço e mesmo estado no site e em cada portal (Standvirtual, OLX ou outro que o stand use). Desfasamentos vêm da sincronização e corrigem-se na fonte.
- Descrição própria no site; a do portal pode ser outra. Para as escrever: `stand-escrever-anuncio`. Para rever a qualidade dos anúncios: `stand-rever-anuncios-viaturas`.
- O anúncio do portal pode aparecer à frente do site numa pesquisa de modelo. Se o contacto chega ao stand, não é um problema a corrigir à força; mede-o pela origem do contacto no CRM.

## Exemplo: três viaturas do Stand Exemplo, Leiria (fictício)

| Viatura fictícia | Situação | Decisão |
|---|---|---|
| Utilitário a gasolina vendido há cinco dias | A página ainda recebe visitas de uma ligação partilhada em redes sociais | A: "Vendida" no topo, semelhantes a gasolina disponíveis; revê no fim da janela combinada |
| SUV vendido há quatro meses | Sem cliques nem ligações; há três SUV da mesma marca em stock | B: 301 para a listagem da marca, num salto; sai do sitemap |
| Comercial de uma marca que o stand não volta a ter | Sem cliques, sem ligações, sem equivalente | C: 410, página de erro com ligações para o stock; sai do sitemap |
