# Contexto português do rastreio de chamadas

Lê antes de recomendar números, mudanças no Perfil ou nos portais, ou testes à gravação. O que está marcado "confirmar" não é afirmação: verifica na fonte indicada antes de o pôr no relatório.

## Numeração

Os números portugueses têm nove dígitos; o indicativo do país é +351. Nos links usa o formato internacional sem espaços: `tel:+351XXXXXXXXX`.

| Começa por | O que é | Nota para o stand |
|---|---|---|
| 2 | Geográfico (por exemplo, 21 Lisboa, 22 Porto) | O indicativo identifica a zona; um número do concelho do stand mostra que é local |
| 9 (91, 92, 93, 96) | Móvel | Verifica se é também o número do WhatsApp: nesse caso a troca dinâmica não lhe pode tocar |
| 30 | Serviço nómada (voz sobre IP) | Pergunta ao fornecedor como é taxado a partir de telemóvel e testa a reacção dos clientes da zona |
| 7 e 8 (por exemplo, 707, 760, 800, 808) | Não geográficos, com regras de preço próprias | Alguns são grátis para quem liga, outros custam mais do que uma chamada normal. Confirma o preço de cada gama no plano de numeração da ANACOM |

Pontos a verificar:

- Que gamas o fornecedor oferece em Portugal e se há números do indicativo do concelho do stand.
- O custo para quem liga de um telemóvel. Não presumas que está incluído no tarifário do cliente.
- Se o stand divulga linhas para contacto do consumidor (por exemplo, pós-venda ou reclamações), confirma o regime aplicável a essas linhas (Decreto-Lei n.º 59/2021; confirmar versão e âmbito) antes de usar gamas 7 ou 8 como único contacto.
- Quem é o titular e se os números podem ser portados para outro operador ou fornecedor. Um número impresso na fachada ou no Perfil que morre com o contrato é um contacto perdido para sempre.

## Telemóveis dos vendedores

Quando o telemóvel de um vendedor está publicado (no anúncio do portal, no cartão, nas mensagens de WhatsApp), o cliente liga-lhe directamente.

- Essas chamadas nunca passam pela plataforma de rastreio. Não aparecem nas contagens nem como perdidas.
- Se o vendedor sai, os clientes ficam com o número dele.
- O telemóvel pessoal de um colaborador é dado pessoal: mascara-o no relatório (`91x xxx x12`).

Opções, para o gestor decidir: telemóveis da empresa; reencaminhamento pela plataforma; registo manual no CRM das chamadas recebidas directamente, com a origem `telefone_directo`. Mostra o que cada uma resolve; não imponhas.

## WhatsApp

Pergunta ao gestor que parte dos contactos chega por WhatsApp: em muitos stands é o canal principal. Nenhuma plataforma de rastreio de chamadas vê conversas nem chamadas de voz feitas pelo WhatsApp.

- **Medir a intenção:** o clique em `wa.me` ou `api.whatsapp.com` é um evento no GA4 (`clique_whatsapp`), não um contacto.
- **Saber de que viatura e de que página:** usa uma mensagem pré-preenchida com a referência, por exemplo `https://wa.me/351XXXXXXXXX?text=Olá, tenho interesse na viatura ref. STK-0417`. O cliente pode apagar o texto: é indicação, não prova.
- **Registar o contacto:** com a aplicação WhatsApp Business num telemóvel, as conversas só existem no telemóvel; o lead entra no CRM à mão. Com a plataforma de negócio do WhatsApp através de um fornecedor pode haver integração com o CRM; confirma com o fornecedor o que existe e quanto custa.
- **Nunca trocar o WhatsApp.** A troca dinâmica não pode mexer no link `wa.me` nem no número escrito ao lado de "WhatsApp". Se o site diz "Ligue ou envie WhatsApp para 91x…" e a troca substitui o número por um de rastreio, o cliente escreve para um número sem WhatsApp. Testa em todas as páginas.
- Mensagens ao cliente depois do primeiro contacto pedem consentimento e forma de oposição: ver `stand-responder-leads`.

## Portais

No Standvirtual, no OLX e noutros portais o telefone vem da conta ou do anúncio do stand. Confirma, na conta do stand e nas regras de cada portal:

- se o portal mostra o número do stand ou um número intermédio do próprio portal;
- se o portal tem relatórios próprios de chamadas ou de cliques em "ver telefone";
- se é possível usar um número diferente por anúncio ou só por conta.

Um número estático por portal mede as chamadas de cada portal, mas trocar o número em todos os anúncios activos tem custo e quebra os clientes que guardaram o antigo. Se o gestor decidir trocar, mantém o número antigo a reencaminhar durante um período decidido por ele. Os contactos por mensagem ou email do portal não são chamadas; contam no CRM.

## Perfil de Empresa no Google e NAP

NAP é nome, morada e telefone. Têm de ser iguais no Perfil, no site, nos portais e nos directórios.

- Antes de pensar em trocar o número: o desempenho do Perfil já mostra cliques em "Ligar" (clique, não chamada atendida), e um UTM no link do site (`utm_source=google&utm_medium=organic&utm_campaign=perfil_empresa`) mede visitas vindas do Perfil sem tocar no número.
- Se o gestor quiser mesmo medir chamadas do Perfil com um número de rastreio, uma opção é pôr o número de rastreio como principal e manter o número do stand como adicional. Confirma nas directrizes actuais da Google se é permitido e como, antes de alterar: a mudança pode levar a nova revisão do perfil e cria inconsistência com directórios e portais se não for planeada.
- O número do Perfil tem de ser local, estável e do stand. Se o contrato com o fornecedor acabar, o número do Perfil não pode morrer com ele.
- No site, mantém no HTML original e no `telephone` do JSON-LD o mesmo número do Perfil, salvo decisão escrita em contrário. O script `extrair_sinais_pagina.py` mostra exactamente esse HTML.
- Nada se altera sem autorização escrita. Para a auditoria completa ao Perfil, usa `stand-auditoria-perfil-google`.

## Gravação e aviso ao cliente

Isto é uma lista de controlo, não um parecer. Quem decide é o encarregado de protecção de dados (EPD) ou um jurista.

Diplomas e fontes a confirmar na versão em vigor:

- RGPD: princípios e licitude (artigos 5.º e 6.º), informação ao titular (13.º), subcontratante (28.º), registo de actividades (30.º), avaliação de impacto quando aplicável (35.º), transferências para fora do EEE (capítulo V).
- Lei n.º 41/2004: confidencialidade das comunicações; confirmar em que condições admite gravações no âmbito de práticas comerciais.
- Orientações e deliberações da CNPD sobre gravação de chamadas: confirmar quais estão em vigor.
- Código do Trabalho: informação aos trabalhadores e limites aos meios de vigilância a distância; confirmar se e como se aplica à gravação das chamadas da equipa.
- Regulamento (UE) 2024/1689, se houver transcrição ou análise automática: restringe o reconhecimento de emoções no local de trabalho; confirmar o âmbito antes de activar análises de "sentimento" ou "emoção".

| Pergunta ao EPD ou jurista | Porque importa | Resposta |
|---|---|---|
| Para que finalidade se grava (prova de uma transacção, qualidade, formação)? | Define o fundamento e o prazo | |
| Qual é o fundamento de licitude? | Muda o texto do aviso e o direito de recusa | |
| O aviso diz quem grava, para quê, por quanto tempo e como recusar? | Informação ao titular | |
| Que alternativa tem quem não quer ser gravado? | Recusar não pode impedir o contacto | |
| As chamadas de saída (o stand liga ao cliente) também são gravadas e avisadas? | Confirma se o aviso também toca nas chamadas de saída | |
| Os colaboradores foram informados por escrito? | São também titulares dos dados | |
| Quanto tempo se guardam gravações e transcrições, e a plataforma apaga sozinha? | Conservação limitada | |
| Onde ficam os dados e há transferências para fora do EEE? | Capítulo V do RGPD | |
| Há contrato de subcontratação com o fornecedor? | Artigo 28.º | |
| Quem pode ouvir e fica registado quem ouviu? | Acessos | |
| Há transcrição ou análise por IA? Quem a faz e onde? | Avaliação de impacto e Regulamento (UE) 2024/1689 | |

Rascunho de aviso, só para o EPD validar (não publicar sem validação):

> "Olá, ligou para o Stand Exemplo. Para [finalidade], esta chamada pode ser gravada. Se preferir que não seja gravada, diga-o a quem o atender. Mais informação em [endereço do site]/privacidade."

Confirma com o fornecedor se é possível parar a gravação a pedido. Se não for, a alternativa (por exemplo, devolver a chamada de uma linha sem gravação) tem de existir antes de se publicar o aviso.

## Fuso, horários e feriados

- Fuso `Europe/Lisbon` no continente e na Madeira, `Atlantic/Azores` nos Açores. Plataforma, GA4, Ads e CRM têm de usar o mesmo para reconciliar.
- Feriados nacionais e o feriado municipal do concelho do stand: horário especial na plataforma, no Perfil e no site.

## Perguntas a fazer a qualquer fornecedor

1. Que gamas de números tem em Portugal? Há números do indicativo do concelho?
2. Quem fica titular dos números e como se portam se o stand sair?
3. A troca dinâmica permite excluir o WhatsApp e o NAP? Como trata robôs de pesquisa?
4. Quanto tempo fica cada número reservado a uma visita? Há relatório de ocupação e avisos de esgotamento?
5. Que integração tem com o GA4 (nome do evento, parâmetros), com o Google Ads (importação de chamadas, `gclid`) e com o CRM do stand?
6. Como deduplica chamadas repetidas do mesmo número?
7. Gravação: como se configura o aviso, a recusa, o prazo de conservação e o apagamento? Onde ficam os dados? Há contrato de subcontratação?
8. Transcrição: em que língua, com que qualidade em português de Portugal (pede para testar com chamadas de teste), e onde é processada?
9. Que exportação dá (CSV com ID, data, duração, origem, estado), sem ter de pedir ao suporte?
10. Quanto custa por número e por minuto, e o que acontece aos números se o plano baixar? Pede por escrito; não cites preços sem proposta.
