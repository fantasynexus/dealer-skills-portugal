# Padrões por página, textos e listas de controlo

O que se espera de cada tipo de página num site de stand, textos de substituição em PT-PT e as listas de controlo de telefone, WhatsApp, formulários, consentimento, financiamento e urgência.

Ajusta ao processo do stand: se o stand vende sobretudo por visita, a principal na viatura é marcar visita; se fecha muito por WhatsApp, o WhatsApp sobe. Pergunta antes de decidir.

## Acções esperadas por tipo de página

| Página | Acção principal | Secundárias | A evitar |
|---|---|---|---|
| Início | "Ver viaturas disponíveis" ou caixa de pesquisa | Ligar, WhatsApp, "Avaliar o meu carro", "Marcar oficina" (se existir) | Quatro ou cinco botões iguais no topo; carrossel com um botão diferente por imagem |
| Listagem | Sem principal de página. Em cada cartão, o cartão inteiro leva à viatura | Filtros e ordenação visíveis; alerta de viaturas semelhantes, só se o stand o faz | Formulário genérico a meio da lista; janela que abre à entrada |
| Viatura | Uma, conforme o processo: "Pedir proposta" ou "Marcar visita" (ou test drive) | WhatsApp sobre esta viatura, Ligar, "Simular prestação", "Avaliar a minha retoma" | "Contactar" genérico; formulário que não leva a viatura; principal só abaixo da galeria |
| Financiamento | "Simular prestação" ou "Pedir simulação" | Ligar, WhatsApp, "Ver viaturas" | Prestação sem TAEG; "aprovação garantida"; formulário com rendimentos logo de início |
| Retoma | "Pedir avaliação do meu carro" | WhatsApp para enviar fotos, Ligar | Prometer o valor final online; pedir documentos no primeiro contacto |
| Oficina ou pós-venda | "Marcar serviço" ou "Pedir orçamento" | Ligar para a oficina (número próprio, se houver), WhatsApp | Acção principal de vendas nesta página |
| Contactos | Acções com o mesmo peso: Ligar, WhatsApp, email ou formulário, "Como chegar" (abre mapas) | Horário e morada bem visíveis | Só formulário, sem telefone nem horário |
| Página local (concelho ou loja) | A acção desse local | Direcções e telefone desse local | Texto igual ao de outras páginas locais, com outro nome de concelho |

Barra fixa em telemóvel na página de viatura: Ligar, WhatsApp e a acção principal. Três no máximo.

## Textos: fraco e melhor

| Fraco | Melhor | Onde |
|---|---|---|
| Saber mais | Ver este carro | Cartão da listagem |
| Contactar | Pedir proposta para este carro | Viatura, principal |
| Enviar | Receber proposta | Botão do formulário de proposta |
| Submeter | Pedir avaliação do meu carro | Formulário de retoma |
| Financiamento | Simular a prestação | Viatura, secundária |
| Marcar | Marcar visita ao stand | Viatura |
| Mais informações | Falar no WhatsApp sobre este carro | Viatura |
| Ligue já! | Ligar para o stand | Barra fixa |
| Agende | Marcar revisão | Oficina |
| Clique aqui | Ver carros até 15 000 € | Início, atalho de pesquisa |

Microtextos junto ao botão, só se forem verdade para o stand:

- "Respondemos por WhatsApp no horário do stand."
- "Avaliação indicativa. O valor final depende de vermos o carro."
- "Sem compromisso de compra."
- "Simulação indicativa, sujeita a aprovação da instituição de crédito."

Nunca escrevas um prazo de resposta ("em 15 minutos") sem o stand confirmar que o cumpre.

## Telefone

- Ligação: `<a href="tel:+351XXXXXXXXX">XXX XXX XXX</a>`. Indicativo `+351` no `href`; o texto visível pode estar agrupado em três blocos de três algarismos.
- Testa num telemóvel: o toque deve propor a chamada com o número certo.
- Custo da chamada: a lei portuguesa obriga a indicar, junto aos números de contacto para consumidores, o preço da chamada (ex.: "Chamada para a rede móvel nacional"). Crê-se que o diploma é o Decreto-Lei n.º 59/2021; confirma a versão e o âmbito em vigor antes de o apontar como falha.
- Número de rastreio de chamadas: aceita-se, desde que o mesmo número não apareça diferente no Perfil de Empresa sem razão. Detalhe em `stand-auditoria-rastreio-chamadas`.

## WhatsApp

- Formato: `https://wa.me/351XXXXXXXXX?text=...` com o número só em algarismos, sem `+`, espaços nem zeros à esquerda, e o texto codificado para URL (espaço = `%20`).
- Texto pré-preenchido numa viatura: "Olá, tenho interesse no [marca] [modelo] [ano] (ref. [referência]) que vi em [URL]." O stand sabe logo de que carro se trata e de onde veio o contacto.
- Testa em telemóvel (deve abrir a aplicação) e em computador (deve abrir o WhatsApp Web ou a página de escolha).
- O número tem de ser o que a equipa atende, no horário anunciado. Se ninguém responde, o problema é de processo: encaminha para `stand-responder-leads`.
- Botão flutuante: não pode tapar a acção principal nem os campos do formulário.

## Formulários: campos mínimos

| Formulário | Necessário | Opcional | A evitar no primeiro contacto |
|---|---|---|---|
| Proposta ou contacto sobre viatura | Nome, um contacto (telefone ou email), viatura preenchida automaticamente | Mensagem, canal preferido, se tem carro para retoma | Morada, NIF, data de nascimento |
| Marcar visita ou test drive | Nome, telefone, viatura, dia e período preferidos | Mensagem | Dados da carta de condução (confirmam-se no stand) |
| Avaliação de retoma | Marca, modelo, ano, quilómetros, contacto | Versão, estado, fotos; matrícula só se o stand precisa dela e diz porquê | Cópia do documento único, NIF |
| Simulação de financiamento | Valor, entrada e prazo para simular; contacto só se o cliente quer proposta | Mensagem | Rendimentos, entidade patronal, IBAN, NIF |
| Oficina | Nome, contacto, marca e modelo, serviço, data preferida | Matrícula, quilómetros | Dados que só a oficina precisa no dia |

Cada campo a mais tem de ter uma razão que o stand saiba explicar.

## Consentimento e privacidade (lista de controlo)

Confirma as versões em vigor e, na dúvida, fala com o encarregado de protecção de dados.

- Informação no momento da recolha (RGPD, artigo 13.º): responsável, finalidade, prazo de conservação, direitos e contacto. Uma frase curta junto ao botão com ligação para a política.
- Responder ao pedido que o próprio cliente fez assenta, em regra, em diligências pré-contratuais e não pede caixa de consentimento.
- Marketing posterior (campanhas, newsletters, mensagens promocionais) pede consentimento próprio, livre, específico e não pré-seleccionado (RGPD, artigo 7.º; Lei n.º 41/2004 para comunicações electrónicas).
- Não juntes numa só caixa "aceito a política de privacidade" e "quero receber novidades".
- O consentimento de marketing nunca é obrigatório para enviar o pedido.

## Financiamento (lista de controlo)

Confirma com quem trata do crédito no stand e com a instituição parceira.

- Publicidade a crédito que indique taxa ou custo deve trazer a TAEG com um exemplo representativo (regime do crédito aos consumidores, Decreto-Lei n.º 133/2009). A Directiva (UE) 2023/2225 substitui o regime europeu, com aplicação prevista a partir de 20 de Novembro de 2026: confirma que diploma português está em vigor à data da auditoria.
- Um stand que promove crédito na venda pode estar a actuar como intermediário de crédito (Decreto-Lei n.º 81-C/2017). Confirma se o site deve indicar essa qualidade, o número de registo no Banco de Portugal e as instituições com que trabalha.
- Sem "aprovação garantida", "crédito para todos" ou equivalentes.
- Se há um preço "com financiamento" mais baixo do que o preço a pronto, os dois e as condições do primeiro têm de estar claros.

## Urgência e pressão

O regime das práticas comerciais desleais (Decreto-Lei n.º 57/2008, confirma a versão em vigor) trata como enganoso, entre outros, declarar falsamente que um produto só está disponível por um período muito limitado.

- Falha: contadores que reiniciam, "última oportunidade" permanente, "5 pessoas a ver este carro" sem dados reais, "reservado" falso para pressionar.
- Aceitável: campanha com data de fim e condições escritas, ou "vendido" quando a viatura foi vendida.

## Plano de experiências

| Campo | O que escrever |
|---|---|
| Hipótese | O que se acredita e porquê, com a prova da auditoria |
| Alteração | O que muda, em que páginas |
| Métrica principal | Ex.: cliques em WhatsApp e telefone por sessão nas viaturas (GA4) |
| Métrica de controlo | O que não pode piorar: pedidos de proposta, contactos falsos |
| Duração | Semanas completas, sem campanhas novas a meio |
| Decisão | Quando se mantém, quando se reverte |

Exemplo (Stand Exemplo, Leiria, fictício): em telemóvel, o WhatsApp só aparece no fim da página de viatura. Alteração: barra fixa com Ligar, WhatsApp e "Pedir proposta". Métrica principal: cliques em WhatsApp e telefone por sessão nas viaturas. Controlo: pedidos de proposta por formulário. Duração: quatro semanas completas. Decisão: manter se a principal sobe sem queda da de controlo.

Com poucas dezenas de contactos por mês, um teste A/B raramente chega a uma conclusão. Prefere correcções claras de boas práticas (`tel:`, WhatsApp com a viatura, um só botão principal) e medição antes e depois, com as datas registadas, tratada como indicação e não como prova.
