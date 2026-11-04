# Auditoria de rastreio de chamadas: [nome do stand]

- **Data da auditoria:** [AAAA-MM-DD]
- **Site:** [domínio]
- **Modo:** [com acesso / público / sem rastreio]
- **Fornecedor de rastreio:** [nome ou "nenhum"]
- **Contas vistas:** plataforma [sim/não], GA4 [G-…], Google Ads [ID], CRM [nome do sistema]
- **Período reconciliado:** [AAAA-MM-DD a AAAA-MM-DD], fuso [Europe/Lisbon]
- **Nota:** [NN]/100 sobre [PP] pontos verificados de [AA] aplicáveis (cobertura [PP] %)

## Em três frases

1. [Entraram X chamadas diferentes; Y foram atendidas; Z ficaram sem resposta.]
2. [A atribuição perde-se em …]
3. [A correcção que recupera mais contactos é …]

## Falhas críticas

| Falha | Onde | Prova (teste ou captura) | Acção imediata |
|---|---|---|---|

[Se não houver: "Nenhuma falha crítica encontrada nos números e testes verificados."]

## Mapa

```text
[origem] → [número mostrado] → [encaminhamento] → [plataforma] → [GA4 / Ads] → [CRM: origem]
WhatsApp: [clique_whatsapp] → [conversa no telemóvel ou na plataforma] → [registo no CRM]
```

Cada ligação marcada como `OK`, `falha` ou `N/V`.

## Inventário de números

| Número (rótulo; pessoais mascarados) | Gama | Onde aparece | Titular | Destino | Quem atende | Rastreado | Grava | Problema |
|---|---|---|---|---|---|---|---|---|

## Nota por área

| Área | Máx. | Aplicável | Verificado | Obtido | Principal falha |
|---|---|---|---|---|---|
| 1. Inventário e propriedade dos números | 8 | | | | |
| 2. Troca dinâmica e persistência | 12 | | | | |
| 3. Conjunto de números e colisões | 8 | | | | |
| 4. Origem, campanha e UTM | 10 | | | | |
| 5. Encaminhamento, IVR, horários, perdidas | 12 | | | | |
| 6. Classificação e revisão humana | 10 | | | | |
| 7. GA4 e Google Ads | 10 | | | | |
| 8. CRM | 12 | | | | |
| 9. Gravação, acesso, aviso, conservação | 10 | | | | |
| 10. Reconciliação e alertas | 8 | | | | |
| **Total** | **100** | | | | |

## Testes controlados

Autorizados por [quem] em [data]. Telefone de teste: [rótulo]. Leads de teste marcados como [etiqueta] e gravações de teste [apagadas / por apagar].

| ID | Data e hora | Origem simulada | Dispositivo | Número mostrado | `tel:` | Esperado | Atendida | Destino | Duração | Aviso ouvido | Origem na plataforma | GA4 | Ads | CRM | Resultado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Reconciliação

Definições aprovadas por [quem]: chamada única [regra]; qualificada [regra]; lead [regra]; venda [regra].

| Etapa | Fonte | Contagem | Nota |
|---|---|---|---|
| Cliques em telefone (não comparável) | GA4 | | |
| Registadas | Plataforma | | |
| Únicas | Plataforma | | |
| Atendidas | Plataforma | | |
| Perdidas (com devolução / sem devolução) | Plataforma e CRM | | |
| Qualificadas | Plataforma ou classificação | | |
| Leads no CRM com origem telefone | CRM | | |
| Oportunidades | CRM | | |
| Vendas | CRM ou DMS | | |
| Conversões de chamada no Ads | Google Ads | | |

Excluídas antes de contar: [N] chamadas de teste, [N] internas, [N] spam ou fornecedores.

### Por número

| Número (rótulo) | Origem | Registadas | Atendidas | Perdidas | Sem devolução | Qualificadas | Leads no CRM | Vendas |
|---|---|---|---|---|---|---|---|---|

### Diferenças explicadas

| Diferença | Quantidade | Causa | Prova | Correcção | Área |
|---|---|---|---|---|---|

## Correcções priorizadas

| Prioridade | Falha | O que mudar e onde | Quem | Risco | Como reverter | Teste de aceitação |
|---|---|---|---|---|---|---|

Nenhum número, encaminhamento ou definição foi alterado durante a auditoria. Mudanças no Perfil Google, nos portais ou no site precisam de autorização escrita de [quem].

## Por confirmar

- **Com o EPD ou jurista:** [finalidade e fundamento da gravação, texto do aviso, alternativa para quem recusa, prazo de conservação, informação aos colaboradores, transcrição ou análise por IA]
- **Com o fornecedor:** [titularidade e portabilidade, exclusão do WhatsApp, tempo de reserva, localização dos dados, contrato de subcontratação]
- **Com a Google:** [directrizes actuais para o telefone do Perfil, importação de chamadas]
- **N/V:** [critério, motivo, o que é preciso para verificar]
