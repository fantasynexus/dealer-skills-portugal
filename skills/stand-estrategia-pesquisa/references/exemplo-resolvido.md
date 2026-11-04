# Exemplo resolvido: Stand Exemplo, Leiria (fictício)

Exemplo para calibrar o nível de detalhe. O stand, os concorrentes e todos os números são inventados para ilustração e não servem de referência para nenhum stand real.

## Situação de partida

- Stand de usados multimarca em Leiria, cerca de 45 viaturas, oficina de manutenção própria, financiamento através de uma financeira parceira, aceita retomas.
- Site de um fornecedor ligado ao programa de stock. Anuncia também no Standvirtual e no OLX.
- Equipa para marketing: o gestor e um comercial, cerca de três horas por semana no total.
- Pedido do gestor: "Quero aparecer mais no Google e ouvi dizer que agora é tudo no ChatGPT."
- Sem auditorias anteriores: **modo A**.

## Triagem (resumo)

| Pilar | Estado | Prova principal | Tipo |
|---|---|---|---|
| 1. Base técnica | Fraco | Duas de duas viaturas abertas têm canónico para a listagem geral; sem dados estruturados de viatura; dados de campo do PageSpeed indisponíveis | Observado (20/10/2026) |
| 2. Google e local | Fraco | Perfil com telefone fixo antigo, diferente do site; sem página de financiamento; Search Console gerido pelo fornecedor do site, sem acesso do stand | Observado e declarado |
| 3. Motores de IA | Fraco | Em quatro perguntas (ChatGPT e Gemini, 20/10/2026, sessão sem conta, Leiria, PT-PT) o stand só aparece quando nomeado, com o telefone antigo; as fontes citadas são o Standvirtual e o Perfil | Observado |
| 4. Reputação | Misto | 112 avaliações, nota 4,6, a mais recente há cinco semanas, menos de metade respondidas; dois concorrentes da zona com avaliações desta semana | Observado (20/10/2026) |

Não verificado: indexação real (sem Search Console), velocidade com dados de campo, origem dos contactos no CRM.

### Verificações do pilar 1, uma a uma

| Verificação | Resultado | Sinal de alerta? |
|---|---|---|
| robots.txt | Permite Googlebot; não menciona bots de IA | Não |
| Páginas de viatura indexáveis | Canónico de duas viaturas aponta para `/viaturas` | Sim (bloqueio 1; extensão por confirmar) |
| Índice | Sem acesso ao Search Console | `N/V` |
| Domínio único e HTTPS | `http://` e `www` redireccionam para a mesma versão | Não |
| Telemóvel | Botão de WhatsApp visível; sem dados de campo no PageSpeed Insights | `N/V` para velocidade |
| Stock legível | Viaturas presentes no código-fonte da listagem | Não |
| Dados estruturados | Só `Organization` na página inicial; nada nas viaturas | Sim |
| Banner de cookies | Permite recusar | Não |

Seis verificações feitas em oito, dois sinais de alerta, um deles bloqueio: `Fraco`.

### Mapa de procura (extracto)

| Intenção | Exemplos de pesquisa | Volume | Responde hoje | Prioridade |
|---|---|---|---|---|
| Descoberta local | "stand de usados Leiria", "carros usados Leiria" | `N/V` | Página inicial e Perfil (com telefone errado) | Alta |
| Retoma | "retoma de carro Leiria", "avaliar carro para retoma" | `N/V` | Formulário sem texto | Média |
| Financiamento | "carros usados com financiamento" | `N/V` | Nada | Alta |
| Oficina | "revisão carro Leiria" | `N/V` | Uma linha na página "Sobre" | Baixa neste trimestre |

### Registo de testes (extracto)

| Data e hora | Superfície | Sessão | Local | Idioma | Pergunta | Resultado |
|---|---|---|---|---|---|---|
| 20/10/2026 10h12 | ChatGPT | Sem conta | Leiria | PT-PT | "O Stand Exemplo em Leiria é de confiança?" | Descreve o stand; telefone antigo; cita Standvirtual |
| 20/10/2026 10h20 | Gemini | Sem conta | Leiria | PT-PT | "Bons stands de usados em Leiria" | Não menciona o stand |

## Bloqueios encontrados

1. **Telefone diferente entre site, Perfil e motores de IA.** Afecta os pilares 2, 3 e 4 de uma vez. Resolve-se em dias e não depende do fornecedor.
2. **Sem acesso ao Search Console.** Sem ele não há linha de base nem confirmação do problema dos canónicos.
3. **Canónicos das viaturas (observado em duas, extensão por confirmar).** Se acontecer em todo o stock, as viaturas não são indexadas como páginas próprias. Precisa de `stand-auditoria-seo` com acesso, não de mais triagem.

## O que o plano não fez

- Não repetiu a auditoria SEO, a do Perfil nem a de IA. Pô-las no roteiro, com o que se espera de cada uma.
- Não escreveu volumes de pesquisa: sem Search Console nem planeador, a coluna ficou `N/V`.
- Não tratou as quatro perguntas em IA como linha de base. A linha de base é a primeira bateria de `stand-visibilidade-ia`.

## Roteiro (extracto)

| Janela | Acção | Pilar | Skill | Responsável | Esforço | Prova de conclusão |
|---|---|---|---|---|---|---|
| Agora | Corrigir telefone no Perfil, no site e nas páginas do stand nos portais | 2, 3, 4 | `stand-auditoria-perfil-google` | Gestor | 2 h | Capturas das quatro fontes com o mesmo número |
| Agora | Pedir ao fornecedor do site acesso de proprietário ao Search Console | 2 | (pedido directo) | Gestor | 1 h | Acesso confirmado em nome do stand |
| 30 dias | Auditoria SEO com acesso, focada em canónicos e páginas de viatura | 1, 2 | `stand-auditoria-seo` | Comercial com o fornecedor | 4 h | Relatório com URLs e pedido ao fornecedor aberto |
| 30 dias | Linha de base em IA com 20 perguntas | 3 | `stand-visibilidade-ia` | Comercial | 3 h | Tabela de resultados datada |
| 30 dias | Rotina de pedido de avaliações na entrega e na oficina | 4 | Link de avaliações do hub, `stand-responder-avaliacoes` | Gestor | 2 h + 15 min/semana | Mensagem aprovada e em uso |
| 60 dias | Página de financiamento com condições e parceiro reais | 2, 3 | `stand-brief-conteudo-aeo` | Gestor | 4 h | Página publicada e indexada |
| 60 dias | Dados estruturados de viatura pedidos ao fornecedor | 1, 3 | `stand-avaliar-site` (para especificar o pedido) | Fornecedor | Do fornecedor | Teste de resultados enriquecidos sem erros em três viaturas |
| 90 dias | Revisão trimestral e nova bateria em IA | Todos | `stand-estrategia-pesquisa` (modo C), `stand-visibilidade-ia` | Gestor | 3 h | Plano dos 90 dias seguintes |

Ficou fora do trimestre: páginas por concelho vizinho (o stand não tem presença real fora de Leiria) e artigos de blogue (sem horas da equipa para os manter).

## Regras de decisão (extracto)

- **Canónicos:** se a 15/12 o fornecedor não tiver corrigido os canónicos, corrigir: escalar por escrito com o relatório da auditoria. Se a 31/01 continuar igual, avaliar alternativas ao fornecedor com prova de que não o consegue fazer.
- **Avaliações:** se em Dezembro entrarem menos avaliações por semana do que o gestor fixou a partir da linha de base de Outubro, corrigir: mudar o momento do pedido (da entrega para a primeira mensagem pós-venda).
- **Página de financiamento:** se 60 dias depois de publicada não tiver impressões no Search Console, corrigir: rever título e ligações internas com `stand-auditoria-seo`. Parar só se a página também não gerar perguntas no WhatsApp.

## Como foi apresentado ao gestor

A primeira linha do resumo executivo foi: "O maior problema não é o ChatGPT: é haver dois números de telefone do stand a circular. Corrigir isso ajuda o Google, os assistentes de IA e os clientes ao mesmo tempo, e faz-se esta semana."
