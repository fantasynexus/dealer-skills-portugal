# Fluxos de email: {stand}

> Preparado em {data}. Modo: {A. programa | B. fluxo específico | C. revisão}. Plataforma: {nome ou "a escolher"}.
> Nada é activado, importado ou enviado sem autorização explícita do gestor.

## 1. Mapa de automação

| # | Fluxo | Natureza | Gatilho | Cadência | Saída | Prioridade | Estado |
|---|---|---|---|---|---|---|---|
| | | {transaccional / pré-contratual / serviço / marketing} | | | | | {novo / manter / corrigir / fora} |

Fluxos que ficaram de fora e porquê:

| Fluxo | Motivo (evento não fiável, sem consentimento, sem capacidade...) | O que falta para entrar |
|---|---|---|

## 2. Eventos e dados

| Evento | Fonte | Fiável | Quem regista | Usado nos fluxos |
|---|---|---|---|---|
| | | {sim / não / N/V} | | |

## 3. Especificação por fluxo

Repete este bloco por fluxo.

### Fluxo {n}: {nome}

| Campo | Valor |
|---|---|
| Objectivo | |
| Natureza e base | {base proposta}, a confirmar com o DPO |
| Público | {descrição sem dados pessoais} |
| Gatilho | |
| Condições de entrada | |
| Exclusões | |
| Cadência | |
| Condição de saída | |
| Responsável | {função} |
| Campos necessários | {campo: existe / não existe; variante sem ele} |
| Eventos de medição | |
| Remetente | {nome da pessoa}, {stand} |
| Ligação a outras skills | |

#### Email {n}.{k}: {dia}

- **Assunto A:**
- **Assunto B:**
- **Preheader:**
- **Corpo:**
- **CTA (um só):**
- **Contactos:**
- **Rodapé:** {serviço | marketing com oposição}
- **Texto simples:** {sim}
- **Variante sem campos opcionais:** {sim / não se aplica}

## 4. Regras globais

| Regra | Valor escolhido pelo stand |
|---|---|
| Limite de marketing por pessoa | {por exemplo, 1 email por semana} |
| Prioridade entre fluxos | segurança, transaccional, documentação, pré-contratual, serviço, marketing |
| Exclusões mútuas | |
| Supressões comuns | |
| Horário de envio | |
| Prazo interno para aplicar oposições | |

## 5. Plano de testes

- [ ] Cada fluxo testado com endereços de teste, com todos os campos e sem os opcionais.
- [ ] Nenhum campo vazio aparece no texto.
- [ ] Todas as ligações abrem a página certa, com UTM.
- [ ] A oposição funciona e chega ao CRM, à plataforma de email e às de SMS e WhatsApp.
- [ ] Um contacto que se opôs continua a receber os transaccionais e deixa de receber marketing.
- [ ] Leitura em telemóvel e em texto simples.
- [ ] Domínio com SPF, DKIM e DMARC; cancelamento com um clique nos emails de marketing.
- [ ] Respostas chegam a uma caixa que alguém lê.
- [ ] Os limites de frequência e as exclusões mútuas funcionam num cliente de teste que entra em dois fluxos ao mesmo tempo.

## 6. Métricas

| Fluxo | Medida principal | Definição | Fonte | Até onde chega |
|---|---|---|---|---|
| | | | | {lead / visita / venda / oficina} |

Medidas de saúde do programa: devoluções, queixas de spam, oposições por fluxo e por email. As metas fixa-as o stand depois de medir.

## 7. Lista de controlo de consentimento e oposição

| Item | Estado | Prova ou nota |
|---|---|---|
| Natureza e base registadas por fluxo | {sim / não / N/V} | |
| Consentimento ou excepção de cliente para cada fluxo de marketing | | |
| Consentimento livre, específico, por canal, com caixa não pré-seleccionada | | |
| Prova de consentimento (data, origem, texto, quem) | | |
| Contactos de portais usados só para o pedido, salvo consentimento | | |
| Empresas separadas e regime confirmado | | |
| Listas de oposição externas: aplicam-se? | | |
| Oposição simples e gratuita em cada email de marketing | | |
| Lista de supressão única para todas as plataformas | | |
| Retirada tão fácil como dar | | |
| Transaccionais mantidos após oposição ao marketing | | |
| Informação aos titulares cobre fluxos e perfilagem | | |
| Sem categorias especiais nem inferência de vulnerabilidade | | |
| Contratos com subcontratantes; transferências fora do EEE | | |
| Prazo de conservação definido | | |
| Registo de envios e oposições | | |

## 8. Revisão pelo DPO ou por um jurista

| Fluxo | Motivo | Quem revê | Estado |
|---|---|---|---|

## 9. A confirmar

| Item | Porquê | Quem confirma |
|---|---|---|
