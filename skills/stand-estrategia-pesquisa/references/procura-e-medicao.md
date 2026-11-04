# Procura e medição

Lê isto nos passos 5 e 7. Primeiro o mapa de procura (o que as pessoas procuram e onde), depois o quadro de métricas (como se sabe se o plano resultou).

## Mapa de procura

Constrói o mapa cruzando três coisas: intenções de compra, zonas que o stand serve de facto e stock que tem ou costuma ter. Uma intenção sem stock nem serviço que lhe responda fica de fora.

Fontes, por ordem de confiança:

1. **Search Console** (com acesso): consultas reais que já trazem impressões. Exporta os últimos três meses e, se houver, o mesmo período do ano anterior.
2. **Perguntas que chegam ao stand:** WhatsApp, telefone, formulários. Pede à equipa as perguntas que mais ouve, sem dados de clientes.
3. **Planeador de palavras-chave do Google Ads ou ferramentas de terceiros:** dão estimativas, muitas vezes em intervalos. Indica a ferramenta, a data e a localização usadas.
4. **Pesquisas de teste e sugestões do Google:** mostram formulações, não volumes.

Nunca escrevas um volume sem fonte e data. Sem fonte, a coluna diz `N/V`.

### Intenções típicas de um stand

| Intenção | Exemplos de pesquisa (PT-PT) | Onde acontece | Deve responder |
|---|---|---|---|
| Descoberta local | "stand de usados [concelho]", "carros usados [cidade]", "stand automóvel perto de mim" | Lista, Maps, IA | Perfil de Empresa, página inicial, página de contactos |
| Marca e modelo | "[marca] [modelo] usado [cidade]", "[modelo] usado à venda" | Lista, portais | Páginas de viatura e listagens filtradas indexáveis |
| Tipo e combustível | "carrinha usada", "SUV usado", "híbrido plug-in usado", "carro eléctrico usado", "comercial usado" | Lista, portais, IA | Listagens por tipo com stock real, guia de compra |
| Preço | "carros usados até [valor] euros" | Lista, portais | Listagens por preço, se o site as tiver indexáveis |
| Financiamento | "carros usados com financiamento", "crédito automóvel usado" | Lista, IA | Página de financiamento com condições e parceiros reais |
| Retoma e venda | "retoma de carro", "avaliar carro para retoma", "vender o meu carro [cidade]" | Lista, IA | Página de retoma com o processo explicado |
| Garantia e confiança | "carros usados com garantia", "[stand] opiniões", "[stand] é de confiança" | Lista, Maps, IA | Página de garantia, avaliações, Perfil |
| Importados | "carro importado", "legalização de carro importado" | Lista, IA | Página própria, só se o stand trabalha com importação |
| Oficina e pós-venda | "oficina [marca] [cidade]", "revisão [marca] [cidade]" | Lista, Maps | Página de oficina, só se o stand a tiver |
| Comparação | "[stand A] ou [stand B]", "[stand] vs [stand]" | Lista, IA | `stand-pagina-comparacao`, quando há procura real |

Regras do mapa:

- Usa o vocabulário de Portugal: "stand", "usado", "carrinha", "gasóleo", "retoma", "concessionário". "Seminovo", "concessionária" e "troca" são usos do Brasil; só entram se o Search Console mostrar que trazem procura.
- Páginas locais só para concelhos onde o stand está ou serve com conteúdo próprio (entregas, clientes, parcerias reais). Páginas iguais com o nome do concelho trocado são um risco nas políticas de spam da Google.
- Outras línguas (inglês, francês, espanhol) vão para `stand-seo-multilingue`.
- Separa consultas com o nome do stand (procura de marca) das sem nome. Crescer só na procura de marca é sinal de notoriedade, não de SEO.

### Perguntas para motores de IA

As pessoas escrevem frases completas aos assistentes. Para cada intenção, escreve uma ou duas perguntas como um cliente as faria:

- "Qual é um bom stand de usados em [concelho] com garantia?"
- "Onde compro um híbrido usado perto de [cidade] com financiamento?"
- "O [stand] é de confiança?"
- "Quanto tempo demora a retoma de um carro num stand em [cidade]?"

Estas perguntas alimentam a bateria de `stand-visibilidade-ia`. Não as corras aqui como medição.

## Quadro de métricas

Escolhe poucas métricas, ligadas a contactos e vendas. Para cada uma diz o que prova e o que não prova.

| Indicador | Fonte | Prova | Não prova |
|---|---|---|---|
| Impressões e cliques em consultas sem o nome do stand | Search Console | Que o site aparece e é escolhido em pesquisas de descoberta | Que esses cliques viram contactos |
| Consultas com o nome do stand | Search Console | Procura de marca | Efeito do SEO |
| Páginas de viatura com impressões | Search Console | Que o stock é encontrado | Qualidade do anúncio |
| Interacções no Perfil de Empresa | Desempenho do Perfil (nomes e métricas variam: por exemplo chamadas, direcções, cliques no site) | Uso do Perfil | Vendas |
| Avaliações novas por mês, nota e percentagem respondida | Perfil e portais | Ritmo de reputação | Satisfação geral de todos os clientes |
| Menções, exactidão e citações em IA | `stand-visibilidade-ia` | O que os motores disseram naquelas perguntas, naquela data | Opinião estável do mercado |
| Sessões referenciadas por IA | GA4, via `stand-analisar-trafego-ia` | Visitas humanas vindas de assistentes | Toda a influência da IA (parte chega como directo) |
| Contactos por origem (formulário, chamada, WhatsApp) | GA4 e CRM | Que canais geram contactos | Que um clique no WhatsApp foi uma conversa |
| Vendas confirmadas por origem | CRM ou DMS | O resultado que importa | Causalidade de uma acção isolada |

Notas de medição:

- Com o modo de consentimento, parte dos dados do GA4 é modelada. Não são contagens exactas.
- O Search Console guarda 16 meses. Exporta a linha de base para não a perder.
- Cliques em "ligar" ou "WhatsApp" não são chamadas nem conversas. Para chamadas, usa `stand-auditoria-rastreio-chamadas`.
- Se o CRM não regista a origem do contacto, o primeiro trabalho é esse, antes de qualquer conteúdo.

## Linha de base

Antes de mudar alguma coisa:

1. Fixa a data e o período (por exemplo, últimos três meses).
2. Exporta cada indicador e guarda o ficheiro com data.
3. Anota o que pode distorcer: sazonalidade, campanhas pagas, mudanças de site, alterações de stock.
4. Para IA, a linha de base é a primeira bateria completa de `stand-visibilidade-ia`, não o teste exploratório da triagem.

## Cadência

- **Semanal, nas primeiras quatro semanas:** tarefas feitas ou não, bloqueios. As métricas de uma semana são quase só ruído.
- **Mensal:** indicadores do quadro face à linha de base.
- **Trimestral:** revisão completa no modo C, nova bateria de IA, plano para os 90 dias seguintes.

## Regras de decisão

Escreve-as antes de começar, com o gestor. Formato:

`Se [indicador] em [data] estiver [acima / abaixo] de [limiar], então [expandir / corrigir / parar] [frente].`

- O limiar sai da linha de base e da capacidade da equipa, não de médias de mercado.
- Cada frente tem uma regra para expandir e outra para parar.
- "Corrigir" diz o que se muda (página, mensagem, canal), não só "melhorar".

## Registo de testes

Todo o teste manual entra numa tabela: data e hora, superfície (Google, Maps, ChatGPT, Gemini, Perplexity, Claude, Copilot, resumos de IA da Google), modelo se visível, conta ou sessão anónima, localização, idioma, pergunta exacta, resultado resumido, ligações citadas. Confirma se uma superfície está disponível em Portugal na data do teste; se não estiver, regista `N/V`.

## Prazos

Não prometas prazos. O Google e os motores de IA actualizam ao seu ritmo e esse ritmo não é público. Em vez de previsões, o plano marca datas de revisão e diz que sinais procurar em cada uma.
