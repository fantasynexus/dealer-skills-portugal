# Entrega de uma viatura em Portugal

Lista de controlo operacional para o dia 0 e para as semanas seguintes. Não é parecer jurídico. Os diplomas citados mudam: confirma a versão em vigor e, para o registo, a lista actual do IRN (Instituto dos Registos e do Notariado). Os itens marcados "confirmar" não entram em mensagens a clientes antes de confirmados.

## 1. Documentos

| Item | Usado | Novo | O que verificar |
|---|---|---|---|
| Contrato de compra e venda, assinado pelas duas partes | sim | sim | Viatura, preço, pagamento, quilómetros à data, garantia acordada, reserva de propriedade se houver. Cópia para o cliente. |
| Factura | sim | sim | Regime de IVA aplicado (nos usados é frequente o regime da margem): menção correcta confirmada com o contabilista do stand. |
| Requerimento de registo automóvel assinado por comprador e vendedor, ou comprovativo do pedido no Automóvel Online | sim | quando o stand trata do registo | Quem submete e quando. O cliente fica com o comprovativo do pedido. |
| Documento Único Automóvel (DUA) ou certificado de matrícula | sim | depois da matrícula | Se fica retido para o registo, o cliente leva a declaração de circulação e o comprovativo do pedido. |
| Declaração de circulação | quando o documento não acompanha a viatura | idem | É uma declaração do stand, não um documento oficial. O modelo do hub indica 60 dias de validade; se o registo demorar mais, emite-se outra. |
| Termo de responsabilidade, com dia e hora da entrega | enquanto o registo não estiver concluído | idem | A partir dessa hora o cliente responde por multas, seguro, imposto e guarda da viatura. Inclui a lista do que foi entregue. |
| Declaração de características | quando a seguradora ou a financeira a pede | idem | Dados da viatura e do cliente antes de o registo estar concluído. |
| Ficha da última inspecção periódica | sim, se já teve | `N/A` até à primeira | Lê a data da próxima na ficha. Não a calcules de cabeça. |
| Livro de revisões e histórico de manutenção | o que existir | sim | Nunca declares histórico que o stand não tem: "desconhecido" é uma resposta válida. |
| Documento da garantia e contacto para a accionar | sim | sim | Ver secção 3. |
| Contrato de crédito e informação pré-contratual | se houve financiamento | idem | Entregues pela financeira. Dúvidas sobre o crédito vão para a financeira ou para quem no stand está habilitado como intermediário de crédito (Decreto-Lei n.º 81-C/2017: confirmar o estatuto do stand). |
| Chaves, manuais, código do rádio, chave das jantes, pneu suplente ou kit, triângulo e colete | sim | sim | Regista no termo de responsabilidade o que foi entregue e o que não existe (por exemplo, "uma só chave"). |

Os modelos de contrato, declaração de circulação, declaração de características, termo de responsabilidade e requerimento de registo estão em [Modelos de documentos](https://onepilot.app/hub/ferramentas/modelos-documentos). São pontos de partida: o stand adapta-os e, na dúvida, pede revisão a um jurista.

## 2. Registo de propriedade

- O contrato prova o negócio. A viatura só fica em nome do comprador com o registo de propriedade, pedido numa conservatória, num balcão do registo automóvel ou no Automóvel Online.
- Escreve quem pede o registo (que pessoa do stand) e quando. O prazo legal para o pedir e os emolumentos mudam: confirma no IRN e não indiques valores de memória. É comum ouvir-se "60 dias"; não o ponhas numa mensagem sem confirmar.
- Se houver reserva de propriedade a favor de uma financeira, explica ao cliente que fica inscrita no registo e como se cancela no fim do crédito. Confirma o procedimento com a financeira.
- Eventos a registar no sistema, com data: `registo_pedido`, `registo_concluido`, `documento_entregue`. São gatilhos de pontos de contacto.
- Não prometas data de chegada do documento. Promete o que o stand controla: "avisamos assim que estiver concluído" e um telefonema se houver atraso.
- **Excepção de atraso:** o stand fixa o prazo que considera normal entre `registo_pedido` e `registo_concluido`. Passado esse prazo, alguém liga ao cliente antes de ele perguntar e renova a declaração de circulação, se for preciso.

## 3. Garantia: três coisas diferentes

Não as mistures nas mensagens.

1. **Garantia legal de conformidade** (Decreto-Lei n.º 84/2021), nas vendas a consumidores. Nos usados, o diploma admite reduzir o prazo por acordo escrito até um mínimo; 18 meses é o mínimo habitualmente referido: confirma no texto em vigor e no contrato. Numa venda a uma empresa o regime é outro: confirma.
2. **Garantia comercial** do stand ou de uma empresa de garantias: voluntária, vale o que está no documento. As mensagens não a alargam nem a resumem por palavras que digam mais do que o documento.
3. **Garantia do fabricante**, nos novos e nos usados ainda dentro dela: condições do fabricante. Não digas ao cliente que a perde se fizer a manutenção fora da marca, nem o contrário: lê as condições escritas.

Em qualquer dos casos, a mensagem diz **como accionar** (quem contactar, o que ter à mão), não o prazo de cor.

## 4. Seguro, imposto e outros pendentes do cliente

- **Seguro obrigatório de responsabilidade civil** activo antes de a viatura sair. Se o stand não é mediador de seguros registado, não recomenda uma seguradora concreta: confirma o estatuto.
- **Imposto Único de Circulação (IUC):** é anual e devido pelo proprietário. Explica no dia 0 que o termo de responsabilidade cobre o intervalo até ao registo e aponta para o Portal das Finanças. Não calcules valor nem data.
- **Via Verde ou outro identificador de portagens:** lembra o cliente de o associar à viatura nova.
- **Inspecção periódica:** data da próxima, tirada da ficha.
- **Multas e portagens no intervalo do registo:** chegam ao proprietário registado. O termo de responsabilidade com dia e hora diz de que lado ficam. Define quem no stand as reencaminha e em quanto tempo.

## 5. Entrega à distância e direitos de desistência

- Se o contrato foi celebrado à distância ou fora do estabelecimento (tudo por telefone, email ou portal, viatura entregue em casa), pode existir direito de livre resolução (Decreto-Lei n.º 24/2014). Confirma com jurista se se aplica e qual o prazo, e prevê a excepção "cliente desiste".
- Se houve crédito ao consumo, o cliente pode ter direito de revogação do contrato de crédito (Decreto-Lei n.º 133/2009, ou o diploma que o substitua na transposição da Directiva (UE) 2023/2225: confirma o que está em vigor). O prazo confirma-se com a financeira.
- Na entrega à distância, a demonstração presencial passa a videochamada ou telefonema marcado, e a checklist segue por email para o cliente confirmar o que recebeu.

## 6. Consentimentos no dia 0

Recolhe em separado, com caixas não pré-seleccionadas e texto claro.

| Finalidade | Exemplos | Precisa de consentimento de marketing? |
|---|---|---|
| Serviço ligado à compra | documentos, registo, garantia, marcação pedida pelo cliente, recolha de segurança | Não, mas não pode levar promoção. |
| Marketing do stand | lembretes de manutenção com oferta, novidades, eventos, retoma, recomendação | Sim, ou a excepção de cliente descrita abaixo. |
| Partilha com terceiros | oficina parceira, marca, financeira, seguradora | Cada uma precisa de base própria: confirmar com o DPO. |

- Um consentimento por canal: email, SMS, WhatsApp, telefone.
- Regista data, canal, texto exacto aceite e quem recolheu. Sem esse registo, para efeitos do programa, não há consentimento.
- **Excepção de cliente** (Lei n.º 41/2004, artigo 13.º-A: confirmar a redacção em vigor): o contacto electrónico obtido na venda pode receber marketing de produtos ou serviços análogos do próprio stand, se o cliente teve a possibilidade de recusar no momento da recolha e a tiver em cada mensagem. Não cobre partilha com terceiros nem produtos de outra natureza. Decide com o DPO se o stand usa esta via e regista a decisão.
- A informação do RGPD (artigos 13.º e 14.º: quem trata, para quê, durante quanto tempo, que direitos) tem de estar no contrato ou na política do stand. Confirma que cobre os contactos deste programa.

## 7. Passagem para a oficina

| Situação | Contacto que o cliente recebe | O stand pode prometer | Cuidado |
|---|---|---|---|
| Oficina própria | pessoa da oficina, com nome e telefone directo | marcação, horário, o que se faz na primeira visita | preços só da tabela em vigor |
| Oficina parceira | contacto da parceira | apresentação e encaminhamento | passar os dados do cliente é partilha com terceiro: pede autorização; não prometas preços nem prazos da parceira |
| Rede da marca | oficina da marca que o cliente escolher | onde marcar | condições da garantia do fabricante |
| Sem oficina | pessoa do stand que trata da garantia | como accionar a garantia | não inventes parcerias |

## 8. Primeira manutenção

- **Usados:** parte do plano do fabricante e do histórico conhecido (data e quilómetros da última manutenção). Se o histórico é desconhecido, diz isso ao cliente e sugere uma verificação. Não inventes intervalos.
- **Novos:** plano do fabricante, tal como está no manual.
- As mensagens usam a data ou os quilómetros confirmados ou, sem eles, "segundo o plano de manutenção da viatura".
- Muitas primeiras manutenções caem depois do dia 90. Nesse caso o programa deixa a data registada no sistema e o lembrete passa para `stand-fluxos-email`.

## 9. Recolhas de segurança da marca

- O aviso de uma campanha de recolha (chamada técnica) é uma comunicação de segurança, não marketing: sem promoções.
- Um stand sem ligação à marca não recebe estes avisos. Pode indicar ao cliente a rede da marca para confirmar se a viatura tem campanhas pendentes.

## 10. Viaturas novas: serviços da marca

- Aplicações e serviços ligados da marca entram na demonstração só quando a marca os tem para aquele modelo e o cliente os quer activar.
- A activação cria uma conta do cliente com a marca: o stand ajuda, não cria a conta por ele nem guarda as credenciais.
