# Fontes citadas e métricas

Como classificar cada resposta, a que categoria pertence cada fonte e como se calculam os números do relatório.

## Classificar uma resposta

| Campo | Valores | Regra |
|---|---|---|
| estado | `valida`, `sem_resposta_util`, `recusa`, `erro_motor`, `sem_resumo_ia` | Só `valida` entra nos denominadores. `sem_resumo_ia` é para a pesquisa Google sem resumo de IA |
| stand_mencionado | `texto`, `so_fontes`, `nao` | `texto`: o nome aparece na resposta. `so_fontes`: só um URL do stand (site ou anúncio) aparece nas fontes. Variantes do nome contam se forem inequívocas |
| posicao | número ou vazio | Ordem do stand entre os stands nomeados na resposta (1 = primeiro). Vazio se não há menção no texto |
| recomendacao | `positiva`, `neutra`, `negativa`, `ausente` | `positiva`: recomendado ou apresentado como boa opção. `neutra`: listado sem juízo. `negativa`: desaconselhado ou com ressalva sobre o stand. `ausente`: não mencionado |
| concorrentes_mencionados | IDs dos concorrentes confirmados | Separados por `;` |
| outros_stands | número | Stands nomeados que não são o stand nem os concorrentes confirmados |
| urls_citados | lista de URLs | Só os que a interface mostra como fonte ou ligação. Não deduzas fontes que não aparecem |
| dominio_proprio_citado | `sim`, `nao`, `sem_fontes` | `sem_fontes` quando a interface não mostra fontes nessa resposta |
| categorias_fonte | números da tabela de categorias | Uma por URL citado, pela mesma ordem |
| erro_evidente | `sim`, `nao`, `nao_verificavel` | Só contra a mini ficha (ver abaixo) |

Na dúvida entre dois valores, escolhe o mais conservador (`neutra` em vez de `positiva`; `nao` em vez de `texto` se o nome for ambíguo) e explica na nota.

## Categorias de fontes

Cada categoria corresponde a um tipo de acção diferente. Regista o domínio de cada URL; a categoria decide-se pelo URL concreto, não só pelo domínio.

| Categoria | Exemplos | O que o stand controla | Skill |
|---|---|---|---|
| 1. Site do stand | o domínio do stand e subdomínios | Tudo: conteúdo, páginas de viatura, contactos, dados estruturados | `stand-auditoria-aeo`, `stand-brief-conteudo-aeo`, `stand-gerar-llms-txt` |
| 2. Portais de anúncios | Standvirtual, OLX, CustoJusto; portais estrangeiros em viaturas importadas | O perfil do stand, os anúncios, as fotografias e a actualização do stock | `stand-rever-anuncios-viaturas`, `stand-escrever-anuncio` |
| 3. Google | Perfil de Empresa, Google Maps, avaliações Google | Informação do Perfil, fotografias, publicações, resposta a avaliações | `stand-auditoria-perfil-google`, `stand-analisar-avaliacoes`, `stand-responder-avaliacoes` |
| 4. Outras avaliações e queixas | avaliações no Facebook, Portal da Queixa, outras plataformas de avaliação | Responder, pedir avaliações a clientes reais, resolver o problema de fundo | `stand-analisar-avaliacoes`, `stand-responder-avaliacoes` |
| 5. Directórios e dados de empresa | directórios de empresas, listas telefónicas online, sites de informação empresarial | Pedir correcção; manter nome, morada e telefone iguais em todo o lado | `stand-auditoria-perfil-google` |
| 6. Marca e importador | site da marca, localizador de concessionários, programas de usados certificados | Pouco, e só se o stand é concessionário ou agente: através da marca | nenhuma; trata-se com a marca |
| 7. Imprensa e editorial | jornais regionais, imprensa automóvel, blogues de referência | Notícias verdadeiras (aniversário, novas instalações, acção na comunidade); não se compram | nenhuma |
| 8. Fóruns, redes e vídeo | Reddit, grupos de Facebook, YouTube, Instagram, TikTok | As contas próprias; participação genuína e identificada | `stand-publicar-redes-sociais` |
| 9. Outros | Wikipédia, sites públicos (IMT, Portal das Finanças, Banco de Portugal), comparadores de crédito, conteúdo genérico | Quase nada | nenhuma |

Casos ambíguos:

- A página do stand dentro do Standvirtual ou do OLX é categoria 2, não 1: o stand controla o conteúdo, mas não o domínio. Conta como `so_fontes` se o nome não aparece no texto.
- A página de Facebook ou o canal de YouTube do stand são categoria 8.
- Uma ligação para o Google Maps com a ficha do stand é categoria 3.
- Conteúdo patrocinado fica na categoria da fonte, com a nota `pago`.
- Uma fonte que não consegues abrir regista-se com o URL e a nota `nao_aberta`. Não a classifiques pelo título que a IA lhe deu.

Não atribuas pesos às categorias. Pesos "de alavanca" são uma convenção, não uma medida, e escondem os números reais. Conta as citações e explica em texto o que o stand pode fazer em cada categoria.

## Mini ficha para erros evidentes

Esta skill só assinala erros que se vêem sem investigação, contra cinco factos que o gestor confirma antes da corrida: nome, morada, telefone, site e tipo de stock ou marcas. Tudo o resto (garantias, financiamento, equipa, reputação, tom) é de `stand-monitorizar-reputacao-ia`. Aqui, regista o erro com a frase exacta e a resposta de onde veio, e encaminha-o.

## Métricas

Todas por motor e por intenção, com numerador e denominador escritos. Em cada fórmula, "respostas" são respostas com estado `valida`.

| Métrica | Fórmula | Leitura |
|---|---|---|
| Taxa de menção | respostas com `stand_mencionado = texto` ÷ respostas | O stand aparece quando alguém pergunta? Mostra `so_fontes` à parte |
| Quota de menção | menções do stand ÷ menções de todos os stands (stand, concorrentes e outros) nas mesmas respostas | Que parte das recomendações de stands vai para este stand |
| Posição | lista das posições nas respostas com menção | Média só com cinco menções ou mais |
| Recomendação positiva | respostas com `recomendacao = positiva` ÷ respostas com menção | Mencionado não é recomendado |
| Citação do domínio próprio | respostas com `dominio_proprio_citado = sim` ÷ respostas com fontes visíveis | O site do stand é usado como fonte? |
| Erro evidente | respostas com `erro_evidente = sim` ÷ respostas com menção | Sinal para passar a `stand-monitorizar-reputacao-ia` |
| Consistência | repetições com menção ÷ repetições da mesma pergunta | 3 de 3 é estável; 1 de 3 é ocasional |

Regras de cálculo:

- Calcula a taxa e a quota de menção para o stand e para cada concorrente sobre as mesmas respostas.
- Um total "todos os motores" só faz sentido se as mesmas perguntas e repetições correram em todos. Caso contrário, mostra só a tabela por motor.
- Com menos de 10 respostas válidas num motor ou numa intenção, mostra só contagens, sem percentagens.
- Separa os resultados do modo API e das outras línguas.

## Exemplo resolvido (fictício)

Stand Exemplo, Leiria (fictício), 24 perguntas, uma repetição, só ChatGPT em sessão privada, 2026-10-15. Os números são inventados para mostrar o cálculo.

- Respostas válidas: 22. Uma recusa e uma sem resposta útil ficam fora.
- Menções no texto: Stand Exemplo 5, Auto Fictício Marinha 9, Carros Inventados Leiria 4, outros stands 8. Total de menções de stands: 26.
- Taxa de menção do Stand Exemplo: 5 de 22. Quota de menção: 5 de 26. Auto Fictício Marinha: 9 de 22 respostas, quota 9 de 26.
- Respostas com fontes visíveis: 18. Com o domínio do stand: 1. Citação do domínio próprio: 1 de 18. Em 7 dessas 18, a fonte do stand era o perfil no Standvirtual (categoria 2).
- Por intenção: 4 das 5 menções vêm de A (identidade) e F (comparação), onde o nome está na pergunta. Nas cinco perguntas B (descoberta), o stand aparece em uma.

Como se escreve no relatório: "O ChatGPT reconhece o Stand Exemplo quando é nomeado, mas raramente o sugere a quem procura um stand em Leiria (1 de 5 perguntas de descoberta). O stand mais nomeado é o Auto Fictício Marinha (9 de 22 respostas). Quando o Stand Exemplo aparece nas fontes, é sobretudo pelo Standvirtual, não pelo site." A explicação vem depois, marcada como hipótese.

## Padrões a investigar

São hipóteses para testar, não conclusões.

| O que se vê | Hipótese | Onde testar |
|---|---|---|
| Aparece com o nome, não aparece sem ele | O motor conhece a entidade, mas não a associa à categoria ou à zona | `stand-auditoria-aeo`, `stand-auditoria-perfil-google` |
| Só aparece através dos portais | A presença depende do Standvirtual ou do OLX; o site pesa pouco | `stand-auditoria-aeo`, `stand-auditoria-seo` |
| Um concorrente domina um motor e não os outros | Esse motor usa fontes onde o concorrente é mais forte | Comparar as categorias de fonte desse motor |
| Muitos "outros stands" e poucos nomes repetidos | Respostas genéricas; pouca informação estruturada sobre a zona | Repetir na corrida seguinte antes de agir |
| Recomendação negativa repetida | Queixas visíveis numa fonte citada | `stand-monitorizar-reputacao-ia`, `stand-analisar-avaliacoes` |
| Erros na morada ou no telefone | Dados diferentes entre Perfil, site, portais e directórios | `stand-monitorizar-reputacao-ia` |
