# Grelha de reputação em IA

Etiquetas, gravidade, estabilidade e a pontuação de 100 pontos por motor. A nota mede se o que o motor diz é verdadeiro, actual e proporcional à prova. Não mede se elogia: um stand com queixas reais pode ter nota alta se o motor as descreve com exactidão.

## Etiquetas por afirmação

| Etiqueta | Quando | Exemplo (Stand Exemplo, Leiria, fictício) |
|---|---|---|
| `correcta` | Coincide com a ficha ou com uma fonte verificável | "Fica na Rua Exemplo, em Leiria", e a ficha confirma |
| `imprecisa` | Parcialmente certa, ou vaga a ponto de enganar | "Abre todos os dias", quando fecha ao domingo |
| `desactualizada` | Foi verdade e deixou de ser | Morada antiga; marca que o stand deixou de representar |
| `sem prova` | Não se consegue confirmar nem desmentir com a ficha nem com a fonte citada | "Os vendedores são muito simpáticos", sem fonte; uma TAEG que a ficha não tem |
| `inventada` | Contradiz a ficha sem fonte, ou a fonte citada não diz aquilo | Um "gerente João" que não existe; "concessionário oficial Peugeot" num stand multimarca |
| `recusa adequada` | O motor diz que não sabe, ou manda confirmar com o stand | "Não tenho informação actual sobre o horário" |

Regras:

- Abre a fonte citada antes de etiquetar. Se a fonte diz o mesmo que a IA e está errada, a afirmação continua errada, mas a causa está nessa fonte: regista-a para [corrigir-fontes.md](corrigir-fontes.md).
- Juízos ("bom atendimento", "preços altos") são `correcta` quando a fonte citada ou as avaliações reais os sustentam em proporção; `sem prova` quando não há fonte; `imprecisa` quando generalizam um caso isolado.
- Quando o facto na ficha está `por confirmar`, a afirmação fica `N/V`.

## Gravidade

| Gravidade | Critério | Exemplos |
|---|---|---|
| crítica | Pode levar o comprador a um erro com dano directo, ou atribui ao stand uma conduta grave | Morada ou telefone errados, ou de outro stand; condição de crédito ou garantia falsa; acusação de burla, fraude ou quilómetros adulterados sem fonte; dados pessoais expostos |
| alta | Afecta a decisão ou a confiança | Horário errado; "concessionário oficial" falso; marcas ou serviços inexistentes (oficina, compra a particulares); colaborador inventado; avaliação ou citação de cliente inventada; TAEG ou prazo sem prova |
| média | Imprecisão relevante que não decide a compra | Anos de actividade, história, dimensão do stock, tipo de clientes |
| baixa | Pormenor ou redacção | Nome com uma letra trocada; freguesia em vez de concelho |

Afirmações sobre garantia e crédito tocam regimes legais: o Decreto-Lei n.º 84/2021 na garantia dos bens vendidos a consumidores e o Decreto-Lei n.º 81-C/2017 na intermediação de crédito. Confirma a versão em vigor. Não interpretes tu esses regimes: compara com o que o stand pratica e assinala. Quem decide a correcção é o stand, com o seu jurista ou com o parceiro de crédito.

## Estabilidade e prioridade

- **Estável:** aparece em 3 de 3 repetições. **Intermitente:** em 2 de 3. **Isolada:** em 1 de 3.
- Prioridade: primeiro a gravidade, depois a estabilidade, depois o número de motores. Um erro crítico isolado vem antes de um erro médio estável.
- Um erro crítico isolado corre mais duas vezes antes de entrar no relatório; regista as cinco corridas e diz em quantas apareceu.

## Pontuação por motor: 100 pontos

Pontua cada motor em separado. Em cada critério:

- **total** quando todas as repetições cumprem;
- **metade**, arredondada para baixo, quando há falha numa parte das repetições;
- **zero** quando falha na maioria das repetições ou em todas;
- `N/V` quando a pergunta não correu ou o facto está por confirmar: sai do denominador.

### 1. Tom e neutralidade: 15

| Critério | Pontos | Perguntas | Total quando |
|---|---|---|---|
| 1.1 Tom adequado à prova | 8 | A1 a A5 | O tom corresponde ao que as fontes citadas e as avaliações reais sustentam |
| 1.2 Sem ressalvas infundadas | 4 | A, D | Não há "convém ter cuidado" ou "há relatos mistos" sem fonte |
| 1.3 Coerência entre repetições | 3 | A | O tom não muda de positivo para negativo entre repetições |

Regista também o tom observado por motor (positivo, neutro, misto, negativo). Vai para o relatório como descrição, não como nota.

### 2. Exactidão factual: 25

| Critério | Pontos | Perguntas | Total quando |
|---|---|---|---|
| 2.1 Identidade | 3 | A1, B1 | Fala do stand certo, sem o confundir com outro |
| 2.2 Morada | 5 | B1 | Morada correcta ou recusa adequada |
| 2.3 Telefone, WhatsApp e site | 4 | B3 | Contactos correctos ou recusa adequada |
| 2.4 Horário | 3 | B2 | Correcto, incluindo sábado e domingo |
| 2.5 Marcas, tipo de stock e estatuto | 4 | B4, B5 | Correcto, incluindo se é oficial ou independente |
| 2.6 Serviços e condições | 4 | B6, C1 a C5 | Correctos, sem acrescentar serviços nem condições |
| 2.7 Responsável e anos de actividade | 2 | B7, B8 | Correcto, público, ou recusa adequada |

### 3. Pontos fortes com prova: 15

| Critério | Pontos | Total quando |
|---|---|---|
| 3.1 Diferenciador real | 6 | Menciona pelo menos um diferenciador da ficha (anos, especialização, garantia praticada, avaliações, serviços) |
| 3.2 Elogios com base | 5 | Nenhum elogio inventado ("o maior stand do distrito", prémios que não existem) |
| 3.3 Serviços reais quando pertinentes | 4 | Nas perguntas A e C refere financiamento, retoma ou oficina que o stand tem |

### 4. Problemas e reclamações: 15

| Critério | Pontos | Total quando |
|---|---|---|
| 4.1 As queixas referidas existem | 6 | Cada queixa tem fonte que a sustenta (avaliações, Portal da Queixa, notícia) |
| 4.2 Proporção e actualidade | 5 | Um caso isolado não é apresentado como padrão; um problema antigo e resolvido não é apresentado como actual |
| 4.3 Acusações graves só com fonte | 4 | Nenhuma acusação de burla, fraude ou ilegalidade sem fonte identificável. Uma só, sem fonte, dá zero |

Se o motor não refere queixas e não há queixas conhecidas, 4.1 e 4.2 têm o total. Se há queixas reais relevantes e o motor as omite sempre, não é falha de reputação: regista em observações.

### 5. Enquadramento competitivo: 15

| Critério | Pontos | Perguntas | Total quando |
|---|---|---|---|
| 5.1 Vantagens com base | 6 | E1 a E3 | O que diz a favor do concorrente e do stand tem fonte ou é verdade |
| 5.2 Não desaconselha sem razão | 5 | E1, E3 | Não recomenda o concorrente "em vez de" sem um motivo concreto |
| 5.3 Não troca dados entre stands | 4 | todas | Não mistura moradas, avaliações ou serviços do concorrente com os do stand |

### 6. Risco de alucinação e desactualização: 15

| Critério | Pontos | Total quando |
|---|---|---|
| 6.1 Sem avaliações ou citações inventadas | 4 | Toda a citação de cliente existe na fonte |
| 6.2 Sem pessoas inventadas | 3 | Nenhum nome ou cargo que não exista |
| 6.3 Sem stock, preços, promoções ou condições inventadas | 3 | Nada disto aparece sem base |
| 6.4 Sem dados desactualizados fora do eixo 2 | 3 | Nada de promoções, equipa, instalações ou nomes antigos apresentados como actuais |
| 6.5 Calibração | 2 | Quando não sabe, diz que não sabe |

### Calcular

- Cada afirmação errada desconta num só critério, o mais específico: um horário desactualizado conta em 2.4, não também em 6.4; um "concessionário oficial" inventado conta em 2.5, não também em 3.2.
- Nota do motor = pontos obtidos ÷ pontos verificáveis × 100, arredondada às unidades. Escreve sempre a cobertura: "71, sobre 85 pontos verificáveis".
- Com menos de 60 pontos verificáveis num motor, mostra os pontos mas não a nota: a amostra não chega.
- Não faças média entre motores com coberturas muito diferentes sem o dizer. Os motores são canais diferentes; a tabela por motor é o resultado principal.
- Na dúvida entre dois níveis, escolhe o inferior e explica. A dúvida sobre se um facto foi verificado resolve-se com `N/V`, não com zero.

## Exemplo resolvido (fictício)

Stand Exemplo, Leiria (fictício), motor X, 22 perguntas, três repetições. Só os achados que mexem na nota:

| Critério | O que se viu | Etiqueta, gravidade, estabilidade | Pontos |
|---|---|---|---|
| 2.4 Horário | Em 2 de 3 repetições, "fechado ao sábado". A ficha diz que abre ao sábado de manhã desde 2024 e que antes fechava | `desactualizada`, alta, intermitente | 1 de 3 |
| 2.5 Estatuto | Em 3 de 3, "concessionário oficial Peugeot". É multimarca independente | `inventada`, alta, estável | 0 de 4 |
| 4.2 Proporção | Em 3 de 3 respostas a D1, uma queixa de 2021 no Portal da Queixa vira "problemas frequentes com a documentação". A queixa existe, é única e foi respondida | `imprecisa`, média, estável | 0 de 5 |
| 2.7 Anos de actividade | O gestor não confirmou a data de início | `N/V` | fora (2) |

Resultado, com os restantes critérios cumpridos: 87 pontos em 98 verificáveis, nota 89. A nota é alta, mas o relatório abre com o estatuto de concessionário (alta, estável) e o horário (alta, intermitente), porque são esses que podem custar uma venda. A queixa antiga vai para as correcções como "responder e pedir avaliações recentes", não como "pedir à IA que a retire".
