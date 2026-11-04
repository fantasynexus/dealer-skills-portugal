# Mensagens da campanha de retoma

Textos de partida em PT-PT para adaptar ao segmento e à voz do stand. Tratam o cliente por "você" ou de forma impessoal, salvo indicação do stand. Todas são marketing: cada uma leva forma de oposição.

## Regras

- **Campos:** `{nome}`, `{viatura}` (marca e modelo do cliente), `{stand}`, `{vendedor}`, `{tel_vendedor}`, `{link_marcacao}`, `{link_oposicao}`, `{duracao_avaliacao}`, `{oferta}` (texto exacto), `{prazo_oferta}`, `{onde_estao_as_condicoes}`, `{modelo_procurado}`, `{mes_fim_contrato}`, `{tipo_contrato}`, `{entidade_contrato}`.
- **Campo em falta:** sem `{nome}`, "Olá,". Sem um campo de uma linha, a linha sai. Sem `{viatura}` fiável, não uses a campanha nesse cliente.
- **Oferta:** copiada do documento, com prazo e condições. Sem oferta escrita, as linhas de oferta saem.
- **Valores:** nenhuma mensagem leva estimativa de retoma, prestação ou taxa.
- **SMS:** acentos podem fazer a plataforma usar codificação Unicode e reduzir o limite de caracteres por mensagem. Confirma na plataforma.

## Sequência base

| # | Dia | Canal | Notas |
|---|---|---|---|
| T1 | 0 | email | abertura própria do segmento |
| T2 | 4 a 5 | SMS ou WhatsApp | só a quem não respondeu e tem base para o canal |
| T3 | 9 a 10 | telefone | só com base para telefone; uma pessoa liga; uma tentativa e um retorno |
| T4 | 14 a 21 | email | última mensagem da campanha |

Quem responde, compra, se opõe ou reclama sai da sequência no próprio dia.

**Rodapé dos emails:**

> {stand} · {morada} · {telefone}
> Recebe este email porque {é cliente do stand | aceitou receber novidades}. Se não quiser receber mais emails destes: {link_oposicao}.

## T1. Email de abertura, por segmento

### A. Fim de contrato

- **Assunto A:** O contrato do seu {viatura} termina em {mes_fim_contrato}
- **Assunto B:** Antes do fim do contrato do {viatura}
- **Preheader:** Se quiser, ajudamos a preparar a decisão com tempo.

> Olá {nome},
>
> Segundo os nossos registos, o contrato de {tipo_contrato} do seu {viatura} termina em {mes_fim_contrato}. Há quem prefira decidir com tempo o que fazer a seguir, por isso deixamos a porta aberta:
>
> - o que acontece à viatura no fim do contrato trata-se com {entidade_contrato}, segundo o que lá está escrito;
> - se estiver a pensar na próxima viatura, mostramos-lhe o que temos e fazemos as contas sem compromisso.
>
> Para marcar uma conversa: {link_marcacao} ou {tel_vendedor}.
>
> {vendedor}
> {stand}

### B. Valor de retoma provável

- **Assunto A:** Quanto vale hoje o seu {viatura}?
- **Assunto B:** Avaliação do seu {viatura}, sem compromisso
- **Preheader:** Com a viatura à frente, a proposta fica por escrito.

> Olá {nome},
>
> Se já pensou em trocar o seu {viatura}, podemos dizer-lhe quanto vale hoje para retoma. A avaliação é feita com a viatura à frente, demora cerca de {duracao_avaliacao} e não obriga a nada. No fim fica com uma proposta escrita, válida até à data que lá constar.
>
> {oferta}, até {prazo_oferta}. Condições: {onde_estao_as_condicoes}.
>
> Para marcar: {link_marcacao} ou {tel_vendedor}.
>
> {vendedor}
> {stand}

### C. Viatura procurada pelo stand

- **Assunto A:** Procuramos {modelo_procurado} para clientes nossos
- **Assunto B:** O seu {viatura} pode interessar a quem nos procura
- **Preheader:** Avaliação sem compromisso, com proposta por escrito.

> Olá {nome},
>
> Temos clientes à procura de {modelo_procurado} e o seu {viatura} corresponde ao que nos pediram. Por isso temos interesse em comprar viaturas como a sua.
>
> Se estiver a pensar trocar ou vender, avaliamos sem compromisso e fica com uma proposta escrita. Não lhe podemos garantir a venda a um cliente concreto; podemos garantir uma avaliação séria.
>
> Para marcar: {link_marcacao} ou {tel_vendedor}.
>
> {vendedor}
> {stand}

### D. Da oficina para as vendas

- **Assunto:** Sobre a troca do {viatura} de que nos falou
- **Preheader:** Se ainda fizer sentido, mostramos-lhe opções.

> Olá {nome},
>
> Quando esteve na nossa oficina em {mes_visita}, falou com {pessoa_oficina} sobre a possibilidade de trocar o {viatura}. Se ainda fizer sentido, {vendedor} pode mostrar-lhe opções e avaliar a sua viatura, sem compromisso.
>
> Se entretanto mudou de ideias, não há problema: diga-nos e não voltamos ao assunto.
>
> {vendedor}
> {stand}

### E. Campanha da marca

- **Assunto:** {nome_campanha}: saiba se se aplica ao seu {viatura}
- **Preheader:** Condições da {marca} até {prazo_campanha}.

> Olá {nome},
>
> A {marca} tem em curso a campanha {nome_campanha}, até {prazo_campanha}: {condicoes_copiadas}.
>
> Pelo que temos registado, a sua viatura pode ser elegível. A elegibilidade confirma-se com {verificacao}. Se quiser saber se se aplica ao seu caso: {link_marcacao} ou {tel_vendedor}.
>
> {vendedor}
> {stand}

### F. Cliente inactivo

- **Assunto:** Há algum tempo que não nos vemos
- **Preheader:** Uma pergunta rápida, e pode dizer-nos que não.

> Olá {nome},
>
> Há algum tempo que não nos vemos. Se ainda tem o {viatura}, ou se já mudou de viatura, gostávamos de saber. Se um dia quiser saber quanto vale para retoma, fazemos a avaliação sem compromisso.
>
> E se preferir não receber mais mensagens nossas, basta carregar no fim deste email. Respeitamos já.
>
> {vendedor}
> {stand}

## T2. SMS ou WhatsApp, por segmento

Só a quem não respondeu ao T1 e tem base para o canal. No WhatsApp, a última frase pode ser "Se preferir não receber estas mensagens, diga-nos."

- **A:** Olá {nome}, é o {vendedor}, do {stand}. O contrato do {viatura} termina em {mes_fim_contrato}. Se quiser preparar a decisão com tempo, ligue {tel_vendedor}. Para não receber mais, responda SAIR.
- **B:** Olá {nome}, é o {vendedor}, do {stand}. Se quiser saber quanto vale hoje o seu {viatura}, avaliamos sem compromisso. Responda SIM e ligo-lhe. Para não receber mais, responda SAIR.
- **C:** Olá {nome}, é o {vendedor}, do {stand}. Temos clientes à procura de {modelo_procurado}. Se pensar vender o seu {viatura}, avaliamos sem compromisso. Responda SIM. Para não receber mais, SAIR.
- **D:** Olá {nome}, é o {vendedor}, do {stand}. Falou-nos na oficina em trocar o {viatura}. Se ainda fizer sentido, mostro-lhe opções. Responda SIM ou ligue {tel_vendedor}. Para não receber mais, SAIR.
- **E:** {stand}: campanha {nome_campanha} da {marca} até {prazo_campanha}. Saiba se se aplica ao seu {viatura}: {tel_vendedor}. Condições: {link_condicoes}. Para não receber mais, SAIR.
- **F:** sem SMS. Para clientes inactivos, o email com a pergunta chega; uma mensagem no telemóvel de quem não fala com o stand há muito tempo é intrusiva.

## T3. Guião da chamada

Só com base para telefone. Uma tentativa e, se não atender, um retorno noutro dia e hora. Sem mensagens de voz gravadas automaticamente.

> Bom dia, fala {vendedor}, do {stand}. Estou a ligar porque {motivo do segmento: o contrato do seu {viatura} termina em breve | temos clientes à procura de {modelo_procurado} | falou-nos em trocar o {viatura}}. Tem dois minutos, ou prefere que ligue noutra altura?

- **Se tem tempo:** ainda tem o {viatura}? Está a pensar trocar nos próximos meses? Quer marcar a avaliação?
- **Se não quer:** "Compreendo. Quer que deixemos de lhe ligar sobre isto?" Regista a resposta no momento.
- **No fim, sempre:** "Prefere ser contactado por email, telefone ou WhatsApp, ou não ser contactado?" Regista.
- **Nunca:** dar valor pelo telefone sem ver a viatura; insistir depois de um "não"; dizer que a oferta acaba quando não acaba.

## T4. Último email

- **Assunto:** Última mensagem sobre a avaliação do seu {viatura}

> Olá {nome},
>
> Esta é a última mensagem desta campanha. Se quiser avaliar o {viatura} mais tarde, o nosso contacto é {tel_vendedor}: a avaliação sem compromisso continua disponível.
>
> {As condições de {oferta} terminam a {prazo_oferta}.}
>
> Obrigado pela atenção,
> {vendedor}
> {stand}

## Guião de avaliação

**Antes (mensagem de serviço, porque o cliente pediu a marcação):**

> Olá {nome}, fica marcada a avaliação do {viatura} para {data}, às {hora}, em {morada}. Se puder, traga o documento da viatura, o livro de revisões ou facturas de manutenção, todas as chaves e a ficha da última inspecção. Para alterar: {tel_vendedor}. {stand}

Não peças cópias de documentos de identificação para a avaliação.

**Durante:**

1. Pergunta: há quanto tempo a tem, manutenções feitas e onde, avarias ou acidentes conhecidos, o que funciona menos bem, se há crédito por pagar ou reserva de propriedade (só para saber se a financeira tem de intervir).
2. Vê: exterior, interior, pneus, avisos no painel, quilómetros comparados com o histórico, documentos; test-drive curto.
3. Explica a proposta: valor firme, por escrito, com validade e condições (por exemplo, sujeita à verificação do registo). O valor da retoma e o preço da viatura que o cliente compra aparecem separados, para o cliente ver os dois.

**Depois:**

- **Aceita:** contrato de compra e venda e requerimento de registo; se houver reserva de propriedade, o cancelamento trata-se com a financeira.
- **Não aceita:** agradece, deixa a proposta escrita com a validade, pergunta se quer contacto futuro e regista a resposta.

## Respostas

| Resposta | O que fazer | Prazo sugerido |
|---|---|---|
| "Sim, quero avaliar" | marca a avaliação; sai da sequência | no mesmo dia útil |
| "Não" | agradece; pergunta se quer deixar de receber marketing; sai da campanha | no mesmo dia útil |
| "Mais tarde" | pergunta quando; regista a data; sai da campanha; volta só nessa data e se a base se mantiver | no mesmo dia útil |
| "Já vendi" ou "não tenho a viatura" | agradece; actualiza o registo da viatura; sai | no mesmo dia útil |
| "Quanto me dão?" | mensagem abaixo; propõe avaliação | no mesmo dia útil |
| "Como têm os meus dados?" | mensagem abaixo; regista o pedido | dentro do prazo legal de resposta a pedidos dos titulares: confirmar com o DPO |
| "Não me contactem" | oposição imediata em todos os canais indicados; confirmação abaixo | no próprio dia |
| Reclamação | sai da campanha; abre caso; responde uma pessoa, sem tom defensivo | no mesmo dia útil |

As respostas positivas seguem como contactos novos: `stand-responder-leads`.

**"Quanto me dão?"**

> Obrigado pela resposta. Sem ver a viatura, qualquer número seria um palpite, e não lhe queremos dar um valor que depois não se confirme. A avaliação demora cerca de {duracao_avaliacao} e no fim fica com uma proposta escrita. Que dia lhe dá jeito?

**"Como têm os meus dados?"**

> O seu contacto está connosco porque {comprou uma viatura | fez manutenção | aceitou receber novidades} em {data}. Usamo-lo para {finalidade}, com base em {base}. Pode pedir para ver, corrigir ou apagar os seus dados, ou opor-se a mensagens comerciais, respondendo a esta mensagem ou através de {contacto_dpo}.

**Confirmação de oposição (mensagem de serviço):**

> Registámos o seu pedido: não volta a receber mensagens comerciais do {stand} por {canal}. Só o contactaremos quando for necessário sobre algo que tenha connosco, como uma marcação ou documentos.
