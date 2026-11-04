---
name: stand-fluxos-email
description: Criar ou rever os fluxos de email automáticos de um stand de automóveis em Portugal, ligados a eventos reais do CRM ou do DMS, como resposta a contacto de portal ou site, seguimento de proposta e de test-drive, confirmação de marcação, boas-vindas após entrega, documentos em falta, lembrete de manutenção, orçamento de oficina não aceite, satisfação, chamada técnica, fim de financiamento, retoma, aniversário de compra, cliente inactivo, recomendação e eventos. Usar quando o gestor fala em "emails automáticos", "automação", "sequência de emails", "newsletter para clientes", "lembretes de revisão", "plataforma de email", "CRM que envia emails" ou quer saber se os emails que já envia respeitam o RGPD. Entrega especificação por fluxo, emails completos em PT-PT, mapa de automação, plano de testes, métricas e uma lista de controlo de consentimento e oposição, com mensagens transaccionais separadas de marketing.
---

# Fluxos de email para stands

Desenha automações que disparam com eventos que o CRM ou o DMS regista de forma fiável, e escreve os emails. Não envia nem configura a plataforma. Não usa o modelo do carrinho abandonado: comprar um carro leva semanas, passa por visita e test-drive, e a insistência automática estraga a relação.

Fronteiras com outras skills:

- Primeiros 90 dias após a entrega, com telefone e WhatsApp: `stand-onboarding-cliente`. Se estiver em uso, os fluxos 5 e 7 cedem-lhe o lugar nesse período.
- Campanha com prazo para renovar viaturas: `stand-campanha-retoma`. O fluxo 13 é a versão permanente e leve.
- Primeira resposta humana a um contacto: `stand-responder-leads`. O fluxo 1 só confirma a recepção.

## Modos

- **A. Programa:** escolher e especificar o conjunto de fluxos.
- **B. Fluxo específico:** um ou dois fluxos pedidos pelo gestor.
- **C. Revisão:** o stand já envia emails. Pede os textos, as regras de envio e um exemplo de cada email recebido, verifica-os contra a lista de controlo e entrega as correcções.

## Antes de começar

1. Que plataforma envia (CRM, DMS, plataforma de email) e se aplica supressões e limites de frequência globais. Se não aplica, isso é um pré-requisito, não um detalhe.
2. Que eventos ficam registados com data e de forma fiável. Pede um exemplo de registo com dados fictícios ou anonimizados, nunca a base.
3. Que consentimentos existem, por canal, e onde está a prova (data, origem, texto).
4. Quem assina os emails e quem lê as respostas.
5. Que fluxos já estão em produção e quais o gestor quer manter.

Pontos de decisão:

- **Evento não fiável:** o fluxo fica de fora. Três fluxos certos valem mais do que dez com dados errados.
- **Sem prova de consentimento:** só fluxos transaccionais, de serviço e pré-contratuais até haver base para marketing.
- **Sem limite global de frequência na plataforma:** o programa arranca com os transaccionais e um único fluxo de marketing, até o limite existir.
- **Pára e pergunta** antes de escrever um fluxo que use dados de crédito, saúde ou outras categorias sensíveis, ou que prometa preço, prestação, campanha ou elegibilidade.

## Passos

1. **Inventário de eventos.** Tabela evento, fonte, fiável (`sim`, `não`, `N/V`), quem regista. Resultado: a lista dos fluxos possíveis.
2. **Escolha.** Lê [references/catalogo-fluxos.md](references/catalogo-fluxos.md) e escolhe os fluxos que os eventos permitem, pela ordem de prioridade do catálogo. Arranque sugerido: 3 a 5 fluxos. Resultado: lista com a razão de cada escolha e de cada exclusão.
3. **Natureza.** Classifica cada fluxo como transaccional ou de serviço, pré-contratual a pedido do cliente, ou marketing, com [references/consentimento-e-envio.md](references/consentimento-e-envio.md). Conteúdo misto conta como marketing.
4. **Especificação.** Preenche [assets/especificacao-fluxo.md](assets/especificacao-fluxo.md) por fluxo: objectivo, público, gatilho, condições de entrada, exclusões, cadência, condição de saída, responsável, campos necessários, eventos de medição.
5. **Emails.** Escreve a partir de [assets/emails.md](assets/emails.md): remetente reconhecível, duas variantes de assunto, preheader, corpo curto, um só CTA, contactos, rodapé certo para a natureza do fluxo e versão em texto simples. Campo que pode faltar tem variante sem ele.
6. **Regras globais.** Limite de frequência, prioridades, exclusões mútuas e supressões comuns, da secção 4 de [references/consentimento-e-envio.md](references/consentimento-e-envio.md).
7. **Testes.** Plano antes de activar: endereços de teste, campos vazios, ligações, oposição a funcionar e a chegar a todas as plataformas, leitura em telemóvel, autenticação do domínio.
8. **Métricas e revisão jurídica.** Uma medida principal por fluxo, até lead, venda ou oficina, e a lista dos fluxos que o DPO ou um jurista têm de rever.

No modo C, os passos 1 a 3 aplicam-se aos fluxos existentes e cada problema encontrado leva a correcção ao lado, com o texto novo.

## Ferramentas

Opcionais; o trabalho faz-se sem elas.

- [Link de avaliações do Google](https://onepilot.app/hub/ferramentas/link-avaliacoes): link directo para a caixa de avaliação, para o fluxo 10.
- As UTM das ligações para o site seguem o plano de medição de `stand-auditoria-ga4-google-ads`.

## Entrega

[assets/especificacao-fluxo.md](assets/especificacao-fluxo.md) preenchido: mapa de automação, eventos e dados, especificação e emails de cada fluxo, regras globais, plano de testes, métricas, lista de controlo de consentimento e oposição com estado por item, fluxos para revisão jurídica e itens a confirmar.

## Limites

- Não envia, não activa automações, não importa listas, não mexe na plataforma.
- Não inventa stock, preço, prestação, TAEG, campanha, intervalo de manutenção, recolha ou elegibilidade.
- Não mete promoções em emails transaccionais nem chama "informação de serviço" a marketing.
- Não presume que o interesse legítimo ou a relação de clientela bastam para todos os canais: a base de cada fluxo confirma-se com o DPO.
- Suprime vendidos, reclamações abertas, contactos inválidos, oposições e excesso de frequência.
- Não pede a base de clientes nem a copia para o documento: a lógica de audiência descreve-se sem dados pessoais.
- Não envia para a avaliação pública só quem respondeu bem ao inquérito.
- As referências legais são lista de controlo: diploma citado e versão em vigor por confirmar.
