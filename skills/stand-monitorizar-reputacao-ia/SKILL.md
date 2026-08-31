---
name: stand-monitorizar-reputacao-ia
description: Auditar a forma como motores de IA descrevem um stand português, detectando erros, informação desactualizada e comparação injustificada. Usar quando o gestor pergunta o que ChatGPT, Gemini, Perplexity, Claude, Copilot ou Google AI dizem sobre o stand.
---

# Monitorizar a reputação do stand em IA

Mede o conteúdo e exactidão das respostas. Para medir apenas presença e quota de citação, usa a skill de visibilidade em IA; para avaliações de clientes, usa a análise de avaliações.

## Amostra

Cria perguntas sobre identidade, localização, marcas, stock, reputação, garantias, financiamento, retoma, pós-venda, equipa, pontos fortes, preocupações e comparação com concorrentes. Usa PT-PT e repete cada pergunta três vezes por motor quando possível.

Regista pergunta, resposta, data, motor/modelo visível, sessão, idioma, localização e fontes. Não combines resultados de datas ou condições diferentes sem os identificar.

## Avaliação de 100 pontos

- tom e neutralidade, 15;
- exactidão factual, 25;
- representação de pontos fortes com prova, 15;
- representação de problemas e reclamações, 15;
- enquadramento competitivo, 15;
- risco de alucinação ou desactualização, 15.

Marca afirmações como `correcta`, `imprecisa`, `desactualizada`, `sem prova` ou `inventada`. Classifica gravidade por dano potencial: baixa, média, alta ou crítica. Um nome de colaborador inventado, condição financeira falsa ou acusação sem fonte merece prioridade elevada.

## Entrega

Inclui resultado por motor, variação entre repetições, tabela de afirmações e fontes, concorrentes favorecidos, correcções nas entidades e fontes controláveis pelo stand, e cadência de repetição. Não tentes “corrigir” directamente um modelo nem prometas remoção. Reduz a causa com informação pública consistente, conteúdo verificável e pedidos formais às plataformas quando disponíveis.
