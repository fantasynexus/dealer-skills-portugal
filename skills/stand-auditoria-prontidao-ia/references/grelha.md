# Grelha de prontidão para IA

Lê isto antes de pontuar. São 17 dimensões em cinco grupos, com três a cinco pontos cada. Os pontos ★ formam a versão curta (um por dimensão). Os pontos marcados **crítico** são bloqueios quando valem 0.

## Regras de pontuação

Para cada ponto, a coluna "Vale 2 quando" diz o que tem de estar verdadeiro, com prova. A partir daí:

- **1:** parte disso existe, ou existe sem prova, ou depende de uma só pessoa, ou só em parte do stand.
- **0:** verificou-se que não existe, ou o responsável confirma que ninguém controla.
- **`N/V`:** não se conseguiu verificar. **`N/A`:** não se aplica a este stand.

Nota de uma dimensão: soma dos pontos verificados a dividir por duas vezes o número de pontos verificados. Um ponto `N/V` ou `N/A` não entra.

## Como perguntar

1. **Pergunta simples e concreta.** "Alguém verificou contactos duplicados no CRM nos últimos seis meses?" e não "Como está a qualidade dos dados?".
2. **Pede a prova sem acusar.** "Para dar 2 preciso de ver a configuração; pode mostrar uma captura com os nomes tapados?"
3. **Diz a nota e o motivo, e segue.** "Fica 1: existe, mas só a Ana sabe fazer e não está escrito. Para 2, basta escrever o passo a passo e nomear quem substitui."

Armadilhas que dão no máximo 1, ou 0:

- "Temos uma coisa parecida": pede o documento ou a configuração. Sem isso, no máximo 1.
- "O fornecedor trata disso": o stand consegue ver o que o fornecedor faz? Sem relatório ou acesso, no máximo 1.
- "Já fizemos isso": o passado não conta. A grelha mede o que é verdade hoje.
- "Toda a gente sabe": cultura sem nada escrito vale no máximo 1.
- "Os resultados mostram que sim": um bom número não prova que o processo existe. Pontua o processo.

## Grupo A. Fundação

### 1. Objectivos e casos de uso

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 1.1 ★ Problema concreto | Documento ou email | O caso de IA está ligado a um problema medido (por exemplo, contactos fora de horas sem resposta), com o número actual e o resultado esperado escritos |
| 1.2 Prioridade entre casos | Lista | Há até cinco casos possíveis ordenados por valor e risco, com o critério |
| 1.3 O que fica com pessoas | Lista aprovada | Está escrito que decisões não se automatizam (preço final, valor de retoma, crédito, reclamações) |

### 2. Patrocínio da gestão e responsáveis

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 2.1 ★ Patrocinador | Nome e função | Um sócio-gerente ou director responde pelo uso de IA e tem acompanhamento marcado na agenda |
| 2.2 Dono por fluxo | Lista | Cada ferramenta ou fluxo tem uma pessoa nomeada no stand (não "o fornecedor") |
| 2.3 Orçamento e tempo | Aprovação | Há valor ou horas aprovados que incluem formação e revisão humana, não só a licença |

### 3. Qualidade de stock, clientes e leads

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 3.1 ★ Ficha de viatura coerente | Cinco viaturas na fonte (programa de stock ou DMS) comparadas com o site e um portal | Preço, quilómetros, ano, combustível e equipamento coincidem nas cinco |
| 3.2 Duplicados e contactos antigos | Relatório ou contagem, sem exportar contactos | Houve verificação nos últimos seis meses, com data e acção tomada |
| 3.3 Origem e estado dos leads | Captura do CRM com dados tapados | Cada contacto tem origem (portal, site, telefone, WhatsApp, presencial) e estado com motivo de perda, e a amostra está preenchida |

### 4. CRM/DMS e integrações

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 4.1 ★ Inventário de sistemas | Lista escrita | Todos os sistemas com dados de clientes, leads, viaturas ou dinheiro estão listados, com dono e tipo de dados (stock, CRM, site, portais, WhatsApp, telefone, email, contabilidade, financeiras) |
| 4.2 Mapa de integrações | Tabela ou esquema | Diz o que passa de onde para onde e como (automático, ficheiro, à mão), e duas pessoas dão a mesma resposta |
| 4.3 Acesso aos próprios dados | Contrato ou exportação de teste | O stand já exportou stock e contactos num formato aberto e sabe o que custa dar acesso a um terceiro |

## Grupo B. Protecção

### 5. Consentimentos, retenção e direitos RGPD

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 5.1 ★ **crítico** Fundamento e informação | Política de privacidade, registo de actividades de tratamento | Para os dados que a IA vai tratar há fundamento identificado e a informação aos titulares cobre essa finalidade e os fornecedores envolvidos |
| 5.2 Consentimento de marketing | Campo no CRM, texto do formulário | Email, SMS e WhatsApp de marketing têm consentimento registado (data, canal, texto) e as oposições são aplicadas (Lei n.º 41/2004; confirmar versão em vigor) |
| 5.3 Prazos de conservação | Política e prova de eliminação | Há prazos para leads não convertidos, gravações e conversas, e prova de que se aplicam |
| 5.4 Pedidos dos titulares | Procedimento e registo | Acesso, rectificação, apagamento e oposição têm responsável e prazo conhecidos |
| 5.5 Avaliação de impacto | AIPD ou nota fundamentada | Para tratamentos de risco elevado (por exemplo, gravação e análise sistemática de chamadas) foi feita a avaliação de impacto, ou está escrito por quem e porque não é exigível |

### 6. Fornecedores, subcontratantes e transferências

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 6.1 ★ **crítico** Contrato de subcontratação | Contrato assinado (artigo 28.º do RGPD) | Cada fornecedor de IA que trata dados pessoais por conta do stand tem contrato que cobre o tratamento |
| 6.2 Subcontratantes e localização | Anexo do contrato ou página do fornecedor | O stand sabe quem são os subcontratantes e onde ficam os dados; transferências para fora do EEE têm garantia identificada |
| 6.3 Uso para treino | Termos ou definição da conta | Está escrito se os dados do stand servem para treinar modelos, e está desligado ou aceite por escrito |
| 6.4 Inventário de ferramentas de IA | Lista | Cada ferramenta tem dono, dados que toca, custo e data de renovação, incluindo extensões e funções de IA dentro de outros programas |

### 7. Acessos, MFA, cópias e resposta a incidentes

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 7.1 ★ **crítico** Autenticação multifactor | Capturas das definições | Está activa no email, CRM, programa de stock, contas de anúncios e ferramentas de IA com dados de clientes |
| 7.2 Contas pessoais e saídas | Lista de utilizadores, último caso de saída | Não há contas partilhadas e a saída de um colaborador retira acessos no próprio dia |
| 7.3 Cópias de segurança | Registo de restauro | Um restauro foi testado, com data, nos últimos doze meses |
| 7.4 Plano de incidente | Documento | Diz quem decide, quem contacta clientes e quem avalia a notificação à CNPD (o RGPD prevê 72 horas em certos casos; confirmar) |

## Grupo C. Controlo

### 8. Supervisão humana e possibilidade de corrigir

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 8.1 ★ **crítico** Revisão antes de sair | Fluxo ou configuração | O que a IA produz para clientes (respostas, anúncios, propostas) tem revisão humana ou limites configurados e testados |
| 8.2 Passagem para pessoa | Regras escritas | Diz quando a conversa passa a uma pessoa (pedido do cliente, reclamação, preço, crédito, retoma) e em quanto tempo |
| 8.3 Corrigir e desligar | Procedimento testado | Alguém no stand corrige uma resposta errada e desliga a ferramenta no mesmo dia, sem depender do fornecedor |

### 9. Exactidão, alucinações e testes

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 9.1 ★ Fonte de verdade | Configuração e teste | A ferramenta responde a partir dos dados do stand (stock, horário, condições) e não de conhecimento geral |
| 9.2 Bateria de testes | Lista de testes e resultados | Antes de lançar, testaram-se perguntas difíceis: preço final, garantia, retoma, crédito, e tentativas de manipular a ferramenta para aceitar preços ou condições absurdas |
| 9.3 Limites de promessa | Configuração e teste | A ferramenta não consegue fechar preço, aprovar crédito, garantir disponibilidade nem prazos de entrega |

### 10. Transparência perante clientes e colaboradores

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 10.1 ★ Cliente sabe que é IA | Captura do chat, guião, mensagem inicial | O cliente é informado de que fala com um sistema automático (Regulamento (UE) 2024/1689, artigo 50.º; confirmar data de aplicação) |
| 10.2 Imagens e textos gerados | Política escrita | Está proibido alterar com IA o estado real da viatura (danos, cor, equipamento) e há regra para assinalar conteúdo gerado quando exigível |
| 10.3 Colaboradores informados | Comunicação escrita | A equipa sabe que dados do seu trabalho a IA trata (gravações, métricas) e para quê; ver limites do Código do Trabalho na referência legal |

### 11. Formação e literacia em IA

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 11.1 ★ Formação registada | Registo de presenças ou conteúdo | Quem usa IA teve formação adequada à função, com data (Regulamento (UE) 2024/1689, artigo 4.º; confirmar alcance) |
| 11.2 Regra para ferramentas gratuitas | Regra escrita e ferramenta aprovada | Está escrito o que nunca se cola em contas pessoais (dados de clientes, propostas, margens) e há uma alternativa aprovada |
| 11.3 Chefias sabem orientar | Conversa com a chefia | Quem coordena sabe explicar o fluxo, os limites e o que fazer quando a IA erra, sem chamar o fornecedor |

## Grupo D. Operação

### 12. Medição de leads, vendas e produtividade

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 12.1 ★ Linha de base | Relatório com data | O número que a IA deve mexer (tempo de primeira resposta, contactos fora de horas, chamadas perdidas, horas em descrições) foi medido antes |
| 12.2 Poucos indicadores | Lista | Três a cinco indicadores por fluxo, cada um com fonte |
| 12.3 Regra de decisão | Documento datado | Está escrito antes do arranque quando se expande, corrige ou pára |
| 12.4 Ligação a vendas | Relatório do CRM | Um contacto consegue seguir-se até venda ou perda |

### 13. Processos de vendas

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 13.1 ★ Distribuição de leads | Regra no CRM ou escrita | Diz quem atende cada contacto e o que acontece se não responder |
| 13.2 Primeira resposta e seguimento | Padrão escrito | Canais, tentativas e prazos definidos (ver `stand-responder-leads`) |
| 13.3 Retoma e preço | Regras escritas | Há critérios de avaliação de retoma e de desconto; nenhum valor final sai sem pessoa |
| 13.4 Financiamento | Lista de quem pode informar | Só quem está habilitado fala de condições de crédito (Decreto-Lei n.º 81-C/2017; confirmar) e a IA não simula nem aprova |

### 14. Pós-venda e oficina

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 14.1 ★ Marcações coerentes | Teste em dois canais | Telefone, site e WhatsApp dão a mesma disponibilidade (`N/A` sem oficina) |
| 14.2 Garantia e reclamações | Registo | Pedidos de garantia e reclamações ficam registados com prazo e resposta (Decreto-Lei n.º 84/2021; confirmar) |
| 14.3 Passagem da entrega ao pós-venda | Fluxo escrito | O cliente novo recebe contactos definidos depois da entrega (ver `stand-onboarding-cliente`) |

### 15. Marketing e conteúdos

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 15.1 ★ Anúncios gerados revistos | Cinco anúncios comparados com a ficha | Textos gerados por IA são revistos contra a ficha antes de publicar, e os cinco batem certo |
| 15.2 Linguagem do stand escrita | Documento de voz | Há regras de linguagem e alegações proibidas (ver `stand-posicionamento`) |
| 15.3 Campanhas reconciliadas | Relatório | Contactos das plataformas batem com o CRM dentro de uma margem conhecida (ver `stand-auditoria-ga4-google-ads`) |
| 15.4 Listas e audiências | Registo de consentimento | Contactos só são carregados em plataformas de anúncios com fundamento e informação adequados |

## Grupo E. Risco e continuidade

### 16. Risco de discriminação em crédito, emprego ou perfilagem

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 16.1 ★ **crítico** Sem decisões automáticas | Descrição dos fluxos | Nenhuma decisão com efeito significativo (crédito, preço individual, recusa de venda, recrutamento) é tomada só pela máquina (RGPD, artigo 22.º) |
| 16.2 Recrutamento e avaliação de pessoas | Avaliação prévia escrita | Ferramentas de triagem de candidatos ou avaliação de colaboradores foram avaliadas antes de usar (podem ser de risco elevado no Regulamento (UE) 2024/1689; confirmar) |
| 16.3 Segmentação | Critérios escritos | Campanhas e prioridades não usam categorias especiais de dados nem substitutos óbvios delas |

### 17. Continuidade e saída do fornecedor

| Ponto | Prova aceitável | Vale 2 quando |
|---|---|---|
| 17.1 ★ Saída prevista | Contrato | Diz como e em quanto tempo os dados são devolvidos e apagados |
| 17.2 Plano manual | Procedimento | Se a ferramenta parar, alguém sabe continuar o trabalho à mão (quem atende o WhatsApp, quem responde aos leads) |
| 17.3 Dependência controlada | Contrato e exportação | Preço de renovação e fidelização conhecidos; dados exportáveis num formato aberto |
