---
name: stand-escrever-anuncio
description: Escrever o anúncio de uma viatura usada de um stand em Portugal para o Standvirtual, o OLX e o site do stand, a partir da ficha do DMS, das fotos e das notas do gestor, ou reescrever um anúncio já publicado. Usar quando o gestor pede "escreve o anúncio", "descrição para o Standvirtual", "texto para o OLX", "título do anúncio", "lista de equipamento", "melhora este anúncio" ou vai pôr uma viatura à venda. Entrega título, descrição por destino, equipamento organizado, destaques e as perguntas a confirmar antes de publicar, sem inventar equipamento, histórico, revisões, garantia ou quilómetros, e com preço, IVA, financiamento e garantia apresentados só como o stand os declara.
---

# Escrever o anúncio de uma viatura

Escreve o anúncio de uma viatura usada com factos que o stand confirma, adaptado a cada destino. Não fixa o preço nem audita o stock: para posicionar o preço há a Análise de stock do hub; para auditar uma amostra de anúncios já publicados, usa `stand-rever-anuncios-viaturas`.

## Antes de começar

1. Pergunta para onde é o anúncio: Standvirtual, OLX, site do stand ou outro portal. Escreve só para os destinos pedidos.
2. Escolhe o modo pela fonte que o gestor tem:
   - **Ficha:** exportação ou cópia do DMS, notas e fotos. É o modo de referência.
   - **Anúncio existente:** URL ou HTML guardado de um anúncio do próprio stand. Extrai os dados com o script (ver Ferramentas) e reescreve. O que lá está foi publicado, não é prova: confirma o que pode ter mudado (preço, quilómetros, disponibilidade, garantia).
   - **Só notas ou fotos:** escreve o rascunho, mas tudo o que não tem fonte sai como `a confirmar`.
3. Pede o que falta numa só lista curta, só com o que muda o anúncio: versão exacta, mês e ano da primeira matrícula, quilómetros, combustível, caixa, potência, preço, regime de IVA, garantia oferecida, origem, revisões documentadas, defeitos conhecidos, se aceita retoma.
4. Pergunta pela voz do stand. Se houver um kit de `stand-posicionamento`, segue-o; sem kit, escreve sóbrio e factual, de forma impessoal ou com "você".
5. Não peças matrícula, VIN, nomes de anteriores proprietários nem documentos. Se vierem na ficha, não os passes para o anúncio; a matrícula segue a política do stand.

## Passos

1. **Ficha de factos.** Antes, lê [references/regras-e-factos.md](references/regras-e-factos.md). Monta a tabela campo / valor / fonte / estado (`confirmado`, `a confirmar`, `não usar`). Resultado: cada facto que vai entrar no anúncio tem uma fonte aceitável.
2. **Contradições.** Se a ficha, as fotos e o anúncio antigo não batem (quilómetros, ano, versão, preço), pára e pergunta. Nunca escolhas o valor mais favorável.
3. **Equipamento.** Separa três níveis: confirmado na viatura (ficha do stand, verificação física, descodificação do VIN pela marca), visível nas fotos (`a confirmar`, com o número da foto) e de catálogo da versão (`não usar`). Só o primeiro entra. Organiza por grupos: segurança e assistência, conforto, multimédia e conectividade, exterior e iluminação, outros.
4. **Preço e condições.** Preço com IVA incluído. Regime da margem ou IVA dedutível só como o stand declara, nunca deduzido. Financiamento só com TAEG e exemplo representativo dados pelo stand e com o registo do stand como intermediário de crédito confirmado. Garantia só como o stand a declara, a distinguir garantia legal de garantia comercial, com o regime do Decreto-Lei n.º 84/2021 para usados a confirmar. Falta um destes dados: a frase sai do anúncio e entra nas perguntas.
5. **Destaques.** Escolhe três a cinco factos confirmados que mais pesam na decisão de quem compra esta viatura: quilómetros, revisões documentadas, equipamento confirmado, garantia, estado. Um adjectivo não é um destaque.
6. **Títulos e descrições por destino.** Segue [references/portais.md](references/portais.md): no Standvirtual mandam os campos estruturados, o OLX pede texto mais directo, o site precisa de título de página, meta descrição e texto próprio. Não copies o mesmo texto para todos. Os limites de caracteres e os campos de cada portal confirmam-se na interface no dia da publicação: quando não souberes o limite, entrega uma versão completa e uma curta.
7. **Fotografias.** Se tiveres as fotos, propõe a ordem, lista as que faltam e assinala documentos, ecrãs com nomes ou outros dados pessoais visíveis. Nunca proponhas editar uma foto para esconder um dano.
8. **Perguntas a confirmar.** Junta tudo o que ficou `a confirmar`, com o motivo. O anúncio não está pronto enquanto houver uma pergunta aberta sobre preço, quilómetros, garantia, financiamento ou defeitos.
9. **Verificação final.** Corre a lista do modelo e entrega ao gestor. Não publicas nada.

## Quando parar e perguntar

- O gestor afirma um facto sem documento ("põe que tem um só dono"): pergunta se o stand o consegue mostrar ao comprador. Se sim, entra como declaração do stand; se não, fica de fora.
- O gestor pede para omitir um defeito conhecido: não omites. Propõe repará-lo antes ou declará-lo de forma objectiva, e explica o risco.
- A viatura aparece como reservada ou vendida no DMS: não escreves o anúncio sem confirmação.
- O preço no DMS e o do anúncio publicado são diferentes: pergunta qual vale antes de escrever.

## Casos especiais

- **Eléctricos e híbridos plug-in:** autonomia só a homologada, com fonte e ciclo; estado da bateria só com relatório datado; garantia da bateria do fabricante só confirmada com a marca ou o importador.
- **Comerciais e viaturas para empresas:** o regime de IVA pergunta-se sempre; lotação, peso e carga só da documentação da viatura.
- **Importadas:** a origem diz-se quando o stand a confirma, nunca por dedução.

## Ferramentas

- `python3 scripts/extrair_sinais_pagina.py <url-ou-ficheiro.html>`: lê um anúncio do stand e devolve título, meta descrição, H1, dados estruturados (marca, modelo, ano, quilómetros, combustível, preço, disponibilidade), Open Graph, contactos e imagens sem texto alternativo. Não executa JavaScript, por isso o que o portal carrega depois não aparece; se o portal bloquear o pedido, pede ao gestor que guarde a página em HTML e corre o script sobre o ficheiro. O resultado mostra o que a página declara, não prova nada sobre a viatura.
- [Análise de stock](https://onepilot.app/hub/ferramentas/analise-stock): compara o preço pedido com anúncios semelhantes no Standvirtual, com dias anunciados e descidas de preço. Serve para o gestor decidir o preço; a skill não o fixa.
- Para auditar uma amostra do stock publicado (fotos, coerência entre site e portais, vendidas ainda activas), usa `stand-rever-anuncios-viaturas`. Para levar a viatura às redes sociais com os mesmos factos, `stand-publicar-redes-sociais`.

## Entrega

Preenche [assets/modelo-anuncio.md](assets/modelo-anuncio.md): ficha de factos, títulos, descrição por destino, equipamento organizado, destaques, preço e condições, fotografias, perguntas a confirmar, o que ficou de fora e verificação final. Um exemplo completo, com viatura e stand fictícios, está em [references/exemplo-resolvido.md](references/exemplo-resolvido.md).

## Limites

- Não inventa nem completa por conhecimento do modelo: equipamento, histórico, revisões, número de proprietários, ausência de acidentes, origem, garantia, quilómetros, estado da bateria ou autonomia.
- Não usa urgência falsa ("último dia", "há outro interessado") nem superlativos sem prova ("impecável", "como novo", "melhor preço do mercado").
- Não esconde defeitos que o stand conhece: propõe a forma objectiva de os declarar.
- Não apresenta um preço que só vale com financiamento ou com retoma sem o dizer junto ao preço e sem mostrar também o preço sem condição.
- Não escreve como particular: um stand anuncia como profissional, em todos os destinos.
- Não publica, não altera anúncios nem mexe no DMS: entrega o texto para o gestor aprovar.
