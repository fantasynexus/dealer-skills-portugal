# Pontos de contacto dos 90 dias

Biblioteca de onde escolhes os 12 a 18 pontos do programa. Os textos estão em [../assets/mensagens-clientes.md](../assets/mensagens-clientes.md), pelo código da última coluna.

- **★** ponto a não cortar, mesmo com pouca capacidade da equipa.
- **S** serviço: necessário para cumprir a venda, a garantia ou um pedido do cliente. Não depende do consentimento de marketing e não leva promoção.
- **M** marketing: promove o stand ou os seus serviços. Precisa de consentimento ou da excepção de cliente, e de oposição em cada mensagem.
- **M?** natureza a confirmar com o DPO; até lá, trata como marketing.

## Fase 1: entrega (dias -2 a 1)

Objectivo: o cliente sai com a viatura, os documentos explicados, o nome de quem o atende depois e a noção do que vem a seguir.

| # | Quando | Canal | Nat. | Responsável | Gatilho | Supressão | Resultado esperado | Texto |
|---|---|---|---|---|---|---|---|---|
| P1 ★ | 1 a 2 dias antes | o preferido do cliente | S | vendedor ou administrativo | entrega marcada | entrega cancelada; se remarcada, recalcula | cliente traz o que é preciso | M1 |
| P2 ★ | dia 0 | presencial | S | vendedor | entrega | nenhuma | checklist assinada; consentimentos registados em separado | G1, cartão |
| P3 ★ | dia 0, no fim da entrega | presencial, ou mensagem se a pessoa não estiver | S | vendedor e pós-venda | fim da entrega | nenhuma | cliente sabe nome e telefone da pós-venda | G2, M3 |
| P4 | dias 0 a 2 | videochamada ou telefone marcado | S | vendedor | entrega à distância | entrega presencial | demonstração feita; checklist confirmada por escrito | G1 adaptado |
| P5 ★ | dia 1 | email, com WhatsApp curto | S | vendedor | entrega registada | nenhuma | resumo e contactos guardados pelo cliente | M2 |

## Fase 2: primeira semana (dias 2 a 7)

Objectivo: apanhar problemas cedo, enquanto são fáceis de resolver e o cliente ainda se lembra de quem o atendeu.

| # | Quando | Canal | Nat. | Responsável | Gatilho | Supressão | Resultado esperado | Texto |
|---|---|---|---|---|---|---|---|---|
| P6 ★ | dias 3 a 5 | telefone, por uma pessoa; WhatsApp se não atender | S | vendedor | 3 dias após a entrega | caso aberto (segue a excepção E2) | problemas registados ou "tudo bem" registado | G3, M4 |
| P7 | dia 7 | email | S | vendedor ou pós-venda | 7 dias após a entrega | cliente pediu só telefone | dúvidas de utilização resolvidas (telemóvel, portagens, documentos) | M5 |

## Fase 3: dias 8 a 30

Objectivo: fechar os pendentes (registo, documentos), pedir a avaliação a todos e deixar a garantia clara.

| # | Quando | Canal | Nat. | Responsável | Gatilho | Supressão | Resultado esperado | Texto |
|---|---|---|---|---|---|---|---|---|
| P8 ★ | evento | o preferido do cliente | S | administrativo | `registo_concluido` | nenhuma | documento entregue ou enviado | M6 |
| P9 | evento | telefone e email | S | administrativo | registo não concluído no prazo que o stand fixou como normal | registo concluído | cliente informado antes de perguntar | M7 |
| P10 ★ | dias 10 a 14 | cartão no dia 0 e mensagem | M? | vendedor | 10 dias após a entrega | oposição; caso aberto adia o pedido, não o cancela | pedido feito a todos os clientes entregues | cartão, M8 |
| P11 | dias 14 a 21 | presencial | S | oficina própria | cliente perto do stand aceitou visitar a oficina | sem oficina própria; cliente longe | cliente conhece a oficina e a pessoa | G4 |
| P12 ★ | dias 25 a 30 | email | S | pós-venda | 25 dias após a entrega | nenhuma | cliente sabe como accionar a garantia | M9 |

## Fase 4: dias 31 a 90

Objectivo: encaminhar a primeira manutenção para o sítio certo, confirmar a experiência e passar o cliente para os fluxos de longo prazo.

| # | Quando | Canal | Nat. | Responsável | Gatilho | Supressão | Resultado esperado | Texto |
|---|---|---|---|---|---|---|---|---|
| P13 | dias 30 a 45 | email | S se só informa; M se promove a oficina | pós-venda | 30 dias, stand com oficina própria ou parceira | sem oficina; sem autorização para passar contacto à parceira | cliente sabe onde e como marcar | M10 |
| P14 ★ | dias 45 a 60 | telefone | S | pós-venda | 45 dias após a entrega | caso aberto (já há contacto) | experiência confirmada; problemas e mudança de preferências registados | G5 |
| P15 | evento | email e SMS | S | oficina | marcação feita pelo cliente | marcação cancelada | marcação cumprida | M11 |
| P16 | 30 dias antes da manutenção prevista | email, SMS se houver consentimento | M, salvo pedido expresso do cliente | oficina | data ou quilómetros previstos registados e dentro dos 90 dias | sem data conhecida; manutenção já feita; oposição | marcação | M12 |
| P17 | dias 75 a 90 | email | M | vendedor ou gerência | 75 dias após a entrega | oposição; caso aberto | recomendações espontâneas | M13 |
| P18 ★ | dia 90 | email | S | pós-venda | 90 dias após a entrega | nenhuma | cliente com datas e contactos à mão; entrada em `stand-fluxos-email` | M14 |

Os pontos ★ somam 10. Um programa de 12 a 18 pontos junta-lhes os que o stand consegue cumprir: P4 só na entrega à distância, P11 e P13 só com oficina, P16 só com data de manutenção conhecida.

## Excepções

| # | Situação | Sinal | Quem decide | Resposta | Volta ao programa |
|---|---|---|---|---|---|
| E1 | Atraso no registo | passou o prazo normal do stand | administrativo | telefonema e M7; declaração de circulação renovada se preciso | com `registo_concluido` |
| E2 | Avaria ou falta de conformidade | cliente reporta | pós-venda, gerência se houver custo | M15 no próprio dia útil; caso aberto com data | quando o caso fecha; os pontos de marketing ficam suspensos até lá |
| E3 | Insatisfação sem avaria (atendimento, promessa) | cliente reporta ou P6/P14 detecta | gerência | contacto de uma pessoa, não automático | quando o cliente o diz ou o caso fecha |
| E4 | Cliente não responde | duas tentativas humanas sem resposta | vendedor | pára; regista; segue só a serviço por email | ponto seguinte de serviço |
| E5 | Livre resolução ou devolução | cliente pede | gerência, com jurista | segue o contrato e a lei aplicável; nada automático | não volta |
| E6 | "Não me contactem" | cliente pede | quem recebe o pedido | regista na hora; confirma por escrito; só passam os contactos obrigatórios | não volta ao marketing |

Na primeira resposta a uma avaria ou queixa, ninguém admite nem nega responsabilidade: regista-se, agradece-se e diz-se quem contacta e quando.

## Regras de cadência

Decisão do stand; estas são as regras por omissão desta skill, não regras legais.

- No máximo um contacto não pedido por semana, fora dos de serviço desencadeados por eventos (registo, marcação).
- Nunca dois pontos no mesmo dia, nem a mesma mensagem por dois canais.
- Horário fixado pelo stand para SMS, WhatsApp e telefone. Sugestão: dias úteis entre as 9h e as 20h e sábado de manhã; nada ao domingo nem em feriados, salvo marcação pedida.
- O cliente que responde por um canal passa a ser contactado por esse.
- Um ponto saltado (cliente de férias, caso aberto) não se repete em dobro depois.

## Campos e eventos no sistema

| Campo ou evento | Usado em | Nota |
|---|---|---|
| `data_entrega`, `tipo_entrega` | todos | presencial ou à distância |
| `vendedor`, `pos_venda` | todos | função e nome |
| `tipo_oficina` | P11, P13, P16 | própria, parceira, marca, nenhuma |
| `canal_preferido` | todos | actualiza quando o cliente muda |
| `consentimentos` | pontos M | canal, finalidade, data, texto, quem recolheu |
| `oposicao` | todos os M | canal e data; global quando é "não me contactem" |
| `registo_pedido`, `registo_concluido`, `documento_entregue` | P8, P9 | datas |
| `caso_aberto` | supressões | data de abertura e de fecho |
| `proxima_manutencao`, `proxima_inspeccao` | P16, P18 | valor e fonte (ficha, plano, histórico) |
| `pedido_avaliacao` | P10 | data do pedido; não se regista o que o cliente escreveu como critério para pedir |

## Métricas

Define cada uma antes de medir. Metas só depois de algumas semanas de dados do próprio stand.

| Métrica | Definição |
|---|---|
| Checklist completa | entregas com checklist assinada ÷ entregas |
| Pós-venda apresentada | entregas com P3 feito ÷ entregas |
| Dias até ao registo | mediana de dias entre venda e `registo_concluido` |
| Contacto na primeira semana | clientes com P6 feito (com resposta) ÷ entregas |
| Problemas cedo | casos abertos nos primeiros 30 dias, por tipo |
| Garantia | casos de garantia abertos e dias até ao fecho |
| Primeira manutenção no stand ou na parceira | manutenções marcadas ÷ clientes com manutenção prevista no período (quando aplicável) |
| Avaliações | avaliações novas no período ÷ pedidos feitos (sem separar por nota) |
| Oposições | oposições e retiradas de consentimento por ponto de contacto |
