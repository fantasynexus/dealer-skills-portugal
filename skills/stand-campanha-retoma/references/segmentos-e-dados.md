# Segmentos, dados e audiência

Como escolher quem entra na campanha, com que prova, e como ler o resultado. Os limiares de tempo e de dimensão são decisões do stand; quando esta referência sugere um valor, é ponto de partida, não facto medido.

## 1. Os seis segmentos

### A. Fim de crédito, leasing, aluguer de longa duração ou renting

- **Entra:** contrato com fim conhecido nos próximos meses (o stand fixa a janela).
- **Dados:** data de fim e tipo de contrato, só se o stand os tem legitimamente (por exemplo, porque intermediou o crédito) e se a finalidade de marketing é compatível ou foi consentida. Revisão jurídica sempre.
- **Não chega:** "comprou a crédito há quatro anos, deve estar a acabar". É uma inferência, não um dado.
- **Diferenças que mudam a mensagem:** no crédito clássico a viatura é do cliente (com possível reserva de propriedade até ao fim). No leasing há normalmente opção de compra pelo valor residual. No aluguer de longa duração e no renting a viatura pode pertencer à locadora até ao fim, conforme o contrato. Confirma o tipo antes de escrever: num renting não há "retoma da sua viatura".
- **Exclusões próprias:** contrato em incumprimento ou renegociação. Nunca é sinal de campanha.
- **Ângulo:** preparar com tempo o que vem a seguir, sem interpretar o contrato do cliente.

### B. Valor de retoma provável

- **Entra:** viaturas cuja idade, quilómetros e modelo tornam razoável que o cliente queira saber quanto valem.
- **Dados:** marca, modelo, versão, ano, quilómetros na última visita (com data) e uma estimativa de mercado com fonte e data.
- **Não chega:** estimativa sem data; quilómetros projectados sem dizer que são projectados; "o mercado está bom".
- **Ângulo:** "saber quanto vale hoje", com avaliação sem compromisso.
- **Risco:** apresentar a estimativa como valor. O capital em dívida é quase sempre desconhecido para o stand.

### C. Viatura procurada pelo stand

- **Entra:** clientes com modelos que o stand quer angariar, com prova de procura.
- **Prova aceitável:** pedidos de clientes registados para aquele modelo e configuração, recentes (o stand fixa a janela), contados sem identificar ninguém; rotação desse modelo no stock do stand; falta em stock.
- **Não chega:** "este modelo vende bem"; tendências de mercado sem fonte.
- **Ângulo:** "temos clientes à procura de {modelo}", só se houver pedidos reais. "Já temos comprador para o seu" só com um pedido concreto para uma viatura com aquelas características, e mesmo assim sem garantir a venda.

### D. Da oficina para as vendas

- **Entra:** cliente de oficina que manifestou interesse em trocar, registado pela oficina com data, ou que perguntou se vale a pena reparar.
- **Não chega:** uma reparação cara recusada, sozinha. Usar o diagnóstico da oficina como pressão para trocar é má prática e pode ser prática comercial agressiva.
- **Fluxo:** a oficina passa o contacto ao vendedor com o conhecimento do cliente.
- **Ângulo:** continuar a conversa que o cliente começou.

### E. Campanha da marca ou do importador

- **Entra:** clientes elegíveis para um programa escrito da marca, com condições e prazo.
- **Dados:** o documento da campanha e um critério de elegibilidade verificável no sistema.
- **Não chega:** "a marca costuma ter campanhas nesta altura".
- **Ângulo:** condições copiadas à letra, com o prazo real.

### F. Cliente inactivo

- **Entra:** relação anterior (compra ou oficina) sem interacção há mais tempo do que o stand fixar.
- **Dados:** data da última interacção; consentimento ou base ainda aplicáveis.
- **Ângulo:** reconexão honesta e pergunta se quer continuar a receber contactos.
- **Risco:** dados desactualizados (mudou de viatura, de contacto, faleceu). É também altura de aplicar o prazo de conservação definido pelo stand.

## 2. Segmentação proibida ou a evitar

- Categorias especiais de dados (RGPD, artigo 9.º): saúde, origem racial ou étnica, religião, entre outras.
- Vulnerabilidade financeira: incumprimento, renegociação, penhoras, atrasos de pagamento na oficina.
- Idade avançada, viuvez ou desemprego como alvo de pressão.
- Nacionalidade ou origem inferidas pelo nome.
- Inferências sobre a vida do cliente a partir de dados da oficina ("fez muitos quilómetros, deve ter mudado de emprego").

## 3. Supressões (todos os segmentos)

| Supressão | Porquê |
|---|---|
| Oposição a marketing | num canal, sai desse canal; "não me contactem", sai de todos |
| Sem prova de consentimento ou base no canal | sem base, não há contacto por esse canal |
| Compra recente (período fixado pelo stand) | quem acabou de comprar está no programa de `stand-onboarding-cliente` |
| Reclamação, caso de garantia ou reclamação formal aberta | primeiro resolve-se |
| Proposta ou negociação em curso com um vendedor | não se cruza com a campanha |
| Contacto inválido ou devolvido | higiene |
| Viatura já vendida, retomada ou que já não é do cliente | a mensagem seria falsa |
| Falecimento comunicado | respeito e dados |
| Pedido de apagamento ou de limitação | direito do titular |
| Contactado noutra campanha no mesmo período | limite global de frequência |
| Empresas (pessoas colectivas) | tratam-se em separado: regime diferente |

## 4. Lógica de audiência legível

Escreve-a assim, sem nomes, telefones, emails nem matrículas. Exemplo com valores ilustrativos:

```
SEGMENTO B: valor de retoma provável
ENTRA SE
  compra no stand entre {4} e {8} anos atrás          fonte: DMS, data_venda
  E quilómetros registados numa visita dos últimos {12} meses
  E (email com consentimento OU excepção de cliente válida)
    OU (SMS com consentimento)
SAI SE
  qualquer supressão da secção 3
CANAL
  email se houver base para email; senão SMS; telefone só com base para telefone
CONTAGEM
  passo a passo, antes e depois de cada regra
```

Os valores entre chavetas são decisão do stand. Mostra sempre a contagem por passo: é aí que se vê quantos clientes ficam de fora por falta de consentimento, o que muitas vezes é o achado mais útil da campanha.

## 5. Estimativa de retoma: como fazer e como dizer

- **Fontes:** anúncios semelhantes (marca, modelo, versão, ano, quilómetros, combustível, caixa) com data de recolha; tabelas profissionais que o stand use; retomas anteriores do próprio stand.
- **Forma:** intervalo, não um número; margem explícita; data da estimativa.
- **Depois de ver a viatura:** estado, manutenção documentada, inspecção, pneus, danos, número de proprietários, equipamento.
- **Uso:** a estimativa é interna. Não vai em mensagens em massa. Em conversa, dá-se o intervalo com as ressalvas, e a proposta firme só depois de ver a viatura, por escrito e com validade.
- **Transparência:** na proposta, o valor da retoma e o preço da viatura que o cliente compra aparecem separados.

## 6. Grupo de controlo e leitura dos resultados

- Separa ao acaso, antes do primeiro envio, dentro do mesmo segmento e depois das supressões.
- O grupo de controlo não recebe a campanha, mas continua a receber as mensagens de serviço.
- Compara a mesma medida (avaliações feitas, propostas, retomas, vendas) na mesma janela de tempo.
- Com números pequenos, uma ou duas vendas mudam a conclusão. Diz isso no relatório.
- Não há uma taxa de resposta "típica" que sirva de referência: compara com o controlo e com campanhas anteriores do próprio stand.

## 7. Métricas e regras de decisão

Funil, com o número de cada passo:

1. elegíveis
2. após supressões (e quantos saíram por falta de consentimento)
3. contactados, por canal
4. entregues
5. respostas
6. avaliações marcadas
7. avaliações feitas
8. propostas
9. retomas concretizadas
10. vendas associadas
11. margem da retoma e da venda

Desvios a contar: oposições por contacto, reclamações, desistências depois da avaliação.

Regras de decisão: o gestor escreve antes do arranque, com números dele, o que leva a **expandir** (por exemplo, avaliações feitas acima de um valor por cada 100 contactados), a **corrigir** (mensagem, canal, oferta) e a **parar**. Parar é sempre imediato perante queixa à CNPD, erro de dados ou mudança da oferta.

## 8. Exemplo resolvido

Stand Exemplo, Leiria (fictício). Todos os números são inventados para mostrar o método.

- **Objectivo:** angariar citadinos automáticos a gasolina para o stock.
- **Prova de procura:** 9 pedidos de clientes registados nos últimos 60 dias para esse tipo de viatura; nenhum em stock. Segmento C, com B como apoio.
- **Contagem:** 412 clientes com compra entre 2018 e 2021; 138 com citadino automático a gasolina; 61 com base para email ou SMS; 54 depois das restantes supressões (5 com caso aberto, 2 com proposta em curso).
- **Controlo:** com 54 clientes não há grupo de controlo útil. Os resultados serão "indícios".
- **Cadência:** email no dia 0; SMS no dia 4 a quem não respondeu; chamada no dia 9 só aos 23 com base para telefone; email final no dia 16.
- **Frase permitida:** "Temos clientes à procura de citadinos automáticos" (há 9 pedidos). **Frase proibida:** "Temos comprador para o seu carro" (não há pedido para aquela viatura concreta).
- **Medida principal:** avaliações feitas. Regra escrita pelo gestor antes do arranque: menos de 3 avaliações feitas ao fim de 16 dias, a campanha não se repete neste formato.
