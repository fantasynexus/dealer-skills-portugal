# Pilares, triagem e encaminhamento

Lê isto no passo 3. A triagem não é uma auditoria: cada verificação demora minutos, serve para classificar o pilar e decidir que skill aprofunda. Se uma verificação exigir mais do que isso, pára e põe a auditoria no roteiro.

## Como classificar um pilar

| Estado | Quando |
|---|---|
| `Forte` | Nenhum sinal de alerta nas verificações feitas, e pelo menos metade delas com prova medida ou observada. |
| `Misto` | Um ou dois sinais de alerta sem bloqueio, ou provas só parciais. |
| `Fraco` | Três ou mais sinais de alerta, ou um bloqueio. |
| `N/V` | Menos de metade das verificações foi possível. Não adivinhes o estado. |

Regista o tipo de prova de cada linha:

- **medido:** dados de uma conta (Search Console, GA4, Perfil, CRM) ou auditoria com data e cobertura;
- **observado:** verificação pública feita nesta sessão, com data e local;
- **declarado:** o gestor ou a equipa dizem, sem prova à vista;
- **N/V:** não verificado.

Quando o modo é B e a prova vem de uma auditoria de outra skill com nota de 0 a 100, usa esta regra da casa (não é padrão do sector): 75 ou mais `Forte`, 50 a 74 `Misto`, menos de 50 `Fraco`. Se a auditoria teve cobertura abaixo de metade, junta "(cobertura baixa)" ao estado.

## Pilar 1. Base técnica

Cobre o que torna o site legível por pessoas, pelo Google e pelos motores de IA: indexação, velocidade no telemóvel, segurança, dados estruturados, páginas de viatura legíveis, consentimento que não parte a medição.

| Verificação | Onde | Sinal de alerta |
|---|---|---|
| robots.txt | `https://dominio/robots.txt` | `Disallow: /` para todos ou para Googlebot; bots de IA bloqueados sem decisão consciente do stand (regista, não decides tu) |
| Páginas de viatura indexáveis | Código-fonte de duas viaturas: `meta robots`, canónico | `noindex`, canónico para outra viatura ou para a listagem |
| Índice | Search Console, relatório de páginas (com acesso) | Viaturas ou páginas principais excluídas sem motivo |
| Domínio único e HTTPS | Abrir `http://` e a variante com e sem `www` | Duas versões abertas sem redireccionamento |
| Telemóvel | Página inicial e uma viatura no telemóvel; [PageSpeed Insights](https://pagespeed.web.dev) | Conteúdo que salta, botões de contacto escondidos, dados de campo maus quando existem |
| Stock legível | Código-fonte de uma listagem | Viaturas só aparecem depois de JavaScript ou dentro de um iframe de outro domínio (hipótese a confirmar) |
| Dados estruturados | [Teste de resultados enriquecidos](https://search.google.com/test/rich-results) numa viatura e na página inicial | Ausentes, ou com preço e quilómetros diferentes do que se vê |
| Banner de cookies | Primeira visita | Não deixa recusar, ou etiquetas disparam antes da escolha |

Encaminha:

- auditoria técnica completa: `stand-avaliar-site`;
- indexação, canónicos e sitemaps: `stand-auditoria-seo`;
- qualidade das páginas e anúncios de viatura: `stand-rever-anuncios-viaturas`;
- site noutras línguas: `stand-seo-multilingue`;
- consentimento e etiquetas: `stand-auditoria-ga4-google-ads`.

## Pilar 2. Google e pesquisa local

Cobre a lista de resultados, o Maps e o Perfil de Empresa: páginas que respondem às intenções reais, consistência local, autoridade.

| Verificação | Onde | Sinal de alerta |
|---|---|---|
| Perfil de Empresa | Pesquisa pelo nome e no Maps | Ausente, nome com palavras-chave a mais, categoria errada, telefone ou horário diferentes do site |
| Identidade consistente | Site, Perfil, página do stand nos portais usados, Facebook | Nome, morada ou telefone diferentes entre fontes |
| Pesquisas de teste | Três pesquisas do mapa de procura, com local definido | O stand não aparece nas pesquisas com o próprio concelho (observação, não medição) |
| Consultas reais | Search Console, últimos três meses (com acesso) | Quase só consultas com o nome do stand; páginas de viatura sem impressões |
| Páginas de intenção | Menu e mapa do site | Sem página própria para financiamento, retoma, oficina ou contactos com morada |
| Páginas locais | Páginas por concelho | Páginas para concelhos onde o stand não está nem serve, com texto trocado só no nome |

Encaminha:

- auditoria SEO completa: `stand-auditoria-seo`;
- Perfil de Empresa: `stand-auditoria-perfil-google`;
- conteúdo novo ou reescrito: `stand-brief-conteudo-aeo`;
- pesquisas "stand A vs stand B": `stand-pagina-comparacao`.

## Pilar 3. Motores de IA (AEO/GEO)

Cobre ser compreendido e citado: acesso dos bots, identidade coerente, respostas citáveis, fontes externas, testes ao vivo.

| Verificação | Onde | Sinal de alerta |
|---|---|---|
| Teste exploratório | Três a cinco perguntas (uma com o nome do stand, duas locais sem marca, uma de serviço) em um ou dois motores disponíveis | O motor não conhece o stand, ou dá morada, horário, marcas ou serviços errados |
| Fontes citadas | Ligações mostradas nas respostas | Só portais e directórios, nunca o site do stand; fontes desactualizadas |
| Acesso dos bots | robots.txt (pilar 1) | Bots de pesquisa de IA bloqueados sem decisão consciente |
| `llms.txt` | `https://dominio/llms.txt` | Só regista se existe; é ajuda de descoberta, não factor garantido |
| Respostas citáveis | Páginas de financiamento, retoma, garantia, oficina | Texto promocional sem factos concretos (condições, prazos, o que inclui) |

Regista cada pergunta com data, motor, modelo se visível, sessão, localização e idioma. Três a cinco perguntas não são linha de base; a linha de base é trabalho de `stand-visibilidade-ia`.

Encaminha:

- causas técnicas e de conteúdo: `stand-auditoria-aeo`;
- linha de base de menções e citações: `stand-visibilidade-ia`;
- erros e informação desactualizada nas respostas: `stand-monitorizar-reputacao-ia`;
- `llms.txt`: `stand-gerar-llms-txt`;
- visitas vindas de IA no GA4: `stand-analisar-trafego-ia`;
- páginas com respostas citáveis: `stand-brief-conteudo-aeo`.

## Pilar 4. Reputação e presença fora do site

Cobre avaliações, respostas, menções externas e coerência nos portais. Pesa no Google local e na forma como os motores de IA descrevem o stand.

| Verificação | Onde | Sinal de alerta |
|---|---|---|
| Avaliações no Google | Perfil do stand e de dois ou três concorrentes locais semelhantes | Poucas face aos concorrentes, a mais recente com meses, negativas sem resposta |
| Outras avaliações | Portais e redes que o stand usa | Notas ou volumes muito diferentes entre plataformas, sem explicação |
| Reclamações públicas | Pesquisa pelo nome com "reclamação" ou "opiniões"; sites de queixas públicas, como o Portal da Queixa | Padrão repetido sem resposta (regista o tema, nunca nomes de clientes) |
| Menções externas | Imprensa local, associações do sector a que o stand pertença, clubes e patrocínios | Nenhuma fonte independente fala do stand |
| Página nos portais | Standvirtual, OLX ou outros que o stand use | Nome, morada, horário ou telefone diferentes do site |

Encaminha:

- análise de avaliações por tema: `stand-analisar-avaliacoes`;
- respostas a avaliações: `stand-responder-avaliacoes`;
- o que os motores de IA dizem: `stand-monitorizar-reputacao-ia`;
- correcções no Perfil: `stand-auditoria-perfil-google`.

## Bloqueios que passam à frente

Um bloqueio vai para `agora` e o plano diz que as acções dependentes esperam por ele.

1. Site ou páginas de viatura fora do índice por `noindex`, robots.txt ou canónicos errados.
2. Perfil de Empresa suspenso, duplicado, sem acesso do stand ou com morada ou telefone errados.
3. Nome, morada ou telefone diferentes entre site, Perfil e portais.
4. Stock que o Google não consegue ler (confirmado por `stand-avaliar-site` ou `stand-auditoria-seo`).
5. Contas (Search Console, GA4, Perfil) em nome de terceiros sem acesso do stand: sem elas não há linha de base.
6. Nenhuma forma de ligar contactos à origem: sem isto não se avalia o plano. Encaminha para `stand-auditoria-ga4-google-ads` e `stand-auditoria-rastreio-chamadas`.

## Como os pilares se reforçam

Dá prioridade a acções que mexem em mais de um pilar:

- identidade igual em todas as fontes ajuda o Google local e a exactidão das respostas de IA;
- uma página de financiamento ou retoma com factos concretos serve a lista de resultados e é citável;
- avaliações frequentes e respondidas pesam no Perfil e na descrição que os motores fazem do stand;
- medição montada antes do conteúdo permite saber o que resultou.

Se o stand não tem nada de concreto a dizer sobre si (provas, diferenças, condições), o conteúdo sai genérico em qualquer pilar. Nesse caso, põe `stand-posicionamento` antes da produção de conteúdo.

## Encaminhamento rápido

| O gestor diz | Skill |
|---|---|
| "Não sei por onde começar" | `stand-por-onde-comecar` |
| "O site é lento" ou "está mal feito" | `stand-avaliar-site` |
| "Não aparecemos no Google" | `stand-auditoria-seo` |
| "O nosso Google Maps está errado" | `stand-auditoria-perfil-google` |
| "O ChatGPT não nos conhece" | `stand-auditoria-aeo`, depois `stand-visibilidade-ia` |
| "O ChatGPT diz coisas erradas sobre nós" | `stand-monitorizar-reputacao-ia` |
| "Recebemos visitas do ChatGPT?" | `stand-analisar-trafego-ia` |
| "Precisamos de textos para o site" | `stand-brief-conteudo-aeo` |
| "Temos clientes estrangeiros" | `stand-seo-multilingue` |
| "Os anúncios das viaturas não convertem" | `stand-rever-anuncios-viaturas` |
| "Há visitas mas poucos contactos" | `stand-auditoria-cta` |
| "Os números do Google Ads não batem" | `stand-auditoria-ga4-google-ads` |
| "Somos iguais aos outros" | `stand-posicionamento` |
| "Temos poucas avaliações" | `stand-analisar-avaliacoes`, `stand-responder-avaliacoes` |

## Rever uma proposta de agência (modo D)

Para cada linha da proposta, diz em que pilar cai e se fecha uma lacuna encontrada na triagem. Depois procura estes sinais de alerta:

- garante primeiro lugar, um número de posições ou presença em respostas de IA;
- vende pacotes de ligações (backlinks) ou artigos patrocinados em massa: confirma as políticas de spam da Google em vigor;
- propõe páginas por concelho onde o stand não tem presença real, ou conteúdo produzido em escala sem revisão;
- relatórios só com posições e impressões, sem contactos nem vendas;
- Search Console, GA4, Perfil de Empresa ou domínio ficam em nome da agência;
- fidelização longa sem saída nem entrega dos conteúdos e acessos;
- propõe mudar de site antes de pedir ao fornecedor actual o que falta;
- não diz quem escreve, quem revê e com que fontes sobre o stand.

Não avalies preço contra "valores de mercado". Diz o que a proposta cobre, o que falta e que perguntas fazer à agência.
