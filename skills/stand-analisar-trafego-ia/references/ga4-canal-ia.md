# Canal de IA no GA4: passo a passo

Como encontrar as visitas de IA que já existem, criar um grupo de canais personalizado com um canal só para assistentes de IA, verificá-lo e montar a exploração da linha de base.

**A interface do GA4 muda com frequência** e os nomes dos menus dependem da língua da conta. Os caminhos abaixo estão em inglês, com a tradução provável entre parênteses quando ajuda. Confirma cada nome na interface actual antes de o escrever ao gestor. Se um menu não estiver onde está indicado, usa a pesquisa do próprio GA4 e regista o caminho que encontraste.

## Antes de mexer

- **Papel na propriedade.** Criar grupos de canais exige um papel com permissão de edição (Editor ou Administrador; confirma na ajuda actual do GA4). Ler relatórios exige só o de Leitor.
- **Autorização.** Criar um grupo de canais não altera os dados recolhidos, mas é uma alteração à propriedade: pede autorização explícita e escrita antes de o fazeres tu.
- **Limite de grupos.** As propriedades têm um número máximo pequeno de grupos de canais personalizados. Vê quantos existem antes de propor um novo; se o limite estiver atingido, propõe acrescentar o canal a um grupo personalizado que já exista.
- **Canal de IA de origem.** Confirma se a Google acrescentou entretanto um canal de IA ao grupo predefinido. Se existir, compara a definição dele com a lista abaixo em vez de duplicar.
- **Grupo principal.** Não mudes o grupo de canais principal da propriedade: afecta os relatórios de todos. O canal novo usa-se escolhendo o grupo nos relatórios e nas explorações.

## Passo 1. Ver onde caem hoje as visitas de IA

1. Reports (Relatórios) > Acquisition (Aquisição) > Traffic acquisition.
2. Período: os últimos 90 dias.
3. Dimensão principal: Session source / medium.
4. Na caixa de pesquisa da tabela, procura `chatgpt`, `openai`, `perplexity`, `gemini`, `copilot`, `claude`, `deepseek`, `mistral`.
5. Muda a dimensão principal para Session default channel group e acrescenta Session source como dimensão secundária: vê em que canal caem essas origens (Referral, Unassigned, Organic Search ou outro).

Resultado: lista das origens de IA com sessões e o canal onde estão hoje.

Repara no meio associado a cada origem. O ChatGPT acrescenta muitas vezes `utm_source=chatgpt.com` às ligações (confirma nos teus dados): essas visitas aparecem com essa origem mesmo sem referenciador. Se o meio ficar vazio ou `(not set)`, podem cair em Unassigned. É por isso que a regra do canal usa a origem e não o meio.

## Passo 2. Exportar para o script

1. No mesmo relatório, com Session source como dimensão e as métricas Sessions, Engaged sessions e Key events, aumenta o número de linhas para ver todas as origens.
2. Share this report (Partilhar este relatório) > Download File > CSV.
3. Corre `python3 scripts/classificar_referencias_ia.py <export.csv> --coluna-origem "<coluna de origem>" --metricas "<sessões>,<eventos-chave>" --regex`, com os nomes das colunas copiados do ficheiro.
4. Revê a amostra de origens não classificadas. Uma origem de IA que lá esteja vai para a lista e para a expressão.

Se o relatório tiver mais linhas do que a exportação inclui, exporta de uma exploração (passo 6) com Session source.

## Passo 3. Lista de origens de IA (datada)

Lista de partida, revista em Novembro de 2026. Muda com frequência: confirma contra os teus dados e contra a lista do script, e regista a data de cada revisão.

| Motor | Origens |
|---|---|
| ChatGPT | `chatgpt.com`, `chat.openai.com` (antigo) |
| Perplexity | `perplexity.ai`, `www.perplexity.ai` |
| Gemini | `gemini.google.com`, `bard.google.com` (antigo) |
| Copilot | `copilot.microsoft.com` |
| Claude | `claude.ai` |
| DeepSeek | `chat.deepseek.com` |
| Mistral | `chat.mistral.ai` |
| Meta AI | `meta.ai` |
| Grok | `grok.com` |

Cuidados:

- **Não incluas** `google`, `google.com`, `bing` nem `bing.com`: misturam pesquisa normal com IA. As visitas vindas dos AI Overviews e do AI Mode do Google chegam como pesquisa orgânica e não se separam no GA4.
- Podem aparecer origens em forma de aplicação (identificadores de apps com `openai`, `perplexity` ou semelhantes). Se aparecerem nos teus dados, confirma o que são e acrescenta-as.
- Uma origem que não reconheces não entra na lista sem confirmares o que é.

## Passo 4. Criar o grupo de canais

1. Admin (Administrador, ícone da engrenagem) > Data display > Channel groups.
2. Create new channel group. Se a interface oferecer copiar o grupo predefinido, copia: o grupo novo fica com os canais habituais e só acrescentas um.
3. Nome do grupo: "Canais com IA". Descrição: "Grupo predefinido mais o canal Assistentes de IA. Lista de origens revista em AAAA-MM-DD."
4. Add new channel. Nome: "Assistentes de IA".
5. Condição: Source · matches regex · a expressão abaixo, ou a que o script devolveu.
6. Guarda o canal.
7. **Ordem.** Os canais são avaliados de cima para baixo e cada sessão fica no primeiro canal cuja condição cumpre. Põe "Assistentes de IA" no topo, ou pelo menos acima de Referral, Organic Search e Unassigned.
8. Guarda o grupo.

Expressão de partida, equivalente à lista do passo 3:

```
^(.*\.)?(chatgpt\.com|chat\.openai\.com|perplexity\.ai|gemini\.google\.com|bard\.google\.com|copilot\.microsoft\.com|claude\.ai|chat\.deepseek\.com|chat\.mistral\.ai|meta\.ai|grok\.com)$
```

Está ancorada (`^` e `$`) para dar o mesmo resultado quer o operador compare a origem inteira, quer procure uma parte, e não apanha `google.com` nem `bing.com`. Antes de a colar:

- testa-a contra as origens do passo 1 (por exemplo, com `re.fullmatch` em Python) e contra esta tabela;
- se o operador disponível na interface for outro, adapta a expressão e diz no relatório qual usaste;
- se a interface recusar a expressão por ser longa, divide-a em duas condições ligadas por OR.

| Origem | Deve entrar no canal |
|---|---|
| `chatgpt.com` | sim |
| `www.perplexity.ai` | sim |
| `gemini.google.com` | sim |
| `copilot.microsoft.com` | sim |
| `google` | não |
| `google.com` | não |
| `bing.com` | não |
| `l.facebook.com` | não |
| `standvirtual.com` | não |

## Passo 5. Verificar

1. Reports > Acquisition > Traffic acquisition. No selector da dimensão principal, escolhe o grupo "Canais com IA" (pode aparecer como Session custom channel group, seguido do nome).
2. Acrescenta Session source como dimensão secundária.
3. Confirma que em "Assistentes de IA" só há origens de IA e que em Referral e Unassigned não ficou nenhuma.
4. Abre um mês anterior à criação do grupo. Segundo a documentação da Google, os grupos de canais aplicam-se também a dados anteriores; confirma se o canal aparece nesse mês. Se não aparecer, a linha de base começa na data de criação, e o relatório diz isso.

Resultado: captura ou exportação com data que mostra o canal e as suas origens.

## Passo 6. Exploração para a linha de base

Explore (Explorar) > Free form. Guarda-a com o nome "IA: linha de base" e partilha-a com quem vai ler os números.

| Elemento | O que pôr |
|---|---|
| Dimensões | grupo "Canais com IA", Session source, Landing page + query string, Month |
| Métricas | Sessions, Engaged sessions, Average engagement time per session, Key events, Session key event rate |
| Filtro | grupo "Canais com IA" igual a "Assistentes de IA", nas tabelas só de IA |
| Tabelas | 1) motor × mês; 2) página de entrada × motor; 3) canal × métricas, sem filtro, para comparar com orgânico, directo, referral e pago |

Notas:

- Se o site tem vários eventos-chave (formulário, WhatsApp, chamada), vê-os um a um para saber qual a IA traz. Se os eventos estão bem definidos é tema de `stand-auditoria-ga4-google-ads`.
- Com os sinais Google activos, o GA4 pode aplicar limiares de dados e esconder linhas com poucos utilizadores. Se aparecer esse aviso, regista-o: com volumes pequenos, os números por motor podem estar incompletos.
- Explorações com muitos dados podem ser amostradas; o GA4 indica-o na própria exploração. Regista também.

## Passo 7. Origem no lead (com autorização)

Para ligar visitas de IA a leads e vendas, o lead tem de levar a origem para o CRM:

- campo escondido no formulário que guarda a origem e o meio da visita (ou os parâmetros `utm_`);
- no CRM, um campo de origem preenchido em todos os leads do site;
- no atendimento, a pergunta "Como nos conheceu?" com a opção "ChatGPT ou outro assistente de IA", registada à parte do medido.

Guarda só a origem: não acrescentes ao lead identificadores de navegação que não sejam precisos, e confirma com o responsável pela protecção de dados que o formulário e a política de privacidade cobrem o campo.

## Uma dimensão personalizada ou um evento no GTM?

Não é preciso. A origem da sessão já diz de que motor veio a visita. Um evento no GTM que lê o referenciador acrescenta manutenção e pode divergir do grupo de canais. Só faz sentido se o stand precisa dessa informação noutro destino (por exemplo, no CRM) e o gestor autoriza a mudança no GTM.

## Manter

- Revê a lista de origens todos os trimestres: corre o script numa exportação nova e acrescenta o que aparecer.
- Cada mudança na expressão leva data e motivo na descrição do grupo e no relatório seguinte: uma definição nova parte a comparação com os meses anteriores.
