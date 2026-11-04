---
name: stand-onboarding-cliente
description: Desenhar os primeiros 90 dias depois da venda de uma viatura num stand em Portugal, da entrega à primeira manutenção. Usar quando o gestor fala em "entrega da viatura", "checklist de entrega", "documentos e registo de propriedade", "garantia", "acompanhamento pós-venda", "clientes que não voltam à oficina", "passar o cliente para a oficina", "pedir avaliação depois da venda" ou "o que mandar ao cliente depois de comprar". Serve para usados e novos, com ou sem oficina própria, entrega no stand ou à distância, por email, SMS, WhatsApp, telefone e presencial. Entrega a checklist do dia 0, 12 a 18 pontos de contacto com responsável e gatilho, mensagens completas em PT-PT, excepções e métricas, sem misturar mensagens de serviço com marketing.
---

# Novo cliente: os primeiros 90 dias

Desenha o programa que a equipa do stand executa do dia da entrega ao dia 90: documentos e registo em ordem, cliente a saber a quem ligar, garantia explicada, primeira manutenção encaminhada e pedido de avaliação igual para todos. A skill desenha; não envia mensagens nem mexe no CRM.

A partir do dia 91, os contactos recorrentes (manutenção, aniversário de compra, recomendação) são de `stand-fluxos-email`. A renovação da viatura, mais tarde, é de `stand-campanha-retoma`.

## Antes de começar

Pergunta ao gestor, por esta ordem. O que ficar sem resposta entra na entrega como `confirmar`, nunca como facto.

1. **Vendas:** usados, novos ou ambos; entrega no stand, em casa do cliente ou à distância; entregas por mês.
2. **Oficina:** própria, parceira, rede da marca ou nenhuma.
3. **Processo actual:** quem prepara a viatura, quem trata do registo, quem entrega, quem atende problemas depois.
4. **Sistema:** onde ficam os contactos (CRM, DMS, folha, agenda) e que eventos ficam com data: entrega, pedido de registo, registo concluído, marcação de oficina.
5. **Canais e consentimentos:** como se recolhem hoje, por canal e por finalidade, e onde fica a prova.
6. **Garantia:** o que está escrito no contrato (prazo, cobertura, como accionar) e se há garantia comercial do stand ou do fabricante.

Pontos de decisão:

- **Sem registo de consentimentos:** desenha os contactos de serviço e deixa os de marketing marcados "activar quando houver consentimento ou base confirmada".
- **Sem oficina própria:** a passagem é para a oficina parceira, para a rede da marca ou para quem no stand trata da garantia. Não prometas preços nem prazos de terceiros.
- **Pouca capacidade da equipa:** mantém os pontos marcados ★ em [references/pontos-de-contacto.md](references/pontos-de-contacto.md), corta os restantes e diz quais e porquê.
- **Pára e pergunta** se te pedem mensagens que prometam o que o contrato não diz: garantia, revisão grátis, data de chegada do documento, preço de oficina.

## Passos

1. **Checklist do dia 0.** Lê [references/entrega-em-portugal.md](references/entrega-em-portugal.md) e monta a lista para o caso do stand: documentos, registo de propriedade, garantia, seguro, equipamento, consentimentos. Resultado: cada item marcado `obrigatório`, `recomendado`, `N/A` ou `confirmar`.
2. **Variante.** Escolhe usado ou novo, tipo de oficina e tipo de entrega. Resultado: uma linha com a variante e o que muda por causa dela.
3. **Pontos de contacto.** Selecciona 12 a 18 pontos de [references/pontos-de-contacto.md](references/pontos-de-contacto.md). Para cada um: dia ou janela, canal, natureza (serviço ou marketing), responsável, gatilho, dados usados, regra de supressão, resultado esperado. Resultado: tabela sem células vazias.
4. **Passagem vendedor → pós-venda.** Define quem é a pessoa de pós-venda ou de oficina, como o cliente a conhece no dia 0 e o que o vendedor lhe passa (só o necessário: viatura, data de entrega, pendentes, canal preferido).
5. **Mensagens.** Adapta os textos de [assets/mensagens-clientes.md](assets/mensagens-clientes.md) à voz do stand. Usa só campos que o sistema tem; quando um campo pode faltar, mantém a variante sem ele.
6. **Excepções.** Atraso no registo, avaria ou falta de conformidade, insatisfação, cliente que não responde, livre resolução ou devolução, pedido para não ser contactado. Para cada uma: quem decide, em quanto tempo responde, que mensagem sai.
7. **Sistema e métricas.** Lista os campos, eventos e automações necessários e as métricas com definição e fonte. Sem metas inventadas: o stand fixa-as depois de medir.
8. **Revisão final** com a lista de verificação da secção Entrega. Entrega com [assets/programa-90-dias.md](assets/programa-90-dias.md).

## Pedido de avaliação

- O mesmo pedido, com o mesmo texto, para todos os clientes entregues. Sem incentivo e sem escolher a quem pedir pelo que se espera que escrevam.
- O cartão com QR entregue em mão no dia 0 é a forma mais simples. O pedido por mensagem segue a natureza que o encarregado de protecção de dados (DPO) confirmar; por prudência, trata-o como marketing.
- Um caso em aberto (avaria, reclamação) é tratado primeiro. O pedido pode esperar pelo fecho do caso, mas não é cancelado por se esperar uma crítica.
- Responder a avaliações é trabalho de `stand-responder-avaliacoes`; encontrar padrões nelas é de `stand-analisar-avaliacoes`.

## Ferramentas

Opcionais; o programa funciona sem elas.

- [Modelos de documentos](https://onepilot.app/hub/ferramentas/modelos-documentos): contrato de compra e venda, declaração de circulação, declaração de características, termo de responsabilidade e requerimento de registo automóvel. Encaixam na checklist do dia 0. São pontos de partida: não substituem a revisão de um jurista nem a lista actual do IRN.
- [Link de avaliações do Google](https://onepilot.app/hub/ferramentas/link-avaliacoes): link directo e QR code para o cartão de entrega e para a mensagem do pedido.

## Entrega

Preenche [assets/programa-90-dias.md](assets/programa-90-dias.md): resumo, checklist do dia 0, tabela de pontos de contacto, passagem para o pós-venda, mensagens adaptadas, excepções, campos e automações, métricas e itens a confirmar.

Lista de verificação antes de entregar:

- [ ] Cada ponto tem natureza (serviço ou marketing) e nenhum ponto de serviço leva promoção.
- [ ] Os pontos de marketing indicam a base (consentimento ou excepção de cliente) e como o cliente se opõe.
- [ ] Nenhuma mensagem afirma prazo de registo, cobertura de garantia, intervalo de manutenção ou data de inspecção que não venha de documento ou do gestor.
- [ ] Os pontos ★ estão todos, ou está escrito porque falta algum.
- [ ] Cada ponto e cada excepção têm um responsável (função).
- [ ] Os itens `confirmar` estão juntos no fim, com quem os confirma.

## Limites

- Não envia, não agenda, não carrega listas, não altera o CRM.
- Não usa chamadas automáticas sem intervenção humana, urgência falsa, nem marketing disfarçado de serviço: uma mensagem de serviço com promoção passa a ser marketing.
- Não pede cartão de cidadão, matrículas, NIF ou bases de clientes para desenhar o programa. Os exemplos usam dados fictícios.
- Os pontos legais são lista de controlo, não parecer: cita o diploma e manda confirmar a versão em vigor. Na dúvida, DPO ou jurista.
- Respeita preferência de canal, oposição e retirada de consentimento em qualquer ponto. A oposição ao marketing não corta as mensagens de serviço necessárias (documentos, garantia, segurança).
