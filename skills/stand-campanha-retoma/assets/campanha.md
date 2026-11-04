# Campanha de retoma: {nome da campanha}

> {stand}, preparado em {data}.
> Nada é carregado em plataformas nem enviado sem autorização explícita do gestor (secção 12).

## 1. Resumo

| Campo | Valor |
|---|---|
| Objectivo | {vender viaturas / angariar usados / ambos} |
| Segmento | {A a F e nome} |
| Oferta real | {texto exacto, condições, prazo, onde está escrita} ou "avaliação sem compromisso" |
| Canais | {email, SMS, WhatsApp, telefone} |
| Janela | {de} a {até} ({n} dias) |
| Contactos por cliente | {n} |
| Elegíveis / após supressões / grupo de controlo | {n} / {n} / {n ou "sem controlo"} |
| Capacidade de avaliações por semana | {n} |
| Responsável | {função} |

## 2. Segmento e dados

| Campo | Valor |
|---|---|
| Regra de entrada | |
| Fonte e data dos dados | {sistema, campo, data da extracção} |
| O que não chega como sinal | |
| Prova de procura (segmento C) | {pedidos registados no período, sem identificar ninguém} |
| Revisão jurídica necessária | {sim, porquê / não} |

## 3. Lógica de audiência

```
SEGMENTO {letra}: {nome}
ENTRA SE
  ...
SAI SE
  qualquer supressão da lista do stand
CANAL
  ...
```

Sem nomes, telefones, emails nem matrículas.

## 4. Contagem

| Passo | Regra | Clientes | Saem |
|---|---|---|---|
| 1 | elegíveis pela regra de entrada | | |
| 2 | sem base no canal | | |
| 3 | compra recente | | |
| 4 | caso ou reclamação aberta | | |
| 5 | proposta em curso | | |
| 6 | outras supressões | | |
| 7 | grupo de controlo | | |
| | **a contactar** | | |

## 5. Grupo de controlo

{Como foi separado (ao acaso, antes do primeiro envio), quantos, o que recebem (só serviço), ou porque não há controlo e o que isso significa para a leitura.}

## 6. Cadência

| # | Dia | Canal | Público | Base | Supressão | Frequência | Horário | Mensagem | Pára se |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | email | todos com base para email | ✓ | ✓ | ✓ | ✓ | T1 | resposta, venda, oposição, reclamação |
| | | | | | | | | | |

## 7. Mensagens finais

{Texto final de cada contacto, adaptado de mensagens.md, com o rodapé ou a linha de oposição.}

## 8. Guião de avaliação

{Adaptado ao stand: o que o cliente traz, o que se pergunta, o que se vê, como se apresenta a proposta, validade da proposta.}

## 9. Tratamento de respostas

| Resposta | O que fazer | Quem | Prazo | Registo no sistema |
|---|---|---|---|---|
| Sim, quero avaliar | | | | |
| Não | | | | |
| Mais tarde | | | | |
| Já vendi ou não tenho a viatura | | | | |
| Quanto me dão? | | | | |
| Como têm os meus dados? | | | | |
| Não me contactem | | | | |
| Reclamação | | | | |

## 10. Métricas e regras de decisão

| Passo do funil | Número | Nota |
|---|---|---|
| Elegíveis | | |
| Após supressões | | |
| Contactados, por canal | | |
| Entregues | | |
| Respostas | | |
| Avaliações marcadas | | |
| Avaliações feitas | | |
| Propostas | | |
| Retomas concretizadas | | |
| Vendas associadas | | |
| Margem (retoma e venda) | | |
| Oposições, reclamações, desistências | | |

Regras escritas antes do arranque, com os números do gestor:

- **Expandir se:** {…}
- **Corrigir se:** {…}
- **Parar se:** {…}; e sempre perante queixa à CNPD, erro de dados ou mudança da oferta.

## 11. Lista de controlo de consentimento e oposição

| Item | Email | SMS | WhatsApp | Telefone | Prova ou nota |
|---|---|---|---|---|---|
| Base identificada por cliente | | | | | |
| Prova de consentimento ou decisão sobre a excepção de cliente | | | | | |
| Oposição em cada mensagem e testada | | | | | |
| Lista de supressão única aplicada | | | | | |
| Prazo interno de oposição testado | | | | | |
| Informação aos titulares cobre a segmentação | | | | | |
| Sem categorias especiais nem vulnerabilidade | | | | | |
| Empresas à parte | | | | | |
| Listas de oposição externas verificadas | | | | | |
| Subcontratantes com contrato | | | | | |
| Mensagens de serviço sem a campanha | | | | | |

Estado por célula: `sim`, `não` ou `N/V`.

## 12. Autorização e registo

| Acção | Autorizado por | Data |
|---|---|---|
| Carregar a audiência na plataforma | | |
| Enviar o contacto 1 | | |
| Enviar os contactos seguintes | | |

## 13. A confirmar

| Item | Porquê | Quem confirma |
|---|---|---|
