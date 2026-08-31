---
name: stand-analisar-trafego-ia
description: Configurar ou auditar a medição de tráfego enviado por assistentes e motores de IA para um stand. Usar para separar referências de ChatGPT, Perplexity, Gemini, Copilot e outros no GA4, estudar páginas de entrada, conversão e rastreio de bots em logs.
---

# Analisar tráfego vindo de IA

Distingue visitas humanas referenciadas por ferramentas de IA de crawlers automáticos. O GA4 não mede bots que não executam JavaScript e parte do tráfego humano pode surgir como directo.

## Escolher o modo

- **Configurar:** ainda não há um canal ou exploração para referências de IA.
- **Auditar:** já existem dados e é preciso validar a implementação e criar uma linha de base.

## Fontes

Usa, quando autorizadas, GA4, Search Console, logs do servidor/CDN e CRM. Mantém uma lista datada de domínios e user agents observados, porque mudam. Não atribuas “Google AI Overview” apenas pela queda de CTR; trata-a como hipótese até haver prova adicional.

## Auditoria de 100 pontos

1. detecção e manutenção de referenciadores, 15;
2. grupo de canais, dimensão e exploração GA4, 15;
3. volume, tendência e qualidade por motor, 10;
4. páginas de entrada e intenção, 10;
5. eventos, leads e vendas no CRM, 15;
6. comparação com orgânico e outros canais, 10;
7. Search Console e mudanças de CTR, 10;
8. crawlers de IA nos logs, robots e resposta técnica, 15.

## Entrega

Produz definição exacta do canal, expressões ou regras configuráveis, inventário de fontes, linha de base por período, páginas de entrada, funil até venda e relatório separado de bots. Indica cobertura, limites de atribuição, amostras pequenas e mudanças de definição.

Não envies logs brutos com IPs, emails ou parâmetros pessoais para serviços externos. Não bloqueies ou permitas crawlers sem autorização do dono do site e avaliação do efeito em pesquisa e licenciamento de conteúdo.
