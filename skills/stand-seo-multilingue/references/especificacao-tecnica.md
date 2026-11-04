# Especificação técnica: arquitectura, hreflang e verificação

Lê isto antes de desenhar a arquitectura, de verificar hreflang ou de propor correcções. Os exemplos usam o domínio reservado `stand-exemplo.example` e o Stand Exemplo (fictício).

## Arquitectura

| Opção | Exemplo | Quando | Notas |
|---|---|---|---|
| Português na raiz, línguas em subpastas | `stand-exemplo.example/` e `/en/` | Quase sempre | Mesmo domínio, mesma propriedade no Search Console e no GA4 |
| Tudo em subpastas, incluindo `/pt/` | `/pt/` e `/en/` | Só se o site já está assim ou é novo | Não migres um português que já está na raiz: muda todos os URLs, obriga a redireccionamentos e arrisca posições sem ganho |
| Subdomínios | `en.stand-exemplo.example` | Só se a plataforma não permite subpastas | Funciona com hreflang; mais trabalho de medição |
| Domínio de outro país | `stand-exemplo.es` | Quase nunca | Sinaliza que o público está nesse país; só faz sentido com presença lá |
| Parâmetro de língua | `?lang=en` | Evitar | Só funciona se cada versão tiver URL próprio rastreável e ligado; é frágil |
| Troca por cookie, JavaScript ou widget, no mesmo URL | O mesmo URL muda de língua | Nunca | O Google vê uma só versão |

Slugs traduzidos (`/en/cars/` em vez de `/en/viaturas/`) são opcionais: ajudam quem lê, mas o que conta é a consistência. Mudar slugs depois de publicados obriga a redireccionamentos.

## Códigos hreflang

- Formato: língua em ISO 639-1 (`pt`, `en`, `es`, `fr`, `de`), opcionalmente com região em ISO 3166-1 alfa-2 (`PT`, `GB`, `ES`, `FR`), separadas por hífen.
- **Português:** `pt-PT` quando a versão é para Portugal (euros, termos portugueses); `pt` se for a única versão portuguesa e se quiser servir qualquer falante. Os dois funcionam; escolhe um e mantém.
- **Inglês:** `en` é quase sempre o certo para um stand, porque quem lê vem de vários países. `en-GB` só se o conteúdo for mesmo para britânicos.
- **Espanhol** `es`; **francês** `fr`.
- **Erros frequentes:** `en-UK` (o código do Reino Unido é `GB`), `pt_PT` (o sublinhado é de outros formatos, como o `og:locale`), `br`, `eng`, região sem língua (`PT`).
- **`x-default`** é opcional. Aponta para a versão a mostrar quando nenhuma língua corresponde: normalmente a portuguesa, ou uma página de escolha de língua se existir.

## Regras para cada conjunto de páginas equivalentes

1. **Auto-referência:** cada página inclui-se a si própria na lista.
2. **Reciprocidade:** se A aponta para B, B aponta para A. Sem retorno, a Google pode ignorar o par.
3. **Só páginas equivalentes:** a viatura em inglês aponta para a mesma viatura em português, não para o início.
4. **Alvos válidos:** todos respondem 200, são indexáveis e têm canónico próprio. Nunca hreflang para páginas com `noindex`, redireccionadas ou com canónico para outra língua.
5. **Canónico na própria língua:** `/en/cars/clio-1234` tem canónico para si mesma, nunca para a versão portuguesa. Um canónico cruzado faz desaparecer a versão em inglês.
6. **Um método:** etiquetas no `<head>`, sitemap, ou cabeçalho HTTP `Link` (este para ficheiros como PDF). Dois métodos com valores diferentes criam conflitos.
7. **Páginas sem equivalente** (um guia que só existe em inglês) não levam hreflang: levam canónico próprio e ligações a partir da navegação dessa língua.

### Exemplo no `<head>`

Página portuguesa `https://stand-exemplo.example/viaturas/renault-clio-1234`:

```html
<html lang="pt-PT">
<link rel="canonical" href="https://stand-exemplo.example/viaturas/renault-clio-1234">
<link rel="alternate" hreflang="pt-PT" href="https://stand-exemplo.example/viaturas/renault-clio-1234">
<link rel="alternate" hreflang="en" href="https://stand-exemplo.example/en/cars/renault-clio-1234">
<link rel="alternate" hreflang="x-default" href="https://stand-exemplo.example/viaturas/renault-clio-1234">
```

Página inglesa: o mesmo conjunto de `alternate`, com `lang="en"` e canónico para `https://stand-exemplo.example/en/cars/renault-clio-1234`.

### Exemplo no sitemap

Para stock grande, o sitemap evita repetir etiquetas em cada página. Cada `<url>` leva o conjunto completo, incluindo a si próprio:

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://stand-exemplo.example/viaturas/renault-clio-1234</loc>
    <xhtml:link rel="alternate" hreflang="pt-PT" href="https://stand-exemplo.example/viaturas/renault-clio-1234"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://stand-exemplo.example/en/cars/renault-clio-1234"/>
  </url>
  <url>
    <loc>https://stand-exemplo.example/en/cars/renault-clio-1234</loc>
    <xhtml:link rel="alternate" hreflang="pt-PT" href="https://stand-exemplo.example/viaturas/renault-clio-1234"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://stand-exemplo.example/en/cars/renault-clio-1234"/>
  </url>
</urlset>
```

Um sitemap leva no máximo 50 000 URLs e 50 MB sem compressão; acima disso, um índice de sitemaps.

## Selector de língua e redireccionamentos

- Ligações `<a href>` para a **página equivalente**, não para o início da outra língua.
- Visível em todas as páginas, com o nome da língua na própria língua ("English", "Español", "Français"). Bandeiras sozinhas indicam países, não línguas.
- **Nunca redireccionar automaticamente por IP ou idioma do navegador.** O robô da Google rastreia sobretudo a partir dos Estados Unidos e sem preferência de língua, e veria só uma versão; e um emigrante em França que quer o site em português fica preso na versão francesa. Uma sugestão discreta que não bloqueia ("This page is available in English") é aceitável.
- Menus, rodapé, botões, formulários e ligações internas na língua da página.

## Como a Google percebe a língua

- A Google determina a língua pelo conteúdo visível, não pelo atributo `lang`. O `lang` continua necessário para leitores de ecrã e para a tradução do navegador.
- Página meio traduzida (menus em inglês, conteúdo em português) confunde a Google e o visitante.
- A Bing dá, segundo a sua documentação, mais peso a sinais como o `lang` e a meta `content-language` do que ao hreflang. Confirma a recomendação actual se o stand se importa com a Bing.

## Stock em várias línguas

- **Uma viatura, um registo.** Preço, quilómetros, ano, combustível e estado vêm da mesma fonte para todas as línguas. Quando a viatura é vendida, todas as versões seguem a mesma regra ao mesmo tempo (regras de viaturas vendidas em `stand-auditoria-seo`).
- **Campos fixos** (combustível, caixa, cor, carroçaria) traduzem-se por uma tabela revista uma vez.
- **Descrições livres:** tradução revista. Sem ela, a página noutra língua mostra os campos traduzidos e a descrição portuguesa assinalada como tal: é mais honesto do que tradução automática, mas conta como cobertura parcial na grelha.
- **Preço** em euros, igual em todas as línguas, com as mesmas condições explicadas da mesma forma.

## Metadata e dados estruturados

- `title`, meta descrição, `og:title`, `og:description` e `alt` das imagens na língua da página.
- `og:locale` usa sublinhado: `pt_PT`, `en_GB`, `es_ES`, `fr_FR`; as outras línguas em `og:locale:alternate`.
- JSON-LD: textos (`name`, `description`) na língua da página. A entidade do stand (`AutoDealer`) é a mesma em todas as versões: mesmo nome, morada, telefone e o mesmo `@id`.
- A propriedade `knowsLanguage` do schema.org pode declarar as línguas em que o stand atende, só as verdadeiras. Não há garantia de que a Google a use.

## Textos legais, privacidade e crédito

- A versão portuguesa existe sempre e é a de referência. Indica nas traduções que, em caso de divergência, prevalece a portuguesa (confirmar a redacção com jurista).
- Política de privacidade e informação de cookies na língua da página, com o mesmo conteúdo da portuguesa (RGPD: informação clara e acessível a quem lê). A tradução não promete menos nem mais. Revisão pelo encarregado de protecção de dados ou por jurista.
- Crédito: publicidade e informação pré-contratual têm regras próprias (Decreto-Lei n.º 133/2009 e a Directiva (UE) 2023/2225, que obriga a rever esse regime). Confirma com a financeira em que línguas a informação pode ser dada.

## Verificação

```bash
python3 scripts/extrair_sinais_pagina.py https://stand-exemplo.example/viaturas/renault-clio-1234
python3 scripts/extrair_sinais_pagina.py https://stand-exemplo.example/en/cars/renault-clio-1234
```

Compara, entre as duas saídas:

- `estado_http` 200 em ambas;
- `canonico` de cada uma aponta para si própria;
- `hreflang`: as duas listas têm os mesmos pares e incluem as duas URLs;
- `idioma`, `titulo`, `meta_descricao` e `open_graph` na língua certa.

Depois:

- hreflang no sitemap: `curl -sL https://stand-exemplo.example/sitemap.xml | grep -c "xhtml:link"` e lê um bloco inteiro;
- hreflang em cabeçalho HTTP: `curl -sI <url> | grep -i '^link:'`;
- Search Console, inspecção de URL da versão noutra língua: o canónico escolhido pela Google tem de ser o próprio URL.

Fica por provar com estas ferramentas: a qualidade da tradução (falante nativo) e as posições.

## Erros frequentes e correcção

| # | Sintoma | Causa provável | Correcção | Gravidade |
|---|---|---|---|---|
| 1 | Páginas em inglês não aparecem no Google | Canónico para a versão portuguesa, ou `noindex` que ficou do ambiente de testes | Canónico próprio; retirar `noindex` | Alta |
| 2 | Widget de tradução automática | Tradução no navegador, sem URLs próprios | Páginas próprias revistas, ou retirar o widget | Alta |
| 3 | Visitantes presos numa língua | Redireccionamento automático por IP ou idioma | Retirar; sugestão discreta no lugar | Alta |
| 4 | Preços ou estado diferentes entre línguas | Stock em duas fontes | Uma só fonte | Alta |
| 5 | Formulário em inglês sem resposta | Encaminhado para um email que ninguém lê | Encaminhar para quem atende na língua | Alta |
| 6 | hreflang ignorado | Sem retorno, códigos inválidos (`en-UK`) ou alvos que redireccionam | Corrigir as listas e os alvos | Média |
| 7 | Todas as páginas portuguesas apontam para o início em inglês | hreflang genérico no modelo do site | Só páginas equivalentes | Média |
| 8 | Menus traduzidos, conteúdo em português | Tradução só da interface | Traduzir o conteúdo principal ou recuar para piloto | Média |
| 9 | Versão abandonada (stock antigo, campanhas expiradas) | Ninguém mantém | Retirar a versão ou reduzi-la ao piloto | Média |

**Retirar uma língua:** 301 de cada página para a equivalente portuguesa, retirar o hreflang das páginas portuguesas no mesmo dia, retirar do sitemap. Diz ao gestor quem atendia nessa língua para responder aos contactos que ainda cheguem.

**Ordem das correcções:** canónicos e `noindex` primeiro, depois hreflang, depois conteúdo e navegação, por fim pedir nova indexação das páginas principais na inspecção de URL.

## Medição

- **Search Console:** filtro de páginas por `/en/` (ou uma propriedade de prefixo de URL para a pasta), por país e por consulta.
- **GA4:** páginas por pasta de língua e eventos de contacto (chamada, WhatsApp, formulário) por pasta.
- **CRM e WhatsApp:** etiqueta com a língua do contacto e a origem. Só contagens.
- **Fim do piloto:** contactos na língua, vendas atribuídas (só se o CRM as regista) e horas gastas a manter. Decide manter, alargar ou retirar.
