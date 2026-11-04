---
name: stand-rever-anuncios-viaturas
description: Rever uma amostra de anúncios de viaturas de um stand português, no site e nos portais (Standvirtual, OLX e outros), e dizer o que corrigir para vender melhor. Usar quando há carros parados há muito tempo, poucos contactos por anúncio, dúvidas sobre fotografias, descrições, preço e encargos, dados técnicos em falta, viaturas vendidas ainda anunciadas, preços ou quilómetros diferentes entre o site e os portais, ou fotos com matrículas e documentos à vista. Entrega nota de 100 pontos por anúncio, falhas transversais do feed, lista de fotos em falta e correcções por impacto.
---

# Rever anúncios de viaturas

Analisa uma amostra de anúncios do stand, no site e nos portais, com uma grelha de 100 pontos, e separa o que é de cada anúncio do que é do processo (fotografia, feed, modelo de página). Não escreves anúncios novos aqui: para isso, `stand-escrever-anuncio`.

## Antes de começar

1. Pede o URL do site, os portais onde o stand publica (Standvirtual, OLX, outros) e, se possível, uma lista do stock com referência, data de entrada e preço (exportação do DMS ou do software de stock). Não precisas de dados de clientes.
2. Pergunta se o stand é independente ou concessionário de marca. Num concessionário, os usados certificados podem ter regras da marca: pede o manual em vez de supor requisitos.
3. Pergunta que dados podes confirmar com o stand (histórico, garantia, preparação). O que não se confirma fica `N/V` ou "a confirmar no DMS/CRM".
4. Escolhe o modo:
   - **Amostra (por omissão):** 8 a 12 viaturas.
   - **Uma viatura:** análise profunda de um anúncio em todos os canais.
   - **Só processo:** o gestor quer saber "como devíamos fotografar e anunciar". Entrega a lista de fotos e os padrões, sem pontuar.
5. Pára e pergunta se os portais exigem login para ver o anúncio completo, se o stand quer que contactes um anúncio (não o faças sem autorização) ou se a amostra proposta tem só viaturas escolhidas a dedo.

## Passos

1. **Escolhe a amostra.** Estratifica por idade, preço, marca, combustível e dias em stock. Inclui pelo menos duas viaturas paradas há mais tempo (dados do stand ou "dias anunciados" da Análise de stock), não só as melhores. Resultado: tabela com referência, viatura, canais e razão da escolha.
2. **Recolhe cada anúncio em cada canal.** No site, corre `python3 scripts/extrair_sinais_pagina.py <url>` e guarda o JSON. Nos portais, regista o que se vê no browser e guarda capturas com data; o portal controla a página, por isso não raspes em massa.
3. **Verifica as fotografias** contra a lista de referência de [references/fotografias.md](references/fotografias.md): número, ângulos essenciais, ordem, qualidade e dados pessoais.
4. **Pontua cada anúncio por canal.** Antes de pontuar, lê [references/grelha.md](references/grelha.md). Marca N/A o que o canal não deixa controlar (dados estruturados num portal) e `N/V` o que não conseguiste confirmar.
5. **Cruza os canais.** Preço, quilómetros, ano, versão e fotos iguais no site e nos portais? Vendidas ainda activas? Anúncios duplicados no mesmo portal?
6. **Situa o preço, sem o pontuar.** Com a Análise de stock do hub ou outra fonte datada, regista onde o preço pedido fica face a anúncios semelhantes e há quantos dias está anunciado. Decidir o preço é do gestor; tu mostras os dados e a data.
7. **Separa transversais de casos.** O mesmo erro em todos os anúncios é de processo, feed ou modelo de página. Indica a origem provável e o responsável (fotógrafo, quem carrega os anúncios, software de stock, fornecedor do site).
8. **Prioriza.** Primeiro o que engana ou expõe dados (preço diferente entre canais, vendida activa, documento com dados pessoais), depois o que faz o cliente desistir (poucas fotos, ficha incompleta), depois o resto.
9. **Entrega** com o modelo [assets/relatorio-anuncios.md](assets/relatorio-anuncios.md).

## Adaptar ao tipo de viatura

- **Eléctricos e híbridos plug-in:** capacidade da bateria, autonomia com a norma (WLTP ou NEDC) e a fonte, tipos de carregamento, cabos incluídos. Estado da bateria só com relatório; nunca o deduzas da autonomia que o painel mostra.
- **Comerciais:** lugares, carga útil, peso bruto, medidas da zona de carga. IVA dedutível ou regime da margem só confirmado pelo stand, nunca inferido.
- **Importados:** data da primeira matrícula no país de origem e em Portugal, e se o ISV e a legalização estão incluídos no preço, confirmados pelo stand.

## Ferramentas

- `python3 scripts/extrair_sinais_pagina.py <url-ou-ficheiro.html>`: na página do site, devolve título, preço e dados da viatura na marcação `Car`/`Vehicle`/`Offer`, contactos, formulários e imagens sem `alt`. Não executa JavaScript: galerias e preços carregados depois não aparecem. Mostra o que a página declara, não que está certo; confirma com o stand.
- [Análise de stock](https://onepilot.app/hub/ferramentas/analise-stock): preço face a anúncios semelhantes no Standvirtual, dias anunciados e descidas de preço. São preços pedidos, não preços de venda.
- Para reescrever um anúncio com a ficha confirmada, `stand-escrever-anuncio`. Para botões e formulários do site, `stand-auditoria-cta`. Para a técnica do site, `stand-avaliar-site`. Para publicações das viaturas nas redes, `stand-publicar-redes-sociais`.

## Entrega

Segue [assets/relatorio-anuncios.md](assets/relatorio-anuncios.md):

- resumo com bloqueios, amostra e cobertura;
- nota por anúncio, canal e dimensão;
- falhas transversais, com origem e responsável;
- divergências entre canais, vendidas activas e duplicados;
- fotos em falta por viatura;
- dados a confirmar no DMS/CRM;
- posição de preço com fonte e data, sem pontuar;
- correcções por impacto.

Para um ou dois anúncios, mostra o antes e depois das primeiras linhas, só com dados confirmados, para ilustrar a correcção. A reescrita completa passa para `stand-escrever-anuncio`, com a ficha confirmada.

## Limites

- Não completes dados por conhecimento do modelo: versão, equipamento, potência, histórico ou garantia que não estão confirmados ficam marcados para validação no DMS/CRM.
- Só afirmas histórico, número de donos, revisões, preparação e garantia quando há prova.
- Não reproduzas nos relatórios matrículas, números de quadro, nomes ou documentos que encontres nas fotos: descreve o problema e identifica a foto.
- Não contactes anúncios, não peças propostas e não te faças passar por cliente sem autorização do stand; nunca em anúncios de concorrentes.
- Não alteres preços nem anúncios. Propões; o stand publica.
- Não uses nem recomendes imagens geradas ou editadas que alterem a viatura (cor, jantes, danos, equipamento).
- As referências legais da grelha são listas de controlo, não pareceres; na dúvida, encaminha para um jurista.
