---
name: stand-analisar-avaliacoes
description: Analisar com honestidade as avaliações de clientes de um stand em Portugal, pelo texto e não pelas estrelas, vindas do Google, Facebook, Portal da Queixa, Trustpilot, portais automóveis ou de uma exportação do stand. Usar quando o gestor pergunta "o que dizem de nós", "porque desceu a nota no Google", "quais são as queixas mais comuns", "analisa estas avaliações", "que avaliações temos de responder", "quem é elogiado", ou quer comparar vendas, financiamento, entrega, oficina e peças, períodos ou fontes. Entrega sentimento, temas com provas e denominador, sinais operacionais com responsável, alertas para jurista e a lista de avaliações a responder com prioridade, que passa a stand-responder-avaliacoes para redigir as respostas.
---

# Analisar avaliações de clientes

Lê o texto completo de cada avaliação; as estrelas não substituem o conteúdo. Cinco estrelas podem trazer um problema e três podem ser sobretudo positivas. Encontra padrões, mostra-os com prova e denominador, e diz o que fazer e quem o faz.

Não redige respostas. A resposta a uma avaliação individual é trabalho de `stand-responder-avaliacoes`, que recebe daqui a prioridade, o motivo e os pontos a cobrir. Para seguir o que os assistentes de IA dizem do stand, usa `stand-monitorizar-reputacao-ia`; para auditar o Perfil de Empresa, `stand-auditoria-perfil-google`.

## Antes de começar

1. **Fonte e período** de cada lote, e como foi recolhido (exportação, cópia manual, leitura pública). Sem isto, não há denominador.
2. **Lote completo ou amostra:** por exemplo, só as avaliações que a página mostra sem carregar mais. Com amostra, as percentagens valem só para a amostra.
3. **Quem vai ler:** gerência (resumo e sinais) ou responsáveis de área (temas e lista de respostas). Por omissão, gerência.
4. **Áreas que o stand tem:** sem oficina ou sem financiamento, essas áreas ficam `N/A`.

Modos:

- **Uma avaliação:** classificação, prioridade e pontos para `stand-responder-avaliacoes`.
- **Lote colado ou exportação** (CSV, folha de cálculo): análise completa.
- **Leitura pública**, se tiveres acesso à web: lê só o que está visível, regista data e hora da recolha e marca a completude como `N/V`.
- **Comparação com concorrentes:** só dados públicos, sem nomes de colaboradores dos outros stands, com a mesma regra de denominador.

Pára e pergunta se o lote mistura stands ou localizações sem coluna que os distinga, ou se te pedem para descobrir quem escreveu uma avaliação.

## Passos

1. **Tabela de trabalho.** Uma linha por avaliação: identificador (fonte, data, número), data, estrelas, texto, se já tem resposta do stand. Troca o nome de quem avaliou pelo identificador. Afasta e conta as que não têm texto, as de outra empresa e as duplicadas. Resultado: total recebido, total analisado e excluídas por motivo.
2. **Classificar cada avaliação** com [references/metodo.md](references/metodo.md): sentimento pelo texto (`positivo`, `misto`, `negativo`, `indeterminado`), área principal e secundárias, fase da experiência, temas de [references/temas.md](references/temas.md), menções a colaboradores tal como aparecem, alegações separadas de factos verificáveis, urgência e motivo, e uma frase curta de prova. Assinala quando estrelas e texto discordam.
3. **Agregar com denominador.** Contagens e percentagens com o total ao lado, por fonte, mês e área.
4. **Separar incidente, sinal e padrão** com as regras de [references/metodo.md](references/metodo.md). Tendência só quando as condições aí descritas se cumprem; abaixo disso, "sinal a confirmar". Não tires política de um incidente.
5. **Sinais operacionais.** Para cada padrão ou sinal forte: o que acontece, prova, acção concreta, responsável (função) e como medir se melhorou. "Melhorar a comunicação" não é acção.
6. **Alertas para jurista ou DPO.** Alegações com possível relevância legal vão numa lista à parte, sem opinião jurídica, com o diploma a confirmar indicado em [references/temas.md](references/temas.md).
7. **Avaliações a responder.** Prioridade, motivo, quem responde, prazo sugerido, pontos a cobrir e o que não dizer. A redacção segue para `stand-responder-avaliacoes`. Se essa skill não estiver instalada, entrega só os pontos e avisa que a resposta deve ser escrita e revista por uma pessoa do stand.
8. **Rever e entregar** com [assets/relatorio.md](assets/relatorio.md) e a lista de verificação da secção Entrega.

## Ferramentas

Opcionais; a análise faz-se sem elas.

- [Nota de visibilidade online](https://onepilot.app/hub/ferramentas/visibilidade): média e número de avaliações do Perfil de Empresa e concorrentes da zona. Dá contexto; não substitui a leitura do texto.
- [Link de avaliações do Google](https://onepilot.app/hub/ferramentas/link-avaliacoes): link directo e QR code para pedir avaliações a todos os clientes, sem escolher. Aumenta a amostra das próximas análises.

## Entrega

[assets/relatorio.md](assets/relatorio.md) preenchido: o que entrou na análise, resumo com números, sentimento, áreas, fontes e meses, temas com prova, menções a colaboradores para uso interno, sinais operacionais, alertas para jurista ou DPO, avaliações a responder, limitações e data da próxima análise.

Lista de verificação antes de entregar:

- [ ] Cada percentagem tem o denominador ao lado e o resumo diz se o lote é completo ou amostra.
- [ ] Cada tema tem pelo menos uma prova curta, com identificador, tirada do lote.
- [ ] Nenhum nome de quem avaliou, matrícula ou telefone aparece no relatório.
- [ ] Nenhuma alegação aparece como facto; o que se pode verificar diz onde e por quem.
- [ ] "Tendência" só aparece quando as condições de [references/metodo.md](references/metodo.md) se cumprem.
- [ ] Cada sinal operacional tem acção concreta, responsável e forma de medir.
- [ ] A lista de avaliações a responder tem pontos a cobrir, não respostas redigidas.

## Limites

- Não inventa citações, temas, datas nem nomes de colaboradores. Cada tema tem pelo menos uma prova real do lote.
- Não amplia dados pessoais: nomes de quem avaliou, matrículas, telefones e acusações a pessoas identificáveis ficam fora do relatório ou anonimizados.
- O Livro de Reclamações não é fonte pública. Reclamações fornecidas pelo stand são confidenciais e não se citam.
- A tabela de menções a colaboradores é para uso interno, não é avaliação de desempenho e não leva recomendações de sanção.
- Não suaviza os negativos nem esconde a dimensão da amostra.
- Não pede remoção de críticas legítimas, não denuncia avaliações só por serem negativas, não oferece incentivos, não filtra clientes satisfeitos e não admite responsabilidade legal em nome do stand.
- Não cria nem sugere avaliações falsas, de colaboradores ou de familiares.
