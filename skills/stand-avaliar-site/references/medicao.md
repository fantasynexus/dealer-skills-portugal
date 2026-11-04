# Como medir

Passos e comandos para cada ferramenta da avaliação. Em todos os casos regista data e hora, ferramenta, dispositivo ou emulação e de onde mediste. Sem isso, a medição não se repete e não serve para cobrar uma correcção ao fornecedor.

## Dados de campo e dados de laboratório

| | Campo (CrUX) | Laboratório (Lighthouse) |
|---|---|---|
| O que é | Experiência real de utilizadores do Chrome que partilham estatísticas de utilização | Um carregamento simulado, num dispositivo e rede emulados |
| Janela | Últimos 28 dias, em contínuo | O momento do teste |
| Métricas | LCP, INP, CLS (e outras) no percentil 75 | LCP, CLS, Total Blocking Time, peso, oportunidades |
| INP | Sim | Não: o INP precisa de interacções reais; o TBT é o indicador mais próximo |
| Quando falta | Sites com pouco tráfego não têm amostra suficiente | Nunca falta, mas varia entre corridas |
| Serve para | Dizer se os clientes têm uma experiência boa | Explicar porquê e testar correcções |

Regras de leitura:

- A avaliação "passa ou não passa" dos Core Web Vitals é sempre de campo. Nunca digas que um site "passa os Core Web Vitals" com base no Lighthouse.
- O PageSpeed Insights mostra campo ao nível do URL quando há dados suficientes e, se não houver, ao nível da origem (o domínio todo). Diz qual usaste: um valor da origem mistura o início, a listagem e todas as viaturas.
- Uma correcção feita hoje aparece no laboratório de imediato, mas nos dados de campo só ao longo dos 28 dias seguintes. Não dês uma correcção por falhada porque o campo ainda não mudou.
- A pontuação de desempenho do Lighthouse (0 a 100) é uma síntese de laboratório. Usa as métricas, não só o número.

## Limiares da Google (percentil 75)

| Métrica | Bom | Precisa de melhorar | Fraco |
|---|---|---|---|
| LCP (maior elemento visível) | até 2,5 s | até 4 s | acima de 4 s |
| INP (resposta a interacções) | até 200 ms | até 500 ms | acima de 500 ms |
| CLS (deslocações de conteúdo) | até 0,1 | até 0,25 | acima de 0,25 |

Confirma em web.dev se os limiares mudaram desde a escrita desta referência.

## Correr o PageSpeed Insights

1. Abre https://pagespeed.web.dev/ e cola o URL completo da página (não só o domínio, excepto para o início).
2. Carrega em "Analisar" e espera pelo relatório. Repete para cada página da amostra.
3. No separador **Telemóvel**, regista o bloco de dados de campo: se a avaliação passou, os valores de LCP, INP e CLS e se são do URL ou da origem.
4. Mais abaixo, no diagnóstico de laboratório, regista a pontuação de desempenho, LCP, CLS, TBT e qual é o elemento LCP (normalmente a primeira foto da viatura ou o banner do início).
5. Repete no separador **Computador**.
6. Guarda a prova: o link do relatório, uma captura dos dois blocos ou o JSON da API.

O PageSpeed Insights não deixa escolher a localização nem o dispositivo de laboratório. Para comparar antes e depois, usa sempre a mesma ferramenta.

## API do PageSpeed Insights

Útil no modo "com rede, sem browser" e para medir várias páginas. Sem chave de API a quota é baixa; com muitas páginas, pede ao gestor uma chave do Google Cloud.

```bash
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https%3A%2F%2Fexemplo.pt%2F&strategy=mobile&category=performance&category=accessibility" -o psi-p1-movel.json
```

```bash
python3 - psi-p1-movel.json <<'EOF'
import json, sys
d = json.load(open(sys.argv[1]))
for chave in ("loadingExperience", "originLoadingExperience"):
    m = d.get(chave, {}).get("metrics", {})
    print(chave, {k: (v.get("percentile"), v.get("category")) for k, v in m.items()})
lh = d["lighthouseResult"]
print("desempenho", lh["categories"]["performance"]["score"])
for a in ("largest-contentful-paint", "cumulative-layout-shift", "total-blocking-time", "total-byte-weight"):
    print(a, lh["audits"][a]["displayValue"])
EOF
```

`loadingExperience` é o campo do URL; `originLoadingExperience` o da origem. Nos dados de campo da API, o CLS costuma vir multiplicado por 100 (5 quer dizer 0,05). Confirma os nomes e escalas na resposta que recebeste antes de os copiar para o relatório.

## Lighthouse no Chrome e na linha de comandos

No Chrome: janela anónima sem extensões, DevTools, separador Lighthouse, modo "Navegação", dispositivo "Telemóvel", categorias Desempenho e Acessibilidade.

Na linha de comandos (precisa de Node e Chrome):

```bash
npx lighthouse https://exemplo.pt/viatura/123 --only-categories=performance,accessibility --output=json --output-path=./lh-p3-movel.json --chrome-flags="--headless"
npx lighthouse https://exemplo.pt/viatura/123 --preset=desktop --only-categories=performance --output=json --output-path=./lh-p3-pc.json --chrome-flags="--headless"
```

O laboratório varia entre corridas. Corre três vezes por página e usa a mediana. Não compares um Lighthouse corrido no teu portátil com um PageSpeed Insights.

## Alojamento e segurança

Substitui `exemplo.pt` pelo domínio do stand.

```bash
# Estado final, número de saltos, versão HTTP e tempo até ao primeiro byte, partindo de http://
curl -sS -L -o /dev/null -w '%{http_code} %{url_effective} saltos=%{num_redirects} http=%{http_version} ttfb=%{time_starttransfer}\n' http://exemplo.pt/

# Mediana de cinco medições do tempo até ao primeiro byte
for i in 1 2 3 4 5; do curl -sS -o /dev/null -w '%{time_starttransfer}\n' https://exemplo.pt/; done | sort -n | sed -n 3p

# Cabeçalhos de segurança e sinais de CDN
curl -sSI https://exemplo.pt/ | grep -iE 'strict-transport-security|x-content-type-options|content-security-policy|server|cf-cache-status|x-cache'

# Validade e emissor do certificado
echo | openssl s_client -connect exemplo.pt:443 -servername exemplo.pt 2>/dev/null | openssl x509 -noout -dates -issuer -subject

# Indício de conteúdo misto no HTML inicial
curl -sSL https://exemplo.pt/ | grep -oiE '(src|href)="http://[^"]+' | head
```

Repete o primeiro comando para `http://www.exemplo.pt/` e `https://www.exemplo.pt/`: todas as variantes devem acabar no mesmo endereço. Para o pormenor de TLS, o SSL Labs (https://www.ssllabs.com/ssltest/) faz um teste público; num site de concorrente, marca a opção para não publicar o resultado.

## Consentimento: o que dispara antes de escolher

1. Janela anónima, DevTools aberto, separador Rede com "Preservar registo" activo.
2. Abre o início e **não** carregues no banner.
3. Filtra por `google-analytics`, `googletagmanager`, `collect`, `googleadservices`, `doubleclick`, `facebook`, `tiktok`, `clarity`, `hotjar` e pelos fornecedores de chat.
4. No separador Aplicação, vê que cookies existem. Regista nomes e domínios, não valores.
5. Repete depois de "Rejeitar" e depois de "Aceitar".

Com o modo de consentimento da Google em versão avançada, o GA4 pode enviar pedidos sem cookies antes da escolha, com o parâmetro `gcs=G100`. Não é o mesmo que etiquetas a funcionar sem consentimento, mas regista-o e pergunta se foi uma decisão consciente. O banner pode estar configurado só para visitantes da União Europeia: se testas de fora, diz que o resultado pode não representar um cliente em Portugal.

O script `extrair_sinais_pagina.py` vê etiquetas e a plataforma de consentimento escritas no HTML inicial; o que o GTM carrega depois só aparece no browser.

## Dados estruturados

- Teste de resultados enriquecidos (https://search.google.com/test/rich-results): diz o que a Google lê e se é elegível para algum resultado enriquecido.
- Schema Markup Validator (https://validator.schema.org/): valida a marcação em geral, incluindo tipos que a Google não usa.
- Compara sempre o que a marcação diz com o que a página mostra: preço, quilómetros, disponibilidade, morada e telefone.

## Acessibilidade

O Lighthouse e outras ferramentas automáticas apanham só parte dos problemas. Completa com:

- Tab por toda a página de viatura e pelo formulário, a ver onde está o foco;
- zoom do browser a 200%;
- leitura do formulário sem cor (os erros explicam-se em texto?);
- contraste dos botões e dos preços com uma ferramenta de contraste.

## Search Console (com acesso)

Abre: Indexação de páginas (motivos de exclusão, filtrados pelo padrão de URL das viaturas), Sitemaps (estado e URLs descobertos), Core Web Vitals (grupos de URLs, dados de campo) e Inspecção de URL numa viatura recente (indexada? que canónico escolheu a Google?). Regista os números com a data; o relatório tem atraso de alguns dias.

## Repetir depois das correcções

Volta a medir as mesmas páginas, com as mesmas ferramentas e modos, e compara lado a lado. Para dados de campo, espera pelo fim da janela de 28 dias antes de concluir.
