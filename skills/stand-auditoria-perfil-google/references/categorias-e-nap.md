# Categorias e consistência de nome, morada e telefone

Lê isto antes de propor categorias e antes de comparar o perfil com outras fontes.

## Como escolher as categorias

1. A **principal** descreve a actividade que traz a maior parte do negócio e que o cliente reconhece ao chegar. Num stand de usados, a categoria de stand de usados; num concessionário oficial, a da marca ou de concessionário.
2. As **secundárias** só servem actividades com presença real: equipa, espaço e horário. A consola aceita várias; confirma o limite actual.
3. Não escolhas categorias para "aparecer em mais pesquisas". Uma categoria sem actividade real é um risco, não uma oportunidade.
4. Vê o que usam os concorrentes da mesma actividade que aparecem no mapa: em modo público vês a principal por baixo do nome.
5. Na consola, escreve o início do nome e escolhe a sugestão exacta. **Regista o nome tal como aparece e a data**: a Google muda nomes e traduções sem aviso.
6. Mudar a categoria principal é uma edição sensível que pode levar a nova verificação. Uma de cada vez, com o resto do perfil estável.

## Categorias relevantes para stands (confirmar na consola)

A coluna de referência usa o nome em inglês, mais estável. A tradução em português é provável, não garantida: a consola pode mostrar outro nome, e ferramentas que lêem a API da Google podem mostrar outro ainda (por exemplo, "Concessionária", com vocabulário do Brasil). Vale o que a consola mostrar no dia.

| Situação do stand | Referência (inglês) | Pode aparecer como (confirmar) | Uso | Não usar quando |
|---|---|---|---|---|
| Vende sobretudo usados | Used car dealer | "Stand de automóveis usados" ou "Concessionário de automóveis usados" | Principal | |
| Vende novos e usados sem ser concessionário de uma marca | Car dealer | "Concessionário de automóveis" | Principal ou secundária | |
| Concessionário oficial de uma marca | [Marca] dealer | "Concessionário [Marca]" | Principal na instalação dessa marca | Sem contrato com a marca: nunca, e pode violar o contrato ou os direitos da marca |
| Oficina própria aberta ao público | Auto repair shop, Car repair and maintenance | "Oficina de reparação automóvel", "Reparação e manutenção automóvel" | Secundária; principal só se for a actividade principal da instalação | A oficina é de terceiros ou não atende público |
| Chapa e pintura | Auto body shop | "Oficina de chapa e pintura" | Secundária | Só subcontrata |
| Pneus | Tire shop | "Loja de pneus" | Secundária | Montagem ocasional sem serviço ao público |
| Peças ao balcão | Auto parts store | "Loja de peças para automóveis" | Secundária | Não vende peças ao público |
| Motos | Motorcycle dealer | "Stand de motos" ou "Concessionário de motociclos" | Principal ou secundária | |
| Comerciais e pesados | Truck dealer | "Concessionário de camiões" | Secundária | Só ligeiros |
| Aluguer de viaturas | Car rental agency | "Agência de aluguer de automóveis" | Secundária | Sem licença para a actividade de aluguer (confirmar o regime aplicável) |
| Renting ou leasing | Car leasing service | "Serviço de leasing de automóveis" | Secundária | Só encaminha para uma financeira |
| Lavagem ou detalhe | Car wash, Car detailing service | "Lavagem automóvel", "Detalhe automóvel" | Secundária | Só prepara as viaturas do próprio stock |
| Financiamento | Categorias de financeira ou crédito | | Não usar | Um stand que apresenta crédito é, no máximo, intermediário de crédito (Decreto-Lei n.º 81-C/2017). O financiamento vai para serviços, não para categorias |
| Inspecção | Car inspection station | "Centro de inspecções" | Não usar | Os centros de inspecção são entidades autorizadas; levar viaturas à inspecção não faz do stand um centro |
| Posto de carregamento | Electric vehicle charging station | "Posto de carregamento" | Não usar como categoria do stand | Um posto público aparece como local próprio, não como categoria do stand |

## Nome: nome comercial e firma

- O nome no perfil é o que está na fachada, no site e nos documentos entregues ao cliente. Pode ser diferente da firma, a denominação no registo comercial. Exemplo fictício: firma "Exemplo Comércio de Automóveis, Lda.", nome "Stand Exemplo".
- Não acrescentes concelho, marcas ou "usados" se não fazem parte do nome real. Se a fachada, o site e as facturas dizem "Stand Exemplo Automóveis", esse é o nome e pode ficar.
- Mudança de nome: primeiro fachada, site e documentos; só depois o perfil. Ver [situacoes-risco.md](situacoes-risco.md).

## Lista de verificação NAP

### Campos e o que conta como diferença

| Campo | Forma de referência | Diferença que conta | Diferença que não conta |
|---|---|---|---|
| Nome | O da fachada | Nome antigo; palavras acrescentadas; nome de outra instalação | "Lda." presente ou não; maiúsculas |
| Morada | Rua, número, andar ou loja, código postal `NNNN-NNN`, localidade postal | Número de porta, código postal, morada antiga, sede fiscal em vez do stand | "R." ou "Rua", "Av." ou "Avenida", "n.º" ou "nº" |
| Localidade | A localidade postal | Localidade de outra instalação | A localidade postal pode não coincidir com o nome do concelho ou da freguesia: não é erro |
| Telefone | `+351` e nove dígitos | Número antigo, de outra instalação, ou que ninguém atende | Com ou sem `+351`; espaços |
| Site | O domínio actual do stand | Domínio antigo; página de um portal quando há site | Parâmetros UTM na ligação do perfil |
| Horário | O real | Dias ou horas diferentes | Formato |

Números de tarifa acrescida (por exemplo, começados por 707 ou 760) em linhas para contacto de consumidores têm limites legais (Decreto-Lei n.º 59/2021). Lista de controlo, não parecer: confirma a redacção em vigor e se se aplica ao stand antes de o apontar como falha.

### Fontes a comparar

| # | Fonte | Onde ver | Nota |
|---|---|---|---|
| 1 | Site | Rodapé, página de contactos, dados estruturados (`AutoDealer` ou `LocalBusiness` no código da página) | É a fonte que a Google mais cruza; corrige-se primeiro |
| 2 | Perfil de Empresa | Perfil público e consola | |
| 3 | Apple Maps | App Mapas; gestão em Apple Business Connect | Usado por quem tem iPhone e por alguns assistentes |
| 4 | Bing Maps | bing.com/maps; gestão em Bing Places | |
| 5 | Standvirtual | Página do profissional ou do stand | Morada e telefone do anúncio |
| 6 | OLX | Perfil profissional | |
| 7 | Outros portais que o stand usa | Página do stand no portal | Só os que o stand usa; nenhum é obrigatório |
| 8 | Facebook e Instagram | Página, secção de informações, bio | |
| 9 | WhatsApp Business | Perfil da empresa | Morada, horário e site do perfil |
| 10 | Marca | Localizador de concessionários | Só para concessionários oficiais |
| 11 | Directórios locais e associações | Câmara municipal, associação comercial ou do sector, se o stand lá aparece | |
| 12 | Sites que publicam dados do registo comercial | Pesquisa pela firma | Mostram firma e sede fiscal, não o nome comercial nem o stand: diferenças aqui não se corrigem no perfil |

### Modelo da tabela de consistência

| Fonte | Nome | Morada | Código postal | Telefone | Site | Horário | Data | Diferença real? |
|---|---|---|---|---|---|---|---|---|
| Site | | | | | | | | referência |
| Perfil de Empresa | | | | | | | | |
| Apple Maps | | | | | | | | |

Para cada diferença real, a acção diz onde se corrige, quem tem acesso e se a fonte tem de ser corrigida antes do perfil.

## Feriados e horários especiais

Para o critério 3.2 da grelha. Confirma a lista e as datas do ano no calendário oficial: Sexta-feira Santa, Páscoa e Corpo de Deus mudam de data todos os anos.

- **Feriados nacionais:** 1 de Janeiro, Sexta-feira Santa, Domingo de Páscoa, 25 de Abril, 1 de Maio, Corpo de Deus, 10 de Junho, 15 de Agosto, 5 de Outubro, 1 de Novembro, 1 de Dezembro, 8 de Dezembro, 25 de Dezembro.
- **Feriado municipal** do concelho de cada instalação (por exemplo, Santo António em Lisboa, São João no Porto). Pergunta ao gestor se fecha.
- **Carnaval:** não é feriado obrigatório; muitos negócios fecham. Pergunta.
- **Vésperas de Natal e de Ano Novo:** horário reduzido é comum. Pergunta.
- **Férias do stand** e encerramentos para obras ou inventário.

Proposta para o calendário de 30 dias: os próximos feriados e o municipal definidos na consola com antecedência, por quem tem acesso.
