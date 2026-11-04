---
name: stand-classificar-chamadas
description: Classificar transcrições de chamadas de um stand automóvel em Portugal em vendas, pós-venda, peças, financiamento ou outros, sem inflacionar leads, com uma frase de prova por chamada e um ficheiro CSV ou JSON de formato fixo. Usar quando o gestor pergunta quantas chamadas foram mesmo de vendas, quer rever as transcrições exportadas da plataforma de chamadas, desconfia dos números de chamadas do fornecedor ou do Google Ads, quer saber em quantas chamadas de vendas a equipa ficou com nome e contacto e quantas acabaram em visita marcada, ou quer separar compradores de quem quer vender o carro ao stand. Serve para uma chamada, um lote colado ou um ficheiro exportado.
---

# Classificar chamadas do stand

Lê cada transcrição completa e põe-na numa de cinco categorias (vendas, pós-venda, peças, financiamento, outros), com uma frase de prova e um motivo. O objectivo é um número honesto de contactos de vendas: na dúvida real, a chamada não conta como venda e vai para revisão humana. Não transcreve áudio, não avalia colaboradores e não prevê quem vai comprar.

## Antes de começar

1. **Autorização.** Confirma que a utilização destas gravações ou transcrições está autorizada (aviso dado a quem ligou, finalidade compatível com a classificação). Se ninguém sabe, pergunta; se a resposta for não, pára. As perguntas sobre gravação estão em `stand-auditoria-rastreio-chamadas`.
2. **Formato da entrada.** Detecta:
   - uma transcrição;
   - um lote colado, com separadores claros (`---`, "Chamada 1", linhas em branco entre blocos);
   - um ficheiro exportado (CSV ou JSON com uma coluna de transcrição).

   Se não é claro onde acaba uma chamada e começa a seguinte, pergunta antes de classificar.
3. **Só áudio.** Não transcreves. Pede as transcrições, ou uma ferramenta de transcrição aprovada pelo stand (quem transcreve é subcontratante para efeitos do RGPD).
4. **Identificadores.** Mantém os da entrada (ID, data e hora, duração, direcção). Sem ID, numera `C001`, `C002`…
5. **Saída.** Pergunta se querem CSV, JSON ou os dois. Por omissão: relatório em Markdown mais CSV.
6. **Lotes grandes.** Processa por blocos, sem saltar chamadas, e confirma no fim que o número de linhas classificadas é igual ao de chamadas recebidas.

## Passos

1. Antes da primeira chamada, lê [references/rubrica.md](references/rubrica.md) (categorias, fluxo de decisão, casos difíceis, campos) e [references/exemplos.md](references/exemplos.md) (transcrições fictícias resolvidas).
2. Lê cada chamada até ao fim. Não classifiques pela primeira frase nem por palavras soltas: "Golf", "crédito" ou "garantia" não decidem nada sozinhas.
3. Aplica o fluxo de decisão. Escolhe a finalidade principal, regista a secundária e marca `sinal_vendas` quando uma chamada que não é de vendas mostra interesse real em comprar.
4. Escreve a `prova` (citação curta, com dados pessoais substituídos por `[nome]`, `[telefone]`, `[matrícula]`…) e o `motivo` (uma frase que liga a prova à categoria).
5. Dá a confiança (`alta`, `media`, `baixa`). Confiança baixa leva sempre `rever = sim`.
6. Só em vendas, preenche os campos de vendas. O que não foi dito fica `nao_referido`; não infiras.
7. Gera a saída no formato fixo de [references/formato-saida.md](references/formato-saida.md).
8. Calcula o resumo com denominadores. As chamadas com `rever = sim` ficam fora do número principal de vendas até uma pessoa decidir.
9. Antes de entregar, corre a validação de [references/formato-saida.md](references/formato-saida.md): número de linhas, valores das listas, campos vazios fora de vendas, nenhum dado pessoal na prova.

## Regra de honestidade

- **Vendas** é intenção nova de negócio sobre uma viatura, activa nesta chamada: comprar (com ou sem retoma, também para um familiar) ou vender a viatura ao stand. Mencionar uma viatura não chega.
- Compradores e quem quer vender ao stand contam em separado; nunca se somam num único número de "leads".
- Uma chamada sobre garantia, devolução, prestação, documentação ou reparação de uma compra passada não é venda só porque fala de uma viatura.
- Na dúvida real: categoria mais provável, confiança baixa, `rever = sim`, fora do número principal.
- Números feios ficam feios: "3 contactos novos de compra em 71 chamadas" é o resultado, não um problema a esconder.

## Entrega

Preenche [assets/relatorio.md](assets/relatorio.md): a frase principal com denominador; a tabela por categoria; os números de vendas separados (contactos de vendas, contactos novos de compra, vendas ao stand, leads válidos na amostra, marcações); a lista para revisão humana; os sinais de vendas noutras chamadas; a tabela por chamada; e o ficheiro CSV ou JSON. Distingue sempre chamadas, contactos de vendas, leads válidos e marcações: não são sinónimos.

## Limites

- Não repete telefone, email, morada, NIF, matrícula, IBAN, rendimentos ou dados de crédito; substitui-os na prova. Não cita dados de saúde nem outras categorias especiais do RGPD, mesmo que o cliente os refira.
- Não inventa nomes, viaturas, origens nem próximas acções.
- Não avalia colaboradores um a um nem tira conclusões disciplinares. No máximo dá indicadores de processo agregados (por exemplo, em quantas chamadas de vendas ficou contacto), com período e tamanho da amostra. Usar gravações para avaliar pessoas é matéria para o encarregado de protecção de dados ou um jurista (Código do Trabalho e Regulamento (UE) 2024/1689; confirmar versão e âmbito).
- Não faz análise de emoções nem de "sentimento" das pessoas.
- Não classifica por duração da chamada nem por listas de palavras-chave.
- Com amostras pequenas não tira tendências nem compara períodos.
- Os sinais de vendas em chamadas de pós-venda só dão seguimento comercial se o cliente aceitou ser contactado para isso.

## Skills relacionadas

- `stand-auditoria-rastreio-chamadas`: de onde vêm as chamadas, quantas ficam perdidas e se a gravação tem aviso.
- `stand-auditoria-ga4-google-ads`: comparar chamadas qualificadas com as conversões do Google Ads e com o CRM.
- `stand-responder-leads`: seguimento dos contactos de vendas encontrados.
