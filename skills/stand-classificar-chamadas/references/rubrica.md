# Rubrica de classificação

Lê antes de classificar. As regras mandam; os exemplos em [exemplos.md](exemplos.md) ilustram. Os valores entre acentos graves são os que vão para o ficheiro, sempre iguais.

## Categorias

| Categoria | Inclui | Não inclui |
|---|---|---|
| `vendas` | Interesse em comprar uma viatura: disponibilidade, preço, estado, visita, test drive, proposta, encomenda; retoma ou crédito como parte dessa compra; quem quer vender a sua viatura ao stand; seguimento comercial de um contacto já existente | Assuntos de uma compra passada; curiosidade sobre o valor de um carro sem intenção de vender; quem já comprou noutro sítio |
| `pos_venda` | Oficina, revisão, avaria, garantia, reclamação, devolução, estado de uma reparação, documentação de uma viatura comprada | Peças pedidas sem marcação de oficina |
| `pecas` | Disponibilidade, preço ou encomenda de peças e acessórios, sem marcação de oficina | Peças referidas numa marcação de oficina (é `pos_venda`) ou num negócio de compra (é `vendas`) |
| `financiamento` | Crédito ou contrato de uma compra já feita ou em curso: documentos para aprovar o crédito de uma viatura já reservada, prestação, liquidação antecipada, declarações | Pergunta de crédito para uma viatura que a pessoa ainda está a escolher (é `vendas`) |
| `outros` | Fornecedores e publicidade, recrutamento, engano, chamadas sem motivo, chamadas internas, informações gerais sem intenção expressa, transcrição insuficiente | Casos difíceis de decidir: esses vão para a categoria mais provável com `rever = sim` |

## Subcategorias

| Categoria | Subcategorias |
|---|---|
| `vendas` | `compra`, `venda_ao_stand` |
| `pos_venda` | `oficina`, `avaria`, `garantia`, `reclamacao`, `devolucao`, `documentacao`, `estado_reparacao` |
| `pecas` | `pecas`, `acessorios` |
| `financiamento` | `processo_credito`, `contrato_existente` |
| `outros` | `fornecedor`, `recrutamento`, `engano`, `sem_motivo`, `interna`, `informacao_geral`, `insuficiente` |

## Fluxo de decisão

Segue por ordem e pára no primeiro "sim".

1. **Dá para perceber o motivo da chamada?** Não: `outros` / `insuficiente` ou `sem_motivo`. Se começava a desenhar-se uma intenção, confiança `baixa` e `rever = sim`.
2. **A finalidade principal é um negócio novo sobre uma viatura** (comprar, ou vender a sua ao stand)? Sim: `vendas`. Se o interesse aparece só de passagem, não é a finalidade principal: continua e marca `sinal_vendas = sim`.
3. **É sobre uma viatura já comprada ou em reparação?** Sim: `pos_venda`.
4. **São peças ou acessórios, sem marcação de oficina?** Sim: `pecas`.
5. **É crédito ou contrato de uma compra já feita ou em curso, sem intenção nova?** Sim: `financiamento`.
6. **Nenhuma das anteriores:** `outros`.

**Finalidade principal** é o que motivou a chamada e ocupou a conversa. Uma chamada muda de finalidade quando sai dela com um passo concreto da nova: quem liga por causa da revisão e acaba com visita marcada para ver um SUV é `vendas`, com `intencao_secundaria = pos_venda`. Quem liga pela revisão e diz "e já agora, têm SUV?" sem marcar nada é `pos_venda` com `sinal_vendas = sim`.

## Casos difíceis

| Situação | Classificação | Porquê |
|---|---|---|
| "Ainda tem o carro do anúncio?" e desliga sem mais | `vendas` / `compra`, confiança `media` | Interesse numa viatura concreta do stock; contacto não captado |
| Pergunta por uma viatura para um familiar | `vendas` / `compra` | A intenção de compra existe, mesmo que o comprador seja outro |
| "Quanto me dão pelo meu carro?" e quer marcar avaliação ou pede proposta | `vendas` / `venda_ao_stand` | Quer vender ao stand |
| "Só queria saber quanto vale, não estou a pensar vender" | `outros` / `informacao_geral` | Sem intenção de vender nem de comprar |
| Retoma num negócio de compra | `vendas` / `compra`, `retoma = sim` | A retoma faz parte da compra |
| "Dá para fazer a crédito o carro que têm anunciado?" | `vendas` / `compra` | O crédito é parte de uma compra nova |
| Documentos do crédito de uma viatura já reservada | `financiamento` / `processo_credito` | Negócio em curso, sem intenção nova |
| Prestação ou liquidação de um contrato antigo | `financiamento` / `contrato_existente` | Compra passada |
| Reclamação ou ameaça de devolver a viatura | `pos_venda` / `reclamacao` ou `devolucao` | "Trocar de carro" como ameaça não é intenção de compra |
| Chamada de saída a seguir um lead, cliente ainda interessado | `vendas` / `compra`, `contacto_novo = nao` | Seguimento, não contacto novo |
| Chamada de saída, cliente já comprou noutro lado | `vendas` / `compra`, `contacto_novo = nao`, `proxima_accao = sem_proxima_accao` | A finalidade era vender; o resultado foi negativo |
| Quem já comprou noutro stand e quer comparar preços | `outros` / `informacao_geral` | Não há compra a fazer |
| Pede um vendedor pelo nome e é transferido sem dizer o motivo | `outros` / `sem_motivo`, `baixa`, `rever = sim` | Pode ser seguimento de vendas, mas não há prova |
| Transcrição cortada a meio de uma pergunta sobre uma viatura | `vendas`, `baixa`, `rever = sim` | Provável mas não confirmado; fica fora do número principal |
| "Quanto fica a prestação do [modelo]?" sem se perceber se é do stock ou de um contrato | Categoria mais provável, `baixa`, `rever = sim` | Ambíguo de verdade |
| Fornecedor que diz "temos clientes interessados no seu stand" | `outros` / `fornecedor` | Vende um serviço, não compra uma viatura |
| Colega da equipa a ligar para o número | `outros` / `interna` | Não é contacto externo |
| Português do Brasil, outra língua ou mistura | Mesmas regras | A prova fica na língua original |

## Confiança

| Valor | Quando |
|---|---|
| `alta` | Motivo explícito, chamada completa, sem contradições |
| `media` | Motivo claro, mas falta parte da chamada depois do motivo, há falhas de transcrição que não tocam no motivo, ou a subcategoria é incerta |
| `baixa` | O motivo depende de interpretação. Leva sempre `rever = sim` |

## Revisão humana

`rever = sim`, com `motivo_revisao` curto, quando:

- a confiança é baixa;
- a chamada acaba antes de o motivo ficar claro;
- a intenção muda e nenhuma predomina;
- a transcrição tem falhas no ponto que decide (nomes de modelos mal reconhecidos, "[imperceptível]");
- alguém pede uma pessoa pelo nome sem dizer porquê.

As chamadas em revisão contam na tabela por categoria (com a coluna "das quais em revisão"), mas não no número principal de vendas.

## Campos de vendas

Só quando `categoria = vendas`; noutras categorias ficam vazios.

| Campo | Valores | Regra |
|---|---|---|
| `viatura_interesse` | Texto, ou `nao_referido` | Marca, modelo, versão e ano como foram ditos. Ano em falta: "Peugeot 308 SW (ano não referido)". Várias: a principal e "considera também …". Procura genérica: "procura genérica: carrinha a gasóleo". Nunca a matrícula |
| `novo_usado` | `novo`, `usado`, `nao_referido` | Quilómetro zero ou demonstração: `usado`, e escreve-o em `viatura_interesse` |
| `retoma` | `sim`, `nao`, `nao_referido`, `nao_aplicavel` | `nao_aplicavel` em `venda_ao_stand` |
| `origem_declarada` | `standvirtual`, `olx`, `outro_portal`, `site`, `google`, `perfil_google`, `redes_sociais`, `recomendacao`, `passou_no_stand`, `cliente_anterior`, `publicidade_offline`, `outro`, `nao_referido` | Só o que quem ligou diz ou confirma. "Viu no Standvirtual?" seguido de "sim" conta; a pergunta sozinha não |
| `proxima_accao` | `visita_marcada`, `test_drive_marcado`, `avaliacao_marcada`, `visita_sem_data`, `proposta_a_enviar`, `ligar_de_volta`, `enviar_whatsapp`, `sem_proxima_accao`, `nao_referido` | "Marcada" só com dia combinado. "Passo aí um dia destes" é `visita_sem_data` |
| `nome_captado` | `sim`, `nao`, `incerto` | Quem atendeu ficou com o nome, dito na chamada |
| `contacto_captado` | `sim`, `nao`, `incerto` | Um meio de contacto confirmado na chamada (número, WhatsApp, email). O número que aparece no ecrã sozinho não conta. Em chamadas de saída é `sim`: o stand já tem o contacto |
| `contacto_novo` | `sim`, `nao`, `nao_referido` | `sim` numa chamada de entrada sem referência a contacto anterior; `nao` quando há ("falei ontem com o seu colega", "a proposta que me mandaram") ou em seguimento de saída; `nao_referido` quando a referência é ambígua |

## Sinal de vendas

`sinal_vendas = sim` numa chamada que não é de vendas quando quem liga mostra interesse real em comprar ou vender ("estou a pensar trocar de carro no próximo ano"). Nunca muda a categoria. Vai para uma lista à parte para seguimento comercial, que só acontece se o cliente aceitou ser contactado para isso. Em `vendas`, o campo fica vazio.

## Prova e motivo

- **Prova:** citação literal e curta (até cerca de 25 palavras) da fala que decide, com `[nome]`, `[telefone]`, `[email]`, `[morada]`, `[matrícula]`, `[nif]` e `[dados_financeiros]` no lugar dos dados pessoais. Sem dados de saúde.
- **Motivo:** uma frase que liga a prova à categoria.

| Bom motivo | Mau motivo |
|---|---|
| "Pergunta se o Clio do Standvirtual ainda está disponível e marca visita para sábado." | "Cliente interessado em comprar." |
| "Liga porque a caixa faz barulho num carro comprado há dois meses; quer saber se a garantia cobre." | "Fala de garantia." |
