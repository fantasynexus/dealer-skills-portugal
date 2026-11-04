---
name: stand-auditoria-rastreio-chamadas
description: Auditar o rastreio de chamadas de um stand automóvel em Portugal, desde a origem da visita e o número mostrado até à chamada atendida, ao lead no CRM e à conversão no Google Ads. Usar quando o gestor quer saber de onde vêm as chamadas, se os números dinâmicos do site funcionam, porque é que as chamadas do fornecedor não batem com o CRM, quantas chamadas ficam perdidas sem resposta, antes de contratar ou mudar de fornecedor de call tracking, antes de mudar o número no Perfil Google ou nos portais, ou para rever a gravação de chamadas e o aviso ao cliente. Trata números fixos, móveis e nómadas, telemóveis dos vendedores e o WhatsApp como canal principal.
---

# Auditoria de rastreio de chamadas

Segue cada chamada desde a origem até ao CRM e diz onde se perde a atribuição ou o próprio contacto. Serve qualquer fornecedor de rastreio: não assumas plataformas norte-americanas nem funcionalidades que o fornecedor não confirmou por escrito. Não classifica o conteúdo das conversas (isso é `stand-classificar-chamadas`) e não dá parecer jurídico sobre gravação.

## Antes de começar

1. Escolhe o modo e escreve-o no relatório:
   - **Com acesso:** leitura na plataforma de rastreio, no GA4 e no Ads, e uma exportação do CRM. Permite pontuar e reconciliar.
   - **Público:** só o site e chamadas de teste autorizadas. Configuração da plataforma e CRM ficam `N/V`.
   - **Sem rastreio:** o stand ainda não tem fornecedor. Entrega o inventário de números, o mapa do que hoje se perde e as perguntas para escolher fornecedor; sem nota.
2. Recolhe:
   - todos os números publicados e onde aparecem (site, Perfil de Empresa no Google, Standvirtual, OLX e outros portais, fachada, viaturas, impressos, redes, assinaturas de email);
   - quem atende cada número, reencaminhamentos e telemóveis de vendedores divulgados;
   - contas de WhatsApp e quem as usa;
   - fornecedor, plano, horário, menu de atendimento (IVR), política de gravação e CRM.
3. Pede autorização escrita para os testes: números de teste, janela horária, quem atende, equipa avisada e como os leads de teste ficam marcados.
4. Antes de qualquer teste à gravação, lê a secção de gravação de [references/contexto-portugal.md](references/contexto-portugal.md). Não graves chamadas reais para experimentar.
5. Pára e pergunta quando:
   - te pedem para trocar o número do Perfil Google, dos portais ou do site;
   - a gravação está activa sem aviso audível (é falha crítica: encaminha para o encarregado de protecção de dados antes de continuar os testes);
   - um teste obrigaria a clicar nos anúncios pagos do próprio stand.

## Passos

1. **Inventário dos números.** Uma linha por número: onde aparece, gama (geográfico, móvel, nómada, não geográfico), titular, destino, rastreado ou não. Telemóveis pessoais de vendedores aparecem mascarados (`91x xxx x12`). Resultado: tabela do modelo.
2. **Mapa.** `origem → número mostrado → encaminhamento → plataforma → GA4/Ads → CRM`, um ramo por origem, mais um ramo à parte para o WhatsApp (`clique → conversa → registo no CRM`). Resultado: cada ligação marcada `OK`, `falha` ou `N/V`.
3. **Site.** Compara o número no HTML original com o que aparece no browser em cada origem; confirma que o `tel:` liga para o número mostrado, que os links `wa.me` não são trocados e que o `telephone` do JSON-LD e o rodapé seguem a decisão do stand.
4. **Testes controlados.** Lê [references/testes-e-reconciliacao.md](references/testes-e-reconciliacao.md) e corre a matriz mínima. Resultado: tabela dos testes com `OK`, `falha` ou `N/V` em cada linha.
5. **Configuração.** Na plataforma: regras de origem, conjunto de números, tempo de reserva, número de recurso, encaminhamento, horários, gravação, conservação e integrações.
6. **Pontuação.** Antes de pontuar, lê [references/grelha.md](references/grelha.md). `N/V` e `N/A` saem do denominador; as falhas críticas saem à parte.
7. **Reconciliação.** Preenche o funil de chamadas para o mesmo período e fuso: registadas, únicas, atendidas, perdidas (com e sem devolução), qualificadas, leads no CRM, oportunidades, vendas e conversões no Ads.
8. **Correcções.** Por falha: o que mudar, onde, quem, risco, como reverter e teste de aceitação. Ordena pelo que recupera contactos primeiro (chamadas perdidas, WhatsApp partido) e só depois pelo que melhora a atribuição.

## Contexto português

Lê [references/contexto-portugal.md](references/contexto-portugal.md) antes de recomendar números ou mudanças: gamas de numeração e o que significam para quem liga, telemóveis dos vendedores, WhatsApp, portais, o número do Perfil Google e a consistência do NAP, gravação e aviso ao cliente, e as perguntas a fazer a qualquer fornecedor.

## Ferramentas

- `python3 scripts/extrair_sinais_pagina.py <url>`: corre na página inicial, numa ficha de viatura, na página de contactos e na de oficina. Usa `contactos.telefones`, `contactos.whatsapp`, o telefone do `json_ld`, `scripts_terceiros` (para identificar o script do fornecedor) e `etiquetas`. Como não executa JavaScript, mostra o número do HTML original, antes da troca dinâmica: comparar com o número visto no browser prova se houve troca nessa visita. Não prova que a origem foi bem atribuída, que o conjunto chega, nem que a chamada foi registada.
- No browser: janelas anónimas com os URLs de teste, telemóvel em dados móveis para ver o tempo de troca, DevTools para ver os pedidos ao fornecedor.

## Entrega

Preenche [assets/relatorio.md](assets/relatorio.md): três frases para o gestor, mapa, inventário de números, falhas críticas, nota e cobertura por área, tabela dos testes, funil de reconciliação, correcções priorizadas e o que falta confirmar com o EPD, o fornecedor ou a Google. Separa sempre chamadas registadas, únicas, atendidas, perdidas, qualificadas, leads e vendas.

## Limites

- Não muda números no Perfil Google, nos portais, no site ou no fornecedor sem autorização escrita. Uma troca de número no Perfil pode afectar a consistência com directórios e portais e levar a nova revisão pela Google (confirmar).
- Não grava chamadas reais para testar e não usa contactos de clientes; mascara os telemóveis pessoais dos vendedores.
- Não clica nos anúncios do próprio stand: custa dinheiro e suja os dados. Simula a origem com parâmetros no URL.
- Não recomenda gravar sem aviso, nem tirar o aviso para não assustar clientes. As referências legais são lista de controlo; a decisão é do EPD ou de um jurista.
- Não usa gravações para avaliar colaboradores um a um.
- Nunca infla "chamadas de vendas": chamada não é lead e lead não é venda.

## Skills relacionadas

- `stand-auditoria-ga4-google-ads`: o lado do GA4, das conversões do Ads e da importação do CRM.
- `stand-classificar-chamadas`: quantas das chamadas atendidas são mesmo de vendas.
- `stand-auditoria-perfil-google`: antes de mexer no telefone do Perfil.
- `stand-auditoria-cta`: botões de chamada e WhatsApp no site.
- `stand-responder-leads`: devolver chamadas perdidas e seguir os contactos.
