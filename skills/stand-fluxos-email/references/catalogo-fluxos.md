# Catálogo de fluxos

Os 17 fluxos possíveis num stand. Só entram no programa os que têm um gatilho fiável no sistema. As naturezas estão explicadas em [consentimento-e-envio.md](consentimento-e-envio.md); onde diz "confirmar", a decisão final é do DPO. Os textos estão em [../assets/emails.md](../assets/emails.md).

Prazos e cadências são sugestões de partida desta skill, não regras legais nem valores medidos: o stand ajusta-os.

## Resumo

| # | Fluxo | Natureza | Prioridade de arranque |
|---|---|---|---|
| 1 | Resposta a novo contacto | transaccional | alta |
| 2 | Seguimento de proposta | pré-contratual | alta |
| 3 | Seguimento de test-drive | pré-contratual | média |
| 4 | Confirmação de marcação | transaccional | alta |
| 5 | Boas-vindas após entrega | serviço | alta |
| 6 | Lembrete de documentação | serviço | alta |
| 7 | Apresentação do pós-venda | serviço ou marketing | média |
| 8 | Lembrete de manutenção | marketing, salvo pedido | média |
| 9 | Orçamento de oficina não aceite | pré-contratual | média |
| 10 | Pós-serviço e satisfação | serviço ou marketing | média |
| 11 | Chamada técnica da marca | segurança | alta, se houver dados |
| 12 | Fim de contrato ou financiamento | marketing | baixa, com revisão jurídica |
| 13 | Momento de retoma ou renovação | marketing | baixa |
| 14 | Aniversário de compra | marketing | baixa |
| 15 | Cliente inactivo | marketing | baixa |
| 16 | Pedido de recomendação | marketing | baixa |
| 17 | Convite para evento | marketing | baixa |

Não há fluxo de aniversário do cliente: a data de nascimento não é precisa para vender nem para reparar viaturas, e pedi-la só para isso contraria a minimização de dados.

## 1. Resposta a novo contacto

- **Gatilho:** contacto criado no CRM (formulário do site, email de portal, pedido de informação).
- **Entrada:** email válido; pedido sobre uma viatura ou um serviço.
- **Exclusões:** contacto já respondido por uma pessoa; pedido repetido do mesmo contacto no mesmo dia.
- **Cadência:** um email imediato. O seguimento é humano, com `stand-responder-leads`.
- **Saída:** primeira resposta humana registada.
- **Campos:** viatura de interesse, origem do contacto, vendedor atribuído, prazo de resposta que o stand cumpre.
- **Medida:** tempo até à primeira resposta humana; contactos que chegam a visita.
- **Cuidado:** não confirmar disponibilidade da viatura se o stock não estiver ligado ao sistema em tempo real. Os portais têm termos próprios sobre o uso dos contactos que entregam: confirmar.

## 2. Seguimento de proposta

- **Gatilho:** proposta enviada sem resposta ao fim de 3 dias.
- **Entrada:** proposta registada com viatura e validade.
- **Exclusões:** viatura vendida ou reservada; cliente comprou; cliente disse que não; reclamação aberta.
- **Cadência:** até 2 emails em 10 dias. Depois disso, ou para outras viaturas, é marketing.
- **Saída:** resposta, visita marcada, compra, recusa ou fim da validade.
- **Campos:** viatura, data e validade da proposta, vendedor.
- **Medida:** propostas com resposta; visitas; vendas.
- **Cuidado:** o email não repete preço nem condições diferentes da proposta escrita. Se falar de prestação, aplica-se a regra de crédito da secção 5 de [consentimento-e-envio.md](consentimento-e-envio.md).

## 3. Seguimento de test-drive

- **Gatilho:** test-drive registado sem proposta nem compra ao fim de 2 dias.
- **Exclusões:** comprou; disse que não; reclamação aberta; já tem proposta (passa ao fluxo 2).
- **Cadência:** até 2 emails em 10 dias.
- **Saída:** resposta, proposta, compra, recusa.
- **Campos:** viatura experimentada, data, vendedor.
- **Medida:** test-drives que passam a proposta.

## 4. Confirmação de marcação

- **Gatilho:** marcação criada ou alterada (visita, test-drive, entrega, oficina, avaliação de retoma).
- **Cadência:** confirmação imediata e lembrete na véspera.
- **Saída:** marcação cumprida ou cancelada.
- **Campos:** data, hora, morada, o que trazer, contacto, ligação para alterar.
- **Medida:** marcações cumpridas ÷ marcações.
- **Cuidado:** sem promoções. Cliente que se opôs ao marketing continua a receber este fluxo.

## 5. Boas-vindas após entrega

- **Gatilho:** entrega registada.
- **Exclusões:** cliente no programa de `stand-onboarding-cliente`; caso aberto.
- **Cadência:** um email no dia seguinte; opcional um segundo ao 7.º dia.
- **Saída:** fim da cadência.
- **Campos:** viatura, vendedor, pessoa de pós-venda, estado do registo, resumo da garantia copiado do contrato.
- **Medida:** respostas com dúvidas ou problemas (é para isso que serve).

## 6. Lembrete de documentação

- **Gatilho:** documento em falta (assinatura, comprovativo) ou documento disponível (registo concluído).
- **Cadência:** um email; um lembrete 5 dias depois se continuar em falta; depois, telefonema de uma pessoa.
- **Saída:** documento entregue.
- **Campos:** que documento, para quê, como entregar.
- **Medida:** dias até o documento estar completo.
- **Cuidado:** não pedir cópias de documentos de identificação por email quando não são precisas; quando são, indicar um canal seguro.

## 7. Apresentação do pós-venda

- **Natureza:** serviço se só diz quem contactar e como accionar a garantia; marketing se promove serviços ou preços de oficina.
- **Gatilho:** 21 a 30 dias após a entrega, quando não há programa de `stand-onboarding-cliente`.
- **Cadência:** um email.
- **Campos:** pessoa de pós-venda, contactos, oficina, como accionar a garantia.

## 8. Lembrete de manutenção

- **Natureza:** marketing, salvo se o cliente pediu os lembretes ou se o contrato de garantia os prevê: confirmar.
- **Gatilho:** data ou quilómetros previstos registados, com fonte. Quilómetros projectados a partir de visitas anteriores são uma estimativa: diz que o são.
- **Exclusões:** manutenção já feita (aqui ou noutro lado, se o cliente disse); viatura vendida; oposição; caso aberto.
- **Cadência:** 2 emails (30 dias antes e na data) e um SMS se houver consentimento para SMS.
- **Saída:** marcação ou fim da cadência.
- **Medida:** marcações ÷ lembretes entregues.
- **Cuidado:** sem data ou quilómetros com fonte, não envia. Não diz que a manutenção no stand é obrigatória para manter a garantia sem ler as condições.

## 9. Orçamento de oficina não aceite

- **Gatilho:** orçamento registado como não aceite.
- **Exclusões:** aceite depois; feito noutro lado; reclamação aberta.
- **Cadência:** um email aos 7 dias e outro aos 30; depois pára.
- **Campos:** trabalho registado pela oficina, número e validade do orçamento.
- **Medida:** orçamentos aceites depois do lembrete.
- **Cuidado:** quando o trabalho mexe com segurança (travões, pneus, direcção), o email descreve o que a oficina registou, sem alarmismo. Não oferece descontos que não existem.

## 10. Pós-serviço e satisfação

- **Natureza:** um inquérito interno sem promoção pode ser serviço (confirmar); o pedido de avaliação pública trata-se como marketing.
- **Gatilho:** serviço ou entrega concluídos.
- **Exclusões:** reclamação aberta (resolve primeiro; o pedido de avaliação espera, não se cancela); pedido de avaliação feito ao mesmo cliente nos últimos meses (o stand fixa o intervalo).
- **Cadência:** um email 1 a 2 dias depois.
- **Medida:** respostas; problemas detectados; avaliações novas.
- **Cuidado:** o link da avaliação vai para todos, com o mesmo texto. Mandar para o Google só quem deu nota alta no inquérito é escolher clientes satisfeitos, o que as regras da Google proíbem.

## 11. Chamada técnica da marca

- **Natureza:** comunicação de segurança.
- **Gatilho:** informação da marca ou do importador que identifica a viatura.
- **Cadência:** um email, um lembrete aos 14 dias e um contacto de uma pessoa se não houver resposta.
- **Saída:** intervenção feita, ou cliente informa que já não tem a viatura.
- **Campos:** referência da campanha e o texto da marca.
- **Cuidado:** copia a informação da marca sem acrescentar nada; sem promoções. Um stand que não recebe estes dados da marca não cria este fluxo.

## 12. Fim de contrato ou de financiamento

- **Gatilho:** data de fim conhecida e com base para este uso. Se o stand intermediou o crédito, confirmar se pode usar essa data para marketing: revisão jurídica.
- **Exclusões:** campanha de `stand-campanha-retoma` activa; oposição; qualquer informação de incumprimento (nunca é sinal).
- **Cadência:** 2 emails, cerca de 90 e 45 dias antes do fim.
- **Cuidado:** em renting e em aluguer de longa duração a viatura pode pertencer à locadora. Escreve "quando o contrato terminar", não "a retoma do seu carro".

## 13. Momento de retoma ou renovação

- **Gatilho:** idade ou quilómetros da viatura acima de um limiar definido pelo stand. Isto é perfilagem para marketing: tem de estar na informação ao cliente, que se pode opor.
- **Exclusões:** compra recente (período fixado pelo stand); campanha de retoma activa; proposta em curso; oposição.
- **Cadência:** no máximo um email por ano por cliente.
- **Cuidado:** não indica valores de retoma. Campanhas com prazo e segmentação fina: `stand-campanha-retoma`.

## 14. Aniversário de compra

- **Gatilho:** data da entrega.
- **Cadência:** um email por ano.
- **Conteúdo:** datas úteis (inspecção, manutenção) e contactos. Mesmo sendo útil, conta como marketing por manter a relação comercial: confirmar.
- **Exclusões:** viatura vendida; reclamação aberta; campanha activa.

## 15. Cliente inactivo

- **Gatilho:** sem interacção há mais tempo do que o stand fixar.
- **Cadência:** um email a perguntar se quer continuar a receber, e um lembrete. Sem resposta, o marketing pára.
- **Cuidado:** inactividade longa é também altura de aplicar o prazo de conservação definido pelo stand (RGPD, artigo 5.º, princípio da limitação da conservação).

## 16. Pedido de recomendação

- **Gatilho:** sinal positivo registado (o cliente disse que recomendaria, voltou a comprar).
- **Cadência:** um pedido; no máximo dois por ano.
- **Cuidado:** pede que o cliente passe o contacto do stand, não que envie dados de terceiros. Incentivo, se existir, com condições escritas, e nunca ligado a avaliações.

## 17. Convite para evento

- **Gatilho:** evento real, com data, local e vagas.
- **Público:** clientes com consentimento e interesse provável (por exemplo, dono de uma marca num evento dessa marca).
- **Cadência:** convite e um lembrete só a quem se inscreveu.
- **Medida:** inscrições e presenças.
