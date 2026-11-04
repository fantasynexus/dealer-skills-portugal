---
name: stand-analisar-trafego-ia
description: Configurar ou auditar a medição das visitas que chegam ao site de um stand automóvel vindas de assistentes de IA (ChatGPT, Perplexity, Gemini, Copilot, Claude e outros) e dos bots de IA que lêem o site. Usar quando o gestor pergunta "quantas visitas nos vêm do ChatGPT?", "a IA traz clientes ao site?", "como vejo o tráfego de IA no Google Analytics?", "criar um canal de IA no GA4", "os leads do site vêm da IA?", "os bots de IA conseguem ler o nosso site?" ou "o robots.txt bloqueia o GPTBot?". Inclui o passo a passo do grupo de canais personalizado no GA4, a classificação de exportações do GA4 por motor de IA, páginas de entrada, ligação a leads e vendas no CRM, sinais no Search Console e a verificação do robots.txt, do acesso e dos logs para cada bot de IA.
---

# Tráfego vindo de IA

Mede duas coisas diferentes, sempre em secções separadas:

- **Visitas humanas** que chegam de um assistente (alguém clicou numa ligação da resposta). Vêem-se no GA4, no Search Console e no CRM.
- **Bots de IA** que lêem o site para treinar modelos, alimentar pesquisa ou responder ao pedido de um utilizador. Vêem-se no robots.txt, nos logs do servidor e no painel do CDN. O GA4 não os mostra: a maioria não executa JavaScript e o GA4 exclui bots conhecidos.

O resto do trabalho sobre IA pertence a outras skills:

| O gestor quer saber | Skill |
|---|---|
| Quantas visitas e contactos a IA traz ao site, e que bots o lêem | esta |
| Se a IA cita ou recomenda o stand | `stand-visibilidade-ia` |
| Se o que a IA diz do stand é verdade | `stand-monitorizar-reputacao-ia` |
| Se o GA4, os eventos, o consentimento e o Google Ads estão bem montados | `stand-auditoria-ga4-google-ads` |
| Porque é que o site não é lido nem citado | `stand-auditoria-aeo` |

## Antes de começar

1. Pergunta: URL do site; propriedade GA4 e o papel que te deram; acesso ao Search Console; quem aloja o site e se há CDN (Cloudflare ou outro); se há logs e quem os pode exportar; que CRM ou DMS regista os leads e se guarda a origem; período (últimos 90 dias por omissão, mais o mesmo período do ano anterior se existir).
2. Escolhe o modo:
   - **Configurar:** não há canal nem relatório de IA. Entregas o passo a passo; só o executas tu com acesso de edição e autorização explícita.
   - **Auditar:** já há dados. Validas a implementação, fazes a linha de base e pontuas.
   - **Público:** sem acesso a nada. Só o robots.txt e o teste de acesso dos bots; o resto fica `N/V`.
3. **Consentimento.** Confirma se o GA4 só carrega depois do consentimento e como está o Consent Mode (lista de controlo: Lei n.º 41/2004 e RGPD, versões em vigor; o detalhe é de `stand-auditoria-ga4-google-ads`). Quem recusa cookies não aparece, ou aparece modelado: todos os números são uma parte das visitas reais. Escreve isso no relatório.
4. **Para e pede autorização** antes de criar ou alterar grupos de canais, eventos, públicos ou definições no GA4 ou no GTM; antes de mudar o grupo de canais principal; antes de tocar no robots.txt ou nas regras de bots do CDN.
5. **Sem acesso a uma fonte**, não pares a auditoria toda:

| Falta | Faz assim | Fica `N/V` |
|---|---|---|
| Acesso ao GA4 | Pede ao gestor a exportação CSV das origens de sessão e das páginas de entrada do período; as métricas saem daí | A configuração: áreas 1 e 2 e critério 5.1 da grelha |
| Search Console | Segue sem ele | Área 7 |
| Logs e painel do CDN | Só robots.txt e teste de acesso | Critério 8.4 |
| CRM | Pede contagens agregadas de leads e vendas por origem, sem nomes nem contactos | Critérios 5.3 e 5.4 |

## Passos

1. **Inventário de origens.** Exporta do GA4 as origens de sessão do período e corre `classificar_referencias_ia.py`. Revê a amostra do que ficou por classificar. Resultado: tabela por motor e lista datada de origens de IA observadas.
2. **Canal de IA no GA4.** Segue [references/ga4-canal-ia.md](references/ga4-canal-ia.md). Em Configurar, entrega o passo a passo com a expressão. Em Auditar, confirma que o canal existe, que está acima de Referral e que nenhuma origem de IA ficou em Referral, Unassigned ou noutro canal.
3. **Linha de base.** Por motor e por mês: sessões, sessões envolvidas, tempo médio de envolvimento, eventos-chave. Lado a lado com pesquisa orgânica, directo, referral e pago, no mesmo período. Com poucas dezenas de sessões, mostra números absolutos e não tires conclusões de taxas.
4. **Páginas de entrada.** Onde aterram as visitas de IA, por tipo de página (viatura, listagem, financiamento, retoma, oficina, contactos, artigo, início). Assinala desajustes: viatura vendida, erro 404, página sem forma de contacto.
5. **Do clique à venda.** Eventos-chave de contacto (formulário, WhatsApp, chamada) por canal; no CRM, se o lead guarda a origem; quantos leads com origem em IA chegaram a venda. Sem origem no CRM, propõe o campo e a pergunta "Como nos conheceu?" com a opção "ChatGPT ou outro assistente de IA", e reporta o declarado à parte do medido. Chamadas sem rastreio: `stand-auditoria-rastreio-chamadas`.
6. **Search Console.** Compara períodos por consulta e por página. Consultas com cliques a descer e impressões e posição estáveis ficam como hipótese de resumos de IA na pesquisa; confirma abrindo a pesquisa, com data e local, antes de as reportar. Nunca atribuas uma queda de CTR aos AI Overviews só pela queda.
7. **Bots de IA.** Segue [references/bots-e-logs.md](references/bots-e-logs.md): `verificar_bots_ia.py`, teste de acesso, painel do CDN e logs. Relatório separado.
8. **Pontua e entrega.** Lê [references/grelha.md](references/grelha.md) e preenche [assets/relatorio.md](assets/relatorio.md).

## Ferramentas

- `python3 scripts/classificar_referencias_ia.py <export.csv> --coluna-origem "<coluna>" --metricas "<col1>,<col2>" --regex`: agrupa por motor de IA (ChatGPT, Perplexity, Gemini, Copilot, Claude, Mistral, DeepSeek, Meta AI e outros), soma as métricas, mostra uma amostra do que não classificou e, com `--regex`, dá a expressão para o canal do GA4. Os nomes das colunas dependem da língua da conta: copia-os do CSV. Não prova que houve uma citação, nem vê as visitas de IA que chegam sem referenciador (contam como directo) ou pelos resumos de IA do Google (contam como pesquisa orgânica).
- `python3 scripts/verificar_bots_ia.py <url-do-site> --caminho /viaturas --testar-acesso`: para cada bot de IA conhecido, diz fornecedor, finalidade (pesquisa, treino, pedido do utilizador) e se cada caminho está permitido no robots.txt e por que regra; lista os sitemaps; com `--testar-acesso`, pede a página com o user agent de cada bot e devolve o estado HTTP. Vê `--help` para passar vários caminhos ou um robots.txt local. O robots.txt é uma declaração: não prova que um bot o respeita nem que visita o site; e o teste de acesso não vem dos IPs do fornecedor.
- Sem como correr scripts, faz o mesmo à mão: lê o robots.txt e agrupa o CSV pela lista de origens de [references/ga4-canal-ia.md](references/ga4-canal-ia.md).

## Entrega

Relatório em [assets/relatorio.md](assets/relatorio.md): definição exacta do canal (condição, expressão, posição, data), lista datada de origens, linha de base por motor e período, comparação com outros canais, páginas de entrada, funil até venda, sinais do Search Console marcados como hipótese, relatório separado de bots com a decisão do dono para cada um, nota da medição por área e prioridades. Indica sempre a cobertura, o efeito do consentimento, as amostras pequenas e qualquer mudança de definição a meio do período.

## Limites

- A nota mede a qualidade da medição, não o desempenho do stand: poucas visitas bem medidas não são uma falha.
- Não inflaciones: não somes directo nem orgânico às visitas de IA, nem extrapoles o que não se vê. O que não se mede, diz-se.
- Não atribuas "Google AI Overview" a uma queda de CTR sem prova adicional.
- Não envies logs brutos com IPs, emails ou parâmetros pessoais para serviços externos. Trata-os localmente e guarda só agregados.
- Não bloqueies nem permitas crawlers sem autorização do dono do site e sem avaliar o efeito na pesquisa e no licenciamento do conteúdo.
- Não alteres GA4, GTM, Google Ads, robots.txt ou CDN sem autorização explícita.
- Uma recomendação de IA que leva ao anúncio no Standvirtual ou no OLX não aparece no GA4 do stand. Diz isso quando o stand vende sobretudo pelos portais.
