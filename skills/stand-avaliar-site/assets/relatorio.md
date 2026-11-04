# Avaliação técnica do site: [nome do stand]

- **Site:** [URL principal]
- **Testes feitos em:** [AAAA-MM-DD, hh:mm a hh:mm]
- **Modo:** [com rede e browser / com rede, sem browser / documental]
- **Site de:** [o próprio stand / concorrente, só verificações públicas]
- **Plataforma ou fornecedor:** [se conhecido, senão "não identificado"]
- **Acessos usados:** [Search Console, GA4, painel de consentimento, nenhum]
- **Testado a partir de:** [país ou serviço; dispositivo ou emulação]

## Veredicto

[Duas a quatro frases em linguagem de gestor: o que mais trava o site e o que fazer primeiro.]

**Bloqueios críticos:** [lista, ou "nenhum observado"]

| Nota | Cobertura | Estado |
|---|---|---|
| [n]/100 | [c]% dos pontos aplicáveis | [final / provisória, cobertura abaixo de 70%] |

## Amostra

| ID | Página | URL | Testada com |
|---|---|---|---|
| P1 | Início | [URL] | [script, PSI, browser] |
| P2 | Listagem | [URL] | |
| P3 | Viatura 1 ([ano], [faixa de preço]) | [URL] | |
| P4 | Viatura 2 | [URL] | |
| P5 | Viatura 3 | [URL] | |
| P6 | Financiamento | [URL ou "não existe"] | |
| P7 | Retoma | [URL ou "não existe"] | |
| P8 | Oficina | [URL ou "não existe"] | |
| P9 | Contactos | [URL] | |
| P10 | Página local | [URL ou "não existe"] | |

## Resultado por dimensão

| # | Dimensão | Obtidos | Verificados | Leitura | Verificações mais fracas |
|---|---|---|---|---|---|
| 1 | Core Web Vitals e peso | | /10 | [forte / misto / fraco] | [ex.: 1.2 LCP 5,1 s em P3] |
| 2 | Disponibilidade, HTTPS e segurança | | /10 | | |
| 3 | Rastreabilidade e indexação | | /10 | | |
| 4 | Dados estruturados e entidade | | /10 | | |
| 5 | Experiência móvel e navegação | | /10 | | |
| 6 | Acessibilidade | | /10 | | |
| 7 | Terceiros, cookies e consentimento | | /10 | | |
| 8 | Contacto | | /10 | | |
| 9 | Páginas e feeds de viatura | | /10 | | |
| 10 | Confiança | | /10 | | |
| | **Total** | **[obtidos]** | **[verificados]** | | |

## Desempenho medido

| Página | Campo: LCP / INP / CLS (URL ou origem) | Lab móvel: LCP / CLS / TBT | Peso | Elemento LCP |
|---|---|---|---|---|
| P1 | [valores ou "sem dados de campo"] | | | |
| P3 | | | | |
| P4 | | | | |

## Cinco problemas prioritários

### 1. [Problema, em uma frase]

- **Prova:** [E3: o que se observou, com valor medido]
- **Páginas afectadas:** [P3, P4, P5 ou "todas as viaturas"]
- **Impacto:** [pontos perdidos e o que significa para o cliente; sem estimar vendas sem dados]
- **Correcção:** [concreta, na página ou no modelo]
- **Responsável provável:** [stand / fornecedor do site / alojamento / agência]
- **Esforço:** [baixo / médio / alto]
- **Como validar:** [teste a repetir e resultado esperado]

[Repetir para 2 a 5.]

## Rápido e estrutural

| Rápido (conteúdo e configuração) | Estrutural (modelo, plataforma, fornecedor) |
|---|---|
| [ex.: ligar telefones com `tel:+351`] | [ex.: reduzir scripts que bloqueiam a primeira renderização] |

## Não verificado

| Verificação | Porquê | O que é preciso para medir |
|---|---|---|
| [1.1 Campo] | [sem dados no CrUX] | [tráfego suficiente ou medição própria no site] |
| [3.6 Indexação] | [sem acesso ao Search Console] | [acesso de leitura] |
| [8.4 Entrega do formulário] | [sem autorização para enviar] | [autorização e um contacto de teste] |

## Provas

| ID | URL ou ficheiro | Método | Data e hora | Observação | Limitação |
|---|---|---|---|---|---|
| E1 | [URL] | `extrair_sinais_pagina.py` | | | [não executa JavaScript] |
| E2 | [URL] | PageSpeed Insights, telemóvel | | | |

## Revalidação

Depois das correcções, repete as mesmas medições nas mesmas páginas, com as mesmas ferramentas e modos. Os dados de campo demoram até 28 dias a reflectir uma mudança.

## Limitações

Avaliação pontual de uma amostra. Não é auditoria de segurança nem declaração de conformidade com o RGPD ou com regras de acessibilidade. [Acrescentar limitações específicas: bloqueios anti-bot, páginas fora da amostra, testes feitos de fora de Portugal.]
