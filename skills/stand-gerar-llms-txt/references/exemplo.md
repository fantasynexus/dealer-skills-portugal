# Exemplo resolvido: Stand Exemplo, Leiria (fictício)

Stand, site, URLs, datas e resultados são inventados para mostrar o método.
O site `stand-exemplo.pt` não existe.

## Entradas

Confirmado pelo gestor:

- usados multimarca, ligeiros de passageiros e comerciais, em Leiria desde 2009;
- clientes sobretudo de Leiria, Marinha Grande, Batalha e Pombal;
- retoma (incluindo carros com crédito por pagar), financiamento através de financeiras parceiras, garantia nos usados, oficina de manutenção multimarca;
- site em WordPress, com acesso do gestor ao painel de alojamento;
- só português; a página `/en` foi uma tradução automática feita há anos;
- bloqueou o GPTBot de propósito e quer manter esse bloqueio.

## Passo 1: acesso

```text
python3 scripts/verificar_bots_ia.py https://stand-exemplo.pt \
  --caminho / --caminho /viaturas --caminho /retoma --caminho /llms.txt
```

Leitura (ilustrativa): robots.txt lido; o grupo `*` permite tudo; o GPTBot
tem grupo próprio com `Disallow: /`; OAI-SearchBot, ChatGPT-User,
Claude-SearchBot, PerplexityBot, Googlebot e Bingbot permitidos em todos os
caminhos; um sitemap declarado. O bloqueio do GPTBot é de treino e é decisão
do gestor: não impede o avanço. Se os agentes de pesquisa estivessem
bloqueados, o trabalho parava aqui com essa recomendação.

## Passo 2: páginas candidatas

Origem: menu, rodapé e o sitemap declarado. Cada URL foi aberto.

| URL | Estado | Decisão | Motivo |
|---|---|---|---|
| `/` | 200 | Fora | O H1 e o resumo já dizem quem é o stand. |
| `/viaturas` | 200 | Dentro | Lista de stock com preço e quilómetros em texto. |
| `/viaturas?combustivel=electrico` | 200 | Fora | Filtro; existe a página estável `/viaturas/electricos`. |
| `/viaturas/electricos` | 200 | Dentro | Categoria com página própria. |
| `/viaturas/comerciais` | 200 | Dentro | Categoria com página própria. |
| `/viaturas/renault-clio-1-0-tce-2021-1234` | 200 | Fora | Ficha individual: sai quando a viatura é vendida. |
| `/retoma` | 200 | Dentro | Texto sobre avaliação e documentos. |
| `/compramos-o-seu-carro` | 301 para `/retoma` | Fora | Duplicado. |
| `/financiamento` | 200 | Dentro | Explica o pedido de simulação. |
| `/garantia` | 200 | Dentro | Prazo e cobertura por escrito. |
| `/entrega` | 404 | Fora | Está no menu mas dá erro: problema para o gestor. |
| `/oficina` | 200 | Dentro | Serviço que existe. |
| `/sobre` | 200 | Dentro | História e equipa. |
| `/contactos` | 200 | Dentro | Morada, horário, telefone, mapa. |
| `/blog` | 200 | Fora | Arquivo com o último artigo de há dois anos. |
| `/blog/documentos-para-comprar-carro-usado` | 200 | `Optional` | Guia revisto em 2026. |
| `/blog/comprar-electrico-usado` | 200 | `Optional` | Guia útil e actual. |
| `/blog/promocao-black-friday-2023` | 200 | Fora | Promoção caducada. |
| `/en` | 200 | Fora | Tradução automática desactualizada. |
| `/politica-de-privacidade` | 200 | `Optional` | Útil a quem vai deixar contactos. |
| Perfil no Standvirtual | 200 | Fora | Outro domínio; vai para o `sameAs` do JSON-LD. |

## Passo 3: problemas a resolver antes de publicar

| Problema | O que fazer | Quem |
|---|---|---|
| `/entrega` no menu dá 404 | Repor a página ou tirar a ligação do menu. Fica fora do ficheiro até existir. | Gestor |
| `/en` desactualizada | Rever ou retirar. Se o stand quiser vender a estrangeiros, ver `stand-seo-multilingue`. | Gestor |
| Promoção de 2023 ainda publicada | Retirar ou marcar como terminada. | Gestor |

## Passo 4: o ficheiro

```markdown
# Stand Exemplo

> Stand de automóveis usados multimarca em Leiria, com retoma, financiamento através de financeiras parceiras, garantia e oficina de manutenção.

O Stand Exemplo vende viaturas ligeiras usadas, de passageiros e comerciais, em Leiria desde 2009. Trabalha sobretudo com clientes dos concelhos de Leiria, Marinha Grande, Batalha e Pombal. Morada, horário e telefone estão na página de contactos.

## Viaturas

- [Viaturas usadas à venda](https://stand-exemplo.pt/viaturas): stock actualizado com preço, quilómetros, data da primeira matrícula e garantia de cada viatura.
- [Eléctricos e híbridos plug-in](https://stand-exemplo.pt/viaturas/electricos): viaturas eléctricas e híbridas plug-in em stock, com a autonomia WLTP anunciada pelo fabricante.
- [Comerciais usados](https://stand-exemplo.pt/viaturas/comerciais): furgões e comerciais ligeiros em stock.

## Comprar e vender

- [Retoma](https://stand-exemplo.pt/retoma): como o stand avalia a viatura, documentos a trazer e retoma de carros com crédito por pagar.
- [Financiamento](https://stand-exemplo.pt/financiamento): como pedir uma simulação, documentos necessários e financeiras com que o stand trabalha.
- [Garantia](https://stand-exemplo.pt/garantia): prazo e cobertura da garantia nas viaturas usadas e como a accionar.

## Serviços

- [Oficina](https://stand-exemplo.pt/oficina): revisões e reparações de manutenção multimarca, com marcação por telefone ou WhatsApp.

## Sobre e contactos

- [Sobre o Stand Exemplo](https://stand-exemplo.pt/sobre): história do stand, equipa e forma de trabalhar.
- [Contactos](https://stand-exemplo.pt/contactos): morada, horário, telefone, WhatsApp e mapa.

## Optional

- [Documentos para comprar um carro usado](https://stand-exemplo.pt/blog/documentos-para-comprar-carro-usado): o que o comprador recebe e assina numa compra no stand, revisto em 2026.
- [Comprar um eléctrico usado](https://stand-exemplo.pt/blog/comprar-electrico-usado): o que verificar na bateria, no carregamento e na garantia antes de comprar.
- [Política de privacidade](https://stand-exemplo.pt/politica-de-privacidade): como o stand trata os dados de quem pede contacto ou simulação.
```

## Passo 5: validação do rascunho

```text
python3 scripts/validar_llms_txt.py rascunho-llms.txt --verificar-links
```

Resultado do formato (este ficheiro passa no validador): `valido: true`,
sem erros nem avisos, cinco secções, 12 ligações. No site real, a opção
`--verificar-links` pediria cada URL; qualquer ligação em
`links_com_problema` sai do ficheiro ou é corrigida antes de publicar.

## Passo 6: depois de publicado

```text
python3 scripts/validar_llms_txt.py https://stand-exemplo.pt/llms.txt --verificar-links
python3 scripts/verificar_bots_ia.py https://stand-exemplo.pt/llms.txt --caminho /llms.txt --testar-acesso
```

Esperado: `estado_http` 200, `content_type` `text/plain` ou `text/markdown`,
acentos legíveis no navegador, `/llms.txt` permitido aos agentes de pesquisa
e de pedido do utilizador, e 200 no teste de acesso. Um 403 no teste de
acesso fica como suspeita a confirmar na firewall, não como bloqueio provado.

Revisão marcada para daqui a três meses, ou antes se `/entrega` voltar.
