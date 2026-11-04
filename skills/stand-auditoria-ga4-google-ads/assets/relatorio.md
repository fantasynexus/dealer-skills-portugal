# Auditoria de GA4 e Google Ads: [nome do stand]

- **Data da auditoria:** [AAAA-MM-DD]
- **Site:** [domínio principal e outros domínios envolvidos]
- **Modo:** [com acesso / público / documental]
- **Contas vistas:** GA4 [G-…], GTM [GTM-…], Google Ads [ID], CRM [nome do sistema]
- **Período reconciliado:** [AAAA-MM-DD a AAAA-MM-DD], fuso [Europe/Lisbon]; [por período / por coorte, extraída a AAAA-MM-DD]
- **Nota:** [NN]/100 sobre [PP] pontos verificados (cobertura [PP] %)

## Em três frases

1. [As plataformas contaram X leads do site; o CRM recebeu Y e Z eram válidos.]
2. [A maior parte da diferença vem de …]
3. [A correcção que mais reduz a diferença é …, a fazer por …]

## Reconciliação

Definições aprovadas por [quem], em [data]:

- Lead válido: [definição]
- Oportunidade: [definição]
- Venda: [definição]

### Por etapa

| # | Etapa | Fonte e relatório | Contagem | Compara com | Diferença abs. | Diferença % (sobre N) | Explicado | Por explicar |
|---|---|---|---|---|---|---|---|---|
| A | Leads de vendas no GA4 | | | C | | | | |
| B | Conversões de lead no Ads | | | C pago | | | | |
| C | Leads brutos do site | | | | | | | |
| C pago | Leads brutos do site vindos de anúncios | | | | | | | |
| D | Leads válidos do site | | | C | | | | |
| E | Oportunidades | | | D | | | | |
| F | Vendas | | | E | | | | |

### Por canal

| Canal | Interacções GA4 | Conversões Ads | Leads brutos | Leads válidos | Oportunidades | Vendas |
|---|---|---|---|---|---|---|
| Formulário do site | | | | | | |
| Telefone a partir do site | | | | | | |
| WhatsApp a partir do site | | | | | | |
| [Portal] | fora do alcance | fora do alcance | | | | |
| Formulário de leads do Google | fora do alcance | | | | | |
| Telefone e WhatsApp directos | fora do alcance | fora do alcance | | | | |
| Presencial e outros | fora do alcance | fora do alcance | | | | |
| **Total** | | | | | | |

### Diferenças explicadas

| Diferença | Quantidade | Causa | Prova | Correcção | Área |
|---|---|---|---|---|---|

Leads de teste excluídos: [N]. Diferenças por explicar: [N], com a hipótese mais provável e o que falta para a provar.

## Falhas críticas

| Falha | Onde | Prova | Acção imediata |
|---|---|---|---|

[Se não houver: "Nenhuma falha crítica encontrada nas páginas e contas verificadas."]

## Nota por área

| Área | Máx. | Verificado | Obtido | Principal falha |
|---|---|---|---|---|
| 1. Propriedade, fluxos, filtros e retenção | 8 | | | |
| 2. Taxonomia de eventos e parâmetros | 12 | | | |
| 3. Eventos-chave sem duplicação | 10 | | | |
| 4. Conversões no Ads | 10 | | | |
| 5. Ligação GA4 e Ads, etiquetagem automática | 8 | | | |
| 6. Formulários, chamadas, WhatsApp, domínios externos | 12 | | | |
| 7. GTM | 8 | | | |
| 8. Consentimento | 12 | | | |
| 9. Importação offline do CRM | 12 | | | |
| 10. Reconciliação e monitorização | 8 | | | |
| **Total** | **100** | | | |

## Mapa do fluxo

```text
[canal] → [página] → [acção] → [evento GA4] → [conversão Ads] → [CRM: campo de origem] → [etapas] → [venda]
```

Uma linha por canal, com cada ligação marcada como `OK`, `falha` ou `N/V`.

## Inventários

### Etiquetas no site

| Etiqueta | ID | Carregada por | Páginas | Respeita consentimento |
|---|---|---|---|---|

### Eventos GA4 (últimos 30 dias)

| Evento | Contagem | Evento-chave | Parâmetros | Fonte do disparo | Problema |
|---|---|---|---|---|---|

### Acções de conversão no Ads

| Acção | Origem | Primária ou secundária | Contagem | Janela | Atribuição | Problema |
|---|---|---|---|---|---|---|

### Formulários e contactos

| Formulário ou botão | Página | Evento | Chega ao CRM | Identificadores passados | Problema |
|---|---|---|---|---|---|

## Plano de correcção

| Prioridade | Falha | Onde mudar (caminho) | Quem | Risco | Como reverter | Teste de aceitação |
|---|---|---|---|---|---|---|

Nada foi alterado nas contas durante a auditoria. Cada correcção precisa de autorização de [quem].

## Não verificado e por confirmar

- **N/V:** [critério, motivo, o que é preciso para verificar]
- **Por confirmar com o EPD ou jurista:** [consentimento, conversões optimizadas, importação com dados cifrados]
- **Por confirmar na documentação da Google:** [nome de colunas, limites, janelas de importação]
