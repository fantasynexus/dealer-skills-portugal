---
name: stand-auditoria-rastreio-chamadas
description: Auditar rastreio e atribuição de chamadas num stand em Portugal. Usar para validar números dinâmicos, origem, encaminhamento, gravação, eventos GA4/Ads e correspondência entre a plataforma de chamadas e o CRM.
---

# Auditoria de rastreio de chamadas

Serve qualquer fornecedor de call tracking. Não assumes CallRail, Invoca ou outra plataforma norte-americana.

## Antes dos testes

Confirma autorização, números de teste, horários, IVR, destinos e política de gravação. Não graves chamadas reais para experimentar. Em Portugal, valida com o encarregado de protecção de dados ou jurista as finalidades admitidas, informação prévia, acessos e prazos de retenção.

## Auditoria de 100 pontos

1. inventário e propriedade dos números, 8;
2. inserção dinâmica e persistência por sessão, 12;
3. dimensão do conjunto de números e colisões, 8;
4. mapeamento de origem, campanha e UTM, 10;
5. encaminhamento, IVR, horários e chamadas perdidas, 12;
6. classificação e revisão humana, 10;
7. eventos e conversões no GA4 e Google Ads, 10;
8. criação e deduplicação no CRM, 12;
9. gravação, acesso, aviso, retenção e direitos, 10;
10. reconciliação e alertas, 8.

## Testes

Faz chamadas controladas por origem e dispositivo, incluindo móvel, pesquisa paga e orgânica quando autorizado. Verifica troca do número, destino, ID, duração, gravação esperada, evento, conversão e lead no CRM. Regista falhas sem usar contactos de clientes.

## Entrega

Inclui mapa `origem → número → encaminhamento → plataforma → GA4/Ads → CRM`, nota e cobertura, tabela dos testes, reconciliação para o mesmo período e correcções priorizadas. Separa chamadas totais, atendidas, qualificadas, leads e vendas; nunca infles “chamadas de vendas”.
