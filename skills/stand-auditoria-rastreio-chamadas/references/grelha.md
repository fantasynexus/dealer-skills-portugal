# Grelha de 100 pontos: rastreio de chamadas

Lê antes de pontuar. Cada critério diz onde verificar, que prova aceitar e o que dá total, parcial ou 0.

## Regras de pontuação

- **Prova aceitável:** linha do teste com data e hora ao minuto; captura da plataforma com data; exportação de chamadas sem números de clientes; registo do CRM com ID interno. Uma afirmação do fornecedor sem prova não conta.
- **`N/V`:** não verificado (sem acesso, sem teste autorizado). Sai do denominador. Nunca é 0.
- **`N/A`:** não aplicável, com razão escrita. Exemplos: sem troca dinâmica porque o stand escolheu números estáticos por canal (áreas 2 e 3); sem gravação nem transcrição (área 9); sem Google Ads (critérios de Ads).
- **Na dúvida entre dois níveis, dá o mais baixo** e escreve o que faltou.
- **Nota** = pontos obtidos ÷ pontos verificados × 100. **Cobertura** = pontos verificados ÷ pontos aplicáveis. Com cobertura abaixo de 60 %, a nota é indicativa e o relatório diz isso.
- Os nomes dos menus variam entre fornecedores; regista o caminho que encontraste.

## Falhas críticas

Saem no topo do relatório, independentemente da nota:

- chamadas gravadas sem aviso audível antes do início da gravação;
- link `wa.me` ou número de WhatsApp trocado para um número de rastreio (o cliente escreve para um número sem WhatsApp);
- `tel:` que liga para um número diferente do que está escrito;
- chamadas fora de horas ou em hora de almoço sem atendimento, sem mensagem e sem registo;
- números de rastreio publicados em canais permanentes (Perfil, fachada, portais) cuja titularidade não é do stand e sem garantia de portabilidade.

## 1. Inventário e propriedade dos números (8)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 1.1 Inventário completo | 3 | Lista do stand, script em várias páginas, Perfil, portais, fotografias da fachada e impressos | Todos os números publicados listados com local, gama, destino e quem atende | Faltam locais (portais, impressos, telemóveis de vendedores): 1 | Ninguém sabe que números estão publicados |
| 1.2 Titularidade e portabilidade | 3 | Contrato ou resposta escrita do fornecedor | Números em nome do stand, com resposta escrita sobre o que acontece se mudar de fornecedor | Titular é o stand mas portabilidade por confirmar: 1 | Números da agência ou do fornecedor sem saída, ou telemóvel pessoal como número principal |
| 1.3 Números por canal fora do site | 2 | Inventário contra a lista de canais que o gestor quer medir | Cada canal a medir (portal, fachada, impressos) tem número próprio, ou há decisão escrita de não medir | Só alguns: 1 | O gestor quer saber a origem mas o número é o mesmo em todo o lado |

## 2. Troca dinâmica de número e persistência (12)

`N/A` se o stand decidiu não usar troca dinâmica.

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 2.1 Troca por origem | 4 | Testes T01 a T05 | Cada origem mostra o número esperado | Algumas origens caem no número errado: 2 | Não troca |
| 2.2 Todas as ocorrências | 3 | Cabeçalho, rodapé, ficha de viatura, botão fixo no telemóvel, contactos | Texto e `tel:` trocados de forma coerente em todas | Uma ocorrência fica com o número original: 1 | Só uma ocorrência trocada |
| 2.3 Exclusões | 2 | Teste T13; JSON-LD e rodapé | WhatsApp nunca trocado; outros departamentos e NAP seguem a decisão escrita | | WhatsApp trocado (falha crítica) ou NAP trocado contra a decisão |
| 2.4 Persistência e tempo de troca | 3 | Testes T06 e T07; telemóvel em dados móveis | O número mantém-se ao mudar de página e no regresso dentro da sessão; o original não fica visível tempo suficiente para ser marcado | Muda entre páginas, ou o original pisca claramente: 1 | Número diferente em cada página, ou troca só depois de vários segundos |

## 3. Conjunto de números e colisões (8)

`N/A` se só há números estáticos.

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 3.1 Dimensão do conjunto | 4 | Relatório de ocupação ou avisos de esgotamento do fornecedor; se não houver, pico de utilizadores simultâneos por origem no GA4 em tempo real, numa hora de ponta | Sem esgotamento no período e margem documentada | Esgotamentos ocasionais: 2 | Esgotamentos frequentes, ou sem forma de saber |
| 3.2 Reserva e chamadas tardias | 2 | Definições do conjunto; pergunta ao fornecedor | Tempo de reserva configurado e regra escrita para quem guarda o número e liga dias depois | Configurado mas sem regra para chamadas tardias: 1 | Desconhecido |
| 3.3 Número de recurso | 2 | Definições; chamada a um número do conjunto fora de sessão | Chamadas sem sessão ficam como "recurso" ou "sem sessão" | | Atribuídas a uma origem qualquer |

## 4. Origem, campanha e UTM (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 4.1 Regras de origem | 3 | Definições de origem; testes | Separa Google pago, orgânico, Perfil Google (pelo UTM), directo, redes, email e referências | Só pago contra o resto: 1 | Tudo "site" |
| 4.2 Campanha e página | 3 | Registo das chamadas de teste | Cada chamada guarda `utm_*` e página de entrada | Só origem, sem campanha: 1 | Nada |
| 4.3 Identificadores de clique | 2 | Teste com `?gclid=TESTE_AUDITORIA` | `gclid` (e `gbraid` ou `wbraid` quando existem) gravados na chamada | | Não gravados (`N/A` sem Google Ads) |
| 4.4 Correspondência com o CRM | 2 | Tabela de nomes de origem da plataforma contra a lista do CRM | Tabela escrita e aplicada | Nomes parecidos mas sem regra: 1 | Nomes diferentes que ninguém liga |

## 5. Encaminhamento, IVR, horários e chamadas perdidas (12)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 5.1 Destino por departamento | 3 | Testes T08 e T09 | Vendas, oficina e peças chegam a quem deve atender; reencaminhamentos para telemóveis documentados e ainda registados na plataforma | Um departamento cai no sítio errado: 1 | Tudo para o mesmo número sem critério |
| 5.2 Fora de horas e feriados | 3 | Teste T10; horário na plataforma, no Perfil e no site | Mensagem com horário e alternativa (WhatsApp, devolução de chamada), correio de voz ouvido, feriados nacionais e municipal previstos | Mensagem sem alternativa, ou feriados esquecidos: 1 | Toca sem resposta ou dá ocupado |
| 5.3 Chamadas perdidas | 4 | Teste T11; lista de perdidas; CRM | Perdidas listadas, regra escrita de devolução (quem e em quanto tempo, decidido pelo stand) e devolução registada | Listadas mas sem regra ou sem registo: 2 | Invisíveis (por exemplo, perdidas no telemóvel de um vendedor) |
| 5.4 Mensagem inicial e IVR | 2 | Ouvir cada número | Identifica o stand, é curta, chega a uma pessoa depressa, inclui o aviso de gravação quando se grava | Longa ou com vários níveis: 1 | Sem identificação do stand |

## 6. Classificação e revisão humana (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 6.1 Categorias | 3 | Etiquetas da plataforma ou do CRM | Vendas, pós-venda, peças, financiamento e outros (as de `stand-classificar-chamadas`) ou equivalência escrita | Categorias diferentes sem equivalência: 1 | Nenhuma |
| 6.2 Regra de chamada qualificada | 3 | Documento ou definição na plataforma | Atendida, com duração mínima decidida pelo stand, categoria de vendas e não repetida | Só duração: 1 | Todas as chamadas contam |
| 6.3 Revisão humana | 4 | Registo de revisões | Amostra periódica revista por uma pessoa, com erros da classificação automática anotados | Revisão ocasional sem registo: 2 | Só automática, ou nenhuma |

## 7. Eventos e conversões no GA4 e no Google Ads (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 7.1 Evento de chamada no GA4 | 3 | DebugView ou relatório de eventos depois de uma chamada de teste | Evento com nome documentado e parâmetros de origem, duração e categoria, sem o número de quem ligou | Evento sem parâmetros: 1 | Sem evento |
| 7.2 Conversão no Ads | 4 | Goals > Conversions; definição de duração mínima | Só chamadas qualificadas como primárias | Todas as chamadas acima de uma duração, de qualquer departamento: 2 | Nenhuma, ou todas como primárias incluindo spam |
| 7.3 Sem dupla contagem | 3 | Lista de acções: `clique_telefone`, chamada da plataforma, chamadas de anúncios | Uma só primária por chamada real | | Duas ou mais primárias para a mesma chamada |

## 8. Criação e deduplicação no CRM (12)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 8.1 Lead criado ou actualizado | 4 | Chamada de teste T01; CRM | Cada chamada qualificada cria ou actualiza um lead, automaticamente ou por processo manual escrito | Só algumas, ou depende de quem atende: 2 | Chamadas nunca chegam ao CRM |
| 8.2 Deduplicação | 4 | Teste T12 | A segunda chamada do mesmo número junta-se ao lead ou cliente existente segundo regra escrita | Junta, mas sem regra escrita: 2 | Cria lead novo em cada chamada |
| 8.3 Origem preservada | 3 | Lead de teste no CRM | O CRM mostra a origem da plataforma, não só "telefone" | Só em parte: 1 | Origem perdida |
| 8.4 Gravação no CRM | 1 | Perfis com acesso no CRM | Ligação à gravação só para quem tem razão para ouvir | | Qualquer utilizador ouve (`N/A` sem gravação) |

## 9. Gravação, acesso, aviso, conservação e direitos (10)

`N/A` se não há gravação nem transcrição. As perguntas jurídicas estão em [contexto-portugal.md](contexto-portugal.md); aqui verifica-se o funcionamento.

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 9.1 Aviso antes de gravar | 3 | Chamadas de teste a cada número, de entrada e de saída | Aviso audível antes de a gravação começar, com finalidade e como recusar | Só em alguns números, ou não nas chamadas de saída: 1 | Grava sem aviso (falha crítica) |
| 9.2 Decisão validada | 2 | Documento do EPD ou jurista; registo de actividades; contrato com o fornecedor | Finalidade e fundamento validados por escrito, colaboradores informados, contrato de subcontratação | Validação oral ou incompleta: 1 | Nenhuma |
| 9.3 Acessos | 2 | Lista de utilizadores da plataforma | Só quem precisa ouve, cada um com conta própria | Contas partilhadas: 1 | Toda a gente ouve |
| 9.4 Conservação | 2 | Definições de conservação | Prazo decidido e apagamento automático de gravações e transcrições | Prazo decidido mas apagamento manual: 1 | Guardado sem prazo |
| 9.5 Direitos | 1 | Processo escrito | Sabe-se como responder a pedidos de acesso, apagamento ou oposição que incluam gravações | | Ninguém sabe |

## 10. Reconciliação e alertas (8)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 10.1 Reconciliação | 4 | Funil de [testes-e-reconciliacao.md](testes-e-reconciliacao.md) ou equivalente | Mensal, com definições escritas, mesmo período e fuso | Feita sem definições: 2 | Nunca feita |
| 10.2 Alertas | 2 | Definições da plataforma ou rotina escrita | Alguém é avisado se um número fica dias sem chamadas, se o script desaparece do site ou se uma integração pára | Verificação manual irregular: 1 | Ninguém olha |
| 10.3 Dono e alterações | 2 | Documento | Uma pessoa responsável e registo de alterações de números e regras | Responsável sem registo: 1 | Ninguém |
