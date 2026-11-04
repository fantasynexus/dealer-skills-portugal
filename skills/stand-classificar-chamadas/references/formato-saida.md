# Formato de saída

O formato é fixo para que um lote de hoje se compare com o do mês seguinte e para que o ficheiro entre numa folha de cálculo ou no CRM sem limpeza. Não acrescentes, tires nem renomeies colunas. Versão do formato: `1.0`.

## Colunas, por esta ordem

| # | Coluna | Valores | Regra |
|---|---|---|---|
| 1 | `id_chamada` | Texto | O ID da entrada; sem ID, `C001`, `C002`… |
| 2 | `data_hora` | `AAAA-MM-DDTHH:MM` ou vazio | Da entrada; nunca estimada |
| 3 | `direccao` | `entrada`, `saida`, `nao_referido` | Da entrada ou da transcrição ("estou a ligar por causa do seu pedido" é `saida`) |
| 4 | `duracao_s` | Inteiro ou vazio | Da entrada; nunca estimada |
| 5 | `categoria` | `vendas`, `pos_venda`, `pecas`, `financiamento`, `outros` | Ver [rubrica.md](rubrica.md) |
| 6 | `subcategoria` | Lista da rubrica | Sempre preenchida |
| 7 | `confianca` | `alta`, `media`, `baixa` | Sem acentos no ficheiro; no relatório escreve "média" |
| 8 | `rever` | `sim`, `nao` | `sim` sempre que a confiança é baixa |
| 9 | `motivo_revisao` | Texto curto ou vazio | Só com `rever = sim` |
| 10 | `intencao_secundaria` | Uma categoria ou vazio | Quando há duas finalidades |
| 11 | `sinal_vendas` | `sim`, `nao` ou vazio | Vazio em `vendas` |
| 12 | `prova` | Citação até cerca de 25 palavras | Dados pessoais substituídos |
| 13 | `motivo` | Uma frase | Liga a prova à categoria |
| 14 | `viatura_interesse` | Texto ou `nao_referido` | Só em `vendas` |
| 15 | `novo_usado` | `novo`, `usado`, `nao_referido` | Só em `vendas` |
| 16 | `retoma` | `sim`, `nao`, `nao_referido`, `nao_aplicavel` | Só em `vendas` |
| 17 | `origem_declarada` | Lista da rubrica | Só em `vendas` |
| 18 | `proxima_accao` | Lista da rubrica | Só em `vendas` |
| 19 | `nome_captado` | `sim`, `nao`, `incerto` | Só em `vendas` |
| 20 | `contacto_captado` | `sim`, `nao`, `incerto` | Só em `vendas` |
| 21 | `contacto_novo` | `sim`, `nao`, `nao_referido` | Só em `vendas` |

Fora de `vendas`, as colunas 14 a 21 ficam vazias (no JSON, `null`).

## CSV

- Codificação UTF-8.
- Separador `;`, para abrir directamente no Excel configurado em português.
- Primeira linha com os nomes das colunas exactamente como acima.
- Aspas duplas à volta de qualquer campo com `;`, aspas ou quebra de linha; aspas dentro do campo duplicadas (`""`).
- Uma linha por chamada. Sem linhas de total nem comentários.

```csv
id_chamada;data_hora;direccao;duracao_s;categoria;subcategoria;confianca;rever;motivo_revisao;intencao_secundaria;sinal_vendas;prova;motivo;viatura_interesse;novo_usado;retoma;origem_declarada;proxima_accao;nome_captado;contacto_captado;contacto_novo
C001;2026-10-07T10:12;entrada;148;vendas;compra;alta;nao;;;;"Vi no Standvirtual um Renault Clio usado, de 2020, a gasóleo. Ainda está disponível?";Pergunta por uma viatura concreta do portal e marca visita com retoma.;Renault Clio 2020 gasóleo;usado;sim;standvirtual;visita_marcada;sim;sim;sim
C002;2026-10-07T11:40;entrada;95;pos_venda;oficina;alta;nao;;;sim;"Queria marcar a revisão do meu Ford Focus. Já agora, têm algum SUV mais recente?";"Marca a revisão; o interesse no SUV fica sem passo concreto.";;;;;;;;
C003;2026-10-07T12:05;entrada;14;vendas;compra;baixa;sim;cortada antes do pedido;;;"liguei por causa do Peugeot que têm no OLX, queria saber se aceit";"Interesse provável numa viatura do OLX; a chamada corta antes do pedido.";Peugeot (modelo não referido);nao_referido;nao_referido;olx;nao_referido;nao;nao;sim
```

## JSON

```json
{
  "versao_formato": "1.0",
  "meta": {
    "data_analise": "2026-11-04",
    "fonte": "exportação CSV da plataforma de chamadas",
    "periodo": { "inicio": "2026-10-01", "fim": "2026-10-31" },
    "fuso": "Europe/Lisbon",
    "recebidas": 3,
    "classificadas": 3
  },
  "chamadas": [
    {
      "id_chamada": "C002",
      "data_hora": "2026-10-07T11:40",
      "direccao": "entrada",
      "duracao_s": 95,
      "categoria": "pos_venda",
      "subcategoria": "oficina",
      "confianca": "alta",
      "rever": "nao",
      "motivo_revisao": null,
      "intencao_secundaria": null,
      "sinal_vendas": "sim",
      "prova": "Queria marcar a revisão do meu Ford Focus. Já agora, têm algum SUV mais recente?",
      "motivo": "Marca a revisão; o interesse no SUV fica sem passo concreto.",
      "viatura_interesse": null,
      "novo_usado": null,
      "retoma": null,
      "origem_declarada": null,
      "proxima_accao": null,
      "nome_captado": null,
      "contacto_captado": null,
      "contacto_novo": null
    }
  ],
  "resumo": {
    "por_categoria": {
      "vendas": { "total": 2, "em_revisao": 1 },
      "pos_venda": { "total": 1, "em_revisao": 0 },
      "pecas": { "total": 0, "em_revisao": 0 },
      "financiamento": { "total": 0, "em_revisao": 0 },
      "outros": { "total": 0, "em_revisao": 0 }
    },
    "contactos_vendas": 1,
    "contactos_novos_compra": 1,
    "vendas_ao_stand": 0,
    "leads_validos_amostra": 1,
    "marcacoes": 1,
    "em_revisao": 1,
    "sinais_vendas": 1
  }
}
```

O exemplo mostra uma só chamada em `chamadas` para poupar espaço; no ficheiro real vão todas, pela ordem da entrada. Campos vazios são `null`, nunca `""` nem omitidos.

## Resumo: como se calcula

Todas as contagens do resumo excluem `rever = sim`, salvo `por_categoria` e `em_revisao`.

| Indicador | Definição |
|---|---|
| `por_categoria` | Todas as chamadas por categoria, com quantas estão em revisão |
| `contactos_vendas` | `categoria = vendas` |
| `contactos_novos_compra` | `vendas`, `subcategoria = compra`, `contacto_novo = sim`, `direccao = entrada`. É o número principal |
| `vendas_ao_stand` | `vendas`, `subcategoria = venda_ao_stand`. Nunca somado aos compradores |
| `leads_validos_amostra` | Contactos novos de compra com `contacto_captado = sim` |
| `marcacoes` | `vendas` com `proxima_accao` em `visita_marcada`, `test_drive_marcado` ou `avaliacao_marcada` |
| `em_revisao` | `rever = sim`, todas as categorias |
| `sinais_vendas` | `sinal_vendas = sim` |

No relatório, cada percentagem leva o denominador: "contacto captado em 9 de 14 contactos novos de compra (64 %)". Estes números são da amostra de chamadas, não do CRM: para os comparar com leads e vendas registados, usa `stand-auditoria-rastreio-chamadas`.

## Validação antes de entregar

1. Linhas classificadas = chamadas recebidas; se não, diz quais faltam e porquê.
2. `id_chamada` único.
3. Todos os valores controlados pertencem às listas: nesses campos, nada de "Vendas", "média" ou "não referido".
4. Colunas 14 a 21 vazias fora de `vendas`; `sinal_vendas` vazio em `vendas`.
5. Toda a linha com `confianca = baixa` tem `rever = sim` e `motivo_revisao`.
6. Nenhum dado pessoal em `prova`, `motivo` ou `viatura_interesse`. Procura em especial:
   - sequências de nove dígitos ou começadas por `+351`;
   - `@`;
   - matrículas portuguesas (`AA-00-AA`, `00-AA-00`, `00-00-AA`, `AA-00-00`);
   - NIF, IBAN, valores de rendimento ou de prestação de um cliente.
7. O resumo bate com as linhas: soma de `por_categoria` = recebidas.
