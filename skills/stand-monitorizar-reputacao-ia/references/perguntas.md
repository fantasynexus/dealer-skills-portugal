# Perguntas para ler a reputação do stand em IA

24 perguntas em português de Portugal, em cinco categorias. Quase todas têm o nome do stand: aqui interessa o que o motor diz quando o comprador já o conhece. Para medir se o stand aparece a quem não o conhece, usa `stand-visibilidade-ia`.

## Marcadores

- `[nome do stand]`: como no Perfil de Empresa. Se há homónimos, usa sempre "[nome do stand], em [concelho]".
- `[concelho]`: concelho da morada.
- `[concorrente 1]`, `[concorrente 2]`: concorrentes confirmados com o gestor.

## A. Identidade e opinião geral (5)

Alimentam os eixos de tom, pontos fortes e problemas.

- A1. O que sabes sobre o [nome do stand], em [concelho]?
- A2. O [nome do stand] é um bom sítio para comprar carro?
- A3. Que reputação tem o [nome do stand]?
- A4. O que dizem os clientes do [nome do stand]?
- A5. Vale a pena comprar um carro usado no [nome do stand]?

## B. Factos (8)

Alimentam a exactidão factual. São as que mais vezes revelam erros com dano directo.

- B1. Qual é a morada do [nome do stand]?
- B2. Qual é o horário do [nome do stand]? Abre ao sábado?
- B3. Qual é o telefone ou o WhatsApp do [nome do stand]?
- B4. Que marcas vende o [nome do stand]? É concessionário oficial de alguma?
- B5. O [nome do stand] vende carros novos ou só usados?
- B6. O [nome do stand] tem oficina própria?
- B7. Há quantos anos existe o [nome do stand]?
- B8. Quem é o responsável ou o dono do [nome do stand]?

B8 testa a calibração: a resposta certa pode ser "não sei". Se o motor der nomes, compara com a ficha, mas não os copies para o relatório; regista só `correcto`, `errado` ou `inventado`.

## C. Condições comerciais (5)

Medem as afirmações com mais risco para o comprador e para o stand.

- C1. O [nome do stand] faz financiamento? Em que condições?
- C2. O [nome do stand] aceita retomas?
- C3. Que garantia dá o [nome do stand] nos carros usados?
- C4. O [nome do stand] compra carros a particulares?
- C5. Os carros do [nome do stand] são revistos antes da venda?

Qualquer número que a IA dê aqui (TAEG, prestação, meses de garantia, valor de retoma) compara-se com a ficha. Se a ficha não o tem, é `sem prova` ou `inventada`, nunca `correcta`.

## D. Queixas e pontos fracos (3)

- D1. Há queixas sobre o [nome do stand]?
- D2. Quais são os pontos fracos do [nome do stand]?
- D3. O [nome do stand] é de confiança ou é melhor evitar?

Abre sempre as fontes que o motor cita aqui. Uma queixa sem fonte e uma queixa com fonte que não diz aquilo são coisas diferentes, e as duas são diferentes de uma queixa real.

## E. Comparação (3)

- E1. [nome do stand] ou [concorrente 1]: onde é melhor comprar um usado?
- E2. Compara o [nome do stand] com o [concorrente 2] em garantia, financiamento e avaliações.
- E3. Porque escolheria o [concorrente 1] em vez do [nome do stand]?

## Escolher entre 20 e 24

- Retira B6 se o stand não tem oficina e nunca teve (se teve, mantém: é aí que aparece a informação desactualizada).
- Retira C4 se o stand não compra a particulares e isso não é tema.
- Mantém sempre B1 a B4, C1, C3, D1 e E1: são as de maior dano potencial.
- Podes trocar até três perguntas por perguntas próprias sobre um tema que preocupa o gestor (uma queixa antiga, uma mudança de instalações), escritas como um comprador as escreveria, sem passar das 24.

## Subconjunto curto para monitorização

Sete perguntas, uma repetição por motor, todos os meses ou depois de uma mudança: B1, B2, B3, B4, C1, C3, A2. Se aparecer um erro novo, corre essa pergunta mais duas vezes antes de o reportar como estável.

## Protocolo de corrida

1. Uma conversa nova por repetição, em janela privada ou conta sem memória. Não corras as três repetições na mesma conversa: o motor tende a repetir-se.
2. Cola a pergunta exacta, sem contexto antes. Não corrijas o motor a meio.
3. Guarda a resposta completa e as fontes visíveis. Faz captura de ecrã quando a interface não deixa copiar as fontes.
4. Regista data, hora, motor, modelo visível, modo (colado, directo, API), conta, idioma e localização.
5. Na pesquisa Google, regista também se apareceu resumo de IA. Com o nome do stand muitas vezes não aparece; isso é um resultado.
6. Não faças perguntas de seguimento que induzam a resposta ("mas eles não dão três anos de garantia?"). Um seguimento conta como pergunta nova, com ID próprio, e nunca entra na nota.

## Variantes de língua

Se o stand vende a residentes estrangeiros ou a muitos clientes brasileiros, corre A1, A3, B1, B3 e C1 em inglês ou em português do Brasil e reporta à parte. Os erros podem ser diferentes de língua para língua.

## Exemplo de extracção (fictício)

Stand Exemplo, Leiria (fictício). Pergunta C3, motor X, repetição 2. Excerto da resposta: "O Stand Exemplo inclui garantia alargada com assistência em viagem em todos os usados e faz financiamento com TAEG a partir de 4,9%."

| Afirmação | Tema | Facto na ficha | Etiqueta | Gravidade |
|---|---|---|---|---|
| "inclui garantia alargada com assistência em viagem em todos os usados" | garantia | Não vende garantia alargada | `inventada` | crítica |
| "faz financiamento" | serviços | Sim, através de um parceiro de crédito | `correcta` | |
| "TAEG a partir de 4,9%" | crédito | A ficha não tem valor de TAEG | `sem prova` | alta |

A segunda linha é verdade e conta a favor. A terceira não é dada como falsa: não há prova de que seja verdade, e uma TAEG publicada por terceiros sem base é um risco para o comprador. Vai para as correcções como "confirmar com o parceiro de crédito o que pode ser publicado".
