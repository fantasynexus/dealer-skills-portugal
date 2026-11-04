---
name: stand-pagina-comparacao
description: Criar uma página de comparação honesta para o site de um stand português, com cada dado citado e datado. Compara dois modelos concorrentes (ex. Clio ou 208 usado, Qashqai ou Kuga), duas opções de compra (usado ou novo, eléctrico ou híbrido, gasóleo ou gasolina) ou o stand e um concorrente nomeado. Usar quando os clientes perguntam "qual é melhor", pesquisam "X vs Y" ou "vale a pena um eléctrico usado", para SEO, motores de IA e apoio à equipa comercial. Só usa especificações com fonte e data, diz para quem cada opção faz sentido e não inventa vantagens nem denigre marcas ou concorrentes.
---

# Página de comparação

Escreve uma página que ajuda um comprador a decidir entre duas opções, com uma tabela em que cada valor tem fonte e data. Uma página por comparação. É conteúdo para o site do stand e serve também à equipa comercial quando o cliente hesita.

Fora do âmbito: briefs para outros conteúdos (`stand-brief-conteudo-aeo`), a posição e o tom do stand (`stand-posicionamento`), anúncios de viaturas (`stand-escrever-anuncio`), medir se a página é citada por motores de IA (`stand-visibilidade-ia`).

## Antes de começar

1. Escolhe o tipo com o gestor:
   - **A. Modelo contra modelo:** dois modelos que os clientes comparam (ex.: Renault Clio ou Peugeot 208 usado).
   - **B. Decisão de compra:** duas formas de resolver a mesma necessidade (usado ou novo; eléctrico ou híbrido; gasóleo ou gasolina).
   - **C. Stand contra stand:** o stand e um concorrente nomeado, quando os clientes os comparam de facto.
2. Pede a pergunta como os clientes a fazem (ao telefone, no WhatsApp, no stand), o público (família, primeiro carro, empresa), as viaturas em stock ligadas ao tema e o que o stand oferece com prova (garantia, preparação, financiamento).
3. Fixa o âmbito antes de recolher dados. Em A, geração, anos e motorizações: um Clio de 2013 e um de 2021 são carros diferentes. Em B, o perfil de utilização (quilómetros por ano, se carrega em casa). Em C, os URLs dos dois stands e a sobreposição real de mercado.
4. Pára e pergunta quando o âmbito não está definido, quando o gestor quer afirmar algo sem prova ou quando não há fontes acessíveis para metade dos critérios (propõe outro tema). Recusa comparar com um particular ou com uma pessoa.

## Passos

1. **Escreve a pergunta da página numa frase**, com o âmbito: "Para [público], [opção A] ou [opção B], considerando [âmbito]?" Resultado: pergunta aprovada pelo gestor.
2. **Escolhe 8 a 12 critérios** do tipo, em [references/criterios-e-fontes.md](references/criterios-e-fontes.md). Só os que mudam a decisão daquele público.
3. **Recolhe os dados.** Cada célula leva valor, unidade, versão a que se refere, fonte e data de consulta, pela hierarquia de fontes da referência. Célula sem fonte fica "não foi possível confirmar", ou o critério sai.
4. **Aplica a regra de justiça.** Cada opção ganha onde os dados o mostram, e a página diz para quem a outra faz mais sentido. Em C, o concorrente vence ou é mais forte em pelo menos uma dimensão quando os dados o mostram, e recebe uma revisão factual antes de lhe atribuíres fraquezas.
5. **Faz as contas com premissas à vista.** Custos de utilização só com premissas escritas (quilómetros por ano, preço da energia com data, tarifário). Nunca um "poupa X € por ano" sem a conta.
6. **Escreve a página** com o modelo [assets/modelo-pagina.md](assets/modelo-pagina.md): abertura que responde à pergunta, resposta rápida, tabela, "quando faz sentido" para cada opção, aprofundamento só das diferenças que contam, perguntas frequentes, metodologia e ligação ao stock real.
7. **Revê** com a lista de verificação do modelo: números com fonte e data, "melhor" só com critério, nada que denigra marcas ou stands, interesse comercial do stand declarado.
8. **Junta os anexos:** título e meta descrição, ligações internas, dados estruturados, guião curto para a equipa comercial, registo de fontes e data da próxima revisão.

Para ver o resultado de cada passo num caso completo, lê [references/exemplo-resolvido.md](references/exemplo-resolvido.md).

## Ferramentas

- [Análise de stock](https://onepilot.app/hub/ferramentas/analise-stock) do hub: preços pedidos e dias anunciados no Standvirtual para viaturas semelhantes. Cita como "preços pedidos em anúncios semelhantes, [data]"; não são preços de venda.
- [Nota de visibilidade online](https://onepilot.app/hub/ferramentas/visibilidade) do hub: no tipo C, avaliações e concorrentes da zona, com data.
- Simulador do IUC no Portal das Finanças, para o custo fiscal de uma viatura concreta (ver a referência).
- Para padrões de avaliações reais no tipo C, `stand-analisar-avaliacoes`.

## Entrega

Uma página pronta a publicar, segundo [assets/modelo-pagina.md](assets/modelo-pagina.md), com:

- intenção e público;
- abertura e resposta rápida que dizem para quem cada opção faz sentido;
- tabela critério / opção A / opção B / fonte e data;
- secções só para diferenças materiais, e contas com premissas;
- perguntas frequentes, metodologia e limitações;
- acção para ver o stock, pedir proposta ou marcar visita;
- título, meta descrição, ligações internas e dados estruturados;
- guião curto para a equipa comercial responder sem atacar ninguém;
- registo de fontes e agenda de revisão: mensal para preços, tarifas, incentivos e avaliações; a cada novo ano-modelo ou mudança de lei, para o resto.

## Limites

- Não escrevas especificações, consumos, autonomias, preços, custos ou classificações sem fonte citada e datada. A memória do modelo não é fonte.
- Não compares valores de normas diferentes (WLTP e NEDC) nem de mercados diferentes sem o dizer na própria célula.
- Não afirmes fiabilidade ou avarias ("o modelo X avaria mais") sem estudo nomeado, com ano, país e método.
- Não prometas benefícios fiscais, incentivos ou poupanças: indica a fonte oficial e manda confirmar à data.
- Não denigras marcas, modelos ou concorrentes, não uses logótipos de marcas, não recolhas informação privada nem te faças passar por cliente.
- Não uses `Review`, `AggregateRating` ou classificações próprias nos dados estruturados como se fossem avaliações independentes. Evita "melhor" sem critério verificável.
- Não prometas disponibilidade: liga para o stock real e escreve "confirmar disponibilidade".
- A publicidade comparativa tem regras próprias: segue a lista de controlo da referência e, na dúvida, encaminha para um jurista.
