---
name: stand-brief-conteudo-aeo
description: Criar o brief de uma página ou artigo do site de um stand de automóveis em Portugal, para responder a perguntas reais de compradores e poder ser citado pela Google e por motores de IA (SEO, AEO, GEO). Usar para páginas de financiamento, retoma, garantia, carros eléctricos, IUC, inspecção, importados, documentação, guias de modelo, comparações, páginas locais ou oficina; quando o gestor pergunta "o que devo escrever para aparecer no ChatGPT", quer um brief para a agência ou para quem escreve no site, ou quer corrigir as lacunas de conteúdo de uma auditoria AEO. Entrega pergunta principal, resposta de abertura pronta a citar, estrutura, perguntas e respostas com o tipo e a fonte de cada afirmação, provas a pedir ao stand, ligações, dados estruturados, CTA e o que não afirmar.
---

# Brief de conteúdo AEO para stands

Produz a prescrição editorial de uma página: que pergunta responde, com que
frases, com que provas e com que fontes. Escreve no brief as partes que mais
pesam (título, H1, abertura, frases citáveis); o resto fica como instrução
para quem escreve. Distingue sempre três coisas: factos do stand, regras
legais ou fiscais, e opinião.

## Antes de começar

Pede:

- tema ou pergunta, e o objectivo da página (leads, retoma, oficina, confiança);
- stand, concelho e concelhos servidos;
- página actual, se existir (URL);
- stock ou serviço relacionado e o que o stand consegue provar (condições escritas, prazos medidos, garantias por contrato);
- acção que a página deve provocar;
- restrições de marca ou do importador, se o stand for concessionário oficial.

Escolhe o modo:

- **A partir de uma pergunta ou tema** (omissão): um brief.
- **A partir de uma auditoria ou medição:** pega nas lacunas das dimensões 5 e 6 de `stand-auditoria-aeo`, ou nas perguntas onde o stand não aparece em `stand-visibilidade-ia`, e faz um brief por lacuna, por ordem de impacto.

Encaminha o que não é brief de página: comparação com um stand concorrente
nomeado para `stand-pagina-comparacao`; anúncio de uma viatura para
`stand-escrever-anuncio`; publicações para redes para
`stand-publicar-redes-sociais`.

## Passos

1. **Perguntas reais.** Lê [references/perguntas-compradores.md](references/perguntas-compradores.md). Confirma a pergunta principal com fontes do stand (mensagens de clientes anonimizadas, chamadas, avaliações) ou, com acesso, com o Search Console. Escreve a pergunta como o comprador a escreve.
2. **Validar.** Três testes: um comprador faz mesmo esta pergunta; o stand pode responder com autoridade e prova; há razão para citar o stand em vez de uma fonte oficial ou do fabricante. Se falha o segundo, pára e pede as provas ou muda o ângulo. Se falha o terceiro (a resposta é só uma regra), a página diz o que o stand faz por si e liga à fonte oficial.
3. **Escolher o tipo.** Lê [references/tipos-de-pagina.md](references/tipos-de-pagina.md). Decide entre página nova, reescrita ou secção de uma página existente, e explica porquê.
4. **Separar afirmações.** Para cada afirmação prevista, marca o tipo: facto do stand (prova interna), regra (fonte primária, data da consulta, "confirmar versão em vigor"), opinião (assumida, com critérios). Sem prova, fica `[CONFIRMAR]`; não sai como facto.
5. **Pesquisar fontes,** quando tens acesso: entidades oficiais (Portal das Finanças, IMT, IRN, Banco de Portugal, Fundo Ambiental, Mobi.E), fabricante para especificações, Euro NCAP para segurança. Regista a data. Nunca cites um stand concorrente como fonte.
6. **Escrever o brief** com o modelo [assets/brief.md](assets/brief.md): título, meta descrição, H1 e resposta de abertura (60 a 100 palavras) escritos por extenso; estrutura com o objectivo de cada secção; perguntas e respostas com a frase citável.
7. **Rever** com a lista de qualidade no fim do modelo. Corrige antes de entregar.
8. **Entregar** como rascunho para aprovação. O artigo só se escreve depois de o brief estar aprovado e as provas recebidas.

Para um brief completo, da entrada à entrega, vê
[references/exemplo-brief.md](references/exemplo-brief.md).

## Ferramentas

- [Análise de stock](https://onepilot.app/hub/ferramentas/analise-stock): para guias de modelo, o preço pedido em anúncios semelhantes no Standvirtual. É preço pedido, não preço de venda: publica-o com a data e a fonte, ou não o publiques.
- Search Console, com acesso: as consultas que já trazem visitas à página actual.

## Entrega

Segue [assets/brief.md](assets/brief.md), com as doze partes:

1. pergunta principal, secundárias, intenção e fase de compra;
2. tipo de página, decisão (nova, reescrita, secção), URL, título, meta descrição e H1;
3. resposta de abertura de 60 a 100 palavras, pronta a citar;
4. estrutura H2/H3 com o objectivo e o conteúdo obrigatório de cada secção;
5. perguntas e respostas com a frase citável, o tipo e a prova ou fonte;
6. provas a pedir ao stand e fontes externas primárias;
7. ligações internas, a dizer quais existem e quais são a criar;
8. dados estruturados adequados;
9. imagens com origem, texto alternativo e nome do ficheiro;
10. CTA principal coerente com a fase de compra;
11. o que não afirmar e o tom;
12. métricas e data de revisão.

## Limites

- Não inventa preços, TAEG, prestações, garantias, prazos, autonomias, consumos, stock, números de clientes nem volumes de pesquisa.
- Regras legais e fiscais são listas a confirmar na fonte primária, não pareceres. Na dúvida, encaminha para um jurista ou para o contabilista do stand.
- Não marca como `FAQPage` perguntas que não aparecem na página e não promete resultados enriquecidos.
- Não cria páginas locais quase iguais para vários concelhos nem conteúdo em série feito para motores.
- Não usa dados pessoais de clientes: perguntas de mensagens entram sem nomes, telefones nem matrículas.
- Não publica nem altera o site. Entrega o brief para aprovação.
- Escreve em PT-PT, com euros e sistema métrico. Os textos para clientes tratam por "você" ou de forma impessoal, salvo indicação do stand.
