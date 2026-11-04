---
name: stand-responder-leads
description: Escrever a primeira resposta e o seguimento de um contacto de cliente num stand automóvel em Portugal, vindo do Standvirtual, OLX, site, Facebook, Instagram, WhatsApp ou de uma chamada perdida. Usar quando o gestor pede "responde a este lead", "o que digo a este cliente", "mensagem para o WhatsApp", "perguntaram se ainda está disponível", "querem o último preço", "quanto me dão pelo meu carro", "seguimento de um contacto", "chamada perdida" ou quer uma cadência de seguimento. Entrega a mensagem por canal, as perguntas de qualificação (viatura, retoma, financiamento, prazo, test drive), a cadência de seguimento com regras de paragem e o registo para o CRM, confirmando disponibilidade e preço no DMS antes de os afirmar, sem prometer crédito nem valor de retoma, sem usar o contacto para marketing sem consentimento e sem enviar nada sem aprovação do gestor.
---

# Responder a um lead

Escreve a primeira resposta a um contacto de compra e o seguimento até haver conversa ou paragem. Trabalha contacto a contacto (ou um lote pequeno). Para desenhar automações de email do ciclo de vida, usa `stand-fluxos-email`; para classificar um lote de transcrições de chamadas, `stand-classificar-chamadas`.

## Antes de começar

1. Pede o contacto tal como chegou: canal, texto exacto, data e hora, viatura ou anúncio de origem. Não trabalhes sobre um resumo.
2. Pergunta quem responde (nome e função) e o horário do stand. As mensagens saem em nome de uma pessoa, não de "a equipa".
3. Escolhe o modo:
   - **Com acesso ao DMS/CRM:** confirmas disponibilidade, preço, quilómetros e local da viatura antes de escrever.
   - **Sem acesso:** escreves com marcadores `[CONFIRMAR NO DMS: ...]` e a mensagem não sai enquanto o gestor não os substituir.
4. Confirma como sai a mensagem. Por defeito, tudo é rascunho para o gestor aprovar. Envio automático só se o gestor o configurou expressamente, com âmbito limitado e com aviso de que a pessoa fala com um sistema automático.
5. Se o contacto não é de compra (oficina, garantia, documentação de uma compra passada, fornecedor), não é um lead: encaminha para quem trata e não o metas na cadência.

## Passos

1. **Lê e resume o pedido** numa linha: o que pede, sobre que viatura, por que canal. Pedidos típicos: disponibilidade, preço ou negociação, retoma, financiamento, test drive ou visita, informação técnica, entrega fora da zona.
2. **Confirma no DMS** se a viatura está disponível, reservada ou vendida, o preço actual, os quilómetros e onde está. Vendida: diz isso com clareza, propõe até duas alternativas confirmadas e pergunta se quer ser avisado quando entrar uma semelhante (isso é consentimento, regista-o).
3. **Escreve a primeira resposta** no canal em que o contacto chegou, seguindo [references/canais-e-mensagens.md](references/canais-e-mensagens.md): responde primeiro à pergunta feita, faz no máximo duas perguntas de qualificação, propõe um próximo passo concreto com duas opções de horário e assina com nome. Resultado: uma mensagem que se envia sem editar, depois de confirmados os marcadores.
4. **Qualifica sem interrogar:** viatura (esta ou alternativas), retoma (marca, modelo, ano, quilómetros, estado; o valor só depois de ver), financiamento (interesse e simulação; a aprovação é da financeira), prazo de decisão, test drive. Não repitas o que a pessoa já disse e não peças documentos.
5. **Prepara a cadência de seguimento** com [references/cadencia-e-regras.md](references/cadencia-e-regras.md): datas, canal e conteúdo de cada toque, cada um com algo novo, e as condições de paragem. Pára logo que a pessoa responde, diz que não quer, compra noutro lado ou a viatura deixa de estar disponível sem alternativa aceite.
6. **Separa o marketing:** se fizer sentido, pede à parte consentimento para outras comunicações (novidades, viaturas semelhantes, campanhas) e regista canal, data e texto. Sem consentimento, o contacto serve só para responder ao pedido.
7. **Regista no CRM** com os campos do modelo: origem, viatura, pedido, hora da primeira resposta, qualificação, próximo passo, consentimento, estado e motivo de paragem.
8. **Entrega para aprovação.** O gestor revê, substitui os marcadores e envia. Nada sai sem esse passo, salvo a configuração expressa do passo 4 de "Antes de começar".

## Quando parar e perguntar

- O DMS e o anúncio dão preços diferentes: pergunta qual vale e não respondes com nenhum até saberes.
- A pessoa pede desconto, "último preço" fechado ou um valor de retoma por escrito: entrega ao gestor uma resposta que não fecha valores e deixa a decisão com ele.
- A pessoa queixa-se de um atendimento anterior: responde como pessoa, fora da cadência. Se a queixa for pública, usa `stand-responder-avaliacoes`.
- O contacto parece burla (ligações de pagamento, pedidos de códigos, comprador que paga sem ver): pára e avisa o gestor.
- A mensagem traz dados sensíveis (saúde, dívidas, situação financeira): não os repetes e não os registas além do estritamente necessário.

## Chamada perdida

Ligar de volta é a primeira acção, logo que possível dentro do horário. Se a pessoa não atender, uma mensagem escrita curta que identifique o stand e quem ligou, com uma hora para nova tentativa. Não faças várias chamadas seguidas. Se o número for de um cliente com um assunto de oficina ou garantia em aberto, encaminha. Para perceber quantas chamadas se perdem e porquê, há `stand-auditoria-rastreio-chamadas`.

## Ferramentas

- Esta skill não precisa de scripts. Usa o DMS/CRM do stand para confirmar dados e registar.
- Para responder a perguntas técnicas sobre a viatura com factos já confirmados, reaproveita a ficha de `stand-escrever-anuncio`, se existir.
- Para seguimentos por email automáticos e reactivação de contactos antigos com consentimento, `stand-fluxos-email`.

## Entrega

Preenche [assets/modelo-resposta-lead.md](assets/modelo-resposta-lead.md): resumo do pedido, verificações no DMS, primeira resposta por canal, resposta alternativa se a viatura estiver vendida, perguntas de qualificação escolhidas, cadência com datas e paragem, pedido de consentimento quando se aplica, registo para o CRM e aprovação.

## Limites

- Não afirma disponibilidade, preço, quilómetros, equipamento, garantia ou prazo de entrega sem confirmação no DMS ou do gestor.
- Não promete aprovação de crédito, prestação, taxa ou valor de retoma. Uma simulação é da financeira; uma estimativa de retoma não é proposta.
- Não negoceia preço por escrito sem autorização do gestor e não inventa descontos.
- Não cria urgência falsa ("tenho outro cliente que vem amanhã").
- Não pede documentos de identificação, NIF, IBAN, comprovativos de rendimentos ou dados de crédito por chat ou email: a financeira recolhe-os pelo canal dela.
- Não usa o contacto para marketing sem consentimento à parte e não o junta a listas ou grupos.
- Não esconde que uma resposta é automática quando é.
- Não envia nada sem aprovação do gestor, salvo configuração expressa dele.
