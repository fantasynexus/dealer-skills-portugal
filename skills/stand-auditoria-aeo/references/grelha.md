# Grelha da auditoria AEO

29 verificações em dez dimensões. Cada uma vale **2** (total), **1** (parcial),
**0** (zero), **N/V** (não verificado: sai do denominador) ou **N/A** (não se
aplica a este stand: sai do denominador, com o motivo escrito). Ao lado de cada
nota fica o ID da prova (ver o modelo do relatório).

Regra de prova: só pontuas o que viste hoje. "Acho que temos" do gestor não é
prova; pede o URL, a captura ou o acesso. Sem prova, é `N/V`, nunca 0.

## 1. Acesso de bots e robots.txt

**1.1 Bots de pesquisa e de pedido do utilizador entram nas páginas-chave.**
Como: `python3 scripts/verificar_bots_ia.py <site> --caminho / --caminho <lista de stock> --caminho <ficha> --caminho <contactos>`.
- 2: todos os agentes de pesquisa e de pedido do utilizador permitidos em todos os caminhos da amostra.
- 1: bloqueio só num caminho secundário, ou só de agentes secundários (por exemplo DuckAssistBot, MistralAI-User).
- 0: Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, Claude-SearchBot ou PerplexityBot bloqueados no site ou nas fichas; ou robots.txt a responder 5xx.
- N/V: o pedido falhou do lado do agente (rede, tempo esgotado), não do site.

**1.2 Sem bloqueio na firewall ou na CDN.**
Como: `python3 scripts/verificar_bots_ia.py <URL de uma ficha> --testar-acesso` (o teste pede o URL que passas como primeiro argumento). Com acesso: painel da CDN ou firewall.
- 2: 200 para os agentes de pesquisa e de pedido do utilizador, ou recusas confirmadas no painel como recusa só de imitações.
- 1: bloqueio confirmado de agentes secundários, ou desafio (captcha) intermitente.
- 0: bloqueio confirmado de agentes principais, ou desafio a todos os visitantes antes de mostrar conteúdo.
- N/V: 403 ou 429 sem acesso ao painel. Regista como suspeita e pede confirmação ao gestor ou ao fornecedor do site.

**1.3 robots.txt coerente.**
Como: lê o ficheiro e a saída do script (`robots.interpretacao`, `regra_aplicada`).
- 2: responde 200, ou 404 (tudo permitido), sem regras acidentais.
- 1: regras ambíguas ou contraditórias em caminhos secundários; CSS ou JavaScript necessários bloqueados.
- 0: `Disallow: /` geral esquecido de um ambiente de testes, ou regras que bloqueiam o stock a todos.

**Política de treino (não pontuada).** Regista se GPTBot, ClaudeBot,
Google-Extended, Applebot-Extended, CCBot, Meta-ExternalAgent e Bytespider
estão permitidos ou bloqueados, e se foi decisão do stand ou omissão da
plataforma. Bloquear treino não é falha.

## 2. Indexação e base técnica

**2.1 Páginas-chave respondem e são indexáveis.**
Como: `python3 scripts/extrair_sinais_pagina.py <url>` em cada página da amostra: `estado_http`, URL final, `meta_robots`, `x-robots-tag`, `canonico`. Com acesso: relatório de páginas do Search Console. Uma pesquisa `site:` não prova indexação.
- 2: todas 200 em HTTPS, sem `noindex`, canónico para si próprias ou para a versão certa no mesmo domínio.
- 1: problema numa página secundária, ou cadeias de redireccionamento.
- 0: início, lista de stock ou fichas com 4xx, 5xx ou `noindex`, ou canónico para outro domínio (por exemplo, o anúncio no portal).

**2.2 Factos essenciais no HTML, sem JavaScript.**
Como: compara a saída do script e o HTML em bruto com o que o navegador mostra.
- 2: preço, quilómetros, data, combustível nas fichas, e morada e telefone do stand, presentes no HTML.
- 1: parte destes factos só aparece depois de o JavaScript correr.
- 0: lista ou fichas vazias sem JavaScript, ou stock só num iframe ou widget de outro domínio.

**2.3 HTTPS, telemóvel e velocidade.**
Como: navegador em largura de telemóvel; PageSpeed Insights ou a Nota de visibilidade online do hub, na página inicial e numa ficha.
- 2: certificado válido, `http` redirecciona para `https`, nada tapa o conteúdo em telemóvel além do aviso de cookies, e a avaliação das Core Web Vitals com dados de campo a passar, quando existe.
- 1: avaliação das Core Web Vitals a falhar, ou intersticial que tapa o conteúdo até ser fechado.
- 0: certificado inválido, site sem HTTPS, ou conteúdo inacessível em telemóvel.
- Sem dados de campo, pontua só HTTPS e telemóvel e escreve-o. O detalhe técnico é de `stand-avaliar-site`.

## 3. Identidade consistente

**3.1 Nome, morada e telefone iguais em todo o lado.**
Como: compara rodapé e contactos do site, JSON-LD, Perfil de Empresa, portais e redes. Formatos equivalentes ("R." e "Rua", telefone com ou sem +351) contam como iguais.
- 2: iguais em todas as fontes verificadas.
- 1: uma divergência menor (andar, número de porta, telefone secundário).
- 0: duas ou mais divergências, ou morada ou telefone principal errado numa fonte principal.

**3.2 Quem é o stand, logo no início da página inicial.**
Como: lê as primeiras 100 palavras de texto da página inicial (não contam menus nem botões).
- 2: nome, concelho, o que vende (usados, marcas, segmentos) e um facto verificável que o distinga.
- 1: dois ou três destes elementos.
- 0: um ou nenhum, ou só slogans.

**3.3 Horário e serviços coerentes.**
Como: compara horário e lista de serviços (retoma, financiamento, garantia, oficina, entrega) no site, no Perfil de Empresa e no JSON-LD.
- 2: coincidem. 1: uma divergência. 0: divergências no horário principal ou serviços anunciados que o stand já não presta.

## 4. Dados estruturados

Antes destas verificações, lê [dados-estruturados.md](dados-estruturados.md).

**4.1 AutoDealer (ou LocalBusiness) válido e fiel.**
Como: `json_ld` da saída do script na página inicial e em contactos; horário e `sameAs` no código-fonte; validador.
- 2: `AutoDealer` (ou subtipo adequado) com `name`, `address` completo, `telephone`, `url` e `openingHoursSpecification`, iguais ao visível e sem erros no validador.
- 1: existe mas faltam dois ou mais campos, um campo diverge, ou só aparece depois do JavaScript (injectado pelo GTM, por exemplo).
- 0: não existe, é inválido, ou descreve outra entidade (dados do tema ou do fornecedor do site).

**4.2 Car com Offer nas fichas.**
Como: as três fichas da amostra.
- 2: as três com `Car` (ou `Vehicle`/`Product`), marca, modelo, quilómetros como número com `KMT`, combustível, data ou ano, e `Offer` com `price` numérico, `priceCurrency` `EUR` e `availability`, iguais ao visível.
- 1: só parte das fichas, ou faltam campos.
- 0: nenhuma ficha com marcação, ou preço ou disponibilidade diferentes do que a página mostra.

**4.3 Sem marcação enganadora.**
- 2: nenhuma das práticas abaixo.
- 1: um caso isolado (uma pergunta em `FAQPage` que não está visível).
- 0: `aggregateRating` ou `Review` sobre o próprio stand, `InStock` em viaturas vendidas, preços diferentes do visível, ou `FAQPage` com perguntas que não estão na página.

## 5. Conteúdo que responde a perguntas reais

**5.1 Perguntas de compra respondidas.**
Como: procura respostas directas, no site, a estas oito perguntas: Fazem financiamento e com que condições se pede? Aceitam retoma e como avaliam? Aceitam retoma de carro com crédito por pagar? Que garantia dão nos usados e o que cobre? Tratam do registo de propriedade e da documentação? Fazem entrega fora do concelho? Posso marcar test drive ou visita? Compram o meu carro sem eu comprar outro? Descarta as que o stand não faz (N/A).
- 2: cinco ou mais respondidas em texto claro. 1: duas a quatro. 0: uma ou nenhuma.

**5.2 Respostas extraíveis.**
- 2: em texto HTML com títulos (`h2`, `h3`) ou listas; acordeões contam se o texto está no HTML.
- 1: parte das respostas em imagens, PDF, vídeo, ou carregadas só ao clicar.
- 0: só em imagens, PDF ou vídeo, ou inexistentes.

**5.3 Linguagem factual.**
Como: três parágrafos (início, sobre, financiamento ou retoma).
- 2: a maioria das frases diz um facto verificável (o quê, onde, quanto, quando, quem).
- 1: mistura de factos e slogans.
- 0: só slogans ("os melhores preços", "qualidade e confiança").

## 6. Stock e serviços com factos citáveis

**6.1 Fichas completas em texto.**
Como: as três fichas. Campos-chave: preço, quilómetros, mês e ano da primeira matrícula, combustível, caixa, potência, garantia (prazo), origem (nacional ou importado).
- 2: todos os campos-chave em texto, com fotos da própria viatura.
- 1: faltam um ou dois campos-chave.
- 0: falta preço ou quilómetros, ou o stock só existe no portal.

**6.2 Stock actualizado.**
Como: compara a lista do site com os anúncios activos no portal, ou, com acesso, com o DMS.
- 2: viaturas vendidas saem ou aparecem como vendidas, e o sitemap não as lista como disponíveis.
- 1: casos isolados de viaturas vendidas como disponíveis.
- 0: várias viaturas vendidas à venda no site.
- N/V: sem forma de comparar.

**6.3 Páginas de serviço com URL própria.**
Como: retoma, financiamento, garantia, oficina e contactos, cada uma com URL estável e texto (não só um formulário ou um pop-up). Serviços que o stand não presta são N/A.
- 2: todas as aplicáveis existem. 1: parte. 0: nenhuma.

## 7. Presença fora do site

**7.1 Perfil de Empresa no Google.**
Como: pesquisa pelo nome; Nota de visibilidade online do hub. Detalhe em `stand-auditoria-perfil-google`.
- 2: reivindicado, categoria principal coerente com o negócio, site, telefone, horário e fotos actuais.
- 1: falta um ou dois destes elementos.
- 0: não existe, não está reivindicado, ou tem morada ou telefone errados.

**7.2 Portais e redes coerentes.**
Como: perfis do stand em Standvirtual, OLX e outros portais que use, Facebook e Instagram.
- 2: mesmo nome, telefone e morada, e ligação ao site onde o portal o permite.
- 1: uma divergência ou perfis sem ligação ao site. 0: várias divergências ou perfis abandonados com dados antigos.

**7.3 Fontes independentes.**
Como: pesquisa pelo nome do stand em imprensa regional, associações do sector, localizador da marca (se for concessionário oficial), directórios (Apple Maps, Bing Places, Páginas Amarelas). Portais pagos pelo stand e os seus próprios perfis não contam.
- 2: pelo menos duas fontes independentes descrevem o stand correctamente.
- 1: uma, ou duas com dados errados.
- 0: nenhuma encontrada.
- N/V: sem ferramenta de pesquisa.

## 8. Avaliações e reclamações

Detalhe e respostas em `stand-analisar-avaliacoes` e `stand-responder-avaliacoes`.

**8.1 Avaliações recentes no Google.**
- 2: avaliações em cada um dos últimos três meses. 1: avaliações nos últimos 12 meses, irregulares. 0: nenhuma nos últimos 12 meses.

**8.2 Respostas do stand.**
- 2: responde à maioria das avaliações recentes, incluindo as negativas, sem dados pessoais. 1: responde a algumas ou só às positivas. 0: não responde.

**8.3 Reclamações públicas tratadas.**
Como: Portal da Queixa e outras plataformas onde apareçam reclamações sobre o stand.
- 2: todas com resposta. 1: algumas sem resposta. 0: várias recentes sem resposta.
- N/A: nenhuma reclamação encontrada (não é prova de nada, por isso não conta).

## 9. Sitemap e llms.txt

**9.1 Sitemap actual.**
Como: sitemaps declarados (saída do `verificar_bots_ia.py`) ou o caminho habitual; com acesso, submissão no Search Console.
- 2: responde 200, inclui lista e fichas actuais, não inclui vendidas nem páginas com erro.
- 1: existe mas está desactualizado ou incompleto. 0: não existe ou dá erro.

**9.2 llms.txt (opcional).**
Como: `python3 scripts/validar_llms_txt.py <site>/llms.txt --verificar-links`.
- Ausente: regista "ausente" e não conta no denominador. A ausência não é falha: nenhum motor documentou que depende dele.
- 2: válido, sem ligações com problema, coerente com o site.
- 1: avisos (redireccionamentos, `http`, ligações a mais ou a menos).
- 0: erros de formato, ligações quebradas, ou factos que contradizem o site. Um ficheiro errado é pior do que nenhum.

## 10. Testes ao vivo nos motores

Protocolo e perguntas em [bots-e-testes.md](bots-e-testes.md). Pontua só os motores testados.

**10.1 Descoberta sem o nome do stand.**
- 2: o stand aparece em pelo menos metade das execuções, em pelo menos dois motores. 1: aparece em alguma execução. 0: nunca aparece.

**10.2 Exactidão com o nome do stand.**
- 2: sem erros materiais (morada, telefone, horário, o que vende, se está aberto). 1: erros menores ou dados desactualizados. 0: um erro material, ou confusão com outro stand.

**10.3 Fontes citadas.**
- 2: o site do stand aparece como fonte em todos os motores testados. 1: só em alguns, ou só os perfis do stand (Perfil Google, portal). 0: nenhuma fonte do stand.

## Cálculo

- Nota da dimensão (0 a 10) = 10 × pontos ÷ (2 × verificações pontuadas). Sem verificações pontuadas, a dimensão é `N/V`.
- Nota global (%) = soma dos pontos ÷ soma dos máximos das verificações pontuadas × 100.
- Cobertura = verificações pontuadas ÷ verificações aplicáveis (as que não são N/A).
- Com cobertura abaixo de 70%, a nota é **provisória** e não leva banda.

Bandas (convenção desta skill, não um padrão do sector): 80 a 100 base sólida;
60 a 79 lacunas a corrigir; 40 a 59 lacunas graves; abaixo de 40 bloqueios de base.

## Bloqueios críticos

Lideram o veredicto, seja qual for a nota: bots de pesquisa principais
bloqueados no site ou nas fichas; robots.txt em 5xx; `noindex` ou erros nas
páginas de stock; preço e quilómetros só com JavaScript, ou stock só num
iframe do portal; morada ou telefone errados no Perfil de Empresa ou nas
respostas dos motores; motores a dizer que o stand fechou.
