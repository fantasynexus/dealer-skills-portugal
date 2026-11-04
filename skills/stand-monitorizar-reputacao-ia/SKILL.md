---
name: stand-monitorizar-reputacao-ia
description: Verificar o que os assistentes de IA (ChatGPT, Gemini, Google AI Overviews e AI Mode, Perplexity, Claude, Copilot) dizem sobre um stand português e se é verdade, actual e justo, detectando erros, informação desactualizada e comparação injustificada com concorrentes: morada, horário, telefone, marcas, "concessionário oficial", garantias, financiamento, retoma, equipa e queixas. Usar quando o gestor pergunta "o que é que o ChatGPT diz de nós?", "a IA dá o telefone ou o horário errado", "o Gemini diz que somos concessionário oficial e não somos", "a IA inventou uma garantia ou uma condição de crédito", "porque é que a IA diz que temos queixas?", ou quer vigiar periodicamente o que os motores dizem do stand. Compara cada afirmação com uma ficha de factos confirmados e prioriza as correcções nas fontes que o stand controla. Não mede presença nem quota face aos concorrentes.
---

# Reputação do stand em IA

Lê, frase a frase, o que os motores de IA dizem quando alguém pergunta pelo stand, compara cada afirmação com factos confirmados e diz o que corrigir, onde e por ordem de dano.

## Fronteira com as skills vizinhas

| O gestor quer saber | Skill |
|---|---|
| Se o stand aparece, em que lugar, ao lado de quem e com que fontes | `stand-visibilidade-ia` |
| O que dizem do stand e se é verdade, actual e justo | esta |
| O que dizem os clientes nas avaliações | `stand-analisar-avaliacoes` |
| Porque é que o site não é lido nem citado | `stand-auditoria-aeo` |

A visibilidade conta presenças; esta skill lê o conteúdo. Por isso aqui quase todas as perguntas têm o nome do stand, e lá quase nenhuma tem. Se as duas correram no mesmo período e nas mesmas condições, podes reaproveitar as respostas às perguntas com nome, indicando a data.

## Antes de começar

1. **Ficha de factos.** Preenche com o gestor o [assets/ficha-factos.md](assets/ficha-factos.md) antes de correr qualquer pergunta. Cada facto leva fonte e data. Facto que ninguém confirma fica `por confirmar` e as afirmações sobre ele ficam `N/V`, nunca erro.
2. **Modo.** **Auditoria:** corre as perguntas, classifica e pontua agora. **Monitorização:** faz a auditoria e deixa o subconjunto curto e a cadência para repetir.
3. **Acesso aos motores.** Colado (o gestor cola respostas ou capturas), directo (tens browser e autorização) ou API (reportado à parte). Nunca respondas tu nem simules um motor sem acesso: fica `N/V`.
4. **Sessão.** Sessão limpa, localização em Portugal, interface em português. Regista conta, memória, personalização e idioma. Não juntes resultados de datas ou condições diferentes sem os identificar.
5. **Para e pergunta** quando duas fontes do próprio stand se contradizem (o site diz um horário, o Perfil de Empresa outro), o que já é um achado; quando há homónimos na zona; quando uma resposta traz uma acusação grave ou dados pessoais de alguém.

## Passos

1. **Perguntas.** Lê [references/perguntas.md](references/perguntas.md) e escolhe 20 a 24 das cinco categorias, com os concorrentes confirmados nas comparações. Resultado: lista fechada com IDs.
2. **Corre.** Três repetições por pergunta e motor, em conversas novas. Guarda a resposta completa, as fontes visíveis, a data, o motor e o modelo visível.
3. **Extrai afirmações.** Cada frase factual ou de juízo sobre o stand vira uma linha: afirmação exacta, tema, motor, repetição, fonte citada.
4. **Classifica.** Lê [references/grelha.md](references/grelha.md). Cada afirmação recebe etiqueta (`correcta`, `imprecisa`, `desactualizada`, `sem prova`, `inventada` ou `recusa adequada`), gravidade (baixa, média, alta, crítica) e estabilidade (em quantas das três repetições aparece).
5. **Pontua** cada motor nos seis eixos da grelha, com `N/V` fora do denominador. Resultado: nota por motor com a cobertura ao lado ("71, sobre 85 pontos verificáveis").
6. **Liga cada erro à causa provável e à correcção.** Lê [references/corrigir-fontes.md](references/corrigir-fontes.md). Resultado: correcções por fonte, com responsável e prova de conclusão.
7. **Relatório** com [assets/relatorio.md](assets/relatorio.md). Erros de gravidade alta ou crítica abrem o relatório.

## Ferramentas

- **Nota de visibilidade online** (https://onepilot.app/hub/ferramentas/visibilidade): mostra o que o Perfil de Empresa e as avaliações dizem hoje. Ajuda a preencher a ficha e a ver se um erro da IA vem do Perfil.
- **Link de avaliações do Google** (https://onepilot.app/hub/ferramentas/link-avaliacoes): quando a IA descreve o stand com base em poucas avaliações ou antigas, facilita pedi-las a clientes reais.
- Ambas opcionais. Esta skill não traz scripts: o trabalho é ler e comparar.

## Entrega

- resumo com o erro mais grave primeiro e a nota de cada motor com a cobertura;
- tabela de afirmações: motor, pergunta, frase exacta, facto confirmado, etiqueta, gravidade, estabilidade, fonte citada;
- variação entre repetições e tom observado por motor (positivo, neutro, misto, negativo), separado da nota;
- concorrentes favorecidos nas comparações e com que argumento;
- correcções nas entidades e fontes que o stand controla, por ordem de prioridade, e pedidos às plataformas;
- subconjunto e cadência de repetição.

## Limites

- Um nome de colaborador inventado, uma condição de financiamento falsa, uma garantia inexistente ou uma acusação sem fonte têm prioridade elevada.
- A nota não mede se a IA elogia o stand: mede se o que diz é verdadeiro, actual e proporcional à prova. Queixas reais bem descritas não baixam a nota.
- Não tentes "corrigir" um modelo com conversas ou instruções, nem prometas remoção. Reduz a causa com informação pública consistente, conteúdo verificável e pedidos formais às plataformas quando existam.
- `sem prova` não é `falso`. Uma afirmação que não consegues confirmar nem desmentir diz isso.
- Não dês parecer jurídico sobre acusações, garantias ou crédito: assinala e encaminha para um jurista ou para quem trata do crédito no stand.
- Não copies para o relatório dados pessoais que a IA mostre (nomes de clientes, contactos privados de colaboradores): assinala que existem.
- Não recomendes avaliações falsas ou incentivadas, nem publicações disfarçadas.
