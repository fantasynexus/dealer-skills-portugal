# Faixas, bloqueios, roteiro e piloto

Lê isto depois de pontuar. Os limiares desta página são regras desta skill, escolhidas para dar decisões consistentes; não são padrões do sector nem médias de mercado.

## Calcular

- **Nota total:** soma dos pontos verificados a dividir por duas vezes o número de pontos verificados, em percentagem.
- **Cobertura:** pontos verificados a dividir pelos pontos aplicáveis (todos menos os `N/A`), em percentagem. No modo orientado curto, calcula-a sobre os 17 pontos ★.
- **Por grupo:** calcula também a nota dos grupos A a E. Uma nota total razoável pode esconder um grupo fraco que impede uma ferramenta concreta.

## Faixas

| Faixa | Nota total | Condições adicionais |
|---|---|---|
| `pronto para escalar` | 80% ou mais | Cobertura de 80% ou mais, nenhum ponto crítico a 0, nenhuma dimensão abaixo de 50% |
| `pronto para piloto` | 60% a 79% | Cobertura de 60% ou mais, nenhum ponto crítico a 0 |
| `piloto limitado` | 40% a 59% | Ou nota mais alta travada por um bloqueio |
| `fundação primeiro` | Menos de 40% | Ou dois ou mais pontos críticos a 0 |

Bloqueios, aplicados depois da nota:

1. **Um ponto crítico a 0** (5.1, 6.1, 7.1, 8.1, 16.1): a faixa não passa de `piloto limitado`, e esse piloto não pode tocar em dados pessoais de clientes nem falar com clientes.
2. **Dois ou mais pontos críticos a 0:** `fundação primeiro`, seja qual for a nota.
3. **Cobertura abaixo de 60%:** a faixa é provisória e não passa de `piloto limitado` até se verificar o resto.
4. **Modo orientado curto:** faixa sempre provisória.
5. **Modo primeiro olhar:** sem faixa. Lista só o que se viu de fora.
6. **Uma ferramenta já decide sobre crédito, preço individual ou recrutamento sem pessoa:** pára a recomendação dessa ferramenta e encaminha para o encarregado de protecção de dados ou jurista.

## O que cada faixa permite

| Faixa | Pode | Não pode |
|---|---|---|
| `fundação primeiro` | Corrigir bloqueios. Usos internos sem dados pessoais, com revisão (por exemplo, rascunhos de textos genéricos) | Ferramentas com dados de clientes ou que falem com clientes |
| `piloto limitado` | Um piloto interno, sem dados pessoais de clientes e sem contacto directo com clientes | Respostas automáticas a clientes, análise de chamadas, carregamento de contactos |
| `pronto para piloto` | Um piloto com dados de clientes ou virado para clientes, com contrato, passagem para pessoa e regra de decisão | Dois pilotos ao mesmo tempo, alargar antes da data de decisão |
| `pronto para escalar` | Alargar o piloto que provou resultado ou lançar o seguinte, um de cada vez | Saltar o desenho do piloto para ferramentas novas |

## Roteiro por faixa

### `fundação primeiro`

- **30 dias:** inventário de sistemas e ferramentas de IA (4.1, 6.4); autenticação multifactor nos sistemas com dados de clientes (7.1); regra escrita para ferramentas gratuitas (11.2); lista de responsáveis (2.2).
- **60 dias:** contratos de subcontratação com quem trata dados (6.1); informação aos titulares e registo de actividades revistos com o encarregado de protecção de dados (5.1); ficha de viatura coerente entre fonte, site e portais (3.1).
- **90 dias:** voltar a pontuar os grupos A e B. Escolher o primeiro piloto só depois.

### `piloto limitado`

- **30 dias:** fechar os pontos críticos a 0; escolher um piloto interno sem dados pessoais e medir a linha de base.
- **60 dias:** correr o piloto com revisão humana de tudo o que sai; registar erros.
- **90 dias:** decidir com a regra escrita; voltar a pontuar os pontos que impediam `pronto para piloto`.

### `pronto para piloto`

- **30 dias:** desenhar o piloto (secção seguinte); bateria de testes (9.2); mensagem de transparência (10.1); passagem para pessoa (8.2).
- **60 dias:** piloto em curso, revisão semanal dos indicadores, sem mudar o âmbito.
- **90 dias:** decisão expandir, corrigir ou parar na data marcada. Não deixar o piloto andar sem decisão.

### `pronto para escalar`

- **30 dias:** escolher a próxima expansão pelo valor medido no piloto anterior, não pelo entusiasmo.
- **60 dias:** lançar uma, com o mesmo desenho.
- **90 dias:** rever contratos, saídas e formação para a escala nova (17, 11).

## Desenho do piloto

Preenche antes de começar, e só começa com tudo preenchido:

| Campo | Conteúdo |
|---|---|
| Problema e número de partida | O que se quer mudar, medido, com data |
| Fronteira | O que a IA faz e o que nunca faz |
| Dados | Que dados toca e quais estão proibidos |
| Dono | Pessoa responsável, com tempo atribuído |
| Passagem para pessoa | Quando, para quem, em quanto tempo |
| Indicadores | Três a cinco, cada um com fonte |
| Linha de base | Valor e período, medidos antes |
| Regra de decisão | Expandir se..., corrigir se..., parar se..., na data... |
| Duração | Fixa, com data de decisão |
| Testes antes de lançar | Bateria do ponto 9.2, com resultados |
| Transparência | Mensagem ao cliente (10.1) e à equipa (10.3) |
| Saída | Como se desliga e o que acontece aos dados |

## Candidatos a piloto num stand

| Piloto | Dados | Faixa mínima | Pontos que têm de estar a 2 | Skill |
|---|---|---|---|---|
| Rascunho de descrições de viatura a partir da ficha, revisto por pessoa | Sem dados pessoais | `piloto limitado` | 3.1, 15.1 | `stand-escrever-anuncio` |
| Revisão de anúncios publicados contra a ficha | Sem dados pessoais | `piloto limitado` | 3.1 | `stand-rever-anuncios-viaturas` |
| Análise de avaliações públicas por tema | Públicos, sem exportar nomes | `piloto limitado` | 11.2 | `stand-analisar-avaliacoes` |
| Rascunhos de resposta a avaliações, publicados por pessoa | Públicos | `piloto limitado` | 8.1, 15.2 | `stand-responder-avaliacoes` |
| Rascunho da primeira resposta a leads, enviado por pessoa | Contacto do cliente | `pronto para piloto` | 5.1, 6.1, 8.1 | `stand-responder-leads` |
| Resposta automática fora de horas no WhatsApp ou chat | Contacto do cliente | `pronto para piloto` | 5.1, 6.1, 8.1, 8.2, 9.3, 10.1 | `stand-responder-leads` |
| Classificação de chamadas gravadas | Voz, dados de clientes e de colaboradores | `pronto para piloto` | 5.3, 5.5, 6.1, 10.3 | `stand-classificar-chamadas` |
| Segmentação de campanhas de retoma com dados do CRM | Dados de clientes | `pronto para piloto` | 5.1, 5.2, 16.3 | `stand-campanha-retoma` |

## Primeiras acções por dimensão fraca

1. Objectivos: escrever o problema com o número actual antes de falar com fornecedores.
2. Patrocínio: nomear quem decide e marcar a primeira revisão.
3. Dados de stock e leads: comparar cinco fichas com o site e um portal; tornar a origem do lead obrigatória no CRM.
4. Sistemas: lista numa página, com dono de cada sistema.
5. RGPD: rever com o encarregado de protecção de dados a informação aos titulares e os prazos de conservação.
6. Fornecedores: pedir o contrato de subcontratação e a lista de subcontratantes a cada fornecedor.
7. Acessos: activar autenticação multifactor e acabar com contas partilhadas.
8. Supervisão: escrever as regras de passagem para pessoa e testar o desligar.
9. Exactidão: montar a bateria de perguntas difíceis e corrê-la antes de cada mudança.
10. Transparência: mensagem inicial a dizer que é um sistema automático; política sobre imagens de viaturas.
11. Formação: sessão curta por função, com registo, e regra para ferramentas gratuitas.
12. Medição: medir a linha de base durante duas semanas antes de qualquer piloto.
13. Vendas: escrever a distribuição de leads e os critérios de retoma.
14. Pós-venda: testar marcações em dois canais e registar reclamações com prazo.
15. Marketing: revisão obrigatória de textos gerados contra a ficha.
16. Discriminação: listar as decisões que nunca são automáticas e confirmar com jurista as ferramentas de recrutamento.
17. Continuidade: ler a cláusula de saída de cada contrato e exportar os dados uma vez.
