---
name: stand-por-onde-comecar
description: Escolher a skill certa, ou uma sequência curta de skills, para o que o gestor de um stand de automóveis em Portugal quer resolver. Usar quando o pedido é vago ("quero mais clientes", "o que faço com IA no meu stand", "por onde começo", "o site não traz contactos"), quando várias skills servem ou para montar um plano de 30 dias com as skills desta biblioteca.
---

# Por onde começar

Transforma um objectivo do stand em, no máximo, três próximos passos, cada um com a skill que o executa. Não faz o trabalho das outras skills: escolhe, explica porquê e passa a vez.

## Antes de começar

Faz no máximo três perguntas, só as que mudam a escolha:

1. **O que quer melhorar primeiro?** Vender mais depressa o stock, receber mais contactos, responder melhor aos que chegam, aparecer no Google, aparecer nas respostas de IA, medir de onde vêm as vendas, trazer clientes antigos de volta.
2. **O que já existe?** Site próprio ou só portais; Perfil de Empresa no Google; GA4 ou outra medição; CRM ou DMS; quem trata das redes sociais.
3. **Quanto tempo há esta semana?** Uma hora, um dia, ou um projecto de várias semanas.

Se o gestor já disse o que quer em concreto ("escreve o anúncio deste carro"), não perguntes nada: encaminha directamente.

## Passos

1. **Classifica o pedido** num dos percursos de [references/percursos.md](references/percursos.md). Quando cabe em dois, escolhe o que dá resultado mais cedo.
2. **Escolhe até três skills** pela ordem em que devem correr. A primeira tem de ser possível com o que o stand já tem; se exigir acesso que não existe (GA4, consola do Perfil Google), diz o que pedir e a quem.
3. **Justifica cada escolha numa frase**, ligada ao que o gestor disse. Nada de "porque é boa prática".
4. **Confirma se as skills estão instaladas.** Se não estiverem, dá o comando de instalação (ver abaixo) em vez de improvisar o trabalho sem elas.
5. **Passa a vez:** com a aprovação do gestor, invoca a primeira skill com o pedido de exemplo do catálogo, já adaptado ao stand.

O catálogo completo, com o que cada skill pede e entrega, está em [references/catalogo.md](references/catalogo.md). Lê-o quando hesitas entre duas.

## Atalhos frequentes

| O gestor diz | Começa por |
|---|---|
| "Escreve o anúncio deste carro" | `stand-escrever-anuncio` |
| "Chegou um contacto do Standvirtual, o que respondo?" | `stand-responder-leads` |
| "Deixaram-nos uma avaliação má" | `stand-responder-avaliacoes` |
| "Preciso de publicações para o Instagram" | `stand-publicar-redes-sociais` |
| "Os carros estão parados há muito tempo" | `stand-rever-anuncios-viaturas` |
| "Não aparecemos no Google" | `stand-auditoria-perfil-google` |
| "O ChatGPT não fala de nós" | `stand-auditoria-aeo` |
| "Não sei de onde vêm as vendas" | `stand-auditoria-ga4-google-ads` |
| "Quero trazer clientes antigos de volta" | `stand-campanha-retoma` |
| "Quero usar IA mas não sei se estamos prontos" | `stand-auditoria-prontidao-ia` |

## Ferramentas grátis do hub

Quando o gestor não sabe por onde pegar, a [Nota de visibilidade online](https://onepilot.app/hub/ferramentas/visibilidade) dá em 40 segundos uma nota de 0 a 100 do perfil Google, avaliações, concorrência e site, e serve de ponto de partida para escolher o percurso. A [Análise de stock](https://onepilot.app/hub/ferramentas/analise-stock) faz o mesmo para o preço e a antiguidade dos anúncios no Standvirtual. São opcionais.

## Instalar uma skill que falta

Qualquer agente: "Instala a skill `<nome>` de https://github.com/fantasynexus/dealer-skills-portugal/tree/main/skills/`<nome>`".

Com Node.js: `npx skills add fantasynexus/dealer-skills-portugal --skill <nome>`.

## Entrega

```markdown
## O que fazer primeiro

1. **<Nome da skill>** (`<nome>`): <porquê, ligado ao que o gestor disse>. Precisa de: <o que ter à mão>.
2. ...
3. ...

Começo pela primeira? Pedido: "<pedido adaptado ao stand>"
```

## Limites

- Nunca mais de três passos. Uma lista com dez skills é um catálogo, não uma recomendação.
- Não faz uma versão rápida do trabalho de outra skill "para adiantar": encaminha.
- Não recomenda comprar software, contratar agências nem ferramentas pagas.
- Não promete resultados (mais vendas, primeiro lugar no Google, presença nas respostas de IA).
