# Banco de perguntas para medir visibilidade em IA

Base de 29 perguntas em português de Portugal, agrupadas por intenção. Escolhe 20 a 30 para cada stand: retira as que não se aplicam e acrescenta, no máximo, cinco próprias. As perguntas medem presença. Quase nenhuma tem o nome do stand, porque é aí que se vê se a IA o recomenda a quem ainda não o conhece.

## Marcadores

| Marcador | Substitui por | Cuidado |
|---|---|---|
| `[nome do stand]` | nome comercial como aparece no Perfil de Empresa e na fachada | Se os clientes usam outra forma (sigla, nome do dono), regista as duas e escolhe uma para as perguntas |
| `[concelho]` | concelho da morada do stand | O nome que as pessoas escrevem ("Leiria", não o nome oficial da freguesia) |
| `[concelho vizinho]` | um concelho servido que não é o da morada | Um ou dois, no máximo |
| `[distrito]` | distrito ou região como as pessoas dizem ("distrito de Leiria", "Grande Porto", "Algarve") | |
| `[marca]` | uma das duas ou três marcas com mais peso no stock real | Pergunta ao gestor; não deduzas pelo site |
| `[modelo]` | modelo com stock frequente dessa marca | Sem ano nem versão, salvo se o stand se especializa nisso |
| `[tipo]` | SUV, citadino, carrinha, comercial, eléctrico, híbrido | Só tipos que o stand tem de forma regular |
| `[orçamento]` | um valor redondo em euros dentro da gama de preços do stock (ex.: 15 000 €) | |
| `[concorrente]` | um dos concorrentes confirmados | |

## As perguntas

### A. Identidade, com o nome do stand (4)

Servem de controlo: se o motor não reconhece o stand nem quando é nomeado, as perguntas sem nome dificilmente o vão trazer. A verificação a fundo do que se diz é de `stand-monitorizar-reputacao-ia`.

- A1. O que sabes sobre o [nome do stand], em [concelho]?
- A2. Onde fica o [nome do stand] e a que horas abre?
- A3. Que tipo de carros e que marcas vende o [nome do stand]?
- A4. O [nome do stand] é um stand de confiança?

### B. Descoberta local, sem marca (5)

- B1. Quais são os melhores stands de carros usados em [concelho]?
- B2. Onde posso comprar um carro usado de confiança perto de [concelho]?
- B3. Recomenda-me stands de automóveis em [concelho] ou [concelho vizinho].
- B4. stand automóveis usados [distrito] (forma curta, como se escreve no Google)
- B5. Tenho [orçamento] para um carro. Onde devo procurar em [concelho]?

### C. Marca, modelo e tipo de stock (6)

- C1. Onde comprar um [marca] [modelo] usado em [concelho]?
- C2. Que stands têm [marca] usados no [distrito]?
- C3. Procuro um [tipo] usado em [concelho]. Que stands me aconselhas?
- C4. Onde comprar um carro eléctrico ou híbrido usado em [concelho]? (só com stock regular)
- C5. Onde encontrar carrinhas comerciais usadas no [distrito]? (só com stock regular)
- C6. concessionário [marca] [concelho] (só se o stand for concessionário ou agente oficial da marca)

### D. Confiança e reputação (4)

- D1. Qual é o stand de usados com melhores avaliações em [concelho]?
- D2. Que stands de usados devo evitar em [concelho]?
- D3. stands [concelho] boas avaliações Google (forma curta)
- D4. Como escolher um stand de usados de confiança no [distrito]?

D2 tem enquadramento negativo de propósito: mostra que fontes o motor usa para criticar. D4 é genérica: regista sobretudo as fontes e se algum stand é nomeado.

### E. Financiamento, retoma, compra e garantia (5)

- E1. Onde posso comprar um carro usado com financiamento em [concelho]?
- E2. Que stands em [concelho] aceitam o meu carro como retoma?
- E3. Quero vender o meu carro em [concelho]. Que stands compram usados?
- E4. stands usados com garantia [concelho] (forma curta)
- E5. Onde comprar um carro importado no [distrito]? (só se o stand importa)

### F. Comparação com concorrentes (3)

- F1. [nome do stand] ou [concorrente]: onde é melhor comprar um usado?
- F2. Quais são as alternativas ao [concorrente] em [concelho]?
- F3. Compara os stands de usados de [concelho]: [nome do stand], [concorrente] e [concorrente].

F2 é a mais reveladora do grupo: mostra se o stand aparece como alternativa a quem domina a zona.

### G. Oficina e pós-venda (2, só se o stand tem oficina)

- G1. Onde fazer a revisão de um [marca] em [concelho]?
- G2. Oficina automóvel de confiança em [concelho]

## Quantas e quais

| Perfil do stand | Perguntas | Notas |
|---|---|---|
| Stand pequeno, usados multimarca, um concelho | 20 a 24 | Retira C6, G e as de stock que não tem |
| Várias marcas fortes ou vários concelhos | 25 a 30 | Repete B1 e C1 para a segunda marca ou o segundo concelho |
| Concessionário ou agente oficial | 25 a 30 | Mantém C6 e G; acrescenta modelos novos só se vende novos |

Núcleo fixo, igual em todas as corridas para comparar trimestres: A1, A4, B1, B2, C1, D1, E1, E2, F1, F2. As restantes podem rodar (outro modelo, outra campanha), mas assinala no registo as que mudaram.

## Regras de redacção

- Escreve como um comprador escreve: frases curtas, sem jargão de marketing, sem o nome do stand nas perguntas de descoberta.
- Nos motores de conversa (ChatGPT, Gemini, Claude, Copilot, Perplexity) usa a frase completa. Na pesquisa Google, corre também as formas curtas (B4, C6, D3, E4) e regista se apareceu resumo de IA. Não aparecer é um resultado, não um erro.
- Confirma, na data da corrida, se o AI Mode está disponível em Portugal e em português. Se não estiver, fica `N/V`.
- Prefere o concelho a "perto de mim". Se usares "perto de mim", regista a localização da sessão.
- Não faças perguntas com premissas por confirmar ("qual é o stand com garantia de três anos em [concelho]?"), nem com termos que só o stand usa.
- Uma pergunta, uma intenção. Se a resposta mistura temas, classifica-a pela intenção da pergunta.
- Não mudes o texto entre repetições nem entre motores. Uma palavra diferente é outra pergunta.
- Não faças perguntas de seguimento na mesma conversa antes de guardar a resposta. Uma pergunta de seguimento é uma pergunta nova, com ID próprio.

## Outras línguas e variantes

Só quando o público real do stand o justifica, e reportadas à parte, nunca somadas ao português:

- **Inglês**, para stands que vendem a residentes estrangeiros: "used car dealers in [concelho]", "where to buy a used car in [concelho]".
- **Português do Brasil**, se uma parte relevante dos clientes é brasileira: "onde comprar carro seminovo em [concelho]", "concessionária de carros usados em [concelho]". O vocabulário muda ("seminovo", "concessionária") e as respostas também.

Três a cinco perguntas por variante chegam: B1, B2, C1, D1 e E1 traduzidas.

## Exemplo de substituição (fictício)

Stand Exemplo, Leiria (fictício): usados multimarca, forte em Peugeot e Renault, faz financiamento e retoma, não tem oficina. Concorrentes confirmados: Auto Fictício Marinha, na Marinha Grande, e Carros Inventados Leiria (ambos fictícios).

| ID | Pergunta final |
|---|---|
| B1 | Quais são os melhores stands de carros usados em Leiria? |
| B3 | Recomenda-me stands de automóveis em Leiria ou Marinha Grande. |
| C1 | Onde comprar um Peugeot 2008 usado em Leiria? |
| C3 | Procuro um SUV usado em Leiria. Que stands me aconselhas? |
| E1 | Onde posso comprar um carro usado com financiamento em Leiria? |
| F2 | Quais são as alternativas ao Auto Fictício Marinha em Leiria? |

Ficaram de fora C5 (sem comerciais), C6 (não é concessionário), E5 (não importa), G1 e G2 (sem oficina): 24 perguntas.

## Manter este banco

- Quando uma pergunta deixa de dar respostas úteis em todos os motores durante duas corridas seguidas, marca-a como retirada em vez de a apagar, para não partir a comparação.
- Antes de acrescentar uma pergunta, confirma: um comprador real escreveria isto a um assistente para decidir onde comprar? Se não, fica de fora.
- Regista a versão do banco (data e lista de IDs) no cabeçalho de cada corrida.
