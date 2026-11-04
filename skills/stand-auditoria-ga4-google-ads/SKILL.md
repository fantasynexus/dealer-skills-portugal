---
name: stand-auditoria-ga4-google-ads
description: Auditar a medição de um stand automóvel em Portugal (GA4, Google Ads, Google Tag Manager, consentimento de cookies e importação de conversões offline do CRM) e reconciliar, etapa a etapa, o que as plataformas reportam com os leads e as vendas confirmados. Usar quando os números do Google não batem com o CRM, o Ads mostra mais ou menos contactos do que a equipa recebeu, há dúvidas antes de aumentar o orçamento de anúncios, mudou a agência ou o site, há formulários, simulador de financiamento ou WhatsApp que não aparecem no GA4, se suspeita de conversões duplicadas ou se quer enviar vendas do CRM para o Google Ads. Serve também para definir os eventos e parâmetros de um site novo antes de o lançar.
---

# Auditoria de GA4 e Google Ads

Verifica se o que o GA4 e o Google Ads contam corresponde a contactos e vendas reais do stand. O resultado principal é a **tabela de reconciliação por etapa**, com cada diferença explicada ou assumida como "por explicar". A nota de 100 pontos diz onde está a falha; não substitui a tabela. Esta skill não gere campanhas, não avalia anúncios nem lances e não altera nada nas contas.

## Antes de começar

1. Pergunta o objectivo e escolhe o caminho:
   - **auditoria completa** (todos os passos);
   - **só reconciliação** (passos 1, 6 e 7, com a grelha só nas áreas que explicam diferenças);
   - **site novo** (desenha a medição com a taxonomia e entrega o plano de eventos e o teste de aceitação; sem nota).
2. Escolhe o modo e escreve-o no relatório:
   - **Com acesso:** papel só de leitura em GA4, Google Ads e GTM, mais uma exportação do CRM. É o único modo que permite reconciliar.
   - **Público:** só o site. Verificas etiquetas, consentimento e disparos no browser; a configuração interna fica `N/V`.
   - **Documental:** capturas e exportações enviadas pelo stand ou pela agência. Vale o que mostram, com data visível.
3. Recolhe: domínios e plataforma do site; IDs (`G-`, `GTM-`, conta Ads); quem gere e quem é titular de cada conta; CRM ou software de gestão usado; formulários, chat e simuladores de terceiros; telefones e WhatsApp publicados; portais onde anuncia; período a reconciliar e fuso horário.
4. Do CRM pede só contagens ou linhas com ID interno, data, origem e etapa. Recusa nomes, emails, telefones, NIF ou matrículas: não são precisos para reconciliar.
5. Pára e pergunta quando:
   - o período ou o fuso não podem ser iguais nas fontes;
   - não há definição escrita de "lead válido", "oportunidade" e "venda" (propõe uma a partir de [references/reconciliacao.md](references/reconciliacao.md) e pede aprovação);
   - te pedem para publicar, pausar ou criar algo nas contas.

## Passos

1. **Mapa do fluxo.** Desenha, por canal, `origem → página → acção → evento GA4 → conversão Ads → registo no CRM → etapa → venda`. Inclui os canais que não passam pelo site (Standvirtual, OLX e outros portais, formulários de leads do Google, redes sociais, presencial). Resultado: cada ligação marcada como verificada, falhada ou `N/V`.
2. **Inventário.** Lista etiquetas no site, eventos GA4 dos últimos 30 dias, eventos-chave, acções de conversão do Ads (origem, primária ou secundária, contagem, janela, modelo) e tags e accionadores do GTM. Resultado: as tabelas do modelo preenchidas.
3. **Testes controlados.** Com autorização e com a equipa avisada:
   - abre o site com `?utm_source=auditoria&utm_medium=teste&utm_campaign=AAAA-MM-DD`;
   - envia um formulário de teste por tipo (proposta, test drive, retoma, financiamento, contacto) com dados fictícios;
   - clica em telefone, WhatsApp, email e mapa, e abre o simulador de financiamento;
   - repete um envio com `?gclid=TESTE_AUDITORIA` só para ver se o identificador chega ao CRM (nunca para importar).

   Resultado: um envio igual a um evento, visto no DebugView ou no separador Network, e o lead de teste no CRM com origem e identificadores. Pede que os leads de teste fiquem marcados como teste para saírem da reconciliação.
4. **Consentimento.** Em janela anónima, testa recusar, aceitar e não responder. Resultado: o que dispara e que cookies existem antes e depois da escolha.
5. **Pontuação.** Antes de pontuar, lê [references/grelha.md](references/grelha.md). O que não verificaste é `N/V` e sai do denominador: nota = pontos obtidos ÷ pontos verificados × 100; cobertura = pontos verificados ÷ 100. As falhas críticas aparecem à parte, seja qual for a nota.
6. **Reconciliação.** Lê [references/reconciliacao.md](references/reconciliacao.md) e preenche as tabelas por etapa e por canal para o mesmo período e fuso. Cada diferença tem causa com prova ou fica em "por explicar".
7. **Plano de correcção.** Por falha: o que mudar, onde (caminho no interface), quem faz, risco, como reverter e teste de aceitação. Ordena pelo efeito na reconciliação, não pelo número de pontos.

## Taxonomia de eventos

Para rever os eventos existentes ou propor novos, usa [references/taxonomia-eventos.md](references/taxonomia-eventos.md): nomes em snake_case, parâmetros de viatura e de origem, eventos-chave e acções de conversão recomendadas. Não renomeies eventos que já têm histórico sem um plano de transição: os relatórios e as conversões importadas partem.

## Ferramentas

- `python3 scripts/extrair_sinais_pagina.py <url>`: corre na página inicial, numa listagem, numa ficha de viatura e em cada página com formulário. Usa `etiquetas` (IDs GA4, GTM e Ads, píxel da Meta, sinais de Consent Mode e CMP), `formularios` (campos, obrigatórios, caixas pré-seleccionadas), `contactos` e `scripts_terceiros`. Não executa JavaScript: o que o GTM injecta depois de carregar não aparece, por isso a falta de um ID `G-` no resultado não prova que o GA4 falta. Também não prova que um evento dispara, que o consentimento é respeitado nem que a conversão conta no Ads.
- No browser: DevTools (Network com os filtros `collect` e `googleadservices`, Application > Cookies), pré-visualização do GTM, DebugView do GA4 e Tag Assistant. São estes que confirmam disparos.

## Entrega

Preenche [assets/relatorio.md](assets/relatorio.md), por esta ordem: reconciliação e diferenças explicadas; falhas críticas; nota e cobertura por área; mapa do fluxo; inventários; plano de correcção com testes de aceitação; o que ficou `N/V` e o que falta confirmar. Para o gestor, abre com três frases: quantos contactos as plataformas dizem, quantos o CRM confirma, e a correcção que mais reduz a diferença.

## Limites

- Não publica, pausa nem cria nada em GTM, GA4 ou Ads sem autorização explícita e sem identificar a versão anterior para reverter.
- Não copia emails, telefones, nomes, NIF, matrículas ou IDs de cliente para o relatório; trabalha com contagens e IDs internos.
- Não recomenda medir antes do consentimento nem enviar dados pessoais ao Google sem base legal, CMP a funcionar e termos de dados do cliente aceites na conta. Conversões optimizadas (enhanced conversions) e importação com email ou telefone cifrados só depois de validadas pelo encarregado de protecção de dados. Diplomas a confirmar na versão em vigor: RGPD e Lei n.º 41/2004.
- Não usa percentagens quando períodos, fusos ou definições não são comparáveis; mostra os absolutos e diz porquê.
- Não inventa valores de lead ou de venda para o Ads nem usa margens reais sem autorização do gestor.
- Não promete que corrigir a medição aumenta vendas nem cita médias do sector como factos.

## Skills relacionadas

- `stand-auditoria-cta`: se os botões e formulários existem, se funcionam e se convencem.
- `stand-auditoria-rastreio-chamadas`: números dinâmicos, chamadas atendidas e conversões de chamada.
- `stand-classificar-chamadas`: quantas chamadas são mesmo de vendas.
- `stand-analisar-trafego-ia`: visitas vindas de assistentes de IA no GA4.
- `stand-responder-leads`: o que acontece ao lead depois de chegar ao CRM.
