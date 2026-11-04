# Mensagens e guiões dos 90 dias

Textos de partida para adaptar à voz do stand. Tratam o cliente por "você" ou de forma impessoal, salvo indicação do stand. Os códigos (M1, G1...) são os de [../references/pontos-de-contacto.md](../references/pontos-de-contacto.md).

## Regras

- **Campos:** `{nome}` (primeiro nome), `{viatura}` (marca e modelo), `{stand}`, `{vendedor}`, `{tel_vendedor}`, `{pos_venda}`, `{tel_pos_venda}`, `{email_pos_venda}`, `{data}`, `{hora}`, `{morada}`, `{duracao_entrega}`, `{link_avaliacao}`, `{link_oposicao}`, `{link_marcacao}`, `{proxima_manutencao}`, `{proxima_inspeccao}`.
- **Campo em falta:** sem `{nome}`, começa por "Olá," ou "Bom dia,". Uma linha cujo campo falta sai inteira; nunca se envia "Olá {nome}".
- **Serviço (S):** sem promoções, sem ligações para stock, sem "aproveite".
- **Marketing (M e M?):** termina com a forma de oposição. SMS e WhatsApp: "Para não receber mais, responda SAIR." Email: rodapé com `{link_oposicao}`.
- **Garantia, registo, manutenção:** os campos `{resumo_garantia}`, `{proxima_manutencao}` e `{proxima_inspeccao}` vêm do contrato, da ficha ou do plano. Sem fonte, a linha sai.
- **SMS:** acentos podem fazer a plataforma usar codificação Unicode e reduzir o limite de caracteres por mensagem. Confirma na plataforma antes de enviar.

## G1. Guião da entrega (dia 0, presencial)

Reserva 30 a 45 minutos, sem pressa. Na entrega à distância, faz o mesmo por videochamada marcada e envia a checklist por email para o cliente confirmar.

1. Recebe o cliente e confirma que o seguro está activo.
2. Dá a volta à viatura com o cliente: estado exterior e interior, comparado com o que está no contrato. Os quilómetros no painel batem com os do contrato.
3. Demonstração: arranque, luzes, climatização, ligação do telemóvel, avisos do painel. Nos novos, a aplicação da marca só se existir para o modelo e o cliente a quiser.
4. Documentos: cada item da checklist, entregue ou explicado (registo, declaração de circulação, termo de responsabilidade com hora).
5. Garantia: lê com o cliente o que cobre e como se acciona.
6. Consentimentos: explica cada caixa e recolhe em separado. "Pode mudar de ideias quando quiser, basta dizer-nos."
7. Apresenta a pessoa de pós-venda (G2).
8. Próximos passos: "Amanhã recebe um resumo por email. Avisamos quando o registo estiver concluído. Daqui a uns dias ligo-lhe para saber como está a correr."
9. Entrega o cartão de entrega.

Frases a evitar: "a garantia cobre tudo", "o documento chega em X dias", "a primeira revisão é grátis" (salvo se estiver escrito), "se não ficar satisfeito, não ponha no Google, fale connosco".

**Cartão de entrega (impresso):**

> Obrigado por escolher o {stand}.
> A sua viatura: {viatura}
> Vendas: {vendedor}, {tel_vendedor}
> Pós-venda e garantia: {pos_venda}, {tel_pos_venda}
> Próxima inspecção: {proxima_inspeccao}
> A sua opinião ajuda outras pessoas a escolher. Se quiser deixar uma avaliação no Google, aponte a câmara ao código QR.

## G2. Passagem vendedor → pós-venda (dia 0)

- Vendedor: "Apresento-lhe {pos_venda}, que trata da garantia e da oficina. Qualquer dúvida depois de hoje pode ligar-lhe directamente."
- Pós-venda: "Guarde o meu número. Se notar alguma coisa estranha nos primeiros dias, ligue logo: é mais fácil resolver cedo."
- Internamente, o vendedor passa: viatura, data de entrega, pendentes combinados, canal preferido, consentimentos.

**M3. Se a pessoa de pós-venda não estiver (S, WhatsApp ou SMS):**

> Olá {nome}, é {pos_venda}, do pós-venda do {stand}. O {vendedor} falou-me da entrega do seu {viatura}. Para garantia, oficina ou qualquer problema com a viatura, o meu contacto directo é este: {tel_pos_venda}.

## M1. Confirmação da entrega (S, 1 a 2 dias antes)

**SMS ou WhatsApp:**

> Olá {nome}, confirmamos a entrega do {viatura} a {data}, às {hora}, em {morada}. Traga o seu documento de identificação e o comprovativo do seguro. Conte com cerca de {duracao_entrega}. Para alterar, responda a esta mensagem ou ligue {tel_vendedor}. {vendedor}, {stand}

**Email**, assunto: "Entrega do seu {viatura}: {data}, às {hora}". Mesmo conteúdo, com a morada e a forma de chegar.

## M2. Resumo da entrega (S, dia 1)

**Email**
Assunto: O resumo da entrega do seu {viatura}
Preheader: Contactos, documentos e o que acontece a seguir.

> Olá {nome},
>
> Obrigado por ter escolhido o {stand}. Fica aqui o resumo de ontem, para ter tudo no mesmo sítio:
>
> - Documentos entregues: {lista_documentos}.
> - Registo de propriedade: {estado_registo}. Avisamos assim que estiver concluído.
> - Garantia: {resumo_garantia}. Para a accionar, fale com {pos_venda} ({tel_pos_venda}).
> - Próxima inspecção: {proxima_inspeccao}.
>
> Se surgir alguma dúvida sobre a viatura, ligue-me ({tel_vendedor}) ou responda a este email.
>
> {vendedor}
> {stand}

**WhatsApp curto:**

> Olá {nome}, é o {vendedor}, do {stand}. Enviei-lhe por email o resumo da entrega. Para garantia e oficina, o contacto é {pos_venda}, {tel_pos_venda}. Qualquer dúvida, diga.

## G3 e M4. Como estão a correr os primeiros dias (S, dias 3 a 5)

**Telefone:**

> Bom dia, fala {vendedor}, do {stand}. Estou a ligar só para saber como estão a correr os primeiros dias com o {viatura}. Tem um minuto?

1. Está tudo a funcionar como esperava?
2. Surgiu alguma dúvida (ligações, comandos, documentos)?
3. Há alguma coisa que devíamos ter explicado melhor na entrega?

Se houver um problema: "Obrigado por me dizer. Vou registar e {pos_venda} contacta-o até {prazo}." Abre o caso (E2).

**Se não atender (WhatsApp):**

> Olá {nome}, é o {vendedor}, do {stand}. Liguei só para saber como estão a correr os primeiros dias com o {viatura}. Se tiver alguma dúvida, responda aqui quando lhe der jeito.

## M5. Dúvidas da primeira semana (S, dia 7)

**Email**
Assunto: Três coisas que costumam surgir na primeira semana

> Olá {nome},
>
> Na primeira semana com uma viatura que ainda é nova para si, as dúvidas costumam ser estas:
>
> - Ligar o telemóvel: se tiver dúvidas, mostramos-lhe no stand ou por videochamada.
> - Via Verde ou outro identificador de portagens: lembre-se de o associar à viatura nova.
> - Documentos: enquanto o registo não estiver concluído, ande com a declaração de circulação, o comprovativo do pedido de registo e o seguro.
>
> Se alguma coisa não estiver a funcionar como esperava, diga-nos já. É mais fácil resolver cedo.
>
> {vendedor}
> {stand}

## M6. Registo concluído (S, evento)

**SMS ou WhatsApp:**

> Olá {nome}, o registo de propriedade do {viatura} está concluído. {O documento está no stand para levantar | Enviámos o documento por correio registado para a morada do contrato}. Qualquer dúvida: {tel_vendedor}. {stand}

## M7. Atraso no registo (S, evento)

Primeiro um telefonema; depois este email, para ficar escrito.

**Email**
Assunto: Ponto de situação do registo do seu {viatura}

> Olá {nome},
>
> O registo de propriedade do {viatura} ainda não está concluído. Pedimo-lo a {data_pedido} e estamos a acompanhar. {motivo, se for conhecido}
>
> Enquanto isso, continue a andar com a declaração de circulação, o comprovativo do pedido de registo e o seguro. {Renovámos a declaração de circulação, que segue em anexo.}
>
> Voltamos a contactá-lo quando houver novidade, ou até {data_proximo_contacto}, o que acontecer primeiro.
>
> {administrativo}
> {stand}

## M8. Pedido de avaliação (M?, dias 10 a 14)

Vai para todos os clientes entregues, com o mesmo texto. Com um caso aberto, espera pelo fecho e segue igual.

**WhatsApp ou SMS:**

> Olá {nome}, é o {vendedor}, do {stand}. Se tiver um minuto, a sua opinião sobre a compra do {viatura} ajuda outras pessoas a escolher: {link_avaliacao}. Se alguma coisa não correu bem, diga-nos também directamente, para podermos resolver. Para não receber mais mensagens destas, responda SAIR.

**Email**
Assunto: A sua opinião sobre a compra do {viatura}

> Olá {nome},
>
> Passaram alguns dias desde a entrega do {viatura}. Se tiver um minuto, gostávamos de saber como correu, numa avaliação no Google: {link_avaliacao}
>
> Escreva o que achar justo, de bom e de menos bom. Se houver alguma coisa por resolver, diga-nos também directamente: {tel_pos_venda}.
>
> Obrigado,
> {vendedor}
> {stand}
>
> Recebe este email porque comprou uma viatura no {stand}. Se não quiser receber pedidos deste tipo: {link_oposicao}

## M9. Garantia: como accionar (S, dias 25 a 30)

**Email**
Assunto: Garantia do seu {viatura}: como funciona

> Olá {nome},
>
> Para ter à mão, caso precise:
>
> - A garantia da sua viatura: {resumo_garantia}.
> - Como accionar: ligue ou escreva a {pos_venda} ({tel_pos_venda}, {email_pos_venda}). Diga o que nota e desde quando e, se puder, envie uma fotografia ou um vídeo.
> - Onde é feita a reparação: {oficina}.
>
> Guarde este email junto dos documentos da viatura.
>
> {pos_venda}
> {stand}

`{resumo_garantia}` copia o contrato ou o documento da garantia. Não o alargues por palavras tuas.

## G4. Visita à oficina (S, dias 14 a 21, só oficina própria)

Dez minutos, combinados com o cliente. A pessoa de pós-venda mostra onde se deixa a viatura, onde se espera, como se marca, e responde a dúvidas. Não se vende nada nesta visita.

## M10. A oficina para o seu {viatura} (dias 30 a 45)

**Oficina própria (S, só informação):**

> Olá {nome},
>
> Sou {pos_venda}, da oficina do {stand}. Quando chegar a altura da manutenção, ou se notar alguma coisa na viatura, pode marcar comigo: {tel_pos_venda} ou {link_marcacao}. Estamos em {morada_oficina}, {horario}.
>
> {pos_venda}

**Oficina parceira (S; só depois de o cliente autorizar a passagem do contacto):**

> Olá {nome},
>
> Como combinámos na entrega, a manutenção e as reparações da garantia do {viatura} são feitas na {oficina_parceira}, em {morada_parceira}. O contacto é {contacto_parceira}. Como autorizou, já lhes passámos o seu contacto.
>
> {pos_venda}
> {stand}

Se a mensagem anunciar preços, descontos ou pacotes de manutenção, passa a marketing (M): precisa de base e de oposição.

## G5. Telefonema dos dois meses (S, dias 45 a 60)

> Bom dia, fala {pos_venda}, do {stand}. Passaram cerca de dois meses desde a entrega do {viatura}. Ligo para saber se está tudo bem. Tem um minuto?

1. Notou alguma coisa na viatura desde a entrega?
2. Ficou claro como funciona a garantia e quem contactar?
3. Prefere que o contactemos por outro canal, ou menos vezes?

Regista as respostas e as mudanças de preferência no mesmo dia.

## M11. Marcação de oficina (S, evento)

**SMS:**

> Olá {nome}, está marcada a visita do {viatura} à oficina para {data}, às {hora}, em {morada_oficina}. Para alterar, responda ou ligue {tel_pos_venda}. {stand}

Lembrete na véspera, mesmo texto com "amanhã".

## M12. Lembrete de manutenção (M, salvo pedido expresso do cliente)

Só sai com `{proxima_manutencao}` confirmada. Sem data, não há lembrete.

**Email**
Assunto: Manutenção do {viatura}: está a chegar a altura

> Olá {nome},
>
> Segundo o plano de manutenção da sua viatura, a próxima intervenção está prevista para {proxima_manutencao}. Se quiser fazê-la connosco, pode marcar com {pos_venda} ({tel_pos_venda}) ou em {link_marcacao}.
>
> Se já a fez noutro lado, diga-nos e actualizamos o registo, para não voltar a receber este lembrete.
>
> {pos_venda}
> {stand}
>
> Se não quiser receber lembretes destes: {link_oposicao}

**SMS:**

> {stand}: a manutenção do {viatura} está prevista para {proxima_manutencao}. Para marcar: {tel_pos_venda}. Para não receber lembretes, responda SAIR.

## M13. Pedido de recomendação (M, dias 75 a 90)

**Email**
Assunto: Conhece alguém à procura de carro?

> Olá {nome},
>
> Se conhecer alguém à procura de viatura, teremos todo o gosto em ajudar, com o mesmo cuidado que tentámos ter consigo. Basta passar-lhe o nosso contacto: {tel_vendedor}.
>
> {Se houver programa de recomendação: condições exactas e onde estão escritas.}
>
> {vendedor}
> {stand}
>
> Se não quiser receber mensagens destas: {link_oposicao}

Pede ao cliente que passe o contacto do stand, não que envie os dados de outra pessoa. Um incentivo por recomendação, se existir, nunca se mistura com avaliações.

## M14. Fecho dos 90 dias (S)

**Email**
Assunto: Os primeiros três meses com o seu {viatura}

> Olá {nome},
>
> Faz hoje três meses que levou o {viatura}. Para ficar com tudo à mão:
>
> - Próxima manutenção: {proxima_manutencao}.
> - Próxima inspecção: {proxima_inspeccao}.
> - Garantia e oficina: {pos_venda}, {tel_pos_venda}.
> - Vendas: {vendedor}, {tel_vendedor}.
>
> Se alguma coisa não correu como esperava nestes três meses, responda a este email. Lemos todas as respostas.
>
> {gerente ou vendedor}
> {stand}

Sem `{proxima_manutencao}`, a linha passa a "Próxima manutenção: segundo o plano de manutenção da viatura. Se quiser, ajudamos a confirmar."

## M15. Primeira resposta a um problema (S, excepção E2)

**WhatsApp ou email:**

> Olá {nome}, obrigado por nos ter dito. Registámos a situação do {viatura}: {o que o cliente descreveu, por palavras dele}. {pos_venda} vai contactá-lo até {prazo} para combinar o passo seguinte. Se lhe parecer que afecta a segurança, evite circular e ligue já para {tel_pos_venda}.

Nesta mensagem não se admite nem se nega responsabilidade, não se fala de custos e não se diz se está ou não na garantia. Isso decide-se depois de ver a viatura.

## Confirmação de oposição (S, excepção E6)

> Registámos o seu pedido: não volta a receber mensagens comerciais do {stand} por {canal}. Só o contactaremos quando for necessário sobre a sua compra, como documentos, garantia ou uma marcação que tenha connosco.
