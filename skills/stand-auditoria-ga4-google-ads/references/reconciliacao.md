# Reconciliação por etapa

Lê antes de comparar números. A reconciliação é o que o gestor percebe e usa: "o Google diz X, o CRM confirma Y, a diferença explica-se assim".

## Definições

Propõe estas definições e pede aprovação ao gestor antes de contar. Se o stand já tem outras, usa as dele e escreve-as no relatório.

| Etapa | Definição proposta | Fonte |
|---|---|---|
| Interacção técnica | Evento enviado pelo browser (`generate_lead`, `clique_telefone`, `clique_whatsapp`) | GA4 |
| Conversão no Ads | Conversão que o Ads atribui a uma interacção com anúncio | Google Ads |
| Lead bruto | Registo criado no CRM, de qualquer canal | CRM |
| Lead válido | Lead bruto sem testes, duplicados, spam e pedidos que não são de vendas (oficina, fornecedores, candidaturas) | CRM |
| Oportunidade | Lead válido com próximo passo concreto: visita, test drive, proposta enviada ou avaliação de retoma | CRM |
| Venda | Contrato assinado ou factura emitida (diz qual); reservas e sinais contam à parte | CRM ou DMS |

Duplicado: a mesma pessoa com o mesmo interesse dentro de um prazo que o stand decide (por exemplo, 30 dias). Uma pessoa que pede proposta no site e depois escreve no WhatsApp sobre a mesma viatura é um lead, não dois.

**Período ou coorte.** Decide e escreve qual usas:

- **por período:** conta o que aconteceu em cada etapa dentro das datas (os leads de Outubro e as vendas de Outubro, mesmo que essas vendas venham de leads de Setembro);
- **por coorte:** pega nos leads criados no período e mostra em que etapa estão na data de extracção. É o modo certo para medir a qualidade de um canal; indica a data de extracção.

## Regras de comparação

1. **Mesmo período e mesmo fuso.** `Europe/Lisbon` no continente e na Madeira, `Atlantic/Azores` nos Açores. O GA4 e a conta do Ads têm cada um o seu fuso nas definições; confirma os dois e o do CRM.
2. **Data do clique ou data da conversão.** Por omissão, o Google Ads atribui as conversões à data da interacção com o anúncio; o GA4 e o CRM contam pela data do evento. Para comparar com o CRM usa as colunas do Ads por hora da conversão (confirma o nome actual da coluna).
3. **Não esperes igualdade.** O GA4 pode aplicar limites de dados em relatórios e o Ads pode incluir conversões modeladas para visitas sem consentimento. Diferenças pequenas e explicáveis são normais; o objectivo é explicar, não igualar.
4. **Importações atrasadas.** Fecha um período só depois de a importação offline desse período estar feita.
5. **Percentagens com denominador.** Escreve sempre "(sobre N)". Com definições ou períodos diferentes não há percentagem. Com contagens pequenas (por exemplo, abaixo de 20), mostra só absolutos.
6. **Intenção não é contacto.** Cliques em telefone ou WhatsApp não se comparam um a um com chamadas ou conversas; escreve "não comparável".
7. **Testes fora.** Exclui leads de teste (da auditoria e de outros testes) e diz quantos foram.
8. **Canais fora do alcance.** Leads de portais, do formulário de leads do Google ou presenciais não passam pelo site; nessas células o GA4 fica "fora do alcance", não zero.

## Tabela 1: por etapa

| # | Etapa | Definição | Fonte e relatório | Contagem | Compara com | Diferença abs. | Diferença % (sobre N) | Explicado | Por explicar |
|---|---|---|---|---|---|---|---|---|---|
| A | Leads de vendas no GA4 | `generate_lead` | GA4 > Reports > Engagement > Events | | C | | | | |
| B | Conversões de lead no Ads | Acção primária de lead do site, por hora da conversão | Ads > Goals > Conversions | | C pago | | | | |
| C | Leads brutos do site | Origem do canal `site_formulario` | Exportação do CRM | | | | | | |
| C pago | Leads brutos do site vindos de anúncios | C com origem técnica `google / cpc` ou `gclid` | Exportação do CRM | | | | | | |
| D | Leads válidos do site | Definição aprovada | CRM | | C | | | | |
| E | Oportunidades do site | Definição aprovada | CRM | | D | | | | |
| F | Vendas do site | Definição aprovada | CRM ou DMS | | E | | | | |

A diferença entre A e C mede a medição do site. A diferença entre B e C pago mede a medição do Ads. De C para F é funil comercial: reporta-se, mas não é falha de medição.

## Tabela 2: por canal e etapa

| Canal | Interacções GA4 | Conversões Ads | Leads brutos | Leads válidos | Oportunidades | Vendas |
|---|---|---|---|---|---|---|
| Formulário do site | | | | | | |
| Telefone a partir do site | cliques (não comparável) | | | | | |
| WhatsApp a partir do site | cliques (não comparável) | | | | | |
| Standvirtual | fora do alcance | fora do alcance | | | | |
| OLX | fora do alcance | fora do alcance | | | | |
| Outros portais | fora do alcance | fora do alcance | | | | |
| Formulário de leads do Google | fora do alcance | | | | | |
| Telefone e WhatsApp directos | fora do alcance | fora do alcance | | | | |
| Presencial e outros | fora do alcance | fora do alcance | | | | |
| **Total** | | | | | | |

## Tabela 3: diferenças explicadas

| Diferença | Quantidade | Causa | Prova | Correcção | Área da grelha |
|---|---|---|---|---|---|

## Causas a procurar

Estas são hipóteses a provar, não diagnósticos. Cada uma só entra na Tabela 3 com prova.

**GA4 conta mais do que o CRM recebe (A maior que C):**

- evento duplicado num formulário (prova: teste no DebugView e eventos desse `formulario_id` contra leads desse formulário);
- evento disparado no clique, mesmo com erro de validação;
- formulário que envia email ao vendedor e nunca cria registo no CRM (prova: emails do período na caixa do stand);
- leads de teste ou de spam que o CRM rejeita e o GA4 conta.

**CRM recebe mais do que o GA4 conta (C maior que A):**

- formulários sem medição, sobretudo os embebidos de fornecedores;
- visitas que recusaram cookies (o GA4 não as vê ou só as modela);
- bloqueadores de publicidade no browser;
- leads de WhatsApp, telefone ou portais registados por engano como `site_formulario`.

**Ads diferente do CRM pago (B contra C pago):**

- a mesma acção primária via tag do Ads e via importação do GA4;
- contagem "Every" num lead;
- comparação pela data do clique em vez da data da conversão;
- `gclid` perdido num redireccionamento, por isso o CRM não sabe que o lead veio do Ads;
- conversões modeladas (assinala como possível causa; raramente se prova lead a lead).

**De lead bruto a lead válido (C para D):** testes, duplicados entre canais, spam, pedidos de oficina feitos no formulário de vendas.

## Exemplo resolvido: Stand Exemplo, Leiria (fictício)

Números fictícios. Período: 1 a 31 de Outubro de 2026, `Europe/Lisbon` nas três fontes. Coorte extraída do CRM a 15 de Novembro.

| # | Etapa | Contagem | Compara com | Diferença | Explicado | Por explicar |
|---|---|---|---|---|---|---|
| A | `generate_lead` no GA4 | 64 | C | +12 (+23 % sobre 52) | 12 | 0 |
| B | Conversões de lead no Ads | 24 | C pago | +3 (sobre 21; amostra pequena, só absolutos) | 2 | 1 |
| C | Leads brutos do site | 52 | | | | |
| C pago | Leads brutos do site com `gclid` | 21 | | | | |
| D | Leads válidos do site | 38 | C | −14 | 14 | 0 |
| E | Oportunidades | 17 | D | funil | | |
| F | Vendas (contrato assinado) | 4 | E | funil | | |

Diferenças explicadas:

| Diferença | Quantidade | Causa | Prova | Correcção | Área |
|---|---|---|---|---|---|
| A contra C | 9 | O formulário de financiamento envia `generate_lead` duas vezes | Teste no DebugView: dois eventos por envio; 18 eventos desse formulário contra 9 leads | Remover a tag duplicada no GTM | 3.2 |
| A contra C | 3 | O formulário de contacto geral envia só email | 3 emails do formulário na caixa do stand sem lead no CRM | Ligar o formulário ao CRM | 6.1 |
| B contra C pago | 2 | Os eventos duplicados acima vindos de sessões pagas, importados como primária | 4 eventos do formulário de financiamento com origem `google / cpc` contra 2 leads | A mesma correcção da 3.2 | 3.2 |
| B contra C pago | 1 | Por explicar; possível conversão modelada | Nenhuma | Rever depois da correcção | |
| C contra D | 14 | 3 testes, 5 duplicados entre formulário e WhatsApp, 2 spam, 4 pedidos de oficina | Exportação do CRM com motivo de exclusão | Separar o formulário de oficina (`pedido_oficina`) | 2.1 |

Leitura para o gestor: "Em Outubro o GA4 contou 64 leads do site e o CRM recebeu 52; 38 eram válidos. A diferença vem de um formulário que conta a dobrar e de outro que nunca chega ao CRM. No mesmo mês, o Standvirtual trouxe leads que o Google não vê: compare-os na tabela por canal antes de mudar orçamento."
