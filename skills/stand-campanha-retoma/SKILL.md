---
name: stand-campanha-retoma
description: Criar uma campanha de retoma ou renovação para clientes actuais de um stand em Portugal, com segmentos baseados em dados reais, cadência de 2 a 4 semanas e mensagens prontas por email, SMS, WhatsApp e telefone. Usar quando o gestor fala em "retoma", "renovação", "trocar de carro", "campanha para a base de clientes", "clientes com carros antigos", "fim de crédito, leasing, ALD ou renting", "precisamos de usados para o stock", "campanha da marca" ou "reactivar clientes antigos". Entrega a lógica de audiência sem dados pessoais, exclusões, guião de avaliação sem prometer valor, tratamento de respostas, métricas até à margem e uma lista de controlo de consentimento e oposição (RGPD, Lei n.º 41/2004) que separa mensagens de serviço de marketing.
---

# Campanha de retoma e renovação

Desenha uma campanha com prazo para clientes que já têm relação com o stand: quem contactar, porquê, por que canal, com que mensagem e quando parar. Parte de dados com data e de autorização por canal. Não carrega audiências e não envia nada.

"Temos comprador para o seu carro" só se usa com prova concreta e actual. Uma estimativa de retoma não é proposta nem valor garantido.

Fronteiras com outras skills:

- O fluxo permanente e leve de retoma está em `stand-fluxos-email`.
- Os primeiros 90 dias após a compra são de `stand-onboarding-cliente`; quem comprou há pouco fica fora desta campanha.
- As respostas que chegam tratam-se como contactos novos, com `stand-responder-leads`.
- A viatura retomada anuncia-se com `stand-escrever-anuncio`.

## Antes de começar

1. **Objectivo:** vender viaturas, angariar usados para o stock, ou ambos. Muda o segmento e a medida.
2. **Dados:** que campos existem no CRM ou no DMS e com que data: compra, viatura, quilómetros na última visita, oficina, contrato de crédito (se o stand o intermediou), consentimentos por canal com prova. Pede a lista de campos e as contagens, nunca a base.
3. **Oferta real:** o que o stand oferece, por escrito, com condições e prazo. Sem oferta, a campanha é de "avaliação sem compromisso".
4. **Canais** com consentimento ou base confirmada, e quem faz as chamadas.
5. **Capacidade:** quantas avaliações por semana a equipa consegue fazer. A campanha não pode gerar mais respostas do que a equipa atende.

Pontos de decisão:

- **Sem prova de consentimento num canal:** esse canal fica fora para esses clientes. Conta-os e diz quantos ficaram de fora.
- **Capital em dívida desconhecido:** nunca se fala ao cliente de "valor positivo" ou de "capitais próprios"; fala-se em saber quanto vale hoje.
- **Dados sem data ou demasiado antigos** (o gestor fixa o limite): actualizar primeiro ou deixar o segmento fora.
- **Pára e pergunta** se te pedem para segmentar por dificuldades financeiras, saúde, idade avançada, nacionalidade ou origem, ou para usar dados de crédito sem base confirmada.

## Passos

1. **Segmento.** Lê [references/segmentos-e-dados.md](references/segmentos-e-dados.md) e escolhe um segmento (no máximo dois, com mensagens separadas). Resultado: regra de entrada, fonte e data dos dados, e o que não chega como sinal.
2. **Audiência.** Escreve a lógica em linguagem legível ou em pseudo-consulta, sem dados pessoais, e aplica as supressões. Resultado: contagem antes e depois de cada exclusão.
3. **Grupo de controlo.** Se o segmento for grande o bastante para a diferença se ver, separa ao acaso uma parte que não é contactada. Com poucas dezenas de clientes não há controlo útil: os resultados chamam-se "indícios".
4. **Cadência.** 2 a 4 semanas, 3 a 5 contactos, canais escalonados, nunca a mesma mensagem por dois canais no mesmo dia. Paragem imediata após resposta, venda, oposição ou reclamação.
5. **Mensagens.** Adapta [assets/mensagens.md](assets/mensagens.md) ao segmento e à voz do stand: oferta copiada à letra, personalização só com campos fiáveis, oposição em cada mensagem.
6. **Avaliação.** Usa o guião de avaliação do mesmo ficheiro: perguntas, o que ver na viatura, como apresentar a proposta sem prometer valor antes de a ver.
7. **Respostas.** Define o tratamento de "sim", "não", "mais tarde", "já vendi", "quanto me dão?", "como têm os meus dados?", oposição e reclamação, com responsável e prazo.
8. **Conformidade.** Preenche a lista de controlo de [references/conformidade.md](references/conformidade.md). Item em falta num canal: a campanha não arranca nesse canal.
9. **Medida.** Escreve antes do arranque as métricas e as regras de decisão (expandir, corrigir, parar), com os limiares que o gestor fixar.

## Ferramentas

Opcionais; a campanha faz-se sem elas.

- [Análise de stock](https://onepilot.app/hub/ferramentas/analise-stock): rotação e dias anunciados do stock do stand no Standvirtual, comparados com anúncios semelhantes. Ajuda a escolher os modelos que o stand quer angariar. Mostra o que roda no stock do stand; não prova que há comprador para a viatura de um cliente nem dá o valor de retoma.
- [Modelos de documentos](https://onepilot.app/hub/ferramentas/modelos-documentos): contrato de compra e venda e requerimento de registo automóvel, para quando a retoma se concretiza e o stand compra a viatura.

## Entrega

Preenche [assets/campanha.md](assets/campanha.md): resumo, segmento e dados, lógica de audiência, contagens, grupo de controlo, cadência com as quatro verificações de cada contacto, mensagens finais, guião de avaliação, tratamento de respostas, métricas e regras de decisão, lista de controlo com estado por item, autorização e itens a confirmar.

## Limites

- Não carrega audiências em plataformas (incluindo audiências personalizadas em redes sociais), não envia mensagens, não liga.
- Não promete valor de retoma, prestação, TAEG, desconto ou campanha da marca que não esteja escrito e em vigor.
- Não usa urgência falsa, prazos inventados, nem "temos comprador" sem pedido real e actual.
- Não segmenta por vulnerabilidade financeira, saúde, origem étnica, nacionalidade ou outras inferências sensíveis.
- Não mete a campanha em mensagens de serviço (confirmações de oficina, documentos, recolhas de segurança).
- Não usa chamadas nem mensagens de voz automáticas sem intervenção humana.
- As referências legais são lista de controlo: diploma citado, versão em vigor por confirmar, DPO ou jurista na dúvida.
