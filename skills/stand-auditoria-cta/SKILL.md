---
name: stand-auditoria-cta
description: Auditar as chamadas à acção do site de um stand automóvel português (botões, telefone, WhatsApp, formulários, chat) e propor textos e correcções. Usar quando o site tem visitas mas poucos contactos, há botões a mais ou a competir, o telefone não liga no telemóvel, o WhatsApp não diz de que carro se trata, os formulários pedem dados a mais, ou há dúvidas sobre botões de pedir proposta, marcar visita ou test drive, simular financiamento, avaliar retoma ou marcar oficina. Entrega inventário por página, nota de 100 pontos com cobertura, textos de substituição em PT-PT e plano de testes.
---

# Auditoria de chamadas à acção

Avalia a facilidade de um comprador dar o próximo passo em cada página: ligar, falar no WhatsApp, pedir proposta, marcar visita, simular financiamento, avaliar a retoma ou marcar oficina. Sem padrões manipuladores e sem recolher mais dados do que o necessário.

Fora do âmbito, com a skill certa:

- velocidade e técnica do site: `stand-avaliar-site`;
- qualidade do anúncio da viatura: `stand-rever-anuncios-viaturas`;
- configuração de GA4 e Google Ads: `stand-auditoria-ga4-google-ads`;
- números de rastreio de chamadas: `stand-auditoria-rastreio-chamadas`;
- resposta e seguimento dos contactos que chegam: `stand-responder-leads`.

## Antes de começar

1. Pede o URL, as páginas que mais importam, o processo comercial (o stand prefere visita, chamada, WhatsApp ou proposta por escrito?), os canais que a equipa de facto atende e em que horário, e se há CRM.
2. Pergunta se podes submeter formulários de teste e com que contacto. Sem autorização, a entrega fica `N/V`.
3. Pergunta se há acesso a GA4, GTM ou CRM para confirmar eventos e chegada dos contactos. Sem ele, a medição fica `N/V`, excepto o que se vê no browser.
4. Escolhe o modo:
   - **Uma página:** análise de cada CTA dessa página.
   - **Amostra (por omissão):** início, listagem, três viaturas, financiamento, retoma, oficina ou pós-venda e contactos.
   - **Site inteiro:** descobre as páginas pelo sitemap, agrupa por modelo de página, pontua um representante por modelo e regista as excepções.
5. Pára e pergunta se o processo não bate com o site (ex.: o site oferece WhatsApp mas ninguém o atende). O problema não é o botão e a recomendação muda.

## Passos

1. **Inventaria.** Em cada página, regista cada CTA: texto exacto, tipo (botão, ligação, `tel:`, WhatsApp, formulário, chat), destino, posição, prioridade visual (principal, secundária, terciária), se se vê sem scroll em telemóvel, evento de medição e dados pedidos. Começa por `python3 scripts/extrair_sinais_pagina.py <url>` e completa no browser. Resultado: tabela de inventário por página.
2. **Classifica a página.** Compara o que existe com o esperado para esse tipo de página em [references/padroes-por-pagina.md](references/padroes-por-pagina.md).
3. **Testa em telemóvel.** A 360 × 740 px em emulação e, se possível, num iPhone e num Android reais: toque no telefone, abertura do WhatsApp, teclado certo em cada campo, barra fixa, banner de cookies e chat por cima dos botões.
4. **Percorre cada caminho até ao fim.** Com autorização, até à confirmação; sem ela, até ao botão de envio, e a entrega fica `N/V`. Verifica foco de teclado, mensagens de erro, validação que não apaga o que foi escrito, confirmação, e se a viatura e a origem seguem para o CRM. Não carregues em "Enviar" com o formulário vazio para ver a validação: pode criar um contacto falso.
5. **Pontua cada página.** Antes de pontuar, lê [references/grelha.md](references/grelha.md). Nota da página = pontos obtidos ÷ pontos verificados × 100; nota da amostra = média das páginas pontuadas; cobertura = pontos verificados ÷ pontos aplicáveis.
6. **Separa padrões de casos.** O mesmo problema em todas as viaturas é do modelo de página (fornecedor do site), não de cada anúncio. Agrupa assim e indica o responsável provável.
7. **Escreve os textos de substituição.** PT-PT, curtos, com verbo e o resultado para o cliente, e só com promessas que o stand cumpre. Pergunta antes de escrever um prazo de resposta.
8. **Prioriza e planeia testes.** Correcções por impacto e esforço. Cada experiência leva hipótese, alteração, métrica principal, métrica de controlo, duração e critério de decisão. Com pouco tráfego, diz que um teste A/B não terá conclusão e propõe medição antes e depois, com datas.
9. **Entrega** com o modelo [assets/relatorio-cta.md](assets/relatorio-cta.md).

## Ferramentas

- `python3 scripts/extrair_sinais_pagina.py <url-ou-ficheiro.html>`: lista telefones, emails e ligações de WhatsApp; formulários com campos, tipos, obrigatórios e caixas pré-seleccionadas; e etiquetas de medição. Não executa JavaScript: botões criados depois do carregamento, chats e formulários de terceiros embebidos não aparecem. Não prova que um formulário entrega nem que um evento dispara.
- DevTools do Chrome em modo dispositivo, para posição, sobreposição e tipos de teclado. Com acesso, Tag Assistant ou GA4 DebugView para eventos.
- Para reescrever o texto do anúncio, `stand-escrever-anuncio`; para um diagnóstico técnico mais largo, `stand-avaliar-site`.

## Entrega

Segue [assets/relatorio-cta.md](assets/relatorio-cta.md):

- frase de abertura com o problema que mais custa, nota e cobertura;
- inventário por página e nota por dimensão;
- conflitos de hierarquia e problemas em telemóvel;
- padrões da amostra, com o responsável provável;
- textos de substituição, antes e depois;
- correcções por impacto e plano de experiências;
- o que ficou `N/V` e o que é preciso para o testar.

## Limites

- Sem urgência falsa, contadores ou "últimas unidades" inventados, caixas pré-seleccionadas, consentimento agregado ou recusa escondida.
- Financiamento não sugere aprovação garantida nem esconde condições. Se o site mostra prestação, verifica a lista de controlo de financiamento em [references/padroes-por-pagina.md](references/padroes-por-pagina.md).
- Não envies dados reais nem contactes o stand sem autorização. Nunca submetas formulários em sites de concorrentes.
- Não prometas aumentos de conversão: as recomendações são hipóteses até serem testadas.
- Não alteres o site, o GTM nem o CRM. Propões; quem tem acesso aplica.
- As referências legais são listas de controlo, não pareceres. Na dúvida, encaminha para o encarregado de protecção de dados ou para um jurista.
