# Skills para stands

[![Validar](https://github.com/fantasynexus/dealer-skills-portugal/actions/workflows/validar.yml/badge.svg)](https://github.com/fantasynexus/dealer-skills-portugal/actions/workflows/validar.yml)
[![Licença MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-black.svg)](LICENSE)

28 skills abertas para gestores e equipas de stands de automóveis em Portugal,
pela [Onepilot](https://onepilot.app). Escrevem anúncios, respondem a leads e
avaliações, auditam o site, o Perfil Google e a presença em motores de IA,
medem de onde vêm as vendas e montam campanhas. Em português de Portugal, com
euros, RGPD, Standvirtual e OLX.

Funcionam em qualquer agente compatível com [Agent Skills](https://agentskills.io):
Claude Code, Codex, Cursor, Gemini CLI, OpenCode e outros. Catálogo com
explicações em [onepilot.app/hub/skills](https://onepilot.app/hub/skills).

## Instalar

**Em qualquer agente**, dá-lhe este pedido:

```text
Instala as skills para stands de https://github.com/fantasynexus/dealer-skills-portugal
```

**No terminal**, com Node.js:

```bash
npx skills add fantasynexus/dealer-skills-portugal                                # escolhe skills e agentes
npx skills add fantasynexus/dealer-skills-portugal --skill stand-escrever-anuncio  # só uma
```

**No Claude Code**, como plugin:

```text
/plugin install stands --marketplace fantasynexus/dealer-skills-portugal
```

Em versões anteriores à 2.1.275: `/plugin marketplace add fantasynexus/dealer-skills-portugal`
e depois `/plugin install stands@dealer-skills-portugal`.

**À mão**: copia a pasta `skills/<nome>` para a pasta de skills do teu agente.
Cada skill é autónoma e funciona sem as outras.

## Por onde começar

Não sabes qual usar? Começa por `stand-por-onde-comecar` e diz ao agente o que
queres resolver ("tenho carros parados há meses", "não aparecemos no Google").
Ela escolhe até três skills, pela ordem certa, e passa-lhes a vez.

## Catálogo

<!-- catalogo:inicio -->
### Dia-a-dia

| Skill | Para quê | Inclui |
|---|---|---|
| [Escrever anúncio](skills/stand-escrever-anuncio/SKILL.md)<br>`stand-escrever-anuncio` | Anúncio de uma viatura para portais e site, sem inventar | 3 referências · 1 modelo · 1 script |
| [Responder a leads](skills/stand-responder-leads/SKILL.md)<br>`stand-responder-leads` | Primeira resposta, qualificação e seguimento de contactos | 2 referências · 1 modelo |
| [Responder a avaliações](skills/stand-responder-avaliacoes/SKILL.md)<br>`stand-responder-avaliacoes` | Resposta pública e plano interno, sem expor o cliente | 2 referências · 1 modelo |
| [Redes sociais](skills/stand-publicar-redes-sociais/SKILL.md)<br>`stand-publicar-redes-sociais` | Publicações, guiões de vídeo curto e calendário semanal | 2 referências · 2 modelos |

### Estratégia

| Skill | Para quê | Inclui |
|---|---|---|
| [Por onde começar](skills/stand-por-onde-comecar/SKILL.md)<br>`stand-por-onde-comecar` | Escolhe a skill certa para o que o stand quer resolver | 2 referências |
| [Estratégia de pesquisa](skills/stand-estrategia-pesquisa/SKILL.md)<br>`stand-estrategia-pesquisa` | Plano de 90 dias para Google e IA, com triagem e encaminhamento | 3 referências · 1 modelo |
| [Prontidão para IA](skills/stand-auditoria-prontidao-ia/SKILL.md)<br>`stand-auditoria-prontidao-ia` | Auditoria com prova antes de comprar ou alargar IA no stand | 3 referências · 1 modelo |
| [Posicionamento do stand](skills/stand-posicionamento/SKILL.md)<br>`stand-posicionamento` | Proposta de valor com prova, voz e kit de linguagem em PT-PT | 2 referências · 1 modelo |

### Pesquisa e IA

| Skill | Para quê | Inclui |
|---|---|---|
| [Auditoria AEO e GEO](skills/stand-auditoria-aeo/SKILL.md)<br>`stand-auditoria-aeo` | Porque é que a IA não cita o stand, com provas e plano | 3 referências · 1 modelo · 3 scripts |
| [Visibilidade em IA](skills/stand-visibilidade-ia/SKILL.md)<br>`stand-visibilidade-ia` | Menções, concorrentes e fontes nas respostas de IA | 2 referências · 2 modelos |
| [Reputação em IA](skills/stand-monitorizar-reputacao-ia/SKILL.md)<br>`stand-monitorizar-reputacao-ia` | O que a IA diz do stand e se é verdade | 3 referências · 2 modelos |
| [Tráfego vindo de IA](skills/stand-analisar-trafego-ia/SKILL.md)<br>`stand-analisar-trafego-ia` | Visitas de assistentes, canal no GA4 e bots de IA | 3 referências · 1 modelo · 2 scripts |
| [Gerador de llms.txt](skills/stand-gerar-llms-txt/SKILL.md)<br>`stand-gerar-llms-txt` | llms.txt verificado, com URLs confirmados, pronto a publicar | 2 referências · 1 modelo · 2 scripts |
| [Brief de conteúdo AEO](skills/stand-brief-conteudo-aeo/SKILL.md)<br>`stand-brief-conteudo-aeo` | Brief de página com perguntas reais, provas e fontes | 3 referências · 1 modelo |

### SEO e presença local

| Skill | Para quê | Inclui |
|---|---|---|
| [Auditoria SEO](skills/stand-auditoria-seo/SKILL.md)<br>`stand-auditoria-seo` | Indexação, procura local, stock e viaturas vendidas no Google | 3 referências · 1 modelo · 1 script |
| [Perfil de Empresa Google](skills/stand-auditoria-perfil-google/SKILL.md)<br>`stand-auditoria-perfil-google` | Perfil no Maps contra a concorrência local, NAP e situações de risco | 3 referências · 1 modelo |
| [SEO multilingue](skills/stand-seo-multilingue/SKILL.md)<br>`stand-seo-multilingue` | Decidir se vale outra língua e fazê-la sem estragar o português | 3 referências · 2 modelos · 1 script |

### Site e conversão

| Skill | Para quê | Inclui |
|---|---|---|
| [Avaliação do site](skills/stand-avaliar-site/SKILL.md)<br>`stand-avaliar-site` | Nota técnica do site com provas e correcções | 2 referências · 1 modelo · 2 scripts |
| [Auditoria de CTA](skills/stand-auditoria-cta/SKILL.md)<br>`stand-auditoria-cta` | Botões, telefone, WhatsApp e formulários que geram contactos | 2 referências · 1 modelo · 1 script |
| [Anúncios de viaturas](skills/stand-rever-anuncios-viaturas/SKILL.md)<br>`stand-rever-anuncios-viaturas` | Nota por anúncio no site e nos portais, com fotos em falta | 2 referências · 1 modelo · 1 script |
| [Página de comparação](skills/stand-pagina-comparacao/SKILL.md)<br>`stand-pagina-comparacao` | Modelos, opções de compra ou stands, com fontes datadas | 2 referências · 1 modelo |

### Medição e vendas

| Skill | Para quê | Inclui |
|---|---|---|
| [GA4 e Google Ads](skills/stand-auditoria-ga4-google-ads/SKILL.md)<br>`stand-auditoria-ga4-google-ads` | Reconcilia GA4, Ads e CRM etapa a etapa | 3 referências · 1 modelo · 1 script |
| [Rastreio de chamadas](skills/stand-auditoria-rastreio-chamadas/SKILL.md)<br>`stand-auditoria-rastreio-chamadas` | Chamadas da origem ao CRM, perdidas incluídas | 3 referências · 1 modelo · 1 script |
| [Classificar chamadas](skills/stand-classificar-chamadas/SKILL.md)<br>`stand-classificar-chamadas` | Quantas chamadas são mesmo de vendas, com prova | 3 referências · 1 modelo |

### Clientes e reputação

| Skill | Para quê | Inclui |
|---|---|---|
| [Novo cliente, 90 dias](skills/stand-onboarding-cliente/SKILL.md)<br>`stand-onboarding-cliente` | Entrega, documentos, garantia, oficina e avaliação | 2 referências · 2 modelos |
| [Fluxos de email](skills/stand-fluxos-email/SKILL.md)<br>`stand-fluxos-email` | Emails automáticos do contacto à oficina, com RGPD | 2 referências · 2 modelos |
| [Campanha de retoma](skills/stand-campanha-retoma/SKILL.md)<br>`stand-campanha-retoma` | Segmentos, cadência e mensagens para renovar viaturas | 2 referências · 2 modelos |
| [Analisar avaliações](skills/stand-analisar-avaliacoes/SKILL.md)<br>`stand-analisar-avaliacoes` | Temas, sentimento e avaliações a responder | 2 referências · 1 modelo |
<!-- catalogo:fim -->

## Como uma skill está feita

```
skills/stand-auditoria-aeo/
├── SKILL.md              o fluxo: o que perguntar, os passos, a entrega, os limites
├── agents/openai.yaml    nome, descrição curta e pedido de exemplo
├── references/           detalhe que o agente lê só quando precisa (grelhas, contexto português, exemplos)
├── assets/               modelos da entrega, para o resultado sair sempre com a mesma estrutura
└── scripts/              verificações determinísticas, em Python sem dependências
```

O agente lê o `SKILL.md` quando a skill se aplica e só abre `references/`
quando o passo em que está o pede. Assim uma skill pode ter profundidade sem
encher o contexto.

Todas seguem as mesmas regras:

- **O que não foi medido diz "não verificado"** e sai da nota. Ausência de
  prova não é falha do stand.
- **Nada é inventado**: garantias, histórico, quilómetros, preços, volumes de
  pesquisa, citações. Falta um dado, pergunta-se.
- **Nada sai sem autorização**: publicar, enviar mensagens, alterar perfis ou
  configurações de medição.
- **As referências legais são listas de controlo**, não pareceres: RGPD, Lei
  n.º 41/2004, Decreto-Lei n.º 84/2021, Regulamento Europeu da IA. A skill
  manda confirmar a versão em vigor.

## Scripts incluídos

Só biblioteca padrão de Python 3.9 ou mais recente (o `python3` que vem com o
macOS serve). Aceitam um URL ou um ficheiro local e escrevem JSON. Cada skill
leva cópia dos que usa, para funcionar instalada sozinha.

<!-- scripts:inicio -->
| Script | O que faz | Skills que o levam |
|---|---|---|
| `extrair_sinais_pagina.py` | Extrai de uma página os sinais que as auditorias de um stand precisam. | 9 |
| `verificar_bots_ia.py` | Diz que agentes de IA o robots.txt de um site deixa entrar, e onde. | 4 |
| `validar_llms_txt.py` | Valida um llms.txt contra o formato de llmstxt.org e as regras das skills. | 2 |
| `classificar_referencias_ia.py` | Agrupa por motor de IA as origens de tráfego de uma exportação do GA4. | 1 |
<!-- scripts:fim -->

## Contribuir

Lê o [AGENTS.md](AGENTS.md): estrutura, regras de escrita e de conteúdo. Antes
de abrir um PR:

```bash
python3 ferramentas/sincronizar.py   # copia partilhado/scripts para as skills
python3 ferramentas/catalogo.py      # regenera este catálogo
python3 ferramentas/validar.py       # estrutura, ligações, grafia, cópias, catálogo
python3 -m unittest discover -s ferramentas/testes
```

O CI corre o mesmo em Python 3.9 e 3.13.

## Origem e licença

Esta biblioteca foi inspirada no projecto MIT
[Dealer AI Skills](https://github.com/arielcoro/dealer-ai-skills) e reescrita
para Portugal pela [Onepilot](https://onepilot.app). As skills do dia-a-dia
(anúncios, leads, avaliações, redes sociais) e os scripts são originais.

O código deste repositório está disponível sob a [licença MIT](LICENSE). A
atribuição e a licença do projecto original estão em
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
