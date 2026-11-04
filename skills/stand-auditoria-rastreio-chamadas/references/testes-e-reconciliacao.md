# Testes controlados e reconciliação de chamadas

Lê antes de fazer chamadas de teste e antes de comparar números da plataforma com o CRM e o Ads.

## Preparação

1. **Autorização escrita** do gestor: janela horária, números a testar, quem atende.
2. **Telefone de teste** do stand (um cartão da empresa, nunca o de um cliente). Se for o telemóvel pessoal de alguém da equipa, mascara-o no relatório.
3. **Equipa avisada.** Quem atende diz "teste de auditoria" e não cria lead, ou cria-o marcado como teste para sair da reconciliação.
4. **Sem cliques em anúncios pagos.** Simula a origem paga com parâmetros no URL. O `gclid=TESTE_AUDITORIA` serve só para ver se o identificador chega à plataforma e ao CRM; não é importado.
5. **Gravação.** Se está activa, a chamada de teste também fica gravada: é a tua voz, não a de um cliente. Ouve e regista o aviso. Pede que as gravações de teste sejam apagadas no fim.
6. **Hora ao minuto** em cada teste, para encontrar a chamada na plataforma.

## Matriz mínima

| ID | Teste | Como | O que confirma |
|---|---|---|---|
| T01 | Directo | Janela anónima, URL sem parâmetros, telemóvel, botão de chamada | Número de "directo", chamada registada, lead no CRM |
| T02 | Pago simulado | `?utm_source=google&utm_medium=cpc&utm_campaign=teste_auditoria`; repete com `&gclid=TESTE_AUDITORIA` | Número de "Google pago", `utm_*` e `gclid` gravados |
| T03 | Orgânico | Pesquisa o nome do stand no Google e clica no resultado orgânico | Número de "orgânico" |
| T04 | Perfil Google | Clica no site a partir do Perfil (o link deve ter UTM) | Origem "Perfil Google" separada do orgânico |
| T05 | Redes ou email | `?utm_source=instagram&utm_medium=social` ou link de uma newsletter | Origem certa |
| T06 | Persistência | No computador, entra por T02, navega três páginas, lê o número e marca-o no telemóvel | O número não mudou e a chamada fica atribuída à origem da visita |
| T07 | Regresso | Volta ao site na mesma sessão e, noutro dia, liga para o número guardado | Comportamento da reserva e de chamadas tardias |
| T08 | Ficha de viatura | Numa ficha, compara número do cabeçalho, da ficha e do botão fixo, texto e `tel:` | Coerência e destino vendas |
| T09 | Departamentos | Liga para os números de oficina e peças | Destino certo, sem passar por vendas |
| T10 | Fora de horas | Liga depois do fecho ou num feriado | Mensagem, alternativa, correio de voz, chamada registada como perdida |
| T11 | Perdida em horário | Deixa tocar até desligar sem atendimento | Aparece como perdida; devolução feita e registada no CRM |
| T12 | Repetida | Segunda chamada do mesmo telefone, no mesmo dia | O CRM junta ao lead existente segundo a regra |
| T13 | WhatsApp | Clica em cada `wa.me` (cabeçalho, ficha, botão fixo, contactos) | Abre o número certo, com mensagem pré-preenchida, nunca um número de rastreio |
| T14 | Estáticos | Liga para o número de cada portal, da fachada ou dos impressos | Atribuição ao canal certo |

Corre só os testes que se aplicam e marca os outros `N/A` com razão.

## Registo de cada teste

| ID | Data e hora | Origem simulada | Dispositivo | Número mostrado | Número no `tel:` | Número esperado | Atendida | Destino | Duração | Aviso ouvido | Origem na plataforma | Evento GA4 | Conversão Ads | Lead no CRM e origem | Resultado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

`Resultado`: `OK`, `falha` (diz qual) ou `N/V` (diz porquê). Conversões no Ads e eventos no GA4 podem demorar a aparecer: volta a verificar no dia seguinte antes de marcar falha.

## Funil de chamadas

| Etapa | Definição | Fonte |
|---|---|---|
| Cliques em telefone | `clique_telefone` no GA4 | GA4 (intenção, não comparável um a um) |
| Registadas | Todas as chamadas recebidas nos números rastreados | Plataforma |
| Únicas | Registadas sem repetições do mesmo número dentro do prazo que o stand decide | Plataforma |
| Atendidas | Únicas atendidas por uma pessoa | Plataforma |
| Perdidas | Únicas não atendidas; separa com devolução e sem devolução | Plataforma e CRM |
| Qualificadas | Atendidas, com a duração mínima decidida, categoria de vendas e não repetidas | Plataforma ou `stand-classificar-chamadas` |
| Leads no CRM | Leads de vendas com origem telefone no período | CRM |
| Oportunidades | Definição do stand | CRM |
| Vendas | Definição do stand | CRM ou DMS |
| Conversões de chamada no Ads | Acção ou acções de chamada, por hora da conversão | Google Ads |

Relações que a lógica impõe (não são médias do sector):

- registadas ≥ únicas = atendidas + perdidas;
- qualificadas ≤ atendidas;
- leads no CRM muito acima das qualificadas: há chamadas para números não rastreados ou registos manuais; muito abaixo: a integração falha ou a equipa não regista;
- conversões no Ads acima das qualificadas de origem paga: o Ads conta chamadas que não são de vendas ou conta repetições.

Regras:

- Mesmo período e mesmo fuso em todas as fontes (ver [contexto-portugal.md](contexto-portugal.md)).
- Chamadas de teste e chamadas internas (da equipa para os números de rastreio) excluídas e contadas à parte.
- Spam, chamadas automáticas e fornecedores contados à parte, nunca em vendas.
- Percentagens só com o denominador escrito; com contagens pequenas, só absolutos.

## Tabela por número

| Número (rótulo, não o número completo se for pessoal) | Origem | Registadas | Atendidas | Perdidas | Perdidas sem devolução | Qualificadas | Leads no CRM | Vendas |
|---|---|---|---|---|---|---|---|---|

## Exemplo resolvido: Stand Exemplo, Leiria (fictício)

Números fictícios. Período: 1 a 31 de Outubro de 2026, `Europe/Lisbon`. Duas chamadas de teste e cinco internas excluídas antes de contar.

| Etapa | Contagem | Nota |
|---|---|---|
| Registadas | 212 | |
| Únicas | 181 | 31 repetições no mesmo dia |
| Atendidas | 139 | |
| Perdidas | 42 | 25 devolvidas, **17 sem devolução** |
| Qualificadas | 58 | Atendidas, duração mínima decidida pelo gestor, categoria vendas, não repetidas |
| Leads no CRM com origem telefone | 44 | 14 a menos que as qualificadas |
| Oportunidades | 21 | |
| Vendas | 6 | Coorte extraída a 15 de Novembro |
| Conversões de chamada no Ads | 37 | Contra 19 qualificadas de origem paga |

Diferenças explicadas:

| Diferença | Quantidade | Causa | Prova | Correcção | Área |
|---|---|---|---|---|---|
| Qualificadas sem lead | 9 | Reencaminhadas para o telemóvel de um vendedor, que não regista no CRM | Destino das chamadas na plataforma | Registo automático ou passo manual obrigatório | 8.1 |
| Qualificadas sem lead | 5 | Por explicar | | Rever com a equipa | |
| Ads contra qualificadas pagas | 11 | O Ads conta chamadas de oficina e peças acima de 30 segundos | Categoria das 37 chamadas | Importar só chamadas qualificadas | 7.2 |
| Ads contra qualificadas pagas | 4 | Spam e fornecedores acima da duração mínima | Idem | Idem | 7.2 |
| Ads contra qualificadas pagas | 3 | Repetições do mesmo número | Idem | Contagem "Uma" | 7.3 |

Leitura para o gestor: "Em Outubro entraram 181 chamadas diferentes. 42 não foram atendidas e 17 dessas nunca tiveram resposta. O Google Ads diz 37 chamadas de anúncios, mas só 19 eram de vendas. Antes de mexer no orçamento, a correcção com mais efeito é uma regra de devolução das chamadas perdidas, com responsável e prazo decididos por si."
