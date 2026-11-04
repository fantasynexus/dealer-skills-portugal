# Grelha de 100 pontos: versões do site noutras línguas

Usa esta grelha no modo auditar, depois de leres [especificacao-tecnica.md](especificacao-tecnica.md). Pontua cada língua adicional em separado quando os resultados diferem; a versão portuguesa é a referência, não é pontuada aqui (é de `stand-auditoria-seo`).

## Regras de pontuação

- Três respostas: **total**, **parcial** (o valor indicado) ou **0**. Sem prova, `N/V`.
- `N/V` (faltou acesso) e **não se aplica** saem do denominador.
- **Nota** = pontos obtidos ÷ pontos verificados × 100. **Cobertura** = pontos verificados ÷ pontos aplicáveis. Abaixo de 60 %, "nota indicativa".
- **Amostra por língua:** início, contactos, listagem, duas viaturas, retoma ou financiamento, e as equivalentes portuguesas. Regista cada par de URLs com a data.
- **Prova:** JSON do script para cada versão, captura, linha do Search Console com período, ou leitura do texto citada.

### Achados críticos (assinalar sempre)

Versão noutra língua com canónico para a portuguesa ou com `noindex` em todas as páginas; redireccionamento automático por IP ou idioma; widget de tradução no lugar de páginas; preços ou estado diferentes entre línguas; formulários na língua que ninguém lê; textos legais ou de crédito traduzidos sem revisão.

## 1. Decisão e atendimento (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 1.1 Procura documentada para a língua | 5 | Search Console, GA4, contactos (ver [publicos-e-procura.md](publicos-e-procura.md)) | Sinais em duas ou mais fontes, com datas | (2) Sinal fraco ou de uma fonte | Nenhum sinal; "achámos que sim" |
| 1.2 Alguém atende na língua | 5 | Gestor: quem, canal, horário | Atende por telefone e no stand | (2) Só por escrito, ou só em parte do horário | Ninguém |

## 2. Arquitectura e URLs (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 2.1 URL próprio e rastreável por língua | 5 | URLs da amostra; script | Subpasta ou subdomínio, cada página com URL próprio | (2) Parâmetro `?lang=` com URLs ligados | Cookie, JavaScript ou widget no mesmo URL |
| 2.2 Estrutura estável e coerente | 3 | Comparação entre línguas | Mesma lógica em todas as línguas; português não migrado sem razão | (1) Mistura de padrões | URLs que mudam com a língua escolhida na sessão |
| 2.3 Sem redireccionamento automático | 2 | Abrir o site com o navegador noutra língua e a partir de outro país (VPN, se houver) | Nenhum; no máximo sugestão que não bloqueia | | Redirecciona por IP ou idioma |

## 3. hreflang (15)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 3.1 Presente nas páginas equivalentes | 5 | Script em cada par; sitemap | Em todos os pares da amostra | (2) Só em parte (início sim, viaturas não) | Ausente |
| 3.2 Auto-referência e reciprocidade | 5 | Listas de hreflang lado a lado | Cada página inclui-se e é incluída pela equivalente | (2) Falhas pontuais | Sem retorno na maioria |
| 3.3 Códigos válidos e `x-default` coerente | 3 | Listas de hreflang | Códigos ISO válidos; `x-default` ausente ou a apontar para a versão de recurso | (1) Um código inválido | Códigos inventados (`en-UK`, `pt_PT`, `br`) em geral |
| 3.4 Um método, sem conflitos | 2 | `<head>`, sitemap e cabeçalho HTTP | Um método, ou vários com os mesmos valores | | Métodos com valores diferentes |

## 4. Canónicos e indexação (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 4.1 Canónico na própria língua | 5 | Script: `canonico` | Cada versão aponta para si | (2) Falhas pontuais | Versões com canónico para a portuguesa |
| 4.2 Versões indexáveis e indexadas | 5 | Script: `estado_http`, `meta_robots`; Search Console: inspecção de URL | 200, sem `noindex` e, com acesso, indexadas com o próprio URL como canónico escolhido | (2) Indexáveis, mas parte fora do índice | `noindex`, erros ou redireccionamentos. Sem acesso: a parte "indexadas" fica `N/V` |

## 5. Qualidade linguística (15)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 5.1 Conteúdo principal traduzido | 5 | Leitura das páginas | Corpo, títulos, botões e formulários na língua | (2) Interface traduzida, partes do corpo em português | Só menus traduzidos |
| 5.2 Revisão por falante competente | 5 | Quem reviu (pergunta ao gestor); leitura | Revisto e natural | (2) Legível, com marcas de tradução automática | Tradução automática sem revisão |
| 5.3 Termos de venda e documentos correctos | 5 | Glossário de [publicos-e-procura.md](publicos-e-procura.md) | Termos certos e documentos portugueses explicados (IPO, IUC, certificado de matrícula) | (2) Alguns termos literais ("retoma" traduzida à letra) | Termos que induzem em erro (garantia com condições diferentes das portuguesas) |

Quem não fala a língua não pontua 5.2 nem 5.3 com confiança: marca `N/V` e pede revisão a um falante nativo.

## 6. Cobertura das páginas que vendem (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 6.1 Páginas previstas existem | 6 | Lista do plano (piloto ou completo) contra o site | Todas as previstas para o público em causa | (3) Cerca de metade | Só o início |
| 6.2 Sem páginas abandonadas | 4 | Datas, campanhas, stock nas páginas da língua | Tudo actual | (2) Uma ou duas páginas desactualizadas | Campanhas expiradas ou stock antigo em destaque |

## 7. Metadata e dados estruturados (8)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 7.1 Título, descrição e Open Graph na língua | 4 | Script: `titulo`, `meta_descricao`, `open_graph` | Todos na língua, `og:locale` certo | (2) Parte em português | Todos em português |
| 7.2 JSON-LD na língua e entidade igual | 4 | Script: `json_ld` | Textos na língua; `AutoDealer` com os mesmos dados em todas as versões | (2) Textos em português | Dados da entidade diferentes entre versões, ou dados estruturados ausentes só nesta língua |

## 8. Navegação e selector (7)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 8.1 Selector para a página equivalente | 4 | Clicar no selector em três páginas | Visível, com o nome da língua, leva à equivalente | (2) Leva ao início da outra língua | Ausente ou escondido |
| 8.2 Navegação na mesma língua | 3 | Menus, rodapé, ligações internas | Tudo na língua da página | (1) Ligações internas que saltam para português | Navegação em português |

## 9. Stock e dados consistentes (7)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 9.1 Mesma fonte de dados | 4 | Duas viaturas nas duas línguas | Preço, quilómetros, ano e estado iguais | | Qualquer diferença |
| 9.2 Vendidas tratadas em todas as línguas | 3 | Uma viatura vendida nas duas línguas | Mesma regra, ao mesmo tempo | (1) Atraso entre línguas | Vendida numa língua, disponível noutra |

## 10. Conversão e medição na língua (8)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 10.1 Contacto na língua chega a quem atende | 4 | Formulário, WhatsApp, mensagens de confirmação; pergunta ao gestor para onde vão | Tudo na língua e encaminhado para quem a fala | (2) Na língua, mas cai na caixa geral | Mensagens de confirmação em português ou contactos que ninguém lê |
| 10.2 Medição por língua | 4 | Search Console, GA4, CRM | Pasta filtrável, eventos de contacto por pasta, língua do contacto no CRM | (2) Só uma das três | Nenhuma |

## Lista de controlo legal (não pontuada, sempre no relatório)

- A versão portuguesa de cada texto legal existe e é a de referência.
- Política de privacidade e cookies na língua, com o mesmo conteúdo.
- Textos de financiamento e garantia revistos por jurista antes de publicados.
- Nada disto é parecer: confirma com o encarregado de protecção de dados ou com um jurista.
