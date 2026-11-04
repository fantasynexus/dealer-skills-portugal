# Auditoria de chamadas à acção: [nome do stand]

- **Site:** [URL]
- **Data:** [AAAA-MM-DD]
- **Modo:** [uma página / amostra / site inteiro]
- **Páginas auditadas:** [n] | **CTA inventariados:** [n]
- **Processo comercial indicado pelo stand:** [ex.: proposta por WhatsApp, depois visita]
- **Testes de envio:** [autorizados com o contacto X / não autorizados: entrega `N/V`]
- **Acessos:** [GA4, GTM, CRM, nenhum]
- **Dispositivos:** [emulação 360 × 740 / iPhone real / Android real]

## Em resumo

**[Uma frase com o problema que mais custa, com números da amostra. Ex.: "Em 3 das 3 viaturas, o telefone não liga no telemóvel e há três botões principais iguais."]**

| Nota da amostra | Cobertura | Estado |
|---|---|---|
| [n]/100 | [c]% | [final / provisória] |

**Bloqueios:** [telefone, WhatsApp ou formulário que não funcionam; ou "nenhum observado"]

## Nota por página

| Página | Tipo | Nota | Vis. /15 | Hier. /20 | Móvel /20 | Texto /15 | Intenção /15 | Form. /10 | Medição /5 |
|---|---|---|---|---|---|---|---|---|---|
| [URL] | Início | | | | | | | | |
| [URL] | Viatura | | | | | | | | |

Valores `N/V` ficam assinalados na célula e saem do denominador.

## Inventário por página

### [Tipo de página]: [URL]

| # | Texto | Tipo | Destino | Posição | Prioridade | 1.º ecrã móvel | Evento | Dados pedidos | Problemas |
|---|---|---|---|---|---|---|---|---|---|
| 1 | "[texto exacto]" | | | | | | | | |

- **Acção principal esperada:** [segundo os padrões e o processo do stand]
- **Conflitos de hierarquia:** [quais e porquê]
- **Telemóvel:** [o que falhou no toque, teclado, sobreposição]
- **Caminho até ao fim:** [confirmação vista / `N/V`; a viatura e a origem chegam ao CRM? / `N/V`]

[Repetir por página.]

## Padrões da amostra

| Padrão | Páginas | Origem provável | Responsável |
|---|---|---|---|
| [ex.: telefone em texto simples] | [todas as viaturas] | [modelo de página] | [fornecedor do site] |

## Textos de substituição

| Página | Antes | Depois | Porquê |
|---|---|---|---|
| Viatura | "Contactar" | "Pedir proposta para este carro" | Diz o que o cliente recebe e liga a acção à viatura |

Microtextos propostos (confirmados com o stand): [lista]

## Correcções por impacto

| Prioridade | Problema | Páginas | Correcção | Responsável | Esforço | Como validar |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

**Rápido (texto e configuração):** [lista]
**Modelo de página (fornecedor):** [lista]
**Processo (equipa):** [ex.: atender o WhatsApp no horário anunciado]

## Plano de experiências

| Hipótese | Alteração | Métrica principal | Métrica de controlo | Duração | Decisão |
|---|---|---|---|---|---|
| | | | | | |

[Se o tráfego for baixo: dizer que o teste A/B não terá conclusão e propor medição antes e depois, com datas.]

## Não verificado

| Verificação | Porquê | O que é preciso |
|---|---|---|
| [6.3 Confirmação do formulário] | [sem autorização para enviar] | [autorização e contacto de teste] |
| [7.1 Eventos] | [sem acesso ao GA4] | [acesso de leitura ou DebugView] |

## Limitações

Recomendações baseadas em boas práticas e na prova recolhida; o efeito real só se conhece medindo. As notas legais são listas de controlo, não pareceres. [Acrescentar: páginas fora da amostra, testes só em emulação.]
