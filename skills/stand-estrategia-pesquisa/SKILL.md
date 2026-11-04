---
name: stand-estrategia-pesquisa
description: Criar a estratégia de pesquisa de um stand automóvel em Portugal, um plano único de 90 dias para aparecer no Google (SEO e pesquisa local), no Perfil de Empresa e nas respostas de ChatGPT, Gemini, Perplexity, Claude, Copilot e resumos de IA da Google (AEO/GEO). Usar quando o gestor pergunta como aparecer mais no Google ou nas IAs, quer perceber a diferença entre SEO, AEO e GEO, tem auditorias soltas e precisa de as juntar em prioridades, quer rever o plano do trimestre ou avaliar a proposta de uma agência de SEO. Faz uma triagem rápida, decide a ordem e encaminha para as skills de auditoria e execução em vez de as repetir.
---

# Estratégia de pesquisa para stands

Junta num plano de 90 dias o que faz o stand aparecer no Google e nas respostas de motores de IA. É a skill de coordenação do grupo de pesquisa: faz uma triagem curta, encontra os bloqueios, decide a ordem e entrega cada trabalho à skill que o executa. Não repete auditorias. Quando uma é precisa, nomeia-a e diz o que se espera dela.

## SEO, AEO e GEO

Abre sempre o plano com esta distinção, em linguagem simples. Dá à equipa e a quem vende serviços ao stand o mesmo vocabulário.

- **SEO:** aparecer na lista de resultados do Google e do Bing, onde a pessoa escolhe um link. Inclui a pesquisa local (Maps e Perfil de Empresa). Mede-se no Search Console e, no fim, em contactos.
- **AEO/GEO:** ser compreendido e citado quando um motor monta uma resposta. Nesta biblioteca são a mesma disciplina. Mede-se em menções, exactidão e fontes citadas, com testes datados.

Uma posição no Google não é uma citação numa IA. Mede e relata as duas em separado.

## Antes de começar

Pede: nome comercial e legal, URL oficial, concelho e zonas realmente servidas, localizações, tipo e dimensão do stock, marcas e segmentos, serviços (oficina, financiamento, retoma), objectivo do gestor, concorrentes que ele reconhece, quem na equipa pode executar e quantas horas por semana, fornecedor do site e quem controla as contas (Search Console, GA4, Perfil de Empresa).

Escolhe o modo:

- **A. Do zero:** não há auditorias. Faz a triagem pública e o plano manda correr as auditorias necessárias no primeiro mês.
- **B. A partir de auditorias:** o gestor traz resultados de outras skills ou de terceiros. Usa-os como prova medida, com data, e só faz triagem do que falta.
- **C. Revisão trimestral:** há um plano anterior. Compara indicadores com a linha de base, aplica as regras de decisão escritas e refaz os 90 dias seguintes.
- **D. Proposta de agência:** o gestor quer saber se uma proposta de SEO ou IA faz sentido. Compara-a com a triagem e com a lista de sinais de alerta.

Sem acesso às contas, trabalha em modo público e marca `N/V` o que só se vê por dentro. Pára e pergunta quando há mais de um domínio e não sabes qual é o oficial, quando não está claro que localizações entram, ou quando o pedido é só publicidade paga (fora do âmbito; para medir Ads usa `stand-auditoria-ga4-google-ads`).

## Passos

1. **Ficha do stand.** Regista os dados recolhidos com a fonte de cada um (gestor, site, Perfil). Resultado: ficha com campos em falta marcados.
2. **Inventário de provas.** Lista o que já existe: auditorias, exportações do Search Console ou GA4, relatórios de agência, testes em IA. Para cada uma: data, autor, cobertura. Prova com mais de seis meses conta como contexto, não como estado actual.
3. **Triagem por pilar.** Lê [references/pilares-e-encaminhamento.md](references/pilares-e-encaminhamento.md). Faz só as verificações rápidas de cada pilar e classifica-o `Forte`, `Misto`, `Fraco` ou `N/V`, com a prova e o tipo (medido, observado, declarado). Resultado: tabela de situação.
4. **Bloqueios.** Procura os bloqueios listados na referência (site fora do índice, Perfil suspenso ou errado, telefone ou morada diferentes entre fontes, stock que o Google não consegue ler). Se houver um, é a prioridade `agora` e o resto do plano depende dele.
5. **Mapa de procura.** Lê [references/procura-e-medicao.md](references/procura-e-medicao.md). Cruza intenções, zonas servidas e stock real. Para cada intenção, diz que página ou superfície deve responder e se existe. Não atribuas volumes sem fonte e data.
6. **Sequência e encaminhamento.** Ordena: bloqueios, medição de partida, consistência da identidade e avaliações, conteúdo, autoridade externa. Prefere acções que mexem em dois pilares. Cada acção leva a skill que a executa, responsável, esforço estimado, prova de conclusão e indicador. Não ponhas mais frentes em paralelo do que as horas da equipa permitem.
7. **Medição e regras de decisão.** Define o quadro de métricas, a linha de base com data e, para cada frente, a regra `expandir / corrigir / parar` com os limiares acordados com o gestor a partir da linha de base, nunca de médias do sector.
8. **Entrega.** Preenche [assets/modelo-estrategia.md](assets/modelo-estrategia.md). Para calibrar o nível de detalhe, vê [references/exemplo-resolvido.md](references/exemplo-resolvido.md).

No modo D, entre os passos 3 e 6, avalia a proposta com a lista da referência de pilares e diz que parte dela fecha uma lacuna real.

## Ferramentas

Esta skill não traz scripts: as verificações técnicas pertencem às skills de execução (`stand-avaliar-site`, `stand-auditoria-aeo` e `stand-analisar-trafego-ia` trazem os seus).

- [Nota de visibilidade online](https://onepilot.app/hub/ferramentas/visibilidade): dá numa só passagem Perfil Google, avaliações, concorrentes da zona, velocidade do site e palavras-chave. Serve para a triagem dos pilares 2 e 4; regista a data e trata o resultado como observado.
- [Link de avaliações do Google](https://onepilot.app/hub/ferramentas/link-avaliacoes): para a acção de pedir avaliações, quando o pilar 4 sai fraco.

## Entrega

Um documento em Markdown, com a estrutura do modelo:

- resumo executivo com a principal limitação e a principal oportunidade;
- SEO, AEO e GEO explicados para este stand;
- situação por pilar, separando medido, observado, declarado e `N/V`;
- bloqueios, se existirem;
- mapa de procura com compra, retoma, financiamento, oficina e localização;
- prioridades `agora`, `30 dias`, `60 dias` e `90 dias`, cada uma com skill, responsável, esforço, prova de conclusão e indicador;
- quadro de métricas com linha de base: Search Console, Perfil de Empresa, chamadas e contactos, citações em IA, leads e vendas confirmadas no CRM;
- regras de decisão, dependências e riscos (acessos, consentimento, fornecedor do site, qualidade dos dados);
- registo de todos os testes feitos.

## Limites

- Não prometas primeiro lugar, presença garantida numa resposta de IA nem prazos para resultados. Usa datas de revisão, não previsões.
- Não inventes volumes de pesquisa, posições, citações, taxas de conversão nem retorno financeiro. Sem fonte, fica `N/V`.
- Regista data, motor ou superfície, localização, conta e idioma de cada teste. Uma resposta isolada de um motor de IA é uma observação, não uma medição.
- Não recomendes mudar de plataforma do site por defeito. Primeiro pede ao fornecedor actual o que falta; a migração só entra com prova de que ele não o consegue fazer.
- Não copies tácticas de um concorrente nomeado. A concorrência informa o plano, não o define.
- Não alteres robots.txt, Perfil de Empresa, Search Console ou o site. Propõe; quem tem autorização executa.
- Referências a consentimento e cookies (RGPD, Lei n.º 41/2004) são listas de controlo operacionais, não parecer jurídico. Confirma a versão em vigor.
