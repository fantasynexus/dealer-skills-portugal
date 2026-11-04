# Plano de línguas do site: [nome do stand]

| Campo | Valor |
|---|---|
| Site | [URL] |
| Data | [AAAA-MM-DD] |
| Modo | decidir / desenhar / corrigir |
| Mercado principal | Português de Portugal |
| Plataforma | [plataforma ou fornecedor] |

## Decisão por língua

| Língua | Público | Procura (0 a 2) | Atendimento (0 a 2) | Manutenção (0 a 2) | Decisão | O que mudaria a decisão | Rever em |
|---|---|---|---|---|---|---|---|
| | residentes / emigrantes / turistas / fronteira / outro | | | | não agora / piloto / completa | | [data] |

### Sinais usados

| Sinal | Fonte | Período | O que mostra |
|---|---|---|---|
| | Search Console / GA4 / CRM / WhatsApp / perfil Google / gestor | | |

[Para emigrantes que pesquisam em português: a resposta é a página em português da secção "Páginas", não uma língua nova.]

## Mapa de URLs

| Página | Português | [língua] | hreflang | Prioridade |
|---|---|---|---|---|
| Início | `/` | `/en/` | sim | 1 |
| Contactos e localização | | | sim | 1 |
| Como comprar no stand | | | sim, se houver equivalente | 1 |
| Listagem de stock | | | sim | 1 ou 2 |
| Viatura | | | sim | 2 |
| Retoma | | | sim | 2 |
| Financiamento | | | sim, depois de revisão jurídica | 2 |
| Garantia | | | sim, depois de revisão jurídica | 2 |
| Oficina e pós-venda | | | sim | 3 |
| Privacidade e cookies | | | sim | antes de publicar |

## Especificação técnica

- **Arquitectura:** [português na raiz, línguas em subpastas, ou outra com a razão]
- **Códigos:** [`pt-PT`, `en`, `es`, `fr`]; `x-default` → [URL ou "não usado"]
- **Método:** [`<head>` / sitemap]; um só
- **Canónicos:** cada versão para si própria
- **Selector:** ligações para a página equivalente, nome da língua na própria língua, em todas as páginas
- **Sem redireccionamento automático** por IP ou idioma
- **Stock:** dados da mesma fonte; campos fixos por tabela revista; descrições [revistas / portuguesa assinalada]
- **Viaturas vendidas:** mesma regra em todas as línguas, ao mesmo tempo
- **Metadata:** `title`, descrição, Open Graph (`og:locale` com sublinhado) e `alt` na língua
- **Dados estruturados:** textos na língua; `AutoDealer` igual em todas as versões
- **Formulários e WhatsApp:** na língua, encaminhados para [quem atende]

## Conteúdo e tradução

| Item | Quem traduz | Quem revê | Revisão jurídica? | Prazo |
|---|---|---|---|---|
| Glossário de termos (a partir do glossário de partida) | | falante nativo | não | |
| Páginas de prioridade 1 | | | não | |
| Financiamento, garantia, privacidade | | | sim | |

## Roteiro de 30, 60 e 90 dias

| Período | Entregas | Quem | Como se confirma |
|---|---|---|---|
| Dias 1 a 30 | [arquitectura, prioridade 1 traduzida e revista, hreflang, selector, medição] | | Script em cada par; inspecção de URL |
| Dias 31 a 60 | [prioridade 2, stock, formulários na língua] | | |
| Dias 61 a 90 | [revisão do piloto: contactos na língua, horas gastas, decisão de manter, alargar ou retirar] | | |

## Correcções (modo corrigir)

| # | Diagnóstico | Correcção | Depende de | Risco | Como se confirma |
|---|---|---|---|---|---|
| 1 | | | | | |

## Medição

- Search Console: filtro por `[pasta]`, por país e por consulta.
- GA4: páginas e eventos de contacto por pasta de língua.
- CRM e WhatsApp: etiqueta de língua do contacto. Só contagens.

## Riscos e o que não fazer

- Tradução automática publicada sem revisão.
- Língua lançada sem quem atenda.
- Migrar o português para `/pt/` sem necessidade.
- Segundo perfil Google por língua.
