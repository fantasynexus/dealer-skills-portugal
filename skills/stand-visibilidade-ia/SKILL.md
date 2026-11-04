---
name: stand-visibilidade-ia
description: Medir se os assistentes de IA (ChatGPT, Gemini, Google AI Overviews e AI Mode, Perplexity, Claude, Copilot) mencionam, recomendam e citam um stand automóvel em Portugal quando um comprador pergunta por stands, marcas, modelos, financiamento ou retoma na zona, e ao lado de que concorrentes. Usar quando o gestor pergunta "o ChatGPT recomenda o meu stand?", "aparecemos quando se pede à IA um stand de usados em Leiria?", "quem é que a IA sugere em vez de nós?", "que sites é que a IA cita?", ou quer uma linha de base e um acompanhamento trimestral da visibilidade em IA. Mede presença observada (menção, posição, recomendação, fontes citadas, concorrentes); não diagnostica as causas técnicas do site nem verifica a fundo se o que é dito sobre o stand é verdade.
---

# Visibilidade do stand em IA

Mede se o stand aparece nas respostas dos assistentes de IA, em que lugar, ao lado de quem e com que fontes. É uma medição do que se observa, não um diagnóstico. O trabalho vizinho pertence a outras skills:

- porque é que o site não é lido nem citado: `stand-auditoria-aeo`;
- se o que a IA diz do stand é verdade, actual e justo: `stand-monitorizar-reputacao-ia`;
- quantas visitas a IA traz ao site: `stand-analisar-trafego-ia`.

## Antes de começar

1. Confirma com o gestor: nome comercial exacto e as variantes que os clientes usam, URL, morada, concelho e concelhos servidos, marcas e tipo de stock (usados, novos, eléctricos, comerciais, importados), serviços reais (financiamento, retoma, compra a particulares, oficina, garantia praticada), 2 a 5 concorrentes com nome e domínio, e o período.
2. Sem concorrentes definidos, propõe três a cinco da mesma zona e tipo de stock e pede confirmação antes de correr. Não os escolhas a partir das respostas que vais medir.
3. Motores: por omissão ChatGPT, Gemini, pesquisa Google (AI Overviews e AI Mode, se disponíveis em Portugal na data do teste: confirma), Perplexity, Copilot e Claude. Acrescenta outros (por exemplo, o Meta AI no WhatsApp) só se estiverem disponíveis e o gestor tiver razões para achar que os clientes os usam.
4. Escolhe o modo e escreve-o no relatório:
   - **Colado** (por omissão): o gestor corre as perguntas e cola cada resposta com as fontes, ou envia capturas.
   - **Directo:** tens browser ou ferramenta com acesso ao motor e autorização para o usar.
   - **API:** perguntas enviadas por API com pesquisa na web. Não é o que o comprador vê na aplicação: reporta à parte, nunca no mesmo denominador.
5. Nunca respondas tu às perguntas com o teu conhecimento nem simules um motor a que não tens acesso. Esse motor fica `N/V`. A tua opinião sobre o stand não é uma medição.
6. Fixa as condições de sessão: sessão limpa (janela privada ou conta sem memória nem histórico), localização em Portugal, interface em português. Regista se havia conta iniciada, memória ou personalização.
7. Para e pergunta quando há stands com nome parecido na zona, quando o stand mudou de nome ou de morada há pouco tempo, ou quando uma pergunta pressupõe um facto que ninguém confirmou.

## Passos

1. **Banco de perguntas.** Lê [references/perguntas.md](references/perguntas.md). Escolhe 20 a 30 perguntas pelas intenções, substitui os marcadores e retira as que não se aplicam (sem oficina, sem perguntas de oficina). Mostra a lista ao gestor e congela-a. Resultado: lista numerada com ID, intenção e texto exacto.
2. **Plano de corrida.** Três repetições por pergunta e motor, em sessões separadas, quando o custo o permite. No modo colado, 25 perguntas em seis motores com três repetições são 450 respostas: propõe começar pelos três motores que o gestor acha que os clientes usam e pelo núcleo fixo com três repetições, e o resto com uma, marcada no registo. Resultado: tabela perguntas × motores × repetições aprovada pelo gestor.
3. **Corre e regista.** Uma linha por resposta no [assets/registo-respostas.md](assets/registo-respostas.md), com a pergunta exacta, data, motor, modelo visível, modo, sessão e a resposta completa (ou a captura). Resposta que não foi guardada não conta.
4. **Classifica.** Lê [references/fontes-e-metricas.md](references/fontes-e-metricas.md) e preenche, para cada resposta: estado, menção do stand, posição, recomendação, concorrentes e outros stands nomeados, URLs citados com a categoria de cada fonte, e erro evidente.
5. **Calcula** por motor e por intenção: taxa de menção, quota de menção, recomendação positiva, citação do domínio próprio, consistência entre repetições e respostas com erro evidente. Escreve sempre o numerador e o denominador ("4 de 18"). Motores `N/V`, recusas e respostas sem conteúdo útil ficam fora do denominador.
6. **Analisa onde o stand perde.** Para as perguntas em que concorrentes aparecem e o stand não: o que apareceu, que fontes sustentaram a resposta, causa provável (escrita como hipótese) e a skill que a trata.
7. **Escreve o relatório** com [assets/relatorio.md](assets/relatorio.md) e anexa o registo.

## Ferramentas

- **Nota de visibilidade online** (https://onepilot.app/hub/ferramentas/visibilidade): mostra os concorrentes da zona e o estado do Perfil de Empresa. Serve para propor concorrentes no ponto 2 de "Antes de começar" e para ver se as fontes Google do stand estão completas. Opcional.
- Esta skill não traz scripts: o trabalho é correr perguntas e classificar respostas. Uma folha de cálculo com o CSV do registo chega para as contas.

## Entrega

Um relatório que o gestor lê em cinco minutos, com o registo em anexo:

- condições da medição (datas, motores, modo, sessão, número de perguntas e repetições);
- uma frase de resumo com números ("mencionado em 6 de 40 respostas; o concorrente A em 15 de 40");
- tabela por motor e por intenção, e matriz de concorrentes;
- fontes dominantes por categoria e presença do stand em cada uma;
- 5 a 10 perguntas onde o stand perde, com o que apareceu em vez dele;
- erros evidentes, encaminhados para `stand-monitorizar-reputacao-ia`;
- plano para o trimestre: acção, fonte, responsável, skill e como se prova que foi feita.

## Limites

- Uma corrida é uma fotografia. Não apresentes uma resposta gerada como opinião estável do mercado, nem fales de tendência sem o registo anterior com as mesmas perguntas e condições.
- Separa observação ("o Gemini nomeou o stand em 3 de 9 respostas") de inferência ("provavelmente porque o Perfil de Empresa tem mais avaliações").
- Não inventes menções, URLs, concorrentes ou posições. Não mistures motores, modos ou datas no mesmo denominador sem os identificar.
- Não prometas aparecer no ChatGPT. O plano melhora fontes que o stand controla ou pode influenciar de forma legítima.
- Não recomendes avaliações falsas ou pagas, publicações disfarçadas em fóruns, texto escondido para IA ou outra manipulação: violam as regras das plataformas e expõem o stand.
- Se uma resposta trouxer dados pessoais de clientes ou colaboradores, não os copies para o relatório: assinala que existem.
