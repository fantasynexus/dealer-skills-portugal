---
name: stand-seo-multilingue
description: Decidir, planear, auditar ou corrigir versões do site de um stand de automóveis em Portugal noutras línguas (inglês, espanhol, francês ou outra) sem prejudicar o mercado principal em português. Usar quando o gestor pergunta se vale a pena traduzir o site, quando há clientes estrangeiros residentes, emigrantes, turistas ou procura da zona fronteiriça com Espanha, ou quando as páginas em inglês não aparecem no Google, o hreflang, os canónicos ou o selector de língua estão partidos, ou o site usa tradução automática. Cobre arquitectura de URLs, hreflang (pt-PT, en, es, fr, x-default), páginas prioritárias, termos de venda de automóveis em cada língua, stock traduzido, atendimento e medição por língua.
---

# SEO multilingue para stands

O mercado principal de um stand em Portugal é quem pesquisa em português de Portugal. Outra língua só entra quando há procura comprovada, alguém que atende nessa língua e quem mantenha as páginas: uma tradução abandonada ou automática transmite menos confiança do que um site claro só em português. Esta skill decide se vale a pena, desenha a versão certa ou corrige a que existe. O SEO do site em português é de `stand-auditoria-seo`.

## Antes de começar

Pede:

1. URL do site, plataforma e línguas que já existem ou que se querem.
2. Quem na equipa atende em cada língua, por telefone, WhatsApp e no stand, e em que horário.
3. Contactos noutras línguas nos últimos 6 a 12 meses: quantos e por que canal. Só contagens, sem dados pessoais.
4. Acesso ao Search Console e ao GA4.
5. Quem mantém preços, stock e textos legais, e se a plataforma traduz o stock.
6. Onde fica o stand e que clientes estrangeiros o gestor já reconhece.

Escolhe o modo e escreve-o no topo da entrega:

- **Decidir:** o gestor pergunta se vale a pena. Termina com uma de três respostas: não agora, piloto ou versão completa.
- **Desenhar:** a decisão está tomada. Entrega mapa de URLs, especificação técnica e plano.
- **Auditar:** há versões publicadas. Pontua com [references/grelha.md](references/grelha.md).
- **Corrigir:** algo está partido (indexação, canónicos, hreflang, selector, tradução automática). Entrega a sequência de correcções.

Pontos de paragem:

- Ninguém atende na língua: a resposta é "não agora", seja qual for a procura. Diz o que mudaria a decisão.
- O pedido é traduzir um texto concreto: isso pede um falante competente, não esta skill. Podes preparar o glossário e o briefing para quem traduz.

## Passos

1. **Mede a procura por língua.** Lê [references/publicos-e-procura.md](references/publicos-e-procura.md). Search Console por país e por consultas noutras línguas; GA4 por idioma do navegador e país; contactos por língua no CRM ou no WhatsApp; avaliações noutras línguas no perfil Google. Fonte e data em cada sinal. Identifica o público: residentes estrangeiros, emigrantes, turistas, zona fronteiriça, brasileiros e outros lusófonos.
2. **Mede atendimento e manutenção:** quem atende, quem revê os textos, quem actualiza as páginas quando o stock muda.
3. **Decide com a matriz** da mesma referência (procura, atendimento, manutenção). Escreve a decisão e o que a mudaria. Emigrantes que pesquisam em português pedem uma página em português, não uma tradução.
4. **Desenha ou verifica a arquitectura.** Lê [references/especificacao-tecnica.md](references/especificacao-tecnica.md). O português fica onde está, normalmente na raiz; cada língua nova numa subpasta (`/en/`, `/es/`, `/fr/`). Não migres o português para `/pt/` só por simetria: muda todos os URLs, obriga a redireccionamentos e arrisca posições sem ganho nenhum.
5. **Verifica cada conjunto de páginas equivalentes:** canónico próprio, hreflang recíproco com códigos válidos, `x-default` quando faz sentido, estado 200, selector que liga à página equivalente, navegação na mesma língua, metadata e dados estruturados na língua da página.
6. **Prioriza o conteúdo** pelo que vende ao público em causa: contactos e localização, como comprar sendo estrangeiro ou a partir do estrangeiro, stock (dados da mesma fonte), retoma, financiamento, garantia, pós-venda.
7. **Prepara os termos** com o glossário de partida da referência de públicos e manda-os rever por falante nativo.
8. **Define a medição:** Search Console por pasta, GA4 por pasta e evento de contacto, CRM com a língua do contacto.
9. **Entrega** no modelo do modo: [assets/relatorio-auditoria.md](assets/relatorio-auditoria.md) para auditar; [assets/plano-linguas.md](assets/plano-linguas.md) para decidir, desenhar ou corrigir.

## Ferramentas

- `python3 scripts/extrair_sinais_pagina.py <url-ou-ficheiro.html>` em cada versão de uma página: devolve idioma, canónico, lista de hreflang, título, meta descrição, estado HTTP, Open Graph e JSON-LD. Compara as listas de hreflang das versões para ver a reciprocidade. **Não prova:** hreflang declarado no sitemap ou no cabeçalho HTTP `Link` (não os lê), etiquetas injectadas por JavaScript, o canónico escolhido pela Google (inspecção de URL no Search Console) nem a qualidade da tradução.
- O Search Console já não tem o relatório de segmentação internacional: os erros de hreflang confirmam-se com o script, à mão ou com um rastreador.
- Perfil Google: um só perfil por instalação, seja qual for o número de línguas; a descrição pode dizer em que línguas o stand atende, se for verdade. A auditoria do perfil é de `stand-auditoria-perfil-google`; respostas a avaliações noutras línguas, de `stand-responder-avaliacoes`; primeira resposta a contactos noutras línguas, de `stand-responder-leads`.

## Entrega

- **Decidir:** decisão por língua (não agora, piloto, versão completa), sinais com fonte e data, o que mudaria a decisão e quando voltar a ver.
- **Desenhar:** mapa de URLs, especificação técnica (códigos, método, canónicos, selector, sitemap), páginas por prioridade, glossário para o tradutor, roteiro de 30, 60 e 90 dias com responsáveis.
- **Auditar:** nota e cobertura por área, problemas com URL e prova, correcções por ordem.
- **Corrigir:** diagnóstico, sequência de correcções por dependência (canónicos antes do hreflang, conteúdo antes de pedir indexação), riscos e como confirmar cada uma.

## Limites

- Não recomendas uma língua sem procura comprovada, sem quem atenda e sem quem mantenha.
- Não assumes que inglês é obrigatório, nem que uma tradução automática cria procura.
- Nunca publicas nem recomendas publicar tradução automática sem revisão de um falante competente. As políticas de spam da Google tratam conteúdo produzido em escala sem revisão como abuso.
- A informação ao consumidor e os documentos do negócio existem sempre em português (Lei n.º 24/96 e Decreto-Lei n.º 238/86; confirmar a redacção em vigor). Traduções de financiamento, garantia, privacidade e contrato são apoio e passam por revisão jurídica antes de publicar.
- Não recomendas redireccionar automaticamente por IP ou idioma do navegador, nem um segundo perfil Google por língua.
- Preços, quilómetros e disponibilidade não se traduzem à mão: vêm da mesma fonte que a versão portuguesa.
- Não alteras o site nem publicas nada sem autorização explícita.
