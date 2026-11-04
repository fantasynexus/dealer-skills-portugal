# Grelha de 100 pontos: SEO do site de um stand

Lê isto antes de pontuar. Cada critério diz o que verificar, onde, que prova aceitar e o que vale total, parcial ou 0.

## Regras de pontuação

- Cada critério tem três respostas possíveis: **total**, **parcial** (o valor indicado) ou **0**. Sem prova, `N/V`.
- `N/V` (não verificado) e **não se aplica** saem ambos do denominador, mas não são a mesma coisa. `N/V`: havia o que ver e faltou acesso. Não se aplica: não existe no stand (por exemplo, hreflang num site só em português).
- **Nota** = pontos obtidos ÷ pontos verificados × 100, arredondada às unidades.
- **Cobertura** = pontos verificados ÷ pontos aplicáveis. Abaixo de 60 %, escreve "nota indicativa" ao lado da nota.
- **Prova aceitável:** URL com data, JSON do script, captura, linha do Search Console com o período, cabeçalho HTTP copiado. "Parece" não é prova.
- A nota descreve a amostra. Quando um defeito vem do modelo da página (todas as viaturas usam o mesmo template), diz isso: corrigir o modelo corrige o site inteiro.

### Leitura da nota

| Nota | Leitura |
|---|---|
| 85 a 100 | Base sólida. O trabalho passa a ser conteúdo, reputação e autoridade local. |
| 70 a 84 | Falhas corrigíveis em semanas, quase sempre no modelo das páginas. |
| 50 a 69 | Há problemas a travar páginas que vendem. Normalmente é preciso o fornecedor do site. |
| Abaixo de 50 | O Google não consegue tratar bem o stock. Corrigir a base antes de investir em conteúdo. |

### Sinais críticos (assinalar sempre, seja qual for a nota)

`Disallow: /` ou `noindex` em listagens ou viaturas; duas versões do domínio indexadas sem redireccionamento; site em manutenção ou ambiente de testes indexado; páginas de spam injectadas (farmácia, apostas, outras línguas que o stand não usa); viaturas vendidas há meses ainda como disponíveis.

## 1. Rastreabilidade e indexação (12)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 1.1 robots.txt deixa passar o que vende | 3 | `/robots.txt`; citar a regra | Nenhuma regra bloqueia início, listagens, viaturas, contactos, CSS ou JS | (1) Bloqueia recursos (CSS, JS, imagens) ou secções secundárias | Bloqueia listagens ou viaturas, ou `Disallow: /` |
| 1.2 Páginas da amostra indexáveis | 4 | Script: `estado_http`, `meta_robots`, `x-robots-tag` | Todas respondem 200 sem `noindex` | (2) Uma página secundária com `noindex` ou erro | Início, listagem ou viaturas com `noindex`, 4xx ou 5xx |
| 1.3 Viaturas activas indexadas | 3 | Search Console: inspecção de URL das viaturas da amostra e motivos de exclusão no relatório de páginas | Todas as viaturas activas da amostra indexadas e exclusões explicáveis (filtros, vendidas) | (1) Parte das activas "rastreada, não indexada" ou "detectada, não indexada" | Maioria das activas fora do índice. Sem acesso: `N/V` |
| 1.4 Ligações rastreáveis para as viaturas | 2 | HTML devolvido (script) contra o navegador | Listagens ligam a cada viatura com `<a href>` no HTML | (1) Ligações só aparecem depois do JavaScript, mas o HTML renderizado da inspecção de URL mostra-as | Viaturas só alcançáveis por pesquisa interna, botões sem `href` ou scroll infinito sem URLs |

## 2. Canónicos, redireccionamentos e sitemaps (8)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 2.1 Canónico próprio e coerente | 3 | Script: `canonico`; Search Console: canónico escolhido pela Google | Cada página aponta para si; ordenações e parâmetros de campanha apontam para a versão limpa | (1) Faltas pontuais, ou página 2 de listagem a apontar para a página 1 | Canónicos para o início, para outra língua, para o domínio antigo ou para URLs que redireccionam |
| 2.2 Uma só versão do domínio | 2 | `curl -sIL` em `http://`, `https://`, com e sem `www`, com e sem barra final | Todas acabam num só URL, num salto | (1) Cadeias de dois ou mais saltos | Versões duplicadas a responder 200 |
| 2.3 Sitemap actual | 3 | `/sitemap.xml` ou o declarado no robots.txt; relatório de sitemaps | Existe, só lista URLs 200 indexáveis e canónicos, viaturas vendidas saem, `lastmod` verdadeiro | (1) Existe mas inclui vendidas, redireccionamentos ou `lastmod` igual em tudo | Não existe, ou dá erro |

## 3. Títulos, descrições, headings e conteúdo principal (12)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 3.1 Títulos únicos e descritivos | 4 | Script: `titulo` de toda a amostra lado a lado | Únicos; viatura com marca, modelo, versão, ano e combustível; listagens com o que listam e a zona | (2) Repetições em páginas secundárias ou viaturas sem ano ou versão | Mesmo título em várias páginas, ou só o nome do stand |
| 3.2 Meta descrições | 2 | Script: `meta_descricao` | Únicas e com o que a página tem (stock, condições, zona) | (1) Em falta ou repetidas em parte da amostra | Iguais em todo o site |
| 3.3 Um H1 que diz o que é a página | 3 | Script: `h1` | Um H1 por página, descritivo | (1) Vários H1 (logótipo, banner) ou H1 genérico ("Bem-vindo") | Sem H1 nas páginas que vendem |
| 3.4 Conteúdo principal responde à intenção | 3 | Leitura da página | Retoma explica como funciona e o que é preciso; financiamento explica condições reais; listagens têm texto curto útil sobre o stock e a zona | (1) Só formulário ou texto genérico copiado entre páginas | Páginas de serviço vazias ou só com imagem |

Comprimentos de título e descrição são orientação, não regra: a Google corta por largura e reescreve muitas vezes a descrição. Não penalizes um título bom por ter 65 caracteres.

## 4. Mapa de palavras-chave e canibalização (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 4.1 Cada intenção tem uma página dona | 4 | Mapa de procura (ver [pesquisa-portuguesa.md](pesquisa-portuguesa.md)) | Todas as intenções que o stand serve têm página própria | (2) Faltam uma ou duas (por exemplo, eléctricos usados num stand que os vende) | Tudo cai no início ou na listagem geral |
| 4.2 Sem canibalização relevante | 4 | Search Console: consulta, separador de páginas; sem acesso: títulos e H1 repetidos | Nenhum grupo | (2) Um ou dois grupos | Três ou mais, ou o início a competir com a listagem pela consulta principal |
| 4.3 Palavras do comprador português | 2 | Texto visível contra consultas reais | Usa "carros usados", "viaturas", marca e modelo, combustível, "retoma", concelho | (1) Mistura com jargão interno ("oportunidades", "gama premium") | Só jargão; nenhuma referência à zona |

## 5. Profundidade, actualidade, utilidade e E-E-A-T (12)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 5.1 Quem é o stand | 3 | Página "sobre", rodapé | História real, pessoas com nome e função, fotografias próprias do espaço, identificação da empresa | (1) Texto genérico sem pessoas nem fotografias próprias | Nada sobre quem vende |
| 5.2 Serviços com informação verificável | 3 | Páginas de retoma, financiamento, garantia, entrega | Condições reais e o que o cliente precisa de levar, sem promessas que o stand não confirmou | (1) Promessas vagas ("as melhores condições") | Afirmações que contradizem a lei ou o que o stand faz |
| 5.3 Actualidade | 3 | Viaturas da amostra, horários, datas dos artigos | Stock bate com o que está à venda; preços iguais aos dos portais; horário actual | (1) Desfasamentos pontuais | Vendidas como disponíveis, preços diferentes do portal, campanhas expiradas em destaque |
| 5.4 Confiança e obrigações visíveis | 3 | Rodapé, contactos, política de privacidade | Contactos completos, política de privacidade, ligação ao Livro de Reclamações Electrónico, informação sobre resolução alternativa de litígios | (1) Falta um elemento | Sem identificação da empresa nem contactos fora de formulários |

Em 5.4, as obrigações são lista de controlo, não parecer. Confirma a redacção em vigor: identificação do prestador no Decreto-Lei n.º 7/2004 (comércio electrónico), Livro de Reclamações no Decreto-Lei n.º 156/2005 e alterações, entidades de resolução alternativa de litígios na Lei n.º 144/2015. Na dúvida, encaminha para um jurista.

## 6. Arquitectura, URLs e ligações internas (10)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 6.1 URLs legíveis e estáveis | 3 | URLs da amostra | Minúsculas, hífenes, marca e modelo mais um identificador; não mudam quando o preço muda | (1) Identificadores opacos mas estáveis | Preço, sessão ou data no URL; o URL muda quando a viatura é editada |
| 6.2 Profundidade de cliques | 3 | Navegação a partir do início | Qualquer viatura activa a três cliques ou menos | (1) Viaturas só a partir da página 4 ou mais da listagem | Viaturas sem caminho por ligações |
| 6.3 Ligações internas úteis | 2 | Página de viatura e artigos | Viatura liga à listagem da marca ou modelo, à retoma e ao financiamento; artigos ligam a stock relevante com texto descritivo | (1) Ligações só no menu | Âncoras "clique aqui" em todo o lado e nenhuma ligação contextual |
| 6.4 Sem órfãs nem becos | 2 | Sitemap contra navegação | Todas as páginas do sitemap têm ligação interna | (1) Páginas de campanha ou serviço órfãs | Páginas que vendem só alcançáveis por anúncios |

## 7. SEO local, entidade e páginas por localização real (12)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 7.1 Nome, morada e telefone iguais ao perfil | 4 | Rodapé e contactos contra o Perfil de Empresa | Iguais (diferenças de abreviatura não contam) | (2) Uma diferença real (telefone antigo, número de porta) | Morada ou telefone diferentes, ou dois nomes |
| 7.2 Contactos ou localização completos | 3 | Página de contactos | Morada com código postal, mapa, horário, telefone clicável (`tel:`), WhatsApp se o stand o usa | (1) Falta horário ou telefone clicável | Só formulário |
| 7.3 Dados estruturados da entidade | 2 | Script: `json_ld` com `AutoDealer` ou `LocalBusiness` | Nome, morada, telefone e horário iguais aos visíveis | (1) Presente com dados incompletos ou desactualizados | Ausente depois de confirmado com JavaScript, ou com dados errados |
| 7.4 Páginas por localização só onde há instalação | 3 | Lista de páginas locais | Uma página por instalação real, ou nenhuma quando há uma só e o início cumpre | (1) Páginas para zonas servidas com conteúdo próprio real (entregas, clientes, percurso) | Páginas por concelho com o mesmo texto e o nome trocado |

## 8. Listagens e páginas de viatura (12)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 8.1 Página de viatura completa e própria | 3 | Três viaturas da amostra | Marca, modelo, versão, ano, quilómetros, combustível, caixa, potência, preço, fotografias próprias e descrição que não é a do portal copiada | (1) Dados completos mas descrição genérica repetida | Dados em falta ou só em imagem |
| 8.2 Dados estruturados de viatura | 3 | Script: `json_ld` (`Car` ou `Vehicle` com `Offer`); confirmar com JavaScript | Preço, moeda EUR, disponibilidade, quilómetros e combustível iguais ao visível | (1) Presentes com campos em falta ou desactualizados | Ausentes depois de confirmado, ou a contradizer a página |
| 8.3 Viaturas vendidas tratadas | 3 | Um URL de viatura vendida; regras em [stock-rotativo.md](stock-rotativo.md) | Regra definida e aplicada (estado visível, 301 para equivalente ou 410) e fora do sitemap | (1) Regra existe mas é inconsistente | Vendidas como disponíveis, 301 em massa para o início, ou página vazia com 200 |
| 8.4 Listagens e filtros controlados | 3 | Um filtro profundo, uma ordenação e a página 2 | Marca, modelo e combustível com procura indexáveis; combinações profundas e ordenações fora do índice; paginação com ligações | (1) Filtros indexáveis sem critério, mas sem explosão de URLs | Milhares de combinações indexáveis, ou paginação que não se rastreia |

## 9. Desempenho móvel e Core Web Vitals (7)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 9.1 Dados de campo em "bom" | 4 | PageSpeed Insights (dados de campo) ou relatório de Core Web Vitals no Search Console | LCP até 2,5 s, INP até 200 ms e CLS até 0,1 no percentil 75, em telemóvel | (2) Uma métrica a precisar de melhoria | Duas ou mais em "fraco" |
| 9.2 Uso prático no telemóvel | 3 | Teste num telemóvel ou emulação | Telefone e WhatsApp clicáveis, galeria funciona, nada tapa o conteúdo, texto legível | (1) Um bloqueio (pop-up de cookies que tapa tudo, galeria lenta) | Contactar o stand no telemóvel é difícil |

Sem dados de campo (pouco tráfego), 9.1 fica `N/V`: os valores de laboratório ajudam a diagnosticar mas não substituem a experiência real. O diagnóstico detalhado é de `stand-avaliar-site`.

## 10. Idioma e hreflang (5)

| Critério | Pts | Onde e prova | Total | Parcial | 0 |
|---|---|---|---|---|---|
| 10.1 Idioma declarado e texto coerente | 2 | Script: `idioma`; texto visível | `lang` com `pt` ou `pt-PT` e conteúdo em português de Portugal | (1) `lang` em falta ou em `en` por defeito da plataforma | Páginas com línguas misturadas sem razão |
| 10.2 hreflang, quando há outras línguas | 3 | Script: `hreflang` em cada versão | Recíproco, códigos válidos, cada versão com canónico próprio | (1) Presente com erros pontuais | Ausente, sem reciprocidade ou com canónicos cruzados |

Site só em português: 10.2 não se aplica. Quando há versões noutras línguas e os problemas são muitos, a auditoria detalhada é de `stand-seo-multilingue`.
