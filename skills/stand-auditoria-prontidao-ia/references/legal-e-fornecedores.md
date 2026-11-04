# Contexto legal e perguntas ao fornecedor

Lê isto quando pontuas os grupos B, C e E, e sempre que o motivo da auditoria é uma ferramenta concreta. É uma lista de controlo operacional, não um parecer. Confirma a versão em vigor de cada diploma em fonte oficial (Diário da República para a legislação portuguesa, EUR-Lex para o direito da União, site da CNPD para orientações) e encaminha as dúvidas para o encarregado de protecção de dados ou para um jurista.

## Diplomas a confirmar

### RGPD: Regulamento (UE) 2016/679

| Artigo | Tema | O que verificar no stand | Dimensão |
|---|---|---|---|
| 5.º | Princípios | A ferramenta recebe só os dados necessários e não os guarda mais tempo do que o preciso | 3, 5 |
| 6.º | Licitude | Há fundamento identificado para cada finalidade nova (por exemplo, analisar conversas) | 5.1 |
| 13.º e 14.º | Informação | A política de privacidade e os avisos cobrem a finalidade e os fornecedores | 5.1, 10.1 |
| 15.º a 21.º | Direitos | Acesso, rectificação, apagamento e oposição chegam também aos dados na ferramenta | 5.4 |
| 22.º | Decisões automatizadas | Nenhuma decisão com efeito significativo é tomada só pela máquina | 16.1 |
| 25.º | Protecção desde a concepção | As opções por defeito da ferramenta são as mais restritivas | 8, 9 |
| 28.º | Subcontratante | Há contrato com cada fornecedor que trata dados por conta do stand | 6.1 |
| 30.º | Registo de actividades | O tratamento novo está no registo | 5.1 |
| 32.º | Segurança | Acessos, cifra e cópias adequados ao risco | 7 |
| 33.º e 34.º | Violação de dados | Há quem avalie a notificação à CNPD e aos titulares nos prazos previstos | 7.4 |
| 35.º | Avaliação de impacto | Feita, ou dispensada por escrito, para tratamentos de risco elevado | 5.5 |
| 37.º a 39.º | Encarregado de protecção de dados | Confirmar se o stand é obrigado a designar e quem é | 5 |
| 44.º a 49.º | Transferências | Dados fora do EEE têm garantia identificada | 6.2 |

### Lei n.º 58/2019

Assegura a execução do RGPD em Portugal e tem regras próprias, por exemplo sobre relações laborais. Confirma os artigos aplicáveis a gravações e a dados de colaboradores.

### Lei n.º 41/2004

Comunicações electrónicas: envio de marketing por email e SMS e armazenamento de informação no equipamento do utilizador (cookies). Tem regras próprias para clientes existentes. Confirma a versão em vigor antes de concluir sobre campanhas ou etiquetas no site.

### Regulamento (UE) 2024/1689 (Regulamento da IA)

- **Papel do stand:** quando usa uma ferramenta de terceiros, é normalmente "responsável pela implantação", não fornecedor. Confirma o papel se o stand desenvolve ou altera a ferramenta.
- **Artigo 4.º, literacia em IA:** obrigação de medidas para que quem usa IA tenha conhecimentos suficientes. Confirma a data de aplicação e o alcance.
- **Artigo 5.º, práticas proibidas:** confirma que nenhuma ferramenta usa técnicas manipuladoras ou explora vulnerabilidades.
- **Artigo 50.º, transparência:** informar as pessoas de que interagem com um sistema de IA e assinalar certos conteúdos gerados. Confirma a data de aplicação: o calendário tem sido alvo de propostas de alteração.
- **Anexo III, risco elevado:** inclui avaliação da solvabilidade de pessoas singulares e sistemas de recrutamento e gestão de trabalhadores. Obrigações e datas a confirmar.

### Código do Trabalho

Os meios de vigilância à distância não podem servir para controlar o desempenho do trabalhador. Antes de usar gravações de chamadas, transcrições ou métricas geradas por IA para avaliar pessoas, confirma com um jurista o regime aplicável e as obrigações de informação e consulta dos trabalhadores.

### Decreto-Lei n.º 57/2008 (práticas comerciais desleais)

O que a ferramenta diz ao cliente é comunicação do stand. Respostas enganosas sobre preço, disponibilidade, garantia ou condições são responsabilidade do stand. Confirma a versão em vigor.

### Decreto-Lei n.º 84/2021 (garantias na venda de bens)

Respostas automáticas sobre garantia têm de bater com a lei e com o contrato. Confirma os prazos aplicáveis a usados na versão em vigor; não os ponhas na ferramenta sem validação.

### Crédito: Decreto-Lei n.º 81-C/2017 e regime do crédito aos consumidores

O primeiro regula os intermediários de crédito: confirma quem no stand pode informar sobre crédito. A publicidade e a informação sobre crédito aos consumidores têm regras próprias (incluindo a TAEG). A Directiva (UE) 2023/2225 substitui o regime europeu anterior; confirma a transposição e o diploma em vigor antes de deixar uma ferramenta falar de condições.

## Casos que mostram o risco

- Fora de Portugal, utilizadores levaram o chatbot de um concessionário a "aceitar" vender uma viatura por um valor simbólico. A defesa é o ponto 9.3: a ferramenta não fecha preço.
- Também fora de Portugal, um tribunal responsabilizou uma companhia aérea pela informação errada que o seu chatbot deu a um cliente. O que a ferramenta promete, o stand pode ter de cumprir.

Usa estes casos para explicar o risco, não como precedente jurídico em Portugal.

## Perguntas ao fornecedor

Para cada resposta, pede o documento. Resposta sem documento vale como declarada (no máximo 1 no ponto correspondente).

| Tema | Pergunta | Prova a pedir | Ponto |
|---|---|---|---|
| Dados | Que dados do stand a ferramenta recebe, e quais pode deixar de receber? | Descrição técnica | 3, 5.1 |
| Dados | Onde ficam guardados e durante quanto tempo? | Documentação, contrato | 5.3, 6.2 |
| Dados | Os dados do stand ou das conversas servem para treinar modelos? Como se desliga? | Termos, definição | 6.3 |
| Contrato | Há contrato de subcontratação (artigo 28.º do RGPD)? | Contrato | 6.1 |
| Contrato | Quem são os subcontratantes, incluindo o fornecedor do modelo? | Lista | 6.2 |
| Contrato | Há transferência para fora do EEE? Com que garantia? | Cláusulas | 6.2 |
| Segurança | Tem autenticação multifactor e contas por utilizador? | Captura | 7.1, 7.2 |
| Segurança | Há registo de quem viu e alterou o quê? | Exemplo de registo | 7 |
| Segurança | Como e em quanto tempo avisa o stand de um incidente? | Cláusula | 7.4 |
| Funcionamento | De onde vêm as respostas: dados do stand ou conhecimento geral? | Demonstração | 9.1 |
| Funcionamento | O que a ferramenta não pode fazer (preço final, crédito, prazos)? Como se garante? | Configuração e teste | 9.3 |
| Funcionamento | Como informa o cliente de que fala com um sistema automático? | Captura | 10.1 |
| Controlo | Como passa a conversa a uma pessoa, e o que vê essa pessoa? | Demonstração | 8.2 |
| Controlo | Quem no stand pode corrigir respostas e desligar a ferramenta? | Procedimento | 8.3 |
| Controlo | Posso correr a minha bateria de testes antes de lançar? | Ambiente de teste | 9.2 |
| Medição | Que relatório mostra o que a ferramenta fez, conversa a conversa? | Exemplo de relatório | 12 |
| Medição | Como liga os contactos ao CRM do stand? | Integração | 4.2, 12.4 |
| Saída | Como e em quanto tempo devolve e apaga os dados se o stand sair? | Cláusula | 17.1 |
| Saída | Em que formato exporta conversas e contactos? | Exportação de teste | 17.3 |
| Preço | Quanto custa a renovação e há fidelização? | Proposta | 17.3 |

Promessas de resultado ("mais vendas", "o dobro de marcações") sem a linha de base do próprio stand não são prova. Regista-as e pede o método.

## Dados que nunca entram sem autorização, minimização e contrato

- bases de clientes completas ou exportações do CRM;
- cópias de documentos de identificação e de carta de condução;
- dados de crédito, rendimentos, recibos de vencimento, IBAN;
- matrículas ou números de quadro associados a pessoas;
- gravações de chamadas;
- dados de saúde ou de outras categorias especiais (por exemplo, em pedidos de adaptação de viatura);
- preços de compra, margens e condições das financeiras: não são dados pessoais, mas são informação do negócio.

## Ferramentas gratuitas e contas pessoais

- Confirma nos termos de cada serviço, na data da auditoria, se os dados introduzidos servem para treino e se há opção para o desligar. Contas pessoais e contas empresariais costumam ter termos diferentes.
- Sem regra escrita e alternativa aprovada, assume que a equipa já usa contas pessoais e regista-o no ponto 11.2.
- Usos sem risco relevante: textos genéricos, ideias, revisão de linguagem, sem dados de clientes nem do negócio.

## Quando chamar o encarregado de protecção de dados ou um jurista

- análise sistemática de chamadas, conversas ou comportamento de clientes;
- qualquer uso de IA em crédito, preço individual, recrutamento ou avaliação de colaboradores;
- transferências para fora do EEE sem garantia clara;
- dúvida sobre se é obrigatória uma avaliação de impacto;
- um incidente com dados pessoais;
- carregamento de contactos em plataformas de anúncios.
