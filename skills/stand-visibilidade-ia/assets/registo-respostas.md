# Registo de respostas

Uma linha por resposta (pergunta × motor × repetição). Guarda o CSV junto do relatório: é ele que permite repetir a medição no trimestre seguinte e comparar. O texto completo de cada resposta fica num ficheiro ou captura à parte, referido na coluna `captura`.

## Cabeçalho da corrida

| Campo | Valor |
|---|---|
| Stand | |
| Período da corrida | AAAA-MM-DD a AAAA-MM-DD |
| Modo | colado / directo / API |
| Motores | |
| Motores não verificados e porquê | |
| Condições de sessão | janela privada / conta sem memória / conta com histórico |
| Localização e idioma da interface | |
| Versão do banco de perguntas | data e lista de IDs |
| Repetições | 3 em todas / 3 no núcleo fixo e 1 nas restantes |
| Concorrentes (ID, nome, domínio) | C1: / C2: / C3: |
| Mini ficha confirmada em | data e função de quem confirmou |

## Mini ficha

| Facto | Valor confirmado |
|---|---|
| Nome comercial (e variantes) | |
| Morada | |
| Telefone | |
| Site | |
| Tipo de stock e marcas principais | |

## Colunas

```csv
id_resposta,data,hora,motor,modelo_visivel,modo,sessao,localizacao,idioma,id_pergunta,intencao,pergunta,repeticao,estado,stand_mencionado,posicao,recomendacao,concorrentes_mencionados,outros_stands,urls_citados,dominio_proprio_citado,categorias_fonte,erro_evidente,nota,captura
```

| Coluna | Valores |
|---|---|
| `modo` | `colado`, `directo`, `api` |
| `sessao` | `privada`, `conta_sem_memoria`, `conta_com_historico` |
| `estado` | `valida`, `sem_resposta_util`, `recusa`, `erro_motor`, `sem_resumo_ia` |
| `stand_mencionado` | `texto`, `so_fontes`, `nao` |
| `posicao` | número ou vazio |
| `recomendacao` | `positiva`, `neutra`, `negativa`, `ausente` |
| `concorrentes_mencionados` | IDs separados por `;` |
| `outros_stands` | número |
| `urls_citados` | URLs separados por `;` |
| `dominio_proprio_citado` | `sim`, `nao`, `sem_fontes` |
| `categorias_fonte` | números de 1 a 9, separados por `;`, pela ordem dos URLs |
| `erro_evidente` | `sim`, `nao`, `nao_verificavel` |
| `nota` | frase exacta do erro, ressalvas, `pago`, `nao_aberta` |
| `captura` | caminho do ficheiro com a resposta completa |

## Exemplo (fictício)

Stand Exemplo, Leiria (fictício). Concorrentes: C1 Auto Fictício Marinha, C2 Carros Inventados Leiria. Os domínios terminam em `.example` porque não existem.

```csv
R001,2026-10-15,10:42,ChatGPT,não visível,colado,privada,Leiria,pt-PT,B1,descoberta,"Quais são os melhores stands de carros usados em Leiria?",1,valida,nao,,ausente,C1;C2,3,"https://auto-ficticio-marinha.example/;https://www.standvirtual.com/",nao,1;2,nao,"C1 em primeiro lugar",capturas/R001.txt
R002,2026-10-15,10:47,ChatGPT,não visível,colado,privada,Leiria,pt-PT,C1,marca_stock,"Onde comprar um Peugeot 2008 usado em Leiria?",1,valida,texto,2,neutra,C1,1,"https://www.standvirtual.com/",nao,2,nao,"Stand surge via anúncio no Standvirtual",capturas/R002.txt
R003,2026-10-15,10:53,ChatGPT,não visível,colado,privada,Leiria,pt-PT,A2,identidade,"Onde fica o Stand Exemplo e a que horas abre?",1,valida,texto,1,neutra,,0,,sem_fontes,,sim,"Diz que fecha ao sábado; a mini ficha diz que abre",capturas/R003.txt
```

## Cuidados com o registo

- Não guardes nomes de clientes nem contactos privados que apareçam nas respostas; escreve na nota que existem.
- Não corrijas linhas antigas: uma reclassificação é uma linha nova na nota, com data.
- Uma resposta sem captura nem texto guardado não entra nas contas.
