# Auditoria AEO e GEO: [nome do stand]

| Campo | Valor |
|---|---|
| Site | [URL] |
| Data da auditoria | [AAAA-MM-DD] |
| Modo | [público / com acesso / documental] |
| Amostra | [n.º de páginas e quais; exclusões] |
| Motores testados | [motor, modo, sessão; os não testados ficam listados como N/V] |
| Nota global | [x]% sobre [y] pontos verificados [provisória, se cobertura < 70%] |
| Cobertura | [verificações pontuadas] de [aplicáveis] ([z]%) |
| Banda | [banda, ou "sem banda: nota provisória"] |
| Documentação dos fornecedores confirmada em | [data] |

## Veredicto

[Duas a quatro frases: o que mais impede o stand de ser compreendido e
citado. Bloqueios críticos primeiro, mesmo com nota alta.]

**Bloqueios críticos:** [lista, ou "nenhum observado"]

## Notas por dimensão

| N.º | Dimensão | Nota (0 a 10) | Verificadas | Leitura | Verificações abaixo de 2 |
|---|---|---|---|---|---|
| 1 | Acesso de bots e robots.txt | | /3 | | |
| 2 | Indexação e base técnica | | /3 | | |
| 3 | Identidade consistente | | /3 | | |
| 4 | Dados estruturados | | /3 | | |
| 5 | Conteúdo que responde a perguntas | | /3 | | |
| 6 | Stock e serviços com factos citáveis | | /3 | | |
| 7 | Presença fora do site | | /3 | | |
| 8 | Avaliações e reclamações | | /3 | | |
| 9 | Sitemap e llms.txt | | /2 | | |
| 10 | Testes ao vivo nos motores | | /3 | | |

Leitura: forte (8 ou mais), mista (5 a menos de 8), fraca (2 a menos de 5), crítica (menos de 2), N/V.

## Provas

| ID | Verificação | URL ou artefacto | Método | Data e hora | Observação | Limitação |
|---|---|---|---|---|---|---|
| P1 | 1.1 | [URL do robots.txt] | verificar_bots_ia.py | | | robots.txt não prova visitas |

## Bots de IA

| Agente | Finalidade | Caminhos bloqueados | Regra | Teste de acesso |
|---|---|---|---|---|

Política de treino do stand: [permitido / bloqueado / sem decisão; intencional ou omissão da plataforma]

## Testes ao vivo

| ID | Motor e modo | Sessão | Data e hora | Pergunta exacta | Stand mencionado | Factos errados | Fontes citadas | Concorrentes |
|---|---|---|---|---|---|---|---|---|

Motores não testados: [lista e motivo]

## Erros factuais nas respostas

| Facto | O que o motor disse | Correcto (fonte) | Gravidade | Origem provável |
|---|---|---|---|---|

## Fontes que os motores usam

[Domínios citados, agrupados por origem: site do stand, Perfil de Empresa,
portais, imprensa, directórios, redes, concorrentes. Contagem por motor.]

## Cinco lacunas prioritárias

| # | Verificação | Porque importa | Correcção | Prova de conclusão |
|---|---|---|---|---|
| 1 | | | | |

## Plano 7 / 30 / 90 dias

| Prazo | Acção | Página ou sistema | Responsável | Esforço | Prova de conclusão | Métrica |
|---|---|---|---|---|---|---|
| 7 dias | | | [stand / fornecedor do site / agência] | [baixo / médio / alto] | | |
| 30 dias | | | | | | |
| 90 dias | | | | | | |

Esforço: baixo (horas), médio (dias), alto (semanas).

## Dados estruturados propostos

[Só quando a dimensão 4 falhou. JSON-LD do AutoDealer e de uma ficha com os
dados reais do stand; `[CONFIRMAR]` em tudo o que não foi verificado.]

## O que não foi verificado

[Verificações N/V e o acesso que as desbloqueia: Search Console, painel da
CDN, registos do servidor, motores sem acesso, DMS.]

## Reteste

Repetir as mesmas perguntas, nos mesmos motores e condições, depois das
correcções principais. Data proposta: [AAAA-MM-DD].

## Limites desta auditoria

As respostas dos motores variam de execução para execução. Uma nota alta não
garante citações, tráfego nem vendas, e uma nota baixa não é prova de vendas
perdidas. A auditoria é pública e não avalia segurança nem cumprimento legal.
