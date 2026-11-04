# Exemplos resolvidos

Transcrições fictícias e curtas do Stand Exemplo, Leiria (fictício). Servem para ancorar decisões em casos parecidos; quando uma chamada real não se parece com nenhuma, aplica o fluxo de [rubrica.md](rubrica.md) e, se continuar ambígua, manda-a para revisão. Os dados pessoais já aparecem substituídos, como devem aparecer na prova.

Em cada exemplo: categoria / subcategoria · confiança · campos relevantes · motivo.

## Vendas

### V1. Viatura do portal, visita marcada, com retoma

> **Stand:** Stand Exemplo, bom dia.
> **Cliente:** Bom dia. Vi no Standvirtual um Renault Clio usado, de 2020, a gasóleo. Ainda está disponível?
> **Stand:** Está, sim. Quer vir vê-lo?
> **Cliente:** Sábado de manhã dá. E tenho um Opel Corsa para dar à troca.
> **Stand:** Fica para sábado às 10h. Diz-me o seu nome e um contacto?
> **Cliente:** Sou o [nome], [telefone].

`vendas` / `compra` · `alta` · viatura "Renault Clio 2020 gasóleo", `usado`, retoma `sim`, origem `standvirtual`, `visita_marcada`, nome `sim`, contacto `sim`, contacto_novo `sim`. Motivo: pergunta por uma viatura concreta do portal e marca visita com retoma.

### V2. Pergunta de disponibilidade e desliga

> **Cliente:** Boa tarde, o Peugeot 2008 cinzento que têm no OLX ainda está aí?
> **Stand:** Está, sim senhor.
> **Cliente:** Ok, obrigado. Depois passo por aí.

`vendas` / `compra` · `media` · viatura "Peugeot 2008 cinzento", `nao_referido`, retoma `nao_referido`, origem `olx`, `visita_sem_data`, nome `nao`, contacto `nao`, contacto_novo `sim`. Motivo: interesse numa viatura do stock anunciada no OLX; quem atendeu não ficou com nome nem contacto.

### V3. Quer vender o carro ao stand

> **Cliente:** Olá, vocês compram carros? Tenho um Volkswagen Golf de 2017 e queria vendê-lo.
> **Stand:** Compramos. Pode trazê-lo para avaliarmos?
> **Cliente:** Quinta à tarde, pode ser?
> **Stand:** Quinta às 15h. O seu nome?
> **Cliente:** [nome]. Este número é o meu WhatsApp.

`vendas` / `venda_ao_stand` · `alta` · viatura "Volkswagen Golf 2017", `usado`, retoma `nao_aplicavel`, origem `nao_referido`, `avaliacao_marcada`, nome `sim`, contacto `sim`, contacto_novo `sim`. Motivo: quer vender a viatura ao stand e marca avaliação; conta à parte dos compradores.

### V4. Crédito para uma viatura do stock

> **Cliente:** Queria saber se dá para fazer a crédito o Toyota Yaris híbrido que têm no site.
> **Stand:** Dá, trabalhamos com financeiras. Quer que lhe envie uma simulação?
> **Cliente:** Pode ser, para o email que deixei no formulário ontem.

`vendas` / `compra` · `alta` · viatura "Toyota Yaris híbrido", `nao_referido`, retoma `nao_referido`, origem `site`, `proposta_a_enviar`, nome `incerto`, contacto `sim`, contacto_novo `nao`. Motivo: crédito como parte de uma compra nova; já tinha deixado contacto no formulário, por isso não é contacto novo.

### V5. Chamada de saída, cliente comprou noutro lado

> **Stand:** Bom dia, é do Stand Exemplo, estou a ligar por causa do pedido que fez sobre o Seat Ibiza.
> **Cliente:** Ah, obrigado, mas já comprei um carro noutro sítio.
> **Stand:** Com certeza, obrigado na mesma.

`vendas` / `compra` · `alta` · direcção `saida`, viatura "Seat Ibiza", `nao_referido`, retoma `nao_referido`, origem `nao_referido`, `sem_proxima_accao`, nome `incerto`, contacto `sim`, contacto_novo `nao`. Motivo: seguimento comercial de um pedido; resultado negativo. Não entra nos contactos novos.

## Pós-venda

### P1. Garantia de uma viatura comprada

> **Cliente:** Comprei-vos um Citroën C4 há dois meses e a caixa faz um barulho ao meter a segunda. Isto está na garantia?
> **Stand:** Traga-o cá para vermos. Terça de manhã?
> **Cliente:** Pode ser.

`pos_venda` / `garantia` · `alta` · `sinal_vendas = nao`. Motivo: avaria numa viatura comprada ao stand, com pergunta sobre a garantia.

### P2. Documentação em atraso

> **Cliente:** Boa tarde, comprei o carro há três semanas e ainda não recebi o documento com o registo em meu nome.
> **Stand:** Vou ver o estado do pedido e ligo-lhe ainda hoje.

`pos_venda` / `documentacao` · `alta`. Motivo: documentação de uma compra passada; mencionar o carro não a torna venda.

### P3. Reclamação com ameaça de devolução

> **Cliente:** O ar condicionado voltou a avariar. Se não resolverem desta vez, devolvo-vos o carro e vou comprar a outro lado.
> **Stand:** Peço desculpa. Traga-o amanhã, fica como prioridade.

`pos_venda` / `reclamacao` · `alta` · `sinal_vendas = nao`. Motivo: avaria repetida numa viatura comprada; "comprar a outro lado" é ameaça, não intenção de compra.

## Peças

### Pc1. Preço de um acessório

> **Cliente:** Têm tapetes de borracha para um Dacia Sandero de 2022? Quanto custam?
> **Stand:** Temos de encomendar, chegam na sexta.
> **Cliente:** Então encomende, eu passo aí a buscar.

`pecas` / `acessorios` · `alta`. Motivo: encomenda de um acessório, sem marcação de oficina nem compra de viatura.

## Financiamento

### F1. Documentos do crédito de uma viatura reservada

> **Cliente:** Já deixei o sinal para o Renault Captur. A financeira pediu o recibo de vencimento, posso mandar por email?
> **Stand:** Pode, para o email que lhe enviei ontem.

`financiamento` / `processo_credito` · `alta`. Motivo: documento do crédito de um negócio já em curso, sem intenção nova. A prova não cita valores nem dados do recibo.

### F2. Liquidação antecipada

> **Cliente:** Comprei-vos o carro a crédito em 2023 e queria saber como faço para pagar o resto de uma vez.
> **Stand:** Isso trata-se com a financeira; dou-lhe o contacto.

`financiamento` / `contrato_existente` · `alta`. Motivo: liquidação de um contrato de uma compra passada.

## Outros

### O1. Fornecedor

> **Pessoa:** Boa tarde, sou da [empresa], temos uma solução de anúncios que traz clientes interessados no seu stand. Podia falar com o responsável?

`outros` / `fornecedor` · `alta`. Motivo: vende um serviço ao stand; "clientes interessados" não é intenção de compra.

### O2. Engano

> **Pessoa:** É da oficina de pneus?
> **Stand:** Não, é um stand de automóveis.
> **Pessoa:** Ah, desculpe.

`outros` / `engano` · `alta`. Motivo: procurava outra empresa.

### O3. Só curiosidade sobre o valor

> **Cliente:** Não estou a pensar vender, mas quanto vale mais ou menos um BMW Série 1 de 2015?
> **Stand:** Depende dos quilómetros e do estado; teria de o ver.
> **Cliente:** Está bem, era só para ter uma ideia.

`outros` / `informacao_geral` · `alta`. Motivo: pede um valor indicativo e diz que não quer vender.

### O4. Desligou antes de falar

> **Stand:** Stand Exemplo, boa tarde.
> [silêncio; a chamada termina]

`outros` / `sem_motivo` · `alta`. Motivo: terminou antes de qualquer pedido.

## Casos ambíguos

### A1. Revisão com interesse de passagem

> **Cliente:** Queria marcar a revisão do meu Ford Focus. Já agora, têm algum SUV mais recente? Estou a pensar trocar, mas não para já.
> **Stand:** Temos alguns. Para a revisão, segunda às 9h?
> **Cliente:** Segunda serve.

`pos_venda` / `oficina` · `alta` · `sinal_vendas = sim`, `rever = nao`. Motivo: a finalidade foi marcar a revisão; o interesse num SUV ficou sem passo concreto e vai para a lista de sinais de vendas.

### A2. Revisão que acaba em visita marcada

> **Cliente:** Liguei para marcar a revisão. E queria ver aquele Kia Sportage que têm na montra.
> **Stand:** Quer vir vê-lo quando trouxer o carro?
> **Cliente:** Sim, segunda às 9h vejo os dois. E o meu entra na troca, se o preço for bom.

`vendas` / `compra` · `alta` · `intencao_secundaria = pos_venda`, viatura "Kia Sportage", `nao_referido`, retoma `sim`, origem `nao_referido`, `visita_marcada`, nome `incerto`, contacto `incerto`, contacto_novo `sim`. Motivo: começa pela revisão mas sai com visita marcada para ver uma viatura, com retoma. "Que têm na montra" não diz como soube da viatura, por isso a origem fica `nao_referido`.

### A3. Transcrição cortada

> **Cliente:** Boa tarde, liguei por causa do Peugeot que têm no OLX, queria saber se aceit

`vendas` / `compra` · `baixa` · `rever = sim`, motivo_revisao "cortada antes do pedido", viatura "Peugeot (modelo não referido)", origem `olx`, contacto `nao`. Fica fora do número principal até alguém ouvir a gravação.

### A4. Transcrição imperceptível

> **Cliente:** Sim, [imperceptível] o Clio [imperceptível] preço [imperceptível] amanhã.
> **Stand:** Desculpe, está a falhar. Pode ligar outra vez?

`outros` / `insuficiente` · `baixa` · `rever = sim`, motivo_revisao "transcrição falha no ponto que decide". Motivo: palavras soltas ("Clio", "preço") não chegam para classificar como venda.

### A5. Prestação de quê?

> **Cliente:** Olhe, quanto fica a prestação do Golf?
> **Stand:** Qual Golf?
> **Cliente:** Depois ligo outra vez, que agora não posso.

`vendas` / `compra` · `baixa` · `rever = sim`, motivo_revisao "não se percebe se é viatura do stock ou contrato existente". Motivo: pergunta por prestação de um modelo sem dizer de que negócio se trata.

### A6. Pede o vendedor pelo nome

> **Cliente:** O [nome] está? Preciso de falar com ele.
> **Stand:** Vou passar.
> [transferência; a transcrição termina]

`outros` / `sem_motivo` · `baixa` · `rever = sim`, motivo_revisao "pedido de pessoa sem motivo; pode ser seguimento de vendas". Motivo: o motivo da chamada não aparece na transcrição.
