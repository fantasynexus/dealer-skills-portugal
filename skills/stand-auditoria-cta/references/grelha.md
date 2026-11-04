# Grelha da auditoria de CTA

Cada página da amostra vale 100 pontos em sete dimensões. Cada verificação dá Total, Parcial ou 0. Marca `N/V` o que não conseguiste testar (sem autorização para enviar, sem acesso ao GA4) e N/A o que não se aplica, com a razão (ex.: a página de contactos não é longa, por isso 2.4 é N/A). Ambas saem do denominador.

Os limiares numéricos (número de botões no primeiro ecrã, palavras por botão) são critérios desta grelha, verificáveis e práticos, não normas. Apresenta-os assim.

## Como calcular

- **Nota da página** = pontos obtidos ÷ pontos verificados × 100.
- **Nota da amostra** = média das notas das páginas pontuadas.
- **Cobertura** = soma dos pontos verificados ÷ soma dos pontos aplicáveis, em toda a amostra.
- Cobertura abaixo de 70%: nota provisória.
- Telefone que não liga, WhatsApp para número errado ou formulário que não envia é um bloqueio: abre o relatório, seja qual for a nota.

Na listagem não há uma acção principal de página. Aplica 1.1, 2.1 e 5.1 aos cartões de viatura e aos filtros: cada cartão tem uma acção clara e os filtros vêem-se sem scroll.

## 1. Visibilidade e legibilidade (15)

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 1.1 | A acção principal vê-se sem scroll em telemóvel (360 × 740 px). Prova: captura do primeiro ecrã. | 6 | 3: só em computador, ou visível mas tapada em parte | abaixo da dobra em ambos |
| 1.2 | A principal distingue-se das secundárias e do texto (cor, tamanho, peso), com contraste de pelo menos 4,5:1. | 4 | 2: todos os botões com o mesmo estilo | confunde-se com o texto |
| 1.3 | No primeiro ecrã de telemóvel, uma principal e até três secundárias. | 3 | 1,5: quatro ou cinco a competir | seis ou mais |
| 1.4 | Em páginas longas (viatura, financiamento), barra fixa ou repetição que mantém a acção à mão sem tapar conteúdo. | 2 | 1: fixa mas tapa conteúdo, ou só no topo | nenhuma |

## 2. Hierarquia entre acção principal e secundárias (20)

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 2.1 | Há uma acção principal clara. | 8 | 4: duas a competir pelo mesmo destaque | três ou mais com o mesmo peso |
| 2.2 | As secundárias são visualmente subordinadas (contorno, tamanho menor) e servem a principal. | 4 | 2: competem em parte | sem distinção |
| 2.3 | O cabeçalho e a barra fixa não puxam para outra acção (ex.: "Marcar oficina" fixo no topo de uma página de viatura). | 4 | 2: diferentes mas compatíveis | em conflito |
| 2.4 | Em páginas longas, a principal reaparece depois das fotos e da ficha, ou está sempre na barra fixa. | 4 | 2: só no topo e no fim | só uma vez |

## 3. Telemóvel, toque, `tel:` e WhatsApp (20)

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 3.1 | Todos os telefones em `tel:+351...`; ao tocar, o telemóvel propõe ligar para o número certo. Prova: `contactos.telefones` do script e toque real ou emulado. | 6 | 3: alguns em texto simples | nenhum ligável |
| 3.2 | WhatsApp em `https://wa.me/351...` abre a conversa com o número do stand e, nas viaturas, com texto pré-preenchido que identifica o carro (marca, modelo, ano, referência ou URL). | 5 | 2,5: abre, mas sem texto ou sem a viatura | partido ou número errado; ou o stand diz atender WhatsApp e não há ligação |
| 3.3 | Áreas de toque confortáveis (orientação da Google: cerca de 48 px) e nunca abaixo de 24 × 24 px (WCAG 2.2, critério 2.5.8), com espaço entre elas. | 3 | 1,5: algumas pequenas ou coladas | muitas abaixo de 24 px |
| 3.4 | Formulário em telemóvel: `type="tel"` e `type="email"` (teclado certo), `autocomplete`, letra que não obriga a zoom, botão de envio alcançável. | 4 | 2: um ou dois problemas | inutilizável em telemóvel |
| 3.5 | Sem erros de telemóvel: chat ou banner por cima do botão, scroll horizontal, barra fixa a esconder campos. | 2: testado em iOS e Android reais, sem erros | 1: sem erros só em emulação, ou um erro menor | erro que impede o contacto |

## 4. Clareza e especificidade do texto (15)

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 4.1 | Verbo de acção específico nas principais. Sem "Saber mais", "Clique aqui", "Enviar", "Submeter", "Mais informações". | 5 | 2,5: misto | genérico em todo o site |
| 4.2 | O texto diz o que o cliente recebe ("Receber proposta para este Clio"), não o processo do stand ("Enviar pedido"). | 4 | 2: misto | só processo |
| 4.3 | Botões curtos: duas a seis palavras. | 2 | 1: alguns longos | botões a fazer de título |
| 4.4 | Junto à acção principal, a expectativa: quem responde, por que canal, em que horário. Só conta se for verdade (pergunta ao stand). | 2 | 1: genérica ("entraremos em contacto") | ausente |
| 4.5 | Sem urgência falsa nem pressão: contadores sem prazo real, "últimas horas" permanentes, "X pessoas a ver" sem dados. | 2 | 1: urgência real mas exagerada | urgência inventada |

## 5. Adequação à intenção da página (15)

Usa a tabela de [padroes-por-pagina.md](padroes-por-pagina.md).

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 5.1 | A acção principal é a esperada para o tipo de página e para o processo do stand. | 7 | 3,5: aceitável mas genérica ("Contactar" numa viatura) | errada (ex.: "Ver viaturas" como principal no fim de uma viatura) |
| 5.2 | As secundárias esperadas existem. | 4 | 2: falta uma | faltam várias |
| 5.3 | Nada essencial falta: na viatura, contacto sobre aquela viatura; na listagem, filtros; no financiamento, condições; na retoma, o que acontece a seguir. | 4 | 2: existe mas está escondido | falta |

## 6. Formulário, confiança, privacidade e conclusão (10)

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 6.1 | Só os campos necessários para o passo seguinte (mínimos em `padroes-por-pagina.md`). Prova: `formularios[].campos` do script. | 3 | 1,5: um ou dois a mais | formulário longo, ou NIF, data de nascimento ou rendimentos no primeiro contacto |
| 6.2 | Informação de privacidade junto ao formulário; consentimento de marketing separado, opcional e não pré-seleccionado. Prova: `formularios[].caixas_pre_seleccionadas`. | 3 | 1,5: falta a informação ou o consentimento é vago | caixa pré-seleccionada, consentimento agregado ou marketing obrigatório para enviar |
| 6.3 | Erros explicados em texto e sem apagar o que foi escrito; confirmação que diz o que acontece a seguir. A confirmação só se pontua com teste autorizado. | 2 | 1 | erros que apagam o formulário ou nenhuma confirmação |
| 6.4 | Confiança junto à acção: nome do stand, horário, quem responde. | 2 | 1: só parte | nada |

## 7. Medição e ligação ao CRM (5)

| # | Verificação e prova | Total | Parcial | 0 |
|---|---|---|---|---|
| 7.1 | Cliques em telefone e WhatsApp e envio de formulário geram eventos, sem duplicados. Prova: Tag Assistant, DebugView ou separador Rede. | 2 | 1: só alguns, ou duplicados | nenhum |
| 7.2 | O contacto chega ao CRM com a viatura (referência ou URL) e a origem. Só com teste autorizado. | 2 | 1: chega sem viatura ou sem origem | não chega |
| 7.3 | Chamadas atribuídas a uma origem (número de rastreio ou evento de clique). | 1 | 0,5: só o clique, sem ligação à chamada | nada |

Medição em detalhe: `stand-auditoria-ga4-google-ads` e `stand-auditoria-rastreio-chamadas`.

## Inventário: colunas obrigatórias

| Coluna | O que registar |
|---|---|
| # | Número do CTA na página |
| Texto | Texto exacto, entre aspas |
| Tipo | Botão, ligação, `tel:`, WhatsApp, formulário, chat |
| Destino | URL, número ou formulário de destino |
| Posição | Cabeçalho, topo, junto ao preço, após a ficha, barra fixa, rodapé |
| Prioridade | Principal, secundária, terciária |
| Primeiro ecrã em telemóvel | Sim ou não |
| Evento | Nome do evento, "nenhum" ou `N/V` |
| Dados pedidos | Campos, ou "nenhum" |
| Problemas | Referência às verificações falhadas (ex.: 3.2, 4.1) |

## Exemplo de leitura (Stand Exemplo, Leiria, fictício)

Página de viatura: três botões iguais no topo ("Contactar", "Financiamento", "Retoma"), telefone em texto simples, WhatsApp sem texto pré-preenchido. 2.1 dá 0 (três principais), 3.1 dá 0, 3.2 dá 2,5, 4.1 dá 2,5. O mesmo nas três viaturas da amostra: padrão do modelo de página, responsável provável o fornecedor do site. Texto proposto: principal "Pedir proposta para este carro", secundárias "Falar no WhatsApp" (com a viatura no texto) e "Ligar para o stand", terciárias "Simular prestação" e "Avaliar a minha retoma".
