# Grelha de 100 pontos: GA4, Google Ads e GTM

Lê antes de pontuar. Cada critério diz onde verificar, que prova aceitar e o que dá total, parcial ou 0.

## Regras de pontuação

- **Prova aceitável:** captura de ecrã com data e conta visíveis; exportação do relatório; pedido no separador Network com o parâmetro visível; evento no DebugView; registo do CRM com ID interno (sem dados pessoais). Uma afirmação da agência sem prova não conta.
- **`N/V` (não verificado):** sem acesso ou sem prova. Sai do denominador. Nunca é 0.
- **`N/A` (não aplicável):** o critério não existe no stand (por exemplo, sem Google Ads ou sem simulador). Sai do denominador e diz-se porquê.
- **Na dúvida entre dois níveis, dá o mais baixo** e escreve o que faltou para o mais alto.
- **Nota** = pontos obtidos ÷ pontos verificados × 100. **Cobertura** = pontos verificados ÷ 100. Com cobertura abaixo de 60 %, a nota é indicativa e o relatório diz isso na primeira linha.
- Os caminhos no interface estão em inglês, como a Google os mostra por omissão; noutra língua ou depois de uma actualização podem mudar. Confirma no ecrã e regista o caminho que encontraste.

## Falhas críticas

Saem no topo do relatório, independentemente da nota:

- dados pessoais (email, telefone, nome, NIF, matrícula) em parâmetros de eventos, em URLs enviados ao GA4 ou em pedidos ao Ads sem cifra;
- etiquetas de publicidade ou de análise a gravar cookies antes de qualquer escolha no aviso de cookies, quando o stand diz usar consentimento prévio;
- a mesma acção contada duas vezes como conversão primária no Ads;
- conversão primária que dispara sem envio real (clique no botão, página vista, erro de validação);
- contas sem nenhum administrador do stand (só da agência ou de um ex-colaborador).

## 1. Propriedade, fluxos, filtros internos e retenção (8)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 1.1 Propriedade canónica | 3 | Network, filtro `collect`, parâmetro `tid=G-…` em três tipos de página; Tag Assistant; Admin > Property details | Um só ID de produção em todas as páginas e dados em Realtime | Segundo ID activo (propriedade antiga, plataforma do site, agência anterior) sem razão escrita: 1 | Sem GA4 ou sem dados |
| 1.2 Fluxo e tráfego interno | 2 | Admin > Data streams > fluxo web > Configure tag settings > Define internal traffic; Admin > Data filters | Domínio certo, regra de tráfego interno para os IP do stand e da agência, filtro activo | Regra criada mas filtro em teste, ou IP desactualizados: 1 | Nada definido |
| 1.3 Fuso e moeda | 1 | Admin > Property details | `Europe/Lisbon` (ou `Atlantic/Azores` para um stand nos Açores) e EUR | | Outro fuso ou moeda |
| 1.4 Retenção | 1 | Admin > Data retention | Retenção de eventos no máximo que a propriedade permite (confirma as opções no ecrã) | | No mínimo por omissão sem decisão escrita |
| 1.5 Referências indesejadas | 1 | Configure tag settings > List unwanted referrals | Domínios de simuladores, pagamentos ou formulários externos para onde o visitante sai e volta estão listados | | Regressos desses domínios aparecem como `referral` e roubam a origem |

## 2. Taxonomia de eventos e parâmetros de viatura e origem (12)

Compara com [taxonomia-eventos.md](taxonomia-eventos.md). Nomes diferentes dos propostos não perdem pontos se forem consistentes e documentados.

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 2.1 Eventos de contacto | 4 | Admin > Events (30 dias); DebugView com os testes | Há evento para cada canal que o site oferece: formulário enviado, telefone, WhatsApp, email, mapa | Falta um ou dois canais: 2 | Só eventos automáticos |
| 2.2 Eventos de stock | 3 | DebugView numa listagem e numa ficha | Ficha de viatura e listagem identificáveis por evento ou por `tipo_pagina` | Só por URL, sem padrão fiável: 1 | Impossível separar fichas de outras páginas |
| 2.3 Parâmetros | 3 | DebugView; Admin > Custom definitions | `viatura_id`, marca, modelo, `tipo_lead`, `tipo_pagina` presentes e registados como dimensões, com valores normalizados | Presentes mas não registados, ou valores misturados ("Gasóleo", "diesel", "GASOLEO"): 1 | Sem parâmetros |
| 2.4 Sem dados pessoais nem ruído | 2 | Network nos testes; relatório de eventos ordenado por contagem | Nenhum dado pessoal; nenhum evento com contagem absurda face às páginas vistas | | Dado pessoal encontrado (é também falha crítica) ou evento a disparar em cada scroll ou movimento |

## 3. Eventos-chave sem duplicação (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 3.1 Lista escrita | 3 | Admin > Key events; documento do stand ou da agência | Só estão marcadas as acções acordadas como contacto, e a lista existe por escrito | Lista certa mas não escrita, ou `form_start`, `page_view` ou `scroll` marcados: 1 | Nenhum ou tudo marcado |
| 3.2 Um envio, um evento | 4 | Teste de cada formulário: DebugView e Network | O evento de lead dispara uma vez, só depois da confirmação de envio | Dispara no clique antes da validação, ou duas vezes num dos formulários: 2 | Duplicado ou disparado sem envio em todos |
| 3.3 Fontes concorrentes | 3 | Network: quem envia o evento (GTM, código da plataforma do site, plugin do formulário, widget de chat) | Uma só fonte por evento | Duas fontes com o mesmo nome, mas só uma marcada como chave: 1 | Duas fontes a contar como evento-chave |

## 4. Conversões no Google Ads: origem, janela e contagem (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 4.1 Inventário com origem | 2 | Goals > Conversions > Summary | Cada acção tem nome claro, origem identificada (site, GA4, chamadas, importação, formulário de leads) e estado activo ou removido | Acções antigas activas sem dono: 1 | Não se sabe o que cada acção mede |
| 4.2 Primárias e secundárias | 3 | Coluna de optimização da acção | Primárias só as que representam contacto real; cliques e micro-acções são secundárias | Um clique (telefone, WhatsApp) como primária sem decisão escrita: 1 | Visitas de página ou scroll como primárias |
| 4.3 Contagem | 3 | Definições da acção > Count | Leads com contagem "One" (Uma), salvo razão escrita | | "Every" em leads sem razão |
| 4.4 Janela e atribuição | 2 | Definições da acção | Janela e modelo escolhidos e escritos, coerentes com o tempo que o stand demora a fechar | Por omissão sem decisão: 1 | Modelos diferentes entre acções comparadas, sem explicação |

## 5. Ligação GA4 e Ads, e etiquetagem automática (8)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 5.1 Ligação activa | 3 | GA4 Admin > Product links > Google Ads links; Ads > ferramentas de contas ligadas | Ligação activa à conta certa | Ligada a uma conta antiga ou de teste: 1 | Sem ligação |
| 5.2 Etiquetagem automática e `gclid` | 3 | Ads > definições da conta (auto-tagging); teste com `?gclid=TESTE_AUDITORIA` | Ligada, e o parâmetro sobrevive a redireccionamentos e chega à página final | Ligada mas um redireccionamento (http para https, idioma, `www`) apaga parâmetros: 1 | Desligada |
| 5.3 Sem dupla contagem | 2 | Lista de acções: mesma acção via tag Ads e via importação GA4 | Só uma das duas é primária | | As duas primárias (é também falha crítica) |

## 6. Formulários, chamadas, WhatsApp e domínios externos (12)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 6.1 Todos os formulários | 4 | Lista de formulários do script e da navegação; teste de cada um | Todos medidos, incluindo os embebidos de fornecedores (CRM, simulador, marcação de oficina) | Algum embebido em `iframe` sem medição: 2 | Só o formulário de contacto geral |
| 6.2 Domínios externos | 3 | Teste de saída e regresso; Configure your domains | Medição entre domínios onde o stand controla os dois lados; onde não controla, clique de saída medido e domínio em referências indesejadas | Saída medida mas regresso parte a sessão: 1 | Perda total da origem |
| 6.3 Telefone e WhatsApp | 3 | Teste dos links `tel:`, `wa.me` e `api.whatsapp.com` em telemóvel | Cliques medidos com `posicao_cta` e `departamento`; chamadas reais vêm da plataforma de rastreio (ver `stand-auditoria-rastreio-chamadas`) | Só alguns botões medidos: 1 | Nada medido |
| 6.4 Canais fora do site | 2 | Mapa do fluxo; CRM por origem | Portais, formulários de leads do Google e redes estão separados como canais que o GA4 não vê | | Contados como falha do GA4 ou misturados com o site |

## 7. GTM: titularidade, versões e tags obsoletas (8)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 7.1 Titularidade | 2 | Admin > User management em GTM, GA4 e Ads | Pelo menos um administrador é uma conta do próprio stand | Só a agência actual administra, com acesso de leitura ao stand: 1 | Ninguém do stand tem acesso |
| 7.2 Versões | 2 | Versions | Versões publicadas com nome e nota do que mudou; pré-visualização usada antes de publicar | Versões sem notas: 1 | Publicações sem rasto |
| 7.3 Tags obsoletas | 2 | Tags: fornecedores antigos, Universal Analytics, píxeis sem contrato | Nenhuma activa | Uma ou duas por limpar: 1 | Várias, incluindo concorrentes de análise |
| 7.4 Accionadores | 2 | Triggers das tags de conversão | Específicos (envio confirmado, evento do `dataLayer`) | Algum por "todos os cliques" sem conversão associada: 1 | Conversão disparada por cliques genéricos |

## 8. Consentimento, Consent Mode e cookies (12)

Verifica o funcionamento, não a legalidade. A conformidade com o RGPD e a Lei n.º 41/2004 (confirmar versão e orientações da CNPD em vigor) é do encarregado de protecção de dados ou de um jurista.

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 8.1 Aviso de cookies | 4 | Janela anónima, primeira visita; Application > Cookies antes de clicar | Recusar tão fácil como aceitar, sem caixas pré-seleccionadas, sem cookies de análise ou publicidade antes da escolha | Recusa escondida num segundo ecrã, ou um cookie não essencial antes da escolha: 2 | Sem aviso, ou aviso que não bloqueia nada |
| 8.2 Consent Mode v2 | 4 | Network: estado por omissão antes das etiquetas e actualização depois da escolha (parâmetros `gcs` e `gcd`; confirma o significado na documentação actual da Google) | Os quatro sinais (`ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`) com valor por omissão e actualizados | Só dois sinais, ou actualização tardia: 2 | Ausente |
| 8.3 Modo decidido | 2 | Configuração da CMP e das etiquetas; decisão escrita | Modo básico ou avançado escolhido e validado pelo EPD ou jurista | Escolhido sem validação: 1 | Ninguém sabe |
| 8.4 Política coerente | 2 | Política de cookies contra os scripts encontrados | A política lista o que o site carrega | Lista desactualizada: 1 | Sem política |

## 9. Importação offline do CRM e ciclo lead-venda (12)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 9.1 Identificadores no CRM | 4 | Lead de teste do passo 3 | `gclid`, `gbraid`, `wbraid` e `utm_*` chegam ao registo do lead | Só UTM, ou só em alguns formulários: 2 | Nada chega |
| 9.2 Etapas com data | 3 | Exportação do CRM | Lead, lead válido, oportunidade e venda são campos ou estados com data | Etapas existem mas sem data, ou sem regra de validade: 1 | Só "lead" |
| 9.3 Mecanismo de importação | 3 | Goals > Conversions > Uploads, ou integração | Importação regular (manual, integração ou conversões optimizadas para leads) dentro da janela que a Google aceita (confirmar) | Feita uma vez ou irregular: 1 | Nenhuma |
| 9.4 Valor decidido | 2 | Definição da acção importada | Valor ou regra de valor escrita pelo gestor (fixo por venda, por categoria, ou nenhum) | Valor por omissão da Google sem decisão: 1 | Margens ou preços reais enviados sem autorização |

## 10. Reconciliação e monitorização (8)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 10.1 Reconciliação | 4 | Tabela de [reconciliacao.md](reconciliacao.md) ou equivalente do stand | Feita com definições escritas, mesmo período e fuso, diferenças explicadas | Feita sem definições ou com períodos diferentes: 2 | Nunca feita |
| 10.2 Alertas | 2 | Alertas do GA4 ou do Ads, ou rotina escrita | Alguém é avisado se o evento de lead cai a zero ou a importação pára | Verificação manual sem data fixa: 1 | Ninguém olha |
| 10.3 Registo de alterações | 2 | Documento partilhado entre stand e agência | Cada alteração de site, GTM ou conversões tem data e autor | Parcial: 1 | Nenhum |
