# Bots de IA: robots.txt, acesso e logs

Como saber que bots de IA o site permite, se o servidor os serve e quais o visitam de facto. São quatro camadas de prova, da mais fraca à mais forte. Cada uma prova uma coisa diferente: não as confundas no relatório.

| Camada | Prova | Não prova |
|---|---|---|
| 1. robots.txt | O que o site declara permitir a cada bot | Que o bot respeita a regra, ou que visita o site |
| 2. Teste de acesso | O estado HTTP que o servidor devolve a um pedido com o user agent do bot | O que o bot real recebe: vem de outros IPs e o CDN pode tratá-lo de forma diferente |
| 3. Logs ou painel do CDN | Pedidos que chegaram com o nome do bot, a que páginas e com que estado | Que eram mesmo do fornecedor: o user agent pode ser falsificado |
| 4. Verificação do IP | Que o pedido veio do fornecedor (listas de IPs publicadas ou DNS inverso) | Que a página foi usada numa resposta |

## Que bots e para quê

A finalidade de cada bot é a que o fornecedor declara. O script traz o seu próprio inventário; esta tabela serve para explicar ao gestor. Confirma na documentação actual de cada fornecedor antes de recomendar um bloqueio, porque nomes e regras mudam.

| Bot | Fornecedor | Finalidade declarada | Efeito provável de bloquear |
|---|---|---|---|
| GPTBot | OpenAI | Treino de modelos | Conteúdo fora do treino; segundo a OpenAI, não tira o site da pesquisa do ChatGPT |
| OAI-SearchBot | OpenAI | Pesquisa do ChatGPT | O site pode deixar de aparecer como fonte nas respostas com pesquisa |
| ChatGPT-User | OpenAI | Pedidos de um utilizador (abrir uma página numa conversa ou num agente) | Pode não seguir o robots.txt por ser um pedido do utilizador; confirma |
| ClaudeBot | Anthropic | Treino de modelos | Como o GPTBot |
| Claude-SearchBot | Anthropic | Pesquisa do Claude | Como o OAI-SearchBot |
| Claude-User | Anthropic | Pedidos de um utilizador | Como o ChatGPT-User |
| PerplexityBot | Perplexity | Índice de pesquisa | O site pode deixar de aparecer nas respostas |
| Perplexity-User | Perplexity | Pedidos de um utilizador | Pode não seguir o robots.txt; confirma |
| Google-Extended | Google | Não é um bot: é um nome no robots.txt que decide se o conteúdo recolhido pelo Googlebot pode ser usado nos modelos Gemini | Segundo a Google, não afecta a pesquisa Google nem os resumos de IA da pesquisa. Não aparece nos logs |
| Googlebot | Google | Pesquisa Google, incluindo AI Overviews e AI Mode | Sair da pesquisa Google. Num stand, nunca |
| Bingbot | Microsoft | Pesquisa Bing, que também alimenta o Copilot | Sair do Bing e, provavelmente, das respostas do Copilot |
| Applebot | Apple | Pesquisa da Apple (Siri, Spotlight, Safari) | Sair dessas sugestões |
| Applebot-Extended | Apple | Como o Google-Extended: nome no robots.txt para o treino de modelos da Apple; não rastreia | Não aparece nos logs |
| CCBot | Common Crawl | Arquivo aberto da web, usado por muitos para treino | Conteúdo fora desse arquivo |
| Meta-ExternalAgent | Meta | Treino e produtos de IA da Meta | Conteúdo fora desses usos |
| Amazonbot | Amazon | Serviços da Amazon, incluindo assistentes | Conteúdo fora desses serviços |
| Bytespider | ByteDance | Treino de modelos | Conteúdo fora do treino |
| DuckAssistBot | DuckDuckGo | Respostas do assistente do DuckDuckGo | O site pode deixar de ser usado nessas respostas |
| MistralAI-User | Mistral | Pedidos de um utilizador no Le Chat | Como o ChatGPT-User |

## Passo 1. robots.txt

```bash
python3 scripts/verificar_bots_ia.py <url-do-site> --caminho /viaturas
```

Escolhe caminhos que importam ao stand: a listagem de viaturas, uma página de viatura, financiamento, retoma, contactos. Vê `--help` para passar vários caminhos ou um robots.txt local (`--robots`).

No resultado, procura:

- bots bloqueados e a regra que os bloqueia;
- bots de pesquisa bloqueados por engano, o que acontece quando alguém copia um robots.txt "anti-IA" sem ver o que cada nome faz;
- os sitemaps declarados (se não houver nenhum, regista; o detalhe é de `stand-auditoria-seo`).

Sem o script, abre `<url-do-site>/robots.txt` e lê as secções. Lembra que um bot segue o grupo com o seu nome e só usa o de `User-agent: *` quando não tem grupo próprio: um `Disallow: /` em `*` bloqueia todos os bots que não têm secção.

## Passo 2. Teste de acesso

```bash
python3 scripts/verificar_bots_ia.py <url-do-site> --caminho /viaturas --testar-acesso
```

- **200 para todos:** o servidor não discrimina estes user agents. Não prova que o bot real recebe 200.
- **403, 429 ou 503 só para alguns:** há uma regra no servidor, na firewall ou no CDN. Pode ser um bloqueio intencional de bots de IA, ou protecção contra bots falsos: o CDN pode recusar um pedido que diz ser o GPTBot mas não vem dos IPs da OpenAI e deixar passar o verdadeiro. Confirma nas regras do CDN ou nos logs antes de concluir.
- **Falha para todos, incluindo o browser normal:** problema do site, não dos bots.

## Passo 3. CDN

Se o site está no Cloudflare ou noutro CDN, pede a quem o gere que veja e te mostre:

- se há opções activas para bloquear bots de IA, ou um robots.txt gerido pelo próprio CDN (o Cloudflare tem as duas coisas; os nomes e o lugar no painel mudam, confirma);
- o painel de bots ou de crawlers de IA, se existir, com pedidos por bot e por página no período.

Regista o que viste e a data. Não alteres nada sem autorização.

## Passo 4. Logs do servidor

Pede a exportação dos logs de acesso do período a quem aloja o site. Trata-os no computador onde estás, nunca num serviço externo: têm IPs e podem ter dados pessoais nos parâmetros dos URLs, e o RGPD aplica-se. Guarda só os agregados e apaga as cópias quando acabares, ou devolve-as a quem tas deu.

Os comandos abaixo são para o formato "combined" de Apache e nginx: confirma numa linha que o user agent é o último campo entre aspas. Não imprimem IPs e cortam os parâmetros dos URLs.

Pedidos por bot (uma contagem por pedido):

```bash
gzip -dcf access.log* | awk -F'"' -v bots="gptbot oai-searchbot chatgpt-user claudebot claude-searchbot claude-user perplexitybot perplexity-user ccbot meta-externalagent amazonbot bytespider duckassistbot mistralai-user applebot bingbot googlebot" '
  BEGIN { n = split(bots, b, " ") }
  { ua = tolower($6); for (i = 1; i <= n; i++) if (index(ua, b[i])) { c[b[i]]++; break } }
  END { for (k in c) print c[k], k }' | sort -rn
```

Páginas mais pedidas por um bot, sem parâmetros:

```bash
gzip -dcf access.log* | awk -F'"' 'tolower($6) ~ /gptbot/ { split($2, r, " "); p = r[2]; sub(/\?.*/, "", p); print p }' | sort | uniq -c | sort -rn | head -20
```

Estados HTTP para um bot:

```bash
gzip -dcf access.log* | awk -F'"' 'tolower($6) ~ /gptbot/ { split($3, s, " "); print s[1] }' | sort | uniq -c
```

Troca `gptbot` pelo nome de cada bot que quiseres ver.

**Verificação do IP (camada 4).** Para os bots com mais pedidos, verifica uma amostra de IPs: alguns fornecedores publicam listas de IPs dos seus bots, outros permitem confirmar por DNS inverso. Procura o método na documentação actual de cada um. Faz isto localmente e não ponhas IPs no relatório: escreve "verificado em x de y pedidos da amostra".

## Ler os resultados

| O que se vê | Leitura | Acção possível, com autorização |
|---|---|---|
| Bots de pesquisa bloqueados no robots.txt | O stand pode estar a sair das respostas com pesquisa desses motores | Mostrar ao dono o efeito; decidir bot a bot |
| Bots de treino bloqueados, bots de pesquisa permitidos | Escolha coerente | Documentar a decisão |
| Permitido no robots.txt, recusado no teste e nos logs | Bloqueio no CDN ou na firewall que o dono pode não conhecer | Rever as regras do CDN |
| Nenhum pedido de bots de IA nos logs | Pouca procura, logs incompletos ou bloqueio a montante | Confirmar o período e a origem dos logs |
| Bots a pedir sobretudo viaturas vendidas ou páginas 404 | Stock antigo acessível, que pode alimentar respostas desactualizadas | `stand-auditoria-seo`, `stand-auditoria-aeo` |
| Muitos pedidos de bots e nenhuma visita humana de IA | Ser lido não é ser citado nem trazer visitas | `stand-visibilidade-ia` |

## Decidir bloquear ou permitir

A decisão é do dono do site. Apresenta, para cada bot: o que o fornecedor diz que faz, o efeito provável de bloquear, o estado actual e quem decidiu. Separa as três famílias:

- **pesquisa:** afecta aparecer como fonte nas respostas;
- **treino:** afecta o uso do conteúdo para treinar modelos;
- **pedidos do utilizador:** afecta quando alguém pede ao assistente para abrir o site.

Lembra o licenciamento: fotografias e textos de terceiros (por exemplo, de marcas) podem ter regras próprias de uso. Para orientar os assistentes para as páginas certas há `stand-gerar-llms-txt`; o `llms.txt` não substitui o robots.txt nem é uma norma que os bots sejam obrigados a seguir.

## Cruzar com o resto

Põe lado a lado três listas: as páginas que os bots mais pedem, as páginas onde aterram as visitas de IA e as páginas citadas nas respostas (de `stand-visibilidade-ia`, se existir). Quando coincidem, o quadro é coerente. Quando não coincidem, é uma pista para investigar, não uma conclusão.
