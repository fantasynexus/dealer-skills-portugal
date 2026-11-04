# Grelha da medição de tráfego de IA: 100 pontos

Pontua a qualidade da medição, não o volume. Um stand com 15 visitas de IA bem medidas e ligadas ao CRM pode ter nota alta; um com 500 visitas misturadas em Referral, não.

## Regras

- Cada critério tem **total**, **parcial** ou **zero**. Parcial vale metade, arredondada para baixo.
- `N/V` quando não houve acesso para verificar: sai do denominador. Falta de acesso não é falha do stand. Falta de configuração, verificada com acesso, é zero.
- Nota = pontos obtidos ÷ pontos verificáveis × 100, arredondada às unidades, sempre com a cobertura ao lado.
- Em Configurar, pontua o estado de partida e volta a pontuar depois de, pelo menos, um mês de dados com o canal.
- Prova aceitável: captura ou exportação com data, ligação para o relatório ou a exploração, saída de um script. "Disseram-me que existe" não é prova: fica `N/V` até se ver.

## 1. Detecção e manutenção de referenciadores: 15

| Critério | Pts | Onde | Total | Parcial | Zero |
|---|---|---|---|---|---|
| 1.1 Lista de origens de IA escrita e datada | 5 | descrição do grupo de canais, documento da equipa | Lista revista nos últimos três meses | Lista sem data ou com mais de três meses | Não existe |
| 1.2 Cobertura das origens que aparecem nos dados | 6 | `classificar_referencias_ia.py` sobre o período | Todas as origens de IA do período estão na regra | Ficam de fora origens com poucas sessões | Fica de fora uma origem com peso (ex.: `chatgpt.com`), ou não há regra |
| 1.3 Sem falsos positivos | 4 | grupo de canais com a origem como dimensão secundária | Só origens de IA no canal | Uma origem duvidosa, assinalada | Apanha `google`, `bing` ou outras que não são IA, ou não há regra |

## 2. Grupo de canais, dimensão e exploração GA4: 15

| Critério | Pts | Onde | Total | Parcial | Zero |
|---|---|---|---|---|---|
| 2.1 Grupo de canais com canal de IA | 6 | Admin > Data display > Channel groups | Existe e é usado nos relatórios | Existe mas está incompleto ou ninguém o usa | Não existe: visitas de IA em Referral ou Unassigned |
| 2.2 Posição e verificação | 5 | relatório de aquisição com o grupo e a origem | Acima de Referral, verificado sem fugas | Acima de Referral, sem verificação | Abaixo de um canal que o apanha, ou não há canal |
| 2.3 Exploração ou relatório guardado | 4 | Explore | Motor, página de entrada e eventos-chave, guardado e partilhado | Falta um dos três | Não existe |

Uma dimensão personalizada criada no GTM não dá pontos extra: a origem da sessão já identifica o motor.

## 3. Volume, tendência e qualidade por motor: 10

| Critério | Pts | Onde | Total | Parcial | Zero |
|---|---|---|---|---|---|
| 3.1 Sessões por motor e por mês | 4 | exploração ou origem da sessão | Reportável para todo o período | Só o total de IA | Não reportável |
| 3.2 Tendência | 3 | exploração por mês | Três meses ou mais, ou período homólogo | Menos de três meses | Só um número |
| 3.3 Envolvimento por motor | 3 | exploração | Sessões envolvidas e tempo de envolvimento por motor | Só para o total | Não |

## 4. Páginas de entrada e intenção: 10

| Critério | Pts | Onde | Total | Parcial | Zero |
|---|---|---|---|---|---|
| 4.1 Páginas de entrada identificadas | 4 | exploração com página de entrada | Lista completa do período | Só as principais, sem exportação | Não |
| 4.2 Tipo de página | 3 | URL ou padrão de URL | Todas as páginas com tipo | Parte | Não |
| 4.3 Desajustes assinalados | 3 | abrir as páginas | Viaturas vendidas, 404 e páginas sem contacto listadas, com acção | Listadas sem acção | Não analisado |

## 5. Eventos, leads e vendas no CRM: 15

| Critério | Pts | Onde | Total | Parcial | Zero |
|---|---|---|---|---|---|
| 5.1 Eventos-chave de contacto | 5 | Admin > eventos-chave; detalhe em `stand-auditoria-ga4-google-ads` | Formulário, WhatsApp e chamada (os que o site tem) marcados, sem duplicação evidente | Só parte, ou duplicação por resolver | Nenhum evento-chave de contacto |
| 5.2 Eventos-chave por motor | 4 | exploração | Reportáveis por motor | Só no total de IA | Não |
| 5.3 Origem no lead | 4 | CRM e formulário | Campo de origem preenchido nos leads do site | Só "Como nos conheceu?" declarado, ou campo preenchido às vezes | Nenhum |
| 5.4 Leads de IA até venda | 2 | CRM | Vendas com origem em IA contadas no período | Leads identificados, desfecho não | Não |

## 6. Comparação com orgânico e outros canais: 10

| Critério | Pts | Onde | Total | Parcial | Zero |
|---|---|---|---|---|---|
| 6.1 Mesmas métricas lado a lado | 5 | exploração sem filtro de canal | IA, orgânico, directo, referral e pago, mesmo período e métricas | Só IA e orgânico | Não |
| 6.2 Peso da IA com denominador | 3 | relatório | "x sessões de IA em y sessões no total" | Percentagem sem denominador | Não calculado |
| 6.3 Cautelas escritas | 2 | relatório | Amostra pequena, consentimento e visitas sem referenciador explicados | Só uma delas | Nenhuma |

## 7. Search Console e mudanças de CTR: 10

| Critério | Pts | Onde | Total | Parcial | Zero |
|---|---|---|---|---|---|
| 7.1 Comparação de períodos | 4 | Search Console > Performance | Por consulta e por página, no período auditado | Só totais | Com acesso e não feita |
| 7.2 Consultas suspeitas como hipótese | 3 | mesmo relatório | Cliques a descer com impressões e posição estáveis, listadas como hipótese | Listadas sem ver a posição | Não analisado, ou apresentadas como facto |
| 7.3 Verificação na página de resultados | 3 | pesquisa Google com data e local | As principais verificadas, com captura | Algumas | Nenhuma |

Até à data desta grelha, o Search Console não separa os resumos de IA nos relatórios de desempenho; segundo a Google, os dados do AI Mode entram nos totais. Confirma se já existe um filtro próprio e, se existir, usa-o em 7.1.

## 8. Crawlers de IA: robots, logs e resposta técnica: 15

| Critério | Pts | Onde | Total | Parcial | Zero |
|---|---|---|---|---|---|
| 8.1 robots.txt verificado por bot | 4 | `verificar_bots_ia.py` | Todos os bots e os caminhos importantes | Só alguns bots ou só a raiz | Não |
| 8.2 Decisão documentada | 3 | documento do dono do site | Por bot: permitir ou bloquear, porquê, quem e quando | Decisão geral sem pormenor | Ninguém sabe porque está assim |
| 8.3 Sem bloqueios não intencionais | 3 | `--testar-acesso`, regras do CDN | O que o servidor e o CDN fazem coincide com a decisão do dono | Diferenças só em bots secundários | Bots de pesquisa recusados sem o dono saber |
| 8.4 Pedidos reais por bot | 5 | logs ou painel do CDN | Pedidos, páginas e estados por bot no período, com IP verificado nos principais | Contagens por bot sem páginas, ou sem verificação de IP | Fonte disponível e não analisada |

Sem logs nem painel do CDN, 8.4 é `N/V`. Um resultado de 403 no teste de acesso sem confirmação nas regras do CDN deixa 8.3 em `N/V`, com a pergunta para quem gere o site.

## Exemplo resolvido (fictício)

Stand Exemplo, Leiria (fictício). Auditoria de Agosto a Outubro de 2026. Leitura no GA4 e no Search Console; sem logs; site no Cloudflare, sem acesso ao painel. Os números são inventados.

Saída do script sobre a exportação de origens: `chatgpt.com` 38 sessões, `perplexity.ai` 5, `gemini.google.com` 3, `copilot.microsoft.com` 1. Por classificar: `standvirtual.com`, `m.facebook.com`, `l.instagram.com`, que não são IA. Todas as de IA estão em Referral. Eventos-chave vindos dessas origens: 2.

| Área | Pontos | Porquê |
|---|---|---|
| 1. Referenciadores | 0 de 15 | Sem lista nem regra |
| 2. Grupo de canais | 0 de 15 | Não existe; IA em Referral |
| 3. Volume e tendência | 10 de 10 | Reportáveis por motor e por mês pela origem da sessão, mesmo sem canal |
| 4. Páginas de entrada | 4 de 10 | Identificadas, sem tipo nem desajustes |
| 5. Eventos e CRM | 9 de 15 | Formulário e WhatsApp marcados e reportáveis por motor; o CRM não guarda a origem |
| 6. Comparação | 5 de 10 | Tabela lado a lado; sem denominador nem cautelas |
| 7. Search Console | 4 de 10 | Comparação feita; nada listado nem verificado |
| 8. Crawlers | 4 de 7 verificáveis | robots.txt verificado (4); sem decisão documentada (0); 403 para GPTBot e ClaudeBot no teste, com o robots.txt a permitir, por confirmar no Cloudflare (`N/V`); sem logs (`N/V`) |

Total: 36 pontos em 92 verificáveis, nota 39. Resumo para o gestor: "47 sessões de assistentes de IA em três meses, 38 delas do ChatGPT, misturadas em Referral; 2 contactos; nenhum ligado a venda porque o CRM não guarda a origem." Prioridades: criar o canal (passo a passo de [ga4-canal-ia.md](ga4-canal-ia.md)), perguntar a quem gere o Cloudflare se há bloqueio de bots de IA activo, e acrescentar o campo de origem no CRM.
