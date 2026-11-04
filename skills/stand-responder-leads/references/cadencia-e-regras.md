# Cadência, consentimento e registo

Lê antes de preparar o seguimento ou de configurar qualquer envio automático. As referências legais são listas de controlo, não pareceres: confirma a redacção em vigor e, na dúvida, o stand fala com o encarregado de protecção de dados ou com um jurista.

## Cadência de seguimento

Uma sugestão a ajustar ao stand. Cada toque acrescenta alguma coisa útil; "só para saber se viu a mensagem" não conta.

| Momento | Canal | Conteúdo |
|---|---|---|
| Dia 0, logo que possível dentro do horário | O de origem | Primeira resposta |
| Dia 0, se a pessoa pediu chamada ou deixou telefone para isso | Telefone | Chamada; se não atender, mensagem curta |
| Dia 1 | O de origem | Algo novo: vídeo curto da viatura, fotos de um pormenor pedido, horários de test drive |
| Dia 3 | O de origem | Pergunta simples: ainda procura? Uma alternativa confirmada, se fizer sentido |
| Dia 7 | O de origem | Último seguimento activo: fica à disposição, sem pressão |
| Dia 14 | O de origem | Fecho: "dou o seu pedido por encerrado; se voltar a procurar, estamos cá" |

Depois do fecho, não há mais contactos sobre este pedido, salvo se a pessoa voltar a escrever ou tiver dado consentimento para outras comunicações.

Regras:

- No máximo um contacto por dia, dentro do horário que o stand define.
- O mesmo vendedor do princípio ao fim, sempre que possível.
- Muda o conteúdo, não só o dia. Se não tens nada novo, salta o toque.
- Uma chamada sem resposta e a mensagem que a segue contam como um único toque.

## Paragem imediata

A cadência pára e o motivo fica registado quando:

- a pessoa responde (passa a ser uma conversa, não uma cadência);
- diz que não quer ser contactada, que já comprou ou que desistiu;
- a viatura é vendida ou reservada e a pessoa não aceita alternativa;
- há uma reclamação ou um tom que pede um responsável;
- o contacto está errado ou é de outra pessoa;
- se percebe que não era um contacto de compra.

Pedidos de "não me contacte mais" valem para todos os canais e para todos os vendedores do stand.

## Bases para usar o contacto

- **Responder ao pedido:** quem pede informação sobre uma viatura está a pedir diligências antes de um contrato. Responder e fazer o seguimento desse pedido cabe nessa finalidade (RGPD, artigo 6.º, n.º 1, alínea b): confirma o enquadramento com o encarregado de protecção de dados). Moderação: o seguimento é sobre o pedido, não sobre outras coisas.
- **Marketing:** novidades, outras viaturas, campanhas, newsletter. Comunicações electrónicas de marketing a pessoas singulares precisam de consentimento prévio (Lei n.º 41/2004, na redacção em vigor: confirmar), pedido à parte, sem caixas pré-seleccionadas, com forma simples de retirar.
- **Informação:** a pessoa tem de poder saber quem trata os dados e para quê. A política de privacidade do stand deve estar no formulário do site; noutros canais, envia a ligação quando a pedirem ou quando recolhes dados novos.
- **Conservação:** um contacto perdido não fica guardado para sempre. O prazo é decisão do stand com o encarregado de protecção de dados.

## Pedir consentimento para marketing

Pergunta à parte, depois de responder ao pedido, e só se fizer sentido para a pessoa:

> Quer que o avisemos por [WhatsApp / email] quando entrar um carro semelhante? Só enviamos se disser que sim, e pode pedir para parar a qualquer momento.

Regista: resposta (sim ou não), canal, data, texto mostrado, quem pediu. Um "sim" para avisos de viaturas semelhantes não é um "sim" para todas as campanhas.

## WhatsApp

- **Aplicação WhatsApp Business:** mensagens escritas por pessoas, uma a uma. Não juntes contactos a grupos nem a listas de difusão sem consentimento.
- **Plataforma do WhatsApp Business (API), através de um fornecedor:** a Meta tem regras sobre mensagens iniciadas pela empresa, consentimento, janelas de conversa e modelos de mensagem aprovados. Confirma a política actual com o fornecedor antes de configurar seguimentos.
- Em ambos: o número é do stand, e o histórico fica acessível a quem substitui o vendedor.

## Envio automático

Por defeito, a skill entrega rascunhos. Se o gestor quiser envio automático, define por escrito:

| Pode sair automático | Não sai automático |
|---|---|
| Confirmação de recepção fora de horas | Preço que não foi lido do DMS no momento |
| Indicação de quando uma pessoa responde | Negociação, descontos |
| Marcação numa agenda real, com confirmação | Simulações de crédito ou valores de retoma |
| Lembrete de uma visita marcada | Respostas a reclamações |

Condições mínimas:

- **Aviso de sistema automático:** quem fala com um agente de IA tem de saber que fala com um sistema automático (Regulamento (UE) 2024/1689, artigo 50.º: confirmar a aplicação ao caso do stand, quem é fornecedor e quem é responsável pela implantação, e a data de aplicação, com as alterações que entretanto tenham sido aprovadas).
- **Passagem para uma pessoa:** a qualquer pedido, e sempre que a conversa sai do que está autorizado.
- **Registo:** o que foi enviado, quando e por que sistema, no CRM.
- **Revisão:** o gestor lê uma amostra das conversas automáticas com regularidade e corrige.

Modelo de aviso:

> Olá, esta é uma resposta automática do Stand Exemplo. Recebemos a sua mensagem sobre o [viatura] e uma pessoa da equipa vai continuar a conversa a partir das [hora] de [dia].

## Registo no CRM

| Campo | Exemplo | Nota |
|---|---|---|
| Data e hora de entrada | 2026-11-04 14:32 | |
| Canal | Standvirtual | Standvirtual, OLX, site, Facebook, Instagram, WhatsApp, telefone |
| Origem | Anúncio [ref. interna] | Referência interna, não matrícula |
| Pedido | Disponibilidade e retoma | Uma linha |
| Primeira resposta | 2026-11-04 14:51, [nome] | Hora e quem respondeu |
| Enviado por | Pessoa / sistema automático | |
| Retoma | Sim: marca, modelo, ano, km aproximados | Sem matrícula nesta fase |
| Financiamento | Interesse: sim / não / não referido | Sem dados financeiros |
| Prazo | "Este mês" / não referido | Palavras da pessoa |
| Test drive | Marcado [data e hora] / não | |
| Próximo passo | Chamada [data] | Sempre com data |
| Consentimento marketing | Sim / não; canal; data; texto | |
| Estado | Novo, em conversa, test drive, proposta, ganho, perdido, sem resposta | |
| Motivo de paragem | Comprou noutro lado / pediu para não contactar / sem resposta ao fecho | |

Usa `não referido` em vez de deduzir. Não registes no CRM o que a pessoa não disse.

## Medir sem inventar

Para o stand perceber se responde bem, mede com os próprios dados:

- tempo entre a entrada e a primeira resposta, por canal e por hora do dia;
- percentagem de contactos respondidos no próprio dia;
- contactos que chegam a visita, test drive, proposta e venda;
- motivos de perda.

Compara o stand consigo próprio ao longo do tempo. Não uses taxas "típicas" do sector como referência sem fonte. Para classificar as chamadas que chegam e separar vendas do resto, usa `stand-classificar-chamadas`.
