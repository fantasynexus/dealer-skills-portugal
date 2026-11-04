# Emails dos fluxos

Textos de partida em PT-PT, para adaptar à voz do stand. Tratam o cliente por "você" ou de forma impessoal, salvo indicação do stand. Os números são os do [catálogo](../references/catalogo-fluxos.md).

## Regras

- **Campos:** `{nome}`, `{viatura}` (marca e modelo), `{stand}`, `{vendedor}`, `{tel_vendedor}`, `{whatsapp}`, `{pos_venda}`, `{tel_pos_venda}`, `{data}`, `{hora}`, `{morada}`, `{link_marcacao}`, `{link_avaliacao}`, `{link_oposicao}`, `{link_confirmar}`.
- **Campo em falta:** sem `{nome}`, "Olá,". Linha cujo campo falta sai inteira. Nunca sai "Olá {nome}".
- **Remetente:** "{vendedor}, {stand}" ou "{pos_venda}, {stand}". Nunca "noreply".
- **Um CTA por email**, dito por extenso ("Marcar a visita", "Responder a este email").
- **Corpo curto:** se passar de um ecrã de telemóvel, corta.

## Rodapés

**Serviço (transaccional, pré-contratual, serviço):**

> {stand} · {morada} · {telefone}
> Recebe este email porque {tem uma marcação connosco | pediu uma proposta | comprou uma viatura no stand}.

**Marketing:**

> {stand} · {morada} · {telefone}
> Recebe este email porque {aceitou receber novidades do stand | é cliente do stand}. Se não quiser receber mais emails destes: {link_oposicao}. Continuará a receber os emails necessários sobre marcações e documentos que tenha connosco.

## 1. Resposta a novo contacto (transaccional)

- **Assunto A:** Recebemos o seu pedido sobre o {viatura}
- **Assunto B:** {stand}: o seu pedido chegou
- **Preheader:** Quem lhe responde e como falar já connosco.

> Olá {nome},
>
> Recebemos o seu pedido sobre o {viatura}. Quem lhe vai responder é {vendedor}, {prazo_resposta}.
>
> Se preferir falar já, ligue {tel_vendedor} ou envie mensagem por WhatsApp para {whatsapp}.
>
> Para adiantar, pode responder a este email com o dia em que lhe dá jeito vir ver a viatura e se tem viatura para retoma.
>
> {vendedor}
> {stand}

`{prazo_resposta}` só com um prazo que o stand cumpre ("hoje, até às 19h", "no próximo dia útil"). Sem ele, a frase acaba em "{vendedor}".

## 2. Seguimento de proposta (pré-contratual)

**2.1, ao 3.º dia**

- **Assunto A:** A proposta do {viatura}: ficou alguma dúvida?
- **Assunto B:** Sobre a proposta que lhe enviámos
- **Preheader:** Respondemos a qualquer dúvida sobre a viatura, a retoma ou o pagamento.

> Olá {nome},
>
> Enviámos-lhe a {data_proposta} a proposta para o {viatura}, válida até {validade}. Se ficou alguma dúvida, sobre a viatura, a retoma ou o pagamento, responda a este email e tratamos disso.
>
> Se preferir ver a viatura outra vez ou fazer um test-drive, diga-nos o dia que lhe dá jeito.
>
> {vendedor}

**2.2, perto do fim da validade**

- **Assunto:** A proposta do {viatura} termina a {validade}

> Olá {nome},
>
> A proposta do {viatura} termina a {validade}. Se não fizer sentido avançar, diga-nos e não voltamos a insistir sobre esta proposta. Se quiser avançar ou mudar alguma coisa, estou disponível em {tel_vendedor}.
>
> {vendedor}

## 3. Seguimento de test-drive (pré-contratual)

- **Assunto A:** Como correu o test-drive do {viatura}?
- **Assunto B:** Ficou alguma dúvida sobre o {viatura}?

> Olá {nome},
>
> Obrigado por ter vindo experimentar o {viatura} a {data}. Ficou alguma dúvida, sobre a viatura, a retoma ou o pagamento? Se quiser experimentar outra vez, ou noutro tipo de estrada, combinamos.
>
> Basta responder a este email ou ligar {tel_vendedor}.
>
> {vendedor}

## 4. Confirmação de marcação (transaccional)

- **Assunto:** Confirmado: {tipo_marcacao} a {data}, às {hora}

> Olá {nome},
>
> Fica confirmado:
>
> - {tipo_marcacao}: {data}, às {hora}
> - Onde: {morada}
> - Traga: {o_que_trazer}
> - Contacto: {pessoa}, {telefone}
>
> Para alterar ou cancelar: {link_marcacao} ou responda a este email.
>
> {stand}

Lembrete na véspera: assunto "Amanhã, às {hora}: {tipo_marcacao} no {stand}", mesmo corpo.

## 5. Boas-vindas após entrega (serviço)

Se o stand usa `stand-onboarding-cliente`, usa os textos desse programa e este fluxo fica desligado nos primeiros 90 dias.

- **Assunto:** O resumo da entrega do seu {viatura}

> Olá {nome},
>
> Obrigado por ter escolhido o {stand}. Para ter tudo no mesmo sítio:
>
> - Registo de propriedade: {estado_registo}. Avisamos quando estiver concluído.
> - Garantia: {resumo_garantia}. Para a accionar: {pos_venda}, {tel_pos_venda}.
> - Próxima inspecção: {proxima_inspeccao}.
>
> Qualquer dúvida sobre a viatura, responda a este email.
>
> {vendedor}

## 6. Lembrete de documentação (serviço)

**Documento em falta**

- **Assunto:** Falta um documento para concluir o registo do {viatura}

> Olá {nome},
>
> Para concluirmos {o_registo | o processo}, falta-nos {documento}. {Como entregar: no stand, de {horario} | por {canal_seguro}}.
>
> Se tiver alguma dúvida sobre o que é preciso, ligue {telefone}.
>
> {administrativo}

**Documento disponível**

- **Assunto:** O documento do seu {viatura} já está pronto

> Olá {nome},
>
> O registo de propriedade do {viatura} está concluído. {Pode levantar o documento no stand | Enviámos o documento por correio registado}.
>
> {administrativo}

## 7. Apresentação do pós-venda (serviço, se só informa)

- **Assunto:** Quem contactar se precisar de alguma coisa com o {viatura}

> Olá {nome},
>
> Sou {pos_venda}, do pós-venda do {stand}. Se notar alguma coisa na viatura, ou precisar de accionar a garantia, fale directamente comigo: {tel_pos_venda}.
>
> {Onde são feitas as reparações: {oficina}, em {morada_oficina}.}
>
> {pos_venda}

Se o email anunciar preços, pacotes ou descontos de oficina, passa a marketing e leva o rodapé de marketing.

## 8. Lembrete de manutenção (marketing, salvo pedido)

Só sai com data ou quilómetros com fonte.

- **Assunto A:** Manutenção do {viatura}: está a chegar a altura
- **Assunto B:** {viatura}: próxima manutenção em {proxima_manutencao}

> Olá {nome},
>
> Segundo o plano de manutenção da sua viatura, a próxima intervenção está prevista para {proxima_manutencao}. Se quiser fazê-la connosco, pode marcar em {link_marcacao} ou com {pos_venda}, {tel_pos_venda}.
>
> Se já a fez noutro lado, diga-nos e actualizamos o registo, para não voltar a receber este lembrete.
>
> {pos_venda}

## 9. Orçamento de oficina não aceite (pré-contratual)

- **Assunto:** O orçamento do {viatura} que ficou por decidir

> Olá {nome},
>
> Na visita de {data}, a oficina registou no {viatura}: {trabalho_registado}. Na altura preferiu não avançar, o que é compreensível.
>
> Se quiser marcar agora, o orçamento {numero_orcamento} é válido até {validade}. Basta responder a este email ou ligar {tel_pos_venda}.
>
> Se já tratou do assunto noutro lado, diga-nos e deixamos de enviar este lembrete.
>
> {pos_venda}

`{trabalho_registado}` copia a ordem de reparação, sem acrescentar consequências que a oficina não escreveu.

## 10. Pós-serviço e satisfação (inquérito: serviço, confirmar; avaliação: marketing)

- **Assunto A:** Correu tudo bem com o {viatura}?
- **Assunto B:** Duas perguntas sobre a sua visita de {data}

> Olá {nome},
>
> Obrigado pela visita de {data}. Duas perguntas rápidas, se tiver um minuto:
>
> 1. Correu como esperava?
> 2. Há alguma coisa que devíamos ter feito melhor?
>
> Basta responder a este email. Lemos todas as respostas.
>
> Se quiser deixar a sua opinião pública no Google, o link é este: {link_avaliacao}. Vale tanto uma crítica como um elogio.
>
> {pos_venda}

O link da avaliação vai para todos, com este texto, independentemente das respostas.

## 11. Chamada técnica da marca (segurança)

- **Assunto:** Campanha de segurança do fabricante para o {viatura}

> Olá {nome},
>
> O fabricante {marca} comunicou uma campanha que abrange o seu {viatura} (referência {ref_campanha}). Segundo a marca: {texto_da_marca}.
>
> Para marcar a intervenção: {contacto_oficina}.
>
> Se já a fez, ou se já não tem esta viatura, diga-nos para actualizarmos o registo.
>
> {pos_venda}

Sem promoções, sem acrescentar nada ao texto da marca.

## 12. Fim de contrato ou financiamento (marketing, revisão jurídica)

- **Assunto:** O contrato do seu {viatura} termina em {mes_fim}

> Olá {nome},
>
> Segundo os nossos registos, o contrato de {tipo_contrato} do {viatura} termina em {mes_fim}. Se quiser preparar com tempo o que vem a seguir, explicamos-lhe o que temos disponível e fazemos as contas sem compromisso.
>
> {Em renting ou aluguer de longa duração: o que acontece à viatura no fim trata-se com {locadora}, segundo o seu contrato.}
>
> Para marcar uma conversa: {link_marcacao} ou {tel_vendedor}.
>
> {vendedor}

## 13. Momento de retoma (marketing)

- **Assunto:** Quer saber quanto vale hoje o seu {viatura}?

> Olá {nome},
>
> Se em algum momento pensar em trocar o {viatura}, fazemos a avaliação sem compromisso, com a viatura à frente, e no fim fica com uma proposta escrita.
>
> Basta responder a este email ou ligar {tel_vendedor}.
>
> {vendedor}

## 14. Aniversário de compra (marketing)

- **Assunto:** Faz hoje {anos} {ano | anos} que levou o {viatura}

> Olá {nome},
>
> Faz hoje {anos} {ano | anos} que levou o {viatura}. Para ter à mão:
>
> - Próxima inspecção: {proxima_inspeccao}.
> - Próxima manutenção: {proxima_manutencao}.
> - Contacto da oficina: {pos_venda}, {tel_pos_venda}.
>
> {stand}

## 15. Cliente inactivo (marketing, pedido de confirmação)

- **Assunto:** Quer continuar a receber notícias do {stand}?

> Olá {nome},
>
> Há algum tempo que não falamos. Para não lhe enviarmos o que não quer: quer continuar a receber os nossos emails de lembretes e novidades?
>
> Se sim: {link_confirmar}
>
> Se não fizer nada, deixamos de lhe enviar emails de novidades a partir de {data_limite}. Se mudou de viatura ou de contacto, também nos pode dizer respondendo a este email.
>
> {stand}

## 16. Pedido de recomendação (marketing)

- **Assunto:** Conhece alguém à procura de carro?

> Olá {nome},
>
> Se conhecer alguém à procura de viatura, teremos todo o gosto em ajudar. Basta passar-lhe o nosso contacto: {tel_vendedor}.
>
> {Se houver programa de recomendação: condições exactas e ligação para onde estão escritas.}
>
> {vendedor}

## 17. Convite para evento (marketing)

- **Assunto:** {nome_evento}, a {data}, no {stand}

> Olá {nome},
>
> No dia {data}, das {hora_inicio} às {hora_fim}, temos {descricao_evento} no {stand}, em {morada}.
>
> {o_que_vai_haver}
>
> Se quiser vir, inscreva-se aqui: {link_inscricao}. {As vagas são {n}, se houver limite real.}
>
> {stand}
