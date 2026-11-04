# Formato do llms.txt para stands

## O que é e o que não é

- Uma proposta publicada em llmstxt.org em 2024: um ficheiro Markdown na raiz
  do site (`/llms.txt`) com um resumo e um índice das páginas mais úteis,
  pensado para modelos de linguagem e agentes.
- É uma proposta, não uma norma. Nenhum organismo de normas a adoptou.
- À data desta skill, nenhum dos grandes motores (Google, OpenAI, Anthropic,
  Perplexity, Microsoft) documentou que usa o `llms.txt` para escolher o que
  cita, e porta-vozes da Google disseram publicamente que a Pesquisa não o
  usa. Confirma se isto mudou antes de prometer qualquer efeito.
- O valor real para um stand: custa pouco, serve os agentes que o procuram e
  obriga a decidir que páginas importam. Não substitui robots.txt, sitemap,
  dados estruturados nem texto claro nas páginas.

## Estrutura, pela ordem da proposta

1. **H1** com o nome do stand. É o único elemento obrigatório, e só pode
   haver um.
2. **Citação** (`>`) com um resumo factual numa ou duas frases.
3. **Texto livre**, sem títulos: parágrafos ou listas com o contexto que
   ajuda a ler o resto.
4. **Secções H2**, cada uma com uma lista de ligações no formato
   `- [Retoma](https://stand-exemplo.pt/retoma): descrição`.
5. **`## Optional`**: secção com significado próprio na proposta (o que se
   pode saltar quando o contexto é curto). Mantém o título em inglês, porque é
   a palavra que a proposta define. É o único título que não traduzes.

A proposta sugere também versões Markdown das páginas (o mesmo URL com
`.md`). Num site de stand isto é raro; não o proponhas sem o fornecedor do
site garantir que as mantém. O `llms-full.txt` (o conteúdo inteiro num só
ficheiro) é uma convenção de terceiros, fora da proposta. Com stock a mudar
todos os dias, não se recomenda.

## Secções para um stand

Ordem sugerida, por legibilidade (não há prova de que os motores dêem peso
à ordem):

| Secção | O que leva |
|---|---|
| `## Viaturas` | Lista de stock e categorias com página estável (eléctricos, comerciais, marcas, se existirem como página própria). |
| `## Comprar e vender` | Retoma, compra de viaturas a particulares, financiamento, garantia, entrega, documentação. |
| `## Serviços` | Oficina, revisões, pneus, preparação, só os que existem. |
| `## Sobre e contactos` | Sobre o stand, contactos (morada, horário, canais). |
| `## Optional` | Guias úteis e actuais, política de privacidade, páginas noutras línguas mantidas. |

No texto livre, põe só factos que raramente mudam e que o gestor confirmou:
concelho, desde quando, o que vende, serviços, concelhos onde trabalha.
Horário e telefone ficam na página de contactos, salvo se alguém se
compromete a actualizar o ficheiro quando mudarem.

Num concessionário oficial, nomeia as marcas representadas no resumo. Um
stand com várias localizações pode ter um ficheiro com uma secção por
localização, ou um ficheiro por domínio: escolhe com o gestor.

## Incluir e excluir

| Incluir | Excluir |
|---|---|
| Lista de stock e categorias estáveis | Fichas de viaturas (vendem-se e o URL morre) |
| Retoma, financiamento, garantia, entrega | Pesquisas com filtros (`?marca=`, `?preco_max=`, `?ordem=`) |
| Oficina e serviços que existem | Parâmetros de campanha (`utm_`, `gclid`, `fbclid`) |
| Sobre e contactos | Páginas só com formulário, sem texto |
| Guias actuais e úteis ao comprador | Notícias antigas e promoções com data passada (liga ao arquivo, se for útil) |
| Política de privacidade (em `Optional`) | Login, favoritos, comparador, carrinho |
| Páginas noutras línguas mantidas | Duplicados: dois URLs com o mesmo conteúdo (fica o canónico) |
| | Páginas em `noindex`, bloqueadas no robots.txt ou com erro |
| | Traduções automáticas que ninguém revê (ver `stand-seo-multilingue`) |

Ligações para outros domínios (perfil no portal, redes) não acrescentam
factos ao que o site já tem. Ficam no JSON-LD do stand (`sameAs`), não no
`llms.txt`. O `validar_llms_txt.py` avisa quando há mais de um domínio.

Para um stand pequeno, 10 a 30 ligações chegam. É uma escolha editorial
desta biblioteca, não uma regra da proposta: menos de 10 costuma querer dizer
que faltam páginas de serviço no site; mais de 30 costuma querer dizer que
entraram fichas ou filtros.

## Escrever as descrições

Uma linha por ligação. Diz o que a página tem, não o que o stand acha de si.
Cada descrição tem de ser verdade na página hoje: se a página não diz
"multimarca", a descrição também não.

| Mau | Bom |
|---|---|
| `Retoma: a melhor avaliação do mercado!` | `Retoma: como avaliamos a viatura, documentos a trazer e retoma de carros com crédito por pagar.` |
| `Financiamento: crédito fácil e rápido` | `Financiamento: como pedir uma simulação, documentos necessários e financeiras com que trabalhamos.` |
| `Viaturas: os melhores carros de Leiria` | `Viaturas usadas à venda: stock actualizado com preço, quilómetros e garantia de cada viatura.` |
| `Oficina` | `Oficina: revisões e reparações de manutenção multimarca, com marcação por telefone ou WhatsApp.` |

Não ponhas no ficheiro preços ("a partir de 9.900 €"), TAEG, prestações,
prazos de entrega ou de garantia que o gestor não confirmou, nem números de
stock. Mudam, e o ficheiro fica a dizer o contrário do site.

## Publicar

- **Caminho:** raiz do domínio canónico (`https://stand-exemplo.pt/llms.txt`).
  Se o site responde com e sem `www`, a versão não canónica redirecciona.
- **Resposta:** `200`, `content-type` `text/plain` ou `text/markdown`, com
  `charset=utf-8`. Sem codificação certa, os acentos podem aparecer trocados
  ("Ã©" em vez de "é"): abre o ficheiro publicado no navegador e confirma.
- **robots.txt:** não pode bloquear `/llms.txt` aos agentes de pesquisa e de
  pedido do utilizador. Não é preciso declará-lo no robots.txt nem no
  sitemap: quem o usa procura-o no caminho `/llms.txt`.
- **WordPress ou alojamento próprio:** carregar na raiz pelo painel de
  alojamento ou por FTP. Alguns plugins de SEO geram o ficheiro
  automaticamente; se for o caso, revê o que geram, porque tendem a listar
  tudo.
- **Site feito por um fornecedor ou plataforma de stands:** pedido por
  escrito, com o ficheiro em anexo e o caminho exacto. Pede confirmação de
  que o ficheiro não é reescrito na próxima actualização.
- **Construtores de sites:** confirma se permitem ficheiros na raiz. Alguns
  não permitem; nesse caso diz-o ao gestor em vez de inventar um caminho
  alternativo.

## Manter

Rever quando: muda o URL de uma página da lista; abre ou fecha um serviço;
muda o nome, a morada ou o telefone; o site muda de plataforma (os URLs
costumam mudar todos). Fora disso, verificar as ligações de três em três
meses com `validar_llms_txt.py --verificar-links`. O ficheiro tem um
responsável com nome, e a próxima data de revisão fica na entrega.
