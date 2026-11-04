# Programa de 90 dias: {stand}

> Preparado em {data}. Variante: {usado | novo | ambos}, {oficina própria | parceira | rede da marca | sem oficina}, {entrega presencial | à distância | ambas}.
> Os itens marcados `confirmar` estão reunidos na secção 9 e não entram em mensagens a clientes antes de confirmados.

## 1. Resumo

| Campo | Valor |
|---|---|
| Entregas por mês | {n} |
| Responsáveis | vendas: {função}; registo: {função}; pós-venda: {função}; gerência: {função} |
| Sistema onde corre | {CRM, DMS, folha, agenda} |
| Canais com consentimento registado | {email, SMS, WhatsApp, telefone}, ou "nenhum registo: só pontos de serviço" |
| Pontos no programa | {n} ({n} ★) |
| Medida principal | {por exemplo, entregas com checklist completa e pós-venda apresentada} |
| Passa a seguir para | `stand-fluxos-email` no dia 91 |

## 2. Checklist do dia 0

| Item | Estado | Quem trata | Notas |
|---|---|---|---|
| Contrato de compra e venda | {obrigatório / recomendado / N/A / confirmar} | | |
| Factura | | | |
| Requerimento de registo ou comprovativo do pedido | | | |
| DUA ou certificado de matrícula | | | |
| Declaração de circulação | | | |
| Termo de responsabilidade com dia e hora | | | |
| Declaração de características | | | |
| Ficha da última inspecção | | | |
| Livro de revisões e histórico | | | |
| Documento da garantia e contacto | | | |
| Contrato de crédito (se houve) | | | |
| Chaves, manuais, equipamento | | | |
| Seguro activo confirmado | | | |
| Consentimentos recolhidos em separado | | | |
| Pós-venda apresentada | | | |
| Cartão de entrega com contactos e QR | | | |

## 3. Pontos de contacto

| # | Quando | Canal | Natureza | Responsável | Gatilho | Dados usados | Supressão | Resultado esperado | Texto |
|---|---|---|---|---|---|---|---|---|---|
| | | | {S / M / M?} | | | | | | |

## 4. Passagem vendedor → pós-venda

- **Pessoa de pós-venda ou oficina:** {função e nome}
- **Como o cliente a conhece no dia 0:** {presencial no fim da entrega | mensagem M3 se não estiver}
- **O que o vendedor passa:** viatura, data de entrega, pendentes combinados, canal preferido, consentimentos. Nada mais.
- **Quando:** {até ao fim do dia da entrega}
- **Onde fica registado:** {campo ou nota no sistema}

## 5. Mensagens

Cola aqui as mensagens adaptadas, com o código do ponto (M1, M2, ...) e a natureza. Cada mensagem de marketing termina com a forma de oposição.

## 6. Excepções

| Situação | Sinal | Quem decide | Prazo de resposta (fixado pelo stand) | Mensagem | Volta ao programa quando |
|---|---|---|---|---|---|
| Atraso no registo | | | | M7 | |
| Avaria ou falta de conformidade | | | | M15 | |
| Insatisfação sem avaria | | | | contacto pessoal | |
| Cliente não responde | | | | | |
| Livre resolução ou devolução | | | | | |
| "Não me contactem" | | | | confirmação por escrito | |

## 7. Campos e automações

| Campo ou evento | Existe hoje? | Onde | Quem preenche | Usado em | Automação |
|---|---|---|---|---|---|
| | {sim / não / N/V} | | | | {manual / automática / a criar} |

## 8. Métricas

| Métrica | Definição | Fonte | Frequência | Meta |
|---|---|---|---|---|
| | | | | fixada pelo stand depois de {n} semanas de dados |

## 9. A confirmar

| Item | Porquê | Quem confirma | Até quando |
|---|---|---|---|
| | | {gestor, contabilista, DPO, jurista, financeira, IRN} | |

## 10. Depois do dia 90

- Lembretes de manutenção, aniversário de compra e recomendação: `stand-fluxos-email`.
- Renovação da viatura, mais tarde: `stand-campanha-retoma`.
- Padrões nas avaliações recebidas: `stand-analisar-avaliacoes`.
