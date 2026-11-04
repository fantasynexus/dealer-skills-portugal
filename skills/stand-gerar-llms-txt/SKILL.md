---
name: stand-gerar-llms-txt
description: Gerar, rever ou validar o ficheiro llms.txt do site de um stand de automóveis em Portugal, um índice curto e factual das páginas que interessam a agentes de IA (stock, retoma, financiamento, garantia, oficina, contactos). Usar quando o gestor pede "cria o llms.txt", "o meu llms.txt está bem?", quando uma auditoria AEO o deu como ausente ou com erros, ou quando o site mudou de páginas ou de plataforma. Confirma primeiro que os bots de IA não estão bloqueados, abre cada URL antes de o incluir, valida o formato e as ligações e entrega o ficheiro pronto a publicar, com os problemas encontrados, instruções de publicação e verificação depois de publicado.
---

# Gerar `llms.txt` para um stand

Cria ou revê o ficheiro `/llms.txt` na raiz do site: um resumo do stand e um
índice das páginas estáveis mais úteis, no formato proposto em llmstxt.org.
O ficheiro ajuda agentes que o procuram; não é uma norma oficial, nenhum
grande motor documentou que o usa para escolher fontes, e não garante
citações. Para diagnosticar porque é que o stand não aparece nas respostas
de IA, usa `stand-auditoria-aeo`.

## Antes de começar

Pede ao gestor, se não estiver claro no site:

- URL canónico do site (com ou sem `www`);
- nome comercial, concelho e o que vende (usados, novos, marcas, segmentos);
- serviços que existem de facto: retoma, compra de viaturas, financiamento, garantia, oficina, entrega;
- línguas em que o site é mantido;
- quem publica o ficheiro: o gestor (WordPress, alojamento próprio) ou o fornecedor do site.

Escolhe o modo:

- **Criar** quando não há `/llms.txt` (404).
- **Rever** quando existe: começa pela validação do actual e mantém o que estiver certo.

Sem acesso à web, constrói o ficheiro só com URLs que o gestor confirma, marca
tudo como "por confirmar" e valida apenas o formato. Nunca inventes um URL
que "deveria existir".

## Passos

1. **Acesso.** Corre `verificar_bots_ia.py` sobre o site com `--caminho /llms.txt` e os caminhos das páginas principais. Se agentes de pesquisa ou de pedido do utilizador (Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, Claude-SearchBot, PerplexityBot) estão bloqueados, ou o robots.txt dá 5xx, pára: diz ao gestor que o `llms.txt` não resolve um site bloqueado e encaminha para `stand-auditoria-aeo`. Bloqueios só de treino (GPTBot, ClaudeBot, Google-Extended) são decisão do stand e não impedem o trabalho.
2. **Ficheiro actual.** No modo rever, corre `validar_llms_txt.py` sobre o URL do ficheiro com `--verificar-links` e regista erros, avisos e ligações com problema.
3. **Candidatas.** Junta páginas do menu, do rodapé e dos sitemaps (a saída do passo 1 lista os declarados). Lê [references/formato.md](references/formato.md) para o que entra e o que fica de fora.
4. **Confirmar cada URL.** Abre-o: 200 sem redireccionamento, canónico próprio, sem `noindex`, com texto útil (não só um formulário), estável (não uma ficha de viatura nem uma pesquisa com filtros). O que falha sai da lista e vai para os problemas.
5. **Escrever.** H1 com o nome comercial; citação com um resumo factual; texto curto só com factos confirmados; secções H2 com uma ligação por linha (`- [Retoma](https://stand-exemplo.pt/retoma): descrição`); `## Optional` para o secundário. Descrições factuais, sem preços, TAEG nem slogans.
6. **Validar o rascunho.** Guarda-o num ficheiro e corre `validar_llms_txt.py rascunho-llms.txt --verificar-links`. Corrige todos os erros. Um aviso que fica tem a razão escrita na entrega.
7. **Entregar** com o modelo [assets/entrega.md](assets/entrega.md).
8. **Depois de publicado** (se o gestor pedir ou voltar com o ficheiro no ar): corre `validar_llms_txt.py` sobre o URL publicado com `--verificar-links` e `verificar_bots_ia.py` sobre esse URL com `--caminho /llms.txt --testar-acesso`.

Para um caso completo, do robots.txt ao ficheiro final, vê
[references/exemplo.md](references/exemplo.md).

## Ferramentas

- `python3 scripts/verificar_bots_ia.py https://stand-exemplo.pt --caminho /llms.txt --caminho /viaturas --caminho /retoma`: o que o robots.txt permite a cada agente de IA, por que regra, e os sitemaps declarados. Com `--testar-acesso`, pede o URL dado com o user agent de cada bot. Não prova que um bot lê o ficheiro nem que visita o site, e um 403 pode ser a CDN a recusar imitações.
- `python3 scripts/validar_llms_txt.py <url-ou-ficheiro> --verificar-links`: H1, resumo, secções, formato das ligações, URLs absolutos, duplicados, parâmetros de campanha, número de ligações, e o estado HTTP e o content-type. Valida a forma; não verifica se as descrições são verdade nem se algum motor usa o ficheiro.

## Entrega

Segue [assets/entrega.md](assets/entrega.md), por esta ordem:

1. o que resolver antes de publicar (bloqueios, URLs com erro, factos por confirmar);
2. as páginas consideradas, com a decisão e o motivo;
3. o ficheiro final num único bloco, sem comentários dentro;
4. como publicar na plataforma do stand e a resposta esperada;
5. os comandos de verificação depois de publicado;
6. quando rever e quem é o responsável;
7. o que o ficheiro não faz.

## Limites

- Nunca inventa URLs, serviços, marcas nem factos do stand. Uma página que falta é sugerida, não inventada.
- Nunca inclui fichas de viaturas, pesquisas com filtros, parâmetros de campanha nem páginas com erro, `noindex` ou bloqueadas.
- Não inclui páginas noutras línguas que ninguém mantém.
- Não publica nem altera o site: entrega o ficheiro para o gestor ou o fornecedor publicar.
- Não promete citações nem indexação, e não apresenta o `llms.txt` como substituto do robots.txt, do sitemap, dos dados estruturados ou do conteúdo das páginas.
- Não mexe no robots.txt para "abrir" bots de treino que o stand bloqueou.
