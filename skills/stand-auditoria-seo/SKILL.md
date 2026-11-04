---
name: stand-auditoria-seo
description: Auditar o SEO tradicional do site de um stand de automóveis em Portugal, ou seja, a presença na lista de resultados do Google. Usar quando o gestor diz que o site não aparece no Google, perdeu tráfego ou posições, mudou de site, de domínio ou de plataforma, ou quer rever indexação e Search Console, títulos, canibalização entre páginas, páginas de viatura e listagens de stock, viaturas vendidas (404, 410 ou 301), filtros e paginação, sitemap, dados estruturados, pesquisa local ("stand" mais concelho, "carros usados" mais distrito, marca e modelo usado, eléctricos usados, retoma) e Core Web Vitals. Funciona com acesso ao Search Console ou só com o que é público. Não mede citações em motores de IA.
---

# Auditoria SEO para stands

Mede se o Google consegue encontrar, perceber e escolher as páginas do site do stand para as pesquisas que trazem compradores, e diz o que corrigir primeiro. Não mede citações em assistentes de IA (`stand-auditoria-aeo`, `stand-visibilidade-ia`) nem substitui a avaliação técnica completa do site (`stand-avaliar-site`).

## Antes de começar

Pede, por esta ordem. Sem o primeiro ponto, pára e pergunta.

1. URL do site e quem o mantém (plataforma ou fornecedor).
2. Concelhos e zonas onde o stand vende de facto, e a morada de cada instalação.
3. Stock típico: marcas, segmentos (usados, eléctricos, comerciais, importados), volume aproximado, e se há oficina, retoma e financiamento.
4. Acesso ao Search Console e ao GA4, ou exportações. Mudanças recentes: site novo, domínio, plataforma, quedas de tráfego e as datas.
5. Três a cinco concorrentes que o gestor sente que lhe tiram clientes.

Decide o modo e escreve-o no topo do relatório:

- **Com acesso:** há Search Console. É o único modo que prova indexação, consultas e canibalização.
- **Público:** só o que qualquer pessoa vê. Indexação e consultas ficam `N/V`; a pesquisa `site:` não prova indexação.
- **Diagnóstico de queda:** o pedido é "perdemos tráfego". Antes de pontuar, compara no Search Console o desempenho por página e por consulta antes e depois da queda, e cruza com o que mudou no site nessas datas.

Se o pedido é só sobre o Perfil de Empresa, usa `stand-auditoria-perfil-google`. Se o problema está nas versões noutras línguas, usa `stand-seo-multilingue` para o detalhe.

## Passos

1. **Define a amostra** (8 a 12 URLs): início, listagem geral, uma listagem de marca ou combustível, três páginas de viatura (uma recente, uma com semanas, uma vendida ou retirada se houver), retoma, financiamento, contactos ou localização, oficina se existir, um artigo. Regista cada URL com a data.
2. **Recolhe os sinais de cada página** com o script (ver Ferramentas) e guarda o JSON. O que depender de JavaScript confirma-se no navegador antes de se dar como ausente.
3. **Confirma no Search Console** (modo com acesso): relatório de páginas e motivos de exclusão, sitemaps, inspecção de URL das viaturas da amostra (canónico escolhido pela Google), desempenho por consulta e por página nos últimos 3 e 12 meses.
4. **Constrói o mapa de procura.** Lê [references/pesquisa-portuguesa.md](references/pesquisa-portuguesa.md). Para cada intenção (stand mais concelho, carros usados mais zona, marca e modelo, combustível, retoma, financiamento) indica a página dona, a fonte e a data. Sem fonte, a consulta é hipótese, nunca volume.
5. **Procura canibalização:** consultas com duas ou mais páginas a alternar no Search Console; sem acesso, títulos e H1 que repetem a mesma intenção. Para cada grupo decide a página dona e o destino das outras (fundir, 301 ou mudar o foco).
6. **Testa o stock rotativo.** Lê [references/stock-rotativo.md](references/stock-rotativo.md). Abre uma viatura vendida, uma reservada, um filtro profundo, uma ordenação e a página 2 de uma listagem; regista o estado HTTP e o que cada uma mostra.
7. **Verifica o local:** nome, morada, telefone e horário iguais no site e no Perfil de Empresa; páginas por localização só onde há instalação real. A auditoria do perfil em si pertence a `stand-auditoria-perfil-google`.
8. **Pontua.** Lê [references/grelha.md](references/grelha.md). Cada critério leva prova (URL, captura, JSON, relatório do Search Console com período) ou `N/V`. Calcula a nota sobre o verificado e a cobertura.
9. **Prioriza** por impacto na procura que traz contactos e depois por esforço. Diz quem executa cada acção: o stand, o fornecedor do site ou quem carrega o stock.
10. **Entrega** no modelo [assets/relatorio.md](assets/relatorio.md).

## Ferramentas

- `python3 scripts/extrair_sinais_pagina.py <url-ou-ficheiro.html>` devolve estado HTTP, `x-robots-tag`, título, meta descrição, meta robots, canónico, idioma, hreflang, H1, JSON-LD (Car, Vehicle, Offer, AutoDealer e outros), contactos e imagens sem `alt`. Corre-o em cada URL da amostra. **Não prova** que a página está indexada, que canónico a Google escolheu, nem posições. Não executa JavaScript: dados estruturados ou ligações injectados depois do carregamento não aparecem, por isso "não tem schema" só vale depois de confirmado no teste de resultados enriquecidos da Google ou na inspecção de URL.
- Search Console, PageSpeed Insights (dados de campo do Chrome só existem com tráfego suficiente) e o teste de resultados enriquecidos da Google.
- [Nota de visibilidade online](https://onepilot.app/hub/ferramentas/visibilidade): em menos de um minuto mostra o perfil Google, as avaliações, os concorrentes da zona, a velocidade do site e palavras-chave. Poupa a recolha da parte local; não substitui o Search Console.

## Entrega

Relatório no modelo [assets/relatorio.md](assets/relatorio.md): resumo para o gestor em cinco linhas, nota e cobertura por área, problemas com URL e prova, mapa de procura, canibalizações, regras de stock rotativo testadas, plano de 90 dias com responsáveis e plano de medição (Search Console, GA4 e origem do contacto no CRM).

Adapta o detalhe a quem lê: o gestor quer as cinco acções que mais pesam; o fornecedor do site quer os URLs, o comportamento actual e o esperado. Descrições únicas das viaturas são trabalho de `stand-escrever-anuncio`; conteúdos novos que o plano pedir podem seguir para `stand-brief-conteudo-aeo`; o plano que junta SEO, perfil e IA é de `stand-estrategia-pesquisa`.

## Limites

- Não atribuis volume, posição ou tráfego sem fonte e data. Números de ferramentas de palavras-chave dizem-se estimativas.
- Não prometes subidas nem prazos de resultados.
- Não alteras o site, o robots.txt, o sitemap nem o Search Console. Propões; só com autorização explícita alguém executa.
- Não misturas SEO com citações em IA.
- Não recomendas páginas por concelho com texto trocado, avaliações inventadas nos dados estruturados, nem manter como disponível uma viatura vendida.
- Não inventas dados de viaturas para preencher dados estruturados: o que falta vem do DMS ou fica por confirmar.
- Não pedes dados de clientes. Para medir contactos basta a contagem por origem.
