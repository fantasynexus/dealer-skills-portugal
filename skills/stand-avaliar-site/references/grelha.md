# Grelha da avaliação do site

Dez dimensões de 10 pontos cada. Cada verificação dá Total, Parcial ou 0, conforme a tabela. Marca `N/V` quando não conseguiste testar e N/A quando não se aplica, com a razão (ex.: o stand não tem oficina, logo não há página de oficina). Ambas saem do denominador; `N/V` conta para a cobertura, N/A não.

Os limiares de Core Web Vitals são os publicados pela Google. Os restantes limiares numéricos (peso de página, número de saltos, tempo até ao primeiro byte) são critérios desta grelha, escolhidos por serem verificáveis; se o gestor perguntar, di-lo assim e não como norma.

Uma verificação sobre várias páginas pontua pela pior página da amostra, salvo indicação em contrário, e regista quais falharam.

## Como calcular

- **Pontos aplicáveis** = 100 menos os pontos marcados N/A.
- **Pontos verificados** = aplicáveis menos os marcados `N/V`.
- **Nota** = pontos obtidos ÷ pontos verificados × 100, arredondada às unidades.
- **Cobertura** = pontos verificados ÷ pontos aplicáveis.
- Cobertura abaixo de 70%: nota provisória. Não a compares com outra avaliação nem com um concorrente.
- Um bloqueio crítico (ver fim do ficheiro) lidera o veredicto mesmo com nota alta.

## 1. Core Web Vitals e peso de página

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 1.1 | Dados de campo em telemóvel no PageSpeed Insights (LCP, INP e CLS no percentil 75). Regista se são do URL ou da origem. | 4: as três métricas em "Bom" | 2: uma fora de "Bom" | duas ou mais fora |
| 1.2 | LCP de laboratório em telemóvel (Lighthouse) no início e nas páginas de viatura. | 2: até 2,5 s | 1: até 4 s | acima de 4 s |
| 1.3 | CLS e Total Blocking Time de laboratório em telemóvel. O TBT é um indicador de laboratório que ajuda a explicar o INP; não o substitui. | 2: CLS até 0,1 e TBT até 200 ms | 1: um dos dois falha | ambos falham |
| 1.4 | Peso transferido da página de viatura em telemóvel (Lighthouse, "total byte weight") e imagens em formato e tamanho adequados. | 2: até 3 MB | 1: até 5 MB | acima de 5 MB |

Sem dados de campo (site com pouco tráfego), 1.1 fica `N/V`, não 0. Explica ao gestor que a Google não tem amostra suficiente e que o laboratório é uma simulação.

## 2. Disponibilidade, HTTPS e segurança básica

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 2.1 | Todas as páginas da amostra respondem 200, ou um único 301 para uma página 200. Sem 5xx. | 2 | 1: cadeias de dois ou mais saltos | algum 4xx ou 5xx numa página de negócio |
| 2.2 | `http://` redirecciona com 301 para `https://`, e só existe uma versão do domínio (com ou sem `www`). | 3 | 1,5: redirecciona, mas com 302 ou com duas versões acessíveis | HTTPS em falta ou sem redireccionamento |
| 2.3 | Certificado válido, emitido para o domínio, com mais de 30 dias até expirar, TLS 1.2 ou superior. | 2 | 1: expira em menos de 30 dias | inválido ou com aviso no browser |
| 2.4 | Cabeçalho `Strict-Transport-Security` presente. | 1 | 0,5: `max-age` inferior a seis meses | ausente |
| 2.5 | Sem conteúdo misto (recursos `http://` em páginas `https://`), na consola do browser ou no HTML. | 1 | n/a | algum |
| 2.6 | Tempo até ao primeiro byte, mediana de cinco pedidos ao início. A Google sugere visar 0,8 s ou menos. | 1: até 0,8 s | 0,5: até 1,8 s | acima de 1,8 s |

Regista de onde mediste o 2.6: um pedido a partir de um servidor fora de Portugal não representa o cliente em Leiria.

## 3. Rastreabilidade, indexação, canónicos, sitemap e robots

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 3.1 | robots.txt responde 200 e não bloqueia caminhos de negócio (início, listagem, viaturas, oficina) para `Googlebot` e `Bingbot`. Prova: `verificar_bots_ia.py`. | 3 | 1,5: bloqueia caminhos secundários úteis | bloqueia viaturas ou o site todo |
| 3.2 | A política para bots de IA (pesquisa, treino, pedido do utilizador) corresponde ao que o stand quer. Pergunta a intenção antes de pontuar. | 1: coerente com a intenção | 0,5: bloqueio acidental de bots de pesquisa | firewall ou CDN bloqueia bots que o robots.txt permite, sem o stand saber |
| 3.3 | Sitemap declarado ou em `/sitemap.xml`, com URLs canónicos que respondem 200, viaturas actuais incluídas e vendidas antigas removidas. | 2 | 1: existe, mas com URLs mortos ou sem viaturas | ausente e descoberta por ligações fraca |
| 3.4 | Canónico de cada página aponta para si própria ou para a versão correcta. Nenhuma viatura com canónico para o início ou para a listagem. | 2 | 1: inconsistências pontuais | padrão errado no modelo de página |
| 3.5 | Nenhuma página de negócio com `noindex` em `meta robots` ou `X-Robots-Tag`. Filtros e ordenações da listagem com tratamento (canónico, `noindex` ou parâmetros não ligados). | 1 | 0,5: filtros indexáveis sem controlo | `noindex` em viaturas ou no início |
| 3.6 | Search Console, relatório de indexação de páginas: viaturas indexadas e motivos das não indexadas. Só com acesso. | 1: sem padrão de exclusão nas viaturas | 0,5: exclusões explicáveis em parte | viaturas excluídas em massa |

Sem acesso ao Search Console, 3.6 é `N/V`. Uma pesquisa `site:` não prova indexação.

## 4. Dados estruturados e consistência de entidade

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 4.1 | Marcação do negócio (`AutoDealer` ou `LocalBusiness`) com nome, morada, telefone e horário iguais ao visível e ao Perfil de Empresa no Google. | 3 | 1,5: presente com campos em falta ou divergentes | ausente |
| 4.2 | Páginas de viatura com marcação de viatura (`Car` ou `Vehicle`) e `Offer` com preço, `priceCurrency` EUR, disponibilidade e estado, iguais ao visível. | 4 | 2: só nalgumas viaturas ou sem `Offer` | ausente |
| 4.3 | Sem erros no Teste de resultados enriquecidos ou no Schema Markup Validator no início e numa viatura. | 2 | 1: só avisos | erros |
| 4.4 | Sem marcação enganadora: classificações próprias em `AggregateRating` ou `Review`, preço diferente do visível, viatura vendida marcada como disponível. | 1 | n/a | algum caso |

Os resultados enriquecidos de viaturas da Google podem não estar disponíveis em Portugal: confirma na documentação actual antes de prometer um efeito visível. A marcação continua útil para coerência e leitura por máquinas.

## 5. Experiência móvel e navegação

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 5.1 | `meta viewport` com `width=device-width` e sem scroll horizontal a 360 px. | 2 | 1: scroll horizontal numa página | ausente ou scroll em várias |
| 5.2 | Botões e ligações principais com área de toque confortável (orientação da Google: cerca de 48 px) e nunca abaixo de 24 × 24 px (WCAG 2.2, critério 2.5.8). | 2 | 1: alguns abaixo | muitos abaixo de 24 px |
| 5.3 | Do início a uma viatura e daí ao contacto em três toques ou menos; menu, pesquisa e filtros funcionam em telemóvel. | 3 | 1,5: caminho longo ou um filtro partido | listagem ou filtros inutilizáveis |
| 5.4 | Galeria da viatura desliza e amplia no telemóvel. | 1 | 0,5: só por botões | fotos cortadas ou partidas |
| 5.5 | Banner de cookies, chat ou barras fixas não tapam conteúdo nem a acção principal. | 2 | 1: tapam parcialmente | tapam o botão de contacto |

## 6. Acessibilidade

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 6.1 | Fotos de viatura com `alt` descritivo; imagens decorativas com `alt` vazio. Prova: `imagens.sem_alt` do script e inspecção. | 2: menos de 5% sem `alt` útil | 1: até 30% | mais de 30% |
| 6.2 | Contraste de pelo menos 4,5:1 no texto normal, nos preços e nos botões (WCAG 2.2 AA). | 2 | 1: falhas pontuais | falhas no texto principal ou nos CTA |
| 6.3 | Campos de formulário com rótulo associado; erros explicados em texto, não só por cor. | 2 | 1: alguns campos sem rótulo | formulário sem rótulos |
| 6.4 | Com a tecla Tab chegas ao menu, filtros, galeria e formulário, com foco visível e sem ficar preso. | 2 | 1: um elemento inacessível | menu ou formulário inacessível |
| 6.5 | Um `h1` por página, títulos em ordem, `lang` em português (`pt-PT` ou `pt`). | 1 | 0,5: um dos três falha | dois ou mais falham |
| 6.6 | Zoom a 200% sem perda de conteúdo; sem `user-scalable=no` nem `maximum-scale=1`. | 1 | n/a | zoom bloqueado |

O Acto Europeu da Acessibilidade (Directiva (UE) 2019/882) aplica-se desde 28 de Junho de 2025 a certos serviços de comércio electrónico, com excepções para microempresas. Confirma com um jurista o diploma português de transposição e se abrange o site do stand. Esta grelha não declara conformidade.

## 7. Scripts de terceiros, cookies e consentimento

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 7.1 | Antes de qualquer escolha no banner, nenhuma etiqueta de publicidade ou análise grava cookies ou envia dados identificáveis. Prova: separador Rede e Cookies numa janela anónima (ver `medicao.md`). | 4 | 2: só pedidos sem cookies do modo de consentimento, por decisão documentada | etiquetas a disparar antes do consentimento |
| 7.2 | "Rejeitar" tão visível e acessível como "Aceitar" na primeira camada; nenhuma finalidade pré-seleccionada. | 2 | 1: rejeitar só na segunda camada | sem forma simples de recusar |
| 7.3 | Política de cookies e de privacidade ligada do banner e do rodapé, com finalidades e terceiros. | 1 | 0,5: genérica, sem terceiros | ausente |
| 7.4 | Scripts de terceiros não bloqueiam a primeira renderização; chat e widgets carregam depois do conteúdo principal. | 2 | 1: um bloqueador | vários bloqueadores ou chat a atrasar o LCP |
| 7.5 | Sem etiquetas duplicadas ou abandonadas (dois contentores GTM, duas propriedades GA4, píxeis de fornecedores antigos). | 1 | 0,5: suspeita sem confirmação | duplicados confirmados |

Base legal a confirmar na versão em vigor: Lei n.º 41/2004 (consentimento para cookies não essenciais) e RGPD. A grelha verifica comportamento observável; não avalia a validade jurídica do consentimento. Problemas de medição vão para `stand-auditoria-ga4-google-ads`.

## 8. Contacto: chamada, WhatsApp, marcação e formulários

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 8.1 | Telefones em ligação `tel:+351...` no cabeçalho ou rodapé e nas páginas de viatura. | 2 | 1: só nalgumas páginas | texto simples |
| 8.2 | WhatsApp em `https://wa.me/351...`, com texto pré-preenchido que identifica a viatura nas páginas de viatura. | 2 | 1: ligação sem texto ou sem viatura | ausente ou partida, se o stand usa WhatsApp |
| 8.3 | Morada, horário e direcções encontram-se em menos de dois toques. | 2 | 1: só numa página escondida | ausentes |
| 8.4 | Formulários pedem só o necessário, com consentimento de marketing separado e não pré-seleccionado. A entrega real fica `N/V` sem teste autorizado. | 2 | 1: campos a mais ou consentimento agregado | formulário partido |
| 8.5 | Na página de viatura em telemóvel, uma acção de contacto sobre aquela viatura visível sem scroll. | 2 | 1: só depois de scroll | ausente |

Para o inventário completo de botões e textos, usa `stand-auditoria-cta`. Para atribuição de chamadas, `stand-auditoria-rastreio-chamadas`.

## 9. Páginas e feeds de viatura

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 9.1 | Cada viatura tem URL estável. Vendidas: 410 ou 404 útil, 301 para viaturas semelhantes, ou página "vendido" temporária fora do sitemap. Nunca redireccionamento em massa para o início. | 3 | 1,5: vendidas ficam activas mais de uma semana | soft 404 ou redireccionamento em massa |
| 9.2 | Marca, modelo, versão, ano, quilómetros, combustível e preço existem no HTML inicial (o script vê-os), não só depois de JavaScript. | 2 | 1: parte dos dados só após JavaScript | ficha só visível após JavaScript |
| 9.3 | Em três viaturas, preço, quilómetros e ano iguais no site e nos portais onde o stand publica. | 2 | 1: uma divergência | duas ou mais |
| 9.4 | Filtros e paginação da listagem não geram URLs infinitos indexáveis; a listagem abre em tempo aceitável. | 2 | 1: um dos dois falha | ambos falham |
| 9.5 | Fotos de viatura servidas em tamanho adequado ao ecrã e com dimensões declaradas. | 1 | 0,5: só nalgumas | imagens em tamanho original |

A qualidade comercial do anúncio (fotos, descrição, preço) é `stand-rever-anuncios-viaturas`.

## 10. Confiança: identidade, políticas e informação comercial

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 10.1 | Denominação, NIF ou NIPC e morada visíveis no rodapé ou numa página "Sobre". | 2 | 1: falta um elemento | nenhum |
| 10.2 | Ligação visível ao Livro de Reclamações Electrónico e informação sobre entidades de resolução alternativa de litígios. Confirma a obrigação actual (regime do Livro de Reclamações e Lei n.º 144/2015). | 2 | 1: só um dos dois | nenhum |
| 10.3 | Política de privacidade com responsável, finalidades, prazos, direitos e contacto. | 2 | 1: genérica ou incompleta | ausente |
| 10.4 | Garantia, preparação, retoma e financiamento descritos com condições concretas e sem promessas vagas. Pergunta ao stand se o texto corresponde à prática. | 2 | 1: vago | promessas contraditórias ou "aprovação garantida" |
| 10.5 | Prova social verificável: avaliações com origem (ligação ao Google ou ao portal), fotos reais da equipa e das instalações. | 2 | 1: testemunhos sem origem | avaliações apresentadas sem fonte como se fossem independentes |

## Bloqueios críticos

Lideram o veredicto e entram nos cinco problemas prioritários, seja qual for a nota:

- páginas de viatura fora do índice por `noindex`, robots.txt ou canónico errado;
- certificado inválido ou site sem HTTPS;
- telefone, WhatsApp ou formulário principal que não funcionam;
- etiquetas de publicidade a gravar cookies antes do consentimento;
- preço ou disponibilidade no site diferentes da realidade em várias viaturas.

## Exemplo de cálculo (Stand Exemplo, Leiria, fictício)

O stand não usa WhatsApp e não quer usar: 8.2 é N/A (2 pontos), pontos aplicáveis 98. Sem dados de campo (1.1, 4 pontos) e sem Search Console (3.6, 1 ponto): 5 pontos `N/V`, pontos verificados 93. Pontos obtidos: 61. Nota = 61 ÷ 93 × 100 = 66. Cobertura = 93 ÷ 98 = 95%. Nota final, não provisória. Havia `noindex` no modelo das páginas de viatura: o veredicto começa por aí, não pelo 66.
