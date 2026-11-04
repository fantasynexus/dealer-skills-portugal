# Taxonomia de eventos recomendada para stands

Proposta para sites de stands em Portugal (usados e novos). Serve de referência para auditar o que existe e para desenhar a medição de um site novo. Nomes diferentes não são erro: a falha é a inconsistência e a falta de documentação.

Onde a Google tem um evento recomendado (`generate_lead`, `view_item`, `view_item_list`), usa esse nome, porque alguns relatórios e integrações reconhecem-no. Os restantes ficam em português, em snake_case. Confirma a lista actual de eventos recomendados na documentação da Google.

## Regras de nomes

- snake_case, minúsculas, sem acentos nem espaços: `clique_whatsapp`, não `Clique WhatsApp` nem `cliqueWhatsApp`.
- O GA4 distingue maiúsculas: `Generate_Lead` e `generate_lead` são eventos diferentes e partem os relatórios.
- Começa por letra; só letras, números e `_`. Não uses os prefixos reservados `google_`, `ga_` e `firebase_`.
- Há limites de comprimento de nomes e valores e de número de parâmetros e dimensões por propriedade. Confirma os valores actuais na documentação antes de desenhar listas longas.
- Valores de parâmetros vêm de listas fechadas, em minúsculas e snake_case (`gasoleo`, `hibrido_plug_in`). Texto livre só onde é inevitável.
- Nunca dados pessoais: email, telefone ou nome do cliente, NIF, matrícula, VIN, texto escrito pelo visitante em campos de mensagem.
- Evita micro-interacções (cada fotografia, cada scroll, cada passagem do rato): enchem relatórios sem responder a nenhuma pergunta do gestor.

## Eventos de contacto

| Evento | Quando dispara | Parâmetros | Evento-chave | No Google Ads |
|---|---|---|---|---|
| `generate_lead` | Envio de formulário de vendas confirmado pelo servidor (mensagem ou página de sucesso). Nunca no clique do botão | `tipo_lead`, `formulario_id`, `tipo_pagina`, `viatura_*` na ficha, `lead_ref` opcional | Sim | Primária |
| `pedido_oficina` | Envio confirmado de marcação ou pedido de oficina ou peças | `formulario_id`, `departamento` | Opcional | Não importar como lead de vendas |
| `clique_telefone` | Clique num link `tel:` | `tipo_pagina`, `posicao_cta`, `departamento`, `viatura_id` | Por decisão do stand | Secundária |
| `clique_whatsapp` | Clique em `wa.me` ou `api.whatsapp.com` | `tipo_pagina`, `posicao_cta`, `departamento`, `viatura_id` | Por decisão do stand | Secundária |
| `clique_email` | Clique num link `mailto:` | `tipo_pagina`, `posicao_cta` | Não | Não importar |
| `clique_mapa` | Clique para o mapa ou direcções | `tipo_pagina` | Não | Não importar |
| `saida_financiamento` | Clique para simulador ou pedido de crédito num domínio de terceiros | `viatura_id`, `tipo_pagina`, `destino` (só o domínio) | Não | Secundária, opcional |
| `simulacao_financiamento` | Simulação concluída num simulador do próprio site | `viatura_id`, `tipo_pagina` | Não | Secundária, opcional |

Notas:

- Um clique em telefone ou WhatsApp é intenção, não contacto: a pessoa pode desistir antes de ligar ou de escrever. Por isso fica secundário no Ads. As chamadas reais vêm da plataforma de rastreio (`stand-auditoria-rastreio-chamadas`); as conversas de WhatsApp só se confirmam no WhatsApp e no CRM.
- O `form_submit` da medição melhorada do GA4 pode disparar sem confirmação de envio (erro de validação, formulário em `iframe` não detectado). Não o marques como evento-chave.
- Separar `pedido_oficina` de `generate_lead` impede que marcações de oficina inflacionem os leads de vendas importados para o Ads.
- No `simulacao_financiamento` nunca envies montantes, rendimentos, prestação ou taxa: são dados financeiros do visitante.

## Eventos de stock

| Evento | Quando dispara | Parâmetros |
|---|---|---|
| `view_item_list` | Listagem de viaturas mostrada | `tipo_pagina` (`listagem`), `lista_nome` (`stock_completo`, `marca`, `pesquisa`, `campanha`) |
| `view_item` | Ficha de viatura vista | `viatura_*` |
| `filtrar_stock` | Filtro aplicado na listagem (opcional) | `filtro_tipo` (`marca`, `preco`, `combustivel`, `ano`, `quilometros`, `caixa`) |

A medição melhorada já envia `view_search_results` quando a pesquisa interna usa um parâmetro no URL; não o dupliques com outro evento.

## Parâmetros

| Parâmetro | Valores | Notas |
|---|---|---|
| `tipo_pagina` | `inicio`, `listagem`, `viatura`, `financiamento`, `retoma`, `pos_venda`, `contactos`, `institucional`, `outra` | Em todos os eventos de contacto |
| `tipo_lead` | `proposta`, `test_drive`, `retoma`, `financiamento`, `reserva`, `contacto_geral`, `venda_ao_stand` | `venda_ao_stand` é quem quer vender a viatura ao stand: é negócio de compra de stock, separa-o nos relatórios |
| `formulario_id` | Identificador estável, por exemplo `form_ficha_viatura` | Não muda quando o texto do botão muda |
| `posicao_cta` | `cabecalho`, `rodape`, `ficha_viatura`, `botao_fixo`, `listagem`, `pagina_contactos` | Diz que botão funciona |
| `departamento` | `vendas`, `oficina`, `pecas` | Para separar cliques de vendas dos de pós-venda |
| `viatura_id` | ID interno do stock | O mesmo do CRM e, se possível, do portal. Nunca matrícula nem VIN |
| `viatura_marca`, `viatura_modelo` | Texto do stock | Sempre com a mesma grafia |
| `viatura_ano` | `AAAA` | Ano do primeiro registo, como no anúncio |
| `viatura_combustivel` | `gasolina`, `gasoleo`, `hibrido`, `hibrido_plug_in`, `electrico`, `gpl`, `outro` | Lista fechada |
| `viatura_estado` | `usado`, `novo` | |
| `viatura_preco` | Inteiro em euros | O preço anunciado, já público. Não o ponhas em `value` |
| `lead_ref` | Identificador aleatório gerado no envio, também gravado no CRM | Opcional. Permite cruzar GA4 e CRM um a um. É um dado pseudonimizado: só com consentimento de análise e com validação do EPD. Muitos valores diferentes enchem a linha "(other)" nos relatórios; usa-o em explorações ou exportações |
| `value`, `currency` | Valor decidido pelo gestor, `EUR` | Só quando há decisão escrita. Nunca o preço da viatura |

Regista como dimensões personalizadas (Admin > Custom definitions) os parâmetros que queres ver em relatórios. Um parâmetro não registado chega ao GA4 mas não aparece nos relatórios padrão.

## Origem

**No GA4**, a origem da sessão vem dos UTM e da etiquetagem automática do Ads. Não cries um parâmetro de origem nos eventos do site.

Convenção para links que o stand controla (confirma no agrupamento de canais predefinido do GA4 em que canal cai cada combinação):

| Onde está o link | `utm_source` | `utm_medium` | `utm_campaign` |
|---|---|---|---|
| Site no Perfil de Empresa no Google | `google` | `organic` | `perfil_empresa` |
| Biografia ou página nas redes | `instagram`, `facebook`, `tiktok` | `social` | `perfil` |
| Publicação orgânica nas redes | `instagram`, `facebook`, `tiktok` | `social` | `AAAA-MM_tema` |
| Newsletter ou email | `newsletter` | `email` | `AAAA-MM_tema` |
| QR code em folhetos, fachada ou viaturas | `qr` | `offline` | `local` (por exemplo, `fachada`) |

Nunca ponhas UTM em links internos do próprio site: reinicia a origem a meio da visita.

**No formulário**, passa ao CRM em campos ocultos: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`, `gclid`, `gbraid`, `wbraid`, página de entrada (sem parâmetros), `viatura_id` e `formulario_id`. Para sobreviverem à navegação entre páginas, estes valores costumam ficar guardados no browser; isso também é armazenamento no equipamento do visitante, por isso valida com o EPD se depende do consentimento.

**No CRM**, mantém dois campos e não deixes um apagar o outro:

- origem técnica (dos campos ocultos ou da integração);
- origem do canal, lista fechada: `site_formulario`, `site_telefone`, `site_whatsapp`, `standvirtual`, `olx`, `outro_portal`, `perfil_google`, `google_ads_formulario`, `redes_sociais`, `telefone_directo`, `whatsapp_directo`, `presencial`, `recomendacao`, `cliente_anterior`, `outro`.

O que o cliente diz ("vi no Standvirtual") é informação útil, mas não substitui a origem técnica.

## Eventos-chave e acções de conversão

| Acção | Fonte | Optimização | Contagem |
|---|---|---|---|
| Lead de vendas do site (`generate_lead`) | Importação do GA4 ou tag do Ads, nunca as duas como primárias | Primária | Uma |
| Clique em telefone ou WhatsApp | GA4 | Secundária | Uma |
| Chamada qualificada | Plataforma de rastreio (duração mínima e categoria de vendas) | Primária por decisão escrita | Uma |
| Formulário de leads do Google | Google Ads | Primária | Uma |
| Lead válido no CRM | Importação offline | Secundária até haver decisão | Uma |
| Venda no CRM | Importação offline | Por decisão de quem gere a conta | Uma |

Não há número de conversões que garanta bons lances; decide com quem gere a conta e regista a decisão. Para enviar etapas do CRM para o GA4, a Google tem eventos recomendados de etapas de lead (por exemplo `qualify_lead` e `close_convert_lead`); confirma a lista e o método de envio actuais antes de propor.

## Exemplo: Stand Exemplo, Leiria (fictício)

Envio confirmado do formulário de test drive numa ficha de viatura:

```js
dataLayer.push({
  event: 'generate_lead',
  tipo_lead: 'test_drive',
  formulario_id: 'form_ficha_viatura',
  tipo_pagina: 'viatura',
  viatura_id: 'STK-0417',
  viatura_marca: 'Peugeot',
  viatura_modelo: '308 SW',
  viatura_ano: 2021,
  viatura_combustivel: 'gasoleo',
  viatura_estado: 'usado',
  viatura_preco: 18900
});
```

Teste de aceitação de cada evento: dispara uma vez por acção; só depois da confirmação; com os parâmetros da lista e valores das listas fechadas; sem dados pessoais no pedido; respeita o estado de consentimento; aparece no DebugView com o nome exacto.
