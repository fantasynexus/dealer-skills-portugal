# Pesquisa em Portugal: padrões, intenções e mapa de procura

Lê isto antes de construir o mapa de procura e de procurar canibalização.

## Regras

- Os padrões abaixo são **hipóteses para confirmar**, não volumes. Nenhum vem com número porque nenhum número seria verdadeiro para todos os stands.
- Fontes de prova, da mais forte para a mais fraca. Regista sempre a fonte e a data.
  1. **Search Console**, relatório de desempenho filtrado por país Portugal: consultas que já dão impressões ao site.
  2. **Planeador de palavras-chave do Google Ads**: intervalos, muitas vezes largos sem campanha activa. Diz-se "estimativa".
  3. **Google Trends**: comparação relativa entre termos e sazonalidade. Não dá volumes.
  4. **Sugestões automáticas e perguntas relacionadas** na página de resultados: qualitativo, serve para descobrir termos.
  5. **[Nota de visibilidade online](https://onepilot.app/hub/ferramentas/visibilidade)**: palavras-chave e posições num momento.
- Pesquisa em janela privada e com a localização do stand. Os resultados locais mudam com a localização de quem pesquisa: uma posição vista assim é uma observação datada, não uma métrica.

## Padrões de pesquisa de quem compra carro em Portugal

Exemplos com o Stand Exemplo, Leiria (fictício).

| # | Padrão | Exemplos | Intenção | Página dona habitual | Cuidado |
|---|---|---|---|---|---|
| 1 | Stand mais concelho | "stand automóveis leiria", "stand carros usados leiria", "stands marinha grande" | Encontrar um stand perto | Início ou página da instalação | O mapa (pack local) decide-se no perfil: `stand-auditoria-perfil-google` |
| 2 | Carros usados mais concelho ou distrito | "carros usados leiria", "carros usados distrito de leiria", "viaturas usadas pombal" | Ver stock da zona | Listagem geral com texto curto sobre a zona | Leiria é concelho e distrito: confirma de que zona fala o gestor |
| 3 | Marca e modelo usado | "peugeot 2008 usado", "renault clio usado leiria", "bmw série 1 usado" | Comparar ofertas de um modelo | Listagem da marca ou do modelo quando há stock habitual; página da viatura | Os portais aparecem em muitas destas pesquisas. O objectivo é o contacto, não ganhar ao portal em todas |
| 4 | Combustível | "carros eléctricos usados", "híbridos usados", "híbrido plug-in usado", "carros a gasóleo usados" | Escolher pela energia | Listagem por combustível com explicação útil | Autonomia e estado da bateria só com dados verificados, nunca estimados |
| 5 | Retoma | "retoma carro", "stand que aceita retoma", "avaliar carro para retoma", "quanto vale o meu carro" | Trocar ou vender o carro actual | Página de retoma: como funciona e o que levar | Não prometer valores de retoma no texto. Campanhas: `stand-campanha-retoma` |
| 6 | Financiamento | "carros usados com financiamento", "crédito automóvel usados", "carros usados a prestações" | Pagar a prestações | Página de financiamento | Ver nota legal abaixo |
| 7 | Orçamento | "carros usados até 10000 euros", "carros baratos leiria" | Filtrar por preço | Filtro da listagem; página fixa só se há sempre stock nessa faixa | Páginas por faixa de preço ficam vazias quando o stock roda |
| 8 | Tipo e uso | "carrinhas usadas", "suv usado", "carros 7 lugares usados", "comerciais usados", "carros automáticos usados" | Escolher pelo uso | Listagem por carroçaria ou caixa | Só quando o stand tem esse stock de forma recorrente |
| 9 | Confiança | "carros usados com garantia", "stand de confiança leiria" | Reduzir o risco | Página de garantia e página "sobre" | Condições de garantia conforme o Decreto-Lei n.º 84/2021; confirmar com jurista o texto |
| 10 | Importados | "carros importados", "carros importados da alemanha" | Comprar importado | Página própria só se o stand importa | Custos de legalização e ISV só com valores confirmados pelo stand |
| 11 | Oficina | "oficina leiria", "revisão automóvel leiria" | Serviço | Página da oficina | Só se a oficina existe |
| 12 | Nome do stand | "stand exemplo", "stand exemplo opiniões" | Ir ao site ou validar | Início; avaliações no perfil | Se um portal ou um directório aparece antes do site na pesquisa pelo nome, investiga |

### Nota legal sobre financiamento

Texto sobre crédito tem regras de publicidade e de informação próprias: Decreto-Lei n.º 133/2009 (crédito aos consumidores) e a Directiva (UE) 2023/2225, que obriga a rever esse regime. Quem apresenta crédito ao cliente deve estar registado como intermediário de crédito (Decreto-Lei n.º 81-C/2017). É lista de controlo, não parecer: confirma o regime em vigor e o registo do stand antes de propor uma página ou frases como "sem entrada" ou "aprovação imediata". Na dúvida, jurista.

## Notas sobre a língua das pesquisas

- **"Perto de mim".** O Google resolve a proximidade pela localização de quem pesquisa e pela distância ao perfil. Encher textos com "perto de mim" não substitui um perfil completo e uma página de localização clara.
- **Grafias.** Quem pesquisa escreve com a grafia do Acordo Ortográfico, com a anterior e sem acentos. O Google costuma agrupar estas variantes, mas confirma no Search Console que consultas aparecem antes de mexer no texto. Não mudes a grafia do site por SEO sem prova.
- **Vocabulário do Brasil.** A comunidade brasileira residente pesquisa com termos como "concessionária", "seminovo" ou "carro zero". Se aparecem no Search Console, podem entrar naturalmente no texto. Não é razão para uma versão pt-BR (ver `stand-seo-multilingue`).
- **"Viatura", "carro", "automóvel".** O stand diz "viatura"; muitos compradores escrevem "carro". As consultas reais decidem que palavra vai para títulos e H1.
- **Concelho, distrito, região.** Há 308 concelhos e, no continente, 18 distritos. As pesquisas usam sobretudo o nome da cidade ou vila; nomes de região ("Algarve", "Minho", "Oeste") aparecem também. Usa as zonas onde o stand vende de facto.

## Modelo do mapa de procura

| Intenção | Consulta de exemplo | Fonte e data | Página dona | Estado | Acção | Quem |
|---|---|---|---|---|---|---|
| Stand mais concelho | | Search Console, últimos 3 meses | | existe / falta / canibalizada / fraca | | stand / fornecedor |

Estado:

- **existe**: a página dona aparece para a consulta e responde à intenção;
- **falta**: o stand serve a intenção mas não tem página;
- **canibalizada**: duas ou mais páginas alternam;
- **fraca**: a página existe mas não responde (só formulário, texto genérico).

## Canibalização: como decidir a página dona

1. No Search Console, filtra a consulta e abre o separador de páginas (últimos 3 meses). Mais de uma página com impressões relevantes é um grupo.
2. A dona é a página que melhor responde à intenção, não a que tem mais impressões hoje.
3. Para as outras, escolhe uma saída:
   - **mudar o foco** (título, H1 e texto passam a servir outra intenção);
   - **fundir e redireccionar com 301** quando o conteúdo se repete;
   - **deixar** quando servem intenções diferentes e só se cruzam em pesquisas pelo nome do stand.
4. Ajusta as ligações internas: o texto âncora com a intenção aponta para a dona.
5. Combina com o stand quando voltar a medir a mesma consulta e regista a data da alteração para comparar antes e depois.

### Grupos que aparecem muito em sites de stands

- Início e listagem geral a disputar "carros usados" mais concelho.
- Página de marca criada à mão e filtro de marca gerado pela plataforma (`/marca/renault` e `/viaturas?marca=renault`).
- Artigo antigo sobre retoma e a página de retoma.
- Páginas de campanha (salão, fim de ano) que ficaram publicadas depois de acabar.
- A mesma descrição na página da viatura e no anúncio do portal. Não é canibalização dentro do site, mas o Google tende a mostrar só uma das versões; uma descrição própria no site resolve. Para a escrever, `stand-escrever-anuncio`.

## Exemplo resolvido: Stand Exemplo, Leiria (fictício)

Contexto inventado para ilustrar: vende usados de várias marcas, tem alguns eléctricos e híbridos, aceita retoma, apresenta crédito de uma financeira, site numa plataforma de stands, Search Console ligado.

| Intenção | Achado | Decisão |
|---|---|---|
| "carros usados leiria" | Início e `/viaturas` alternam ao longo do período | A listagem é a dona. O início passa a apresentar o stand ("Stand Exemplo, automóveis usados em Leiria") e liga à listagem com a âncora "carros usados em Leiria" |
| "carros eléctricos usados" | Não há página; o filtro `?combustivel=electrico` tem canónico para `/viaturas` | Criar `/viaturas/electricos` indexável, com texto curto sobre o que o stand verifica nas viaturas eléctricas, só se o verifica de facto |
| "retoma carro leiria" | A página de retoma só tem formulário; um artigo antigo sobre retoma aparece mais vezes | Fundir o artigo na página de retoma (como funciona, documentos a levar, quanto tempo o stand demora a responder) e 301 do artigo para a página |
| "carros usados com financiamento" | Página existe e promete "aprovação garantida" | Retirar a promessa e confirmar registo de intermediário de crédito antes de qualquer outra mudança |

Nenhum número do exemplo é real. Num relatório verdadeiro, cada achado leva a fonte e o período.
