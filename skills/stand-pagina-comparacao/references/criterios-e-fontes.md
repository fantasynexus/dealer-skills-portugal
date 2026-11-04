# Critérios, fontes e regras

Que critérios usar em cada tipo de comparação, de onde vêm os dados, como os tornar comparáveis, como fazer contas de custos em Portugal e o que a lei pede a uma comparação.

## A regra das fontes

Cada valor da tabela leva cinco coisas: **valor, unidade, versão a que se refere, fonte e data de consulta**. Sem as cinco, o valor não entra.

Hierarquia, da mais forte para a mais fraca:

1. **Documentos da viatura concreta:** ficha do stand confirmada com o Certificado de Conformidade ou o Documento Único Automóvel. Usa só campos técnicos; nunca dados do proprietário.
2. **Fabricante ou importador oficial:** ficha técnica, catálogo ou tabela de preços daquele ano-modelo e versão. Num usado, a do ano de fabrico, não a do modelo actual.
3. **Organismos e bases com método publicado:** Euro NCAP (segurança, com o ano do teste), Portal das Finanças (IUC), Direcção-Geral de Energia e Geologia (preços de combustíveis), entidade gestora da rede Mobi.e (carregamento público), Fundo Ambiental (incentivos).
4. **Ensaios de imprensa especializada,** datados e atribuídos: só para medições próprias ou opiniões, citadas como tal ("no ensaio de [publicação], [data], o consumo medido foi [valor]").
5. **Dados de mercado:** Análise de stock do hub ou contagens num portal, sempre como "preços pedidos em anúncios, [data]".

Não são fontes: a memória do modelo, fóruns e grupos, a Wikipédia como fonte única, médias "típicas" sem origem, valores de outro mercado (autonomia EPA americana, consumos em mpg, versões do Reino Unido) apresentados como portugueses, e o texto de vendas do próprio stand.

Se o fabricante já não publica a ficha de um ano antigo, procura o arquivo de imprensa do importador ou um catálogo datado; se não houver, a célula fica "não foi possível confirmar".

## Comparabilidade

- **WLTP e NEDC:** o WLTP é obrigatório nas novas matrículas da União Europeia desde Setembro de 2018. Viaturas anteriores podem ter só valores NEDC. Não se comparam: se um lado só tem NEDC, escreve-o na célula e não declares vencedor nesse critério.
- **Autonomia:** a autonomia WLTP não é a autonomia real; varia com temperatura, velocidade e climatização. Um valor "real" só com fonte e método.
- **Bateria:** diz se a capacidade é bruta ou útil. Compara a mesma.
- **Potência:** cavalo-vapor métrico (cv) e quilowatt (kW); 1 kW equivale a cerca de 1,36 cv. Usa a mesma unidade dos dois lados.
- **Bagageira:** fabricantes medem com métodos diferentes (até à chapeleira, até ao tejadilho). Compara só com o mesmo método, ou diz que diferem.
- **Euro NCAP:** as estrelas dependem do protocolo do ano do teste. Resultados de anos diferentes não se comparam directamente; cita sempre o ano.
- **Versões equivalentes:** potência, caixa e nível de equipamento parecidos. Não compares a versão mais barata de um com a mais equipada do outro.
- **Preços:** tabela do novo com data e versão (com IVA); preço pedido no usado. Não compares preço de tabela com preço de transacção.

## Custos de utilização em Portugal

Sempre com premissas escritas e data. Nunca um valor sem a conta à vista.

| Custo | Como obter | Cuidados |
|---|---|---|
| IUC | Simulador no Portal das Finanças, para características concretas (data da matrícula, cilindrada, CO2, combustível) | Taxas mudam com o Orçamento do Estado e o gasóleo tem regras próprias. Crê-se que os veículos exclusivamente eléctricos estão isentos; confirma no Código do IUC em vigor |
| ISV | Pago na primeira matrícula em Portugal; pesa nos importados | O stand diz se o preço inclui legalização; confirma com o stand |
| Combustível | Preço médio de venda ao público publicado pela DGEG × consumo (com a norma) × quilómetros por ano do público | Média nacional numa data; confirma o endereço actual do portal da DGEG |
| Electricidade em casa | Preço do kWh do tarifário do cliente ou de um tarifário nomeado, com data | Bi-horário e tri-horário mudam a conta; não generalizes |
| Carregamento público | Rede Mobi.e: o preço soma tarifa do operador do posto, do comercializador de electricidade para a mobilidade eléctrica e taxas | Varia por posto e contrato; não publiques um custo por 100 km sem nomear posto, contrato e data |
| Seguro | Simulações por condutor | Não publiques valores |
| Manutenção | Plano de manutenção do fabricante (intervalos) | Não inventes custos de revisão; preços da oficina do stand só com data |
| Incentivos | Aviso do Fundo Ambiental em vigor | Programas anuais, regras e dotação mudam, muitas vezes só para novos; nunca prometas |
| Empresas | IVA dedutível, tributação autónoma, depreciações | Encaminha para o contabilista; marca "a confirmar" |

Modelo de conta (preenche só com valores citados):

```text
Custo de energia por 100 km = consumo por 100 km [valor, norma, fonte] × preço da energia [valor, fonte, data]
Custo anual = custo por 100 km × (quilómetros por ano do público ÷ 100)
```

## Critérios por tipo

### A. Modelo contra modelo (usados)

| Critério | Fonte preferida | Nota |
|---|---|---|
| Geração e anos abrangidos | Fabricante, imprensa datada | Delimita sempre |
| Motorizações e potência | Ficha técnica do ano-modelo | Versões equivalentes |
| Caixa (manual, automática e tipo) | Ficha técnica | |
| Consumo, com norma | Ficha técnica ou homologação | WLTP ou NEDC na célula |
| Dimensões e bagageira | Ficha técnica | Mesmo método de medição |
| Segurança | Euro NCAP, com ano | |
| Equipamento por nível | Catálogo do ano | Série ou opcional |
| Custo fiscal | Simulador do IUC para duas viaturas concretas | |
| Manutenção | Plano do fabricante | |
| Oferta de usados | Análise de stock ou contagem datada no portal | Preços pedidos |
| Campanhas de recolha | Fabricante (consulta por número de quadro) ou Safety Gate da UE | Não estendas uma campanha a todos os anos |
| Garantia do fabricante remanescente | Condições do fabricante, pela data da primeira matrícula | Confirma se passa para o novo dono |

### B. Decisão de compra

**Usado ou novo:** preço de compra (tabela do novo com data e versão; preços pedidos de usados semelhantes); garantia legal e comercial (Decreto-Lei n.º 84/2021, confirma prazos para novos e usados) e garantia do fabricante remanescente; desvalorização só com estudo citado, senão explica o princípio sem números; prazo de entrega do novo segundo a marca ou o stand, à data; equipamento e tecnologia dos anos em causa; histórico do usado comprovado; financiamento de cada oferta, com TAEG e data.

**Eléctrico ou híbrido:** define o tipo de híbrido na página (híbrido que não carrega, híbrido plug-in, híbrido ligeiro); autonomia com norma e fonte face aos quilómetros diários do público; onde carrega (casa, condomínio, trabalho, rede pública); custo de energia com premissas; estado da bateria do usado concreto (relatório) e garantia da bateria do fabricante (prazos e transmissão a confirmar); fiscalidade a confirmar; restrições locais de circulação a confirmar na câmara municipal.

**Gasóleo ou gasolina:** quilómetros por ano e tipo de uso do público; consumo com norma e preço do combustível com data; condições de regeneração do filtro de partículas segundo o manual do fabricante (cita-o, não generalizes); IUC pelo simulador; restrições locais a confirmar.

### C. Stand contra stand

Localização e acessos; gama de stock (marcas, segmentos, faixas de preço, contagem datada no site ou portal); dias anunciados, só se públicos e datados; qualidade da informação dos anúncios; preparação e garantia declaradas; financiamento e retoma publicados; entrega; oficina e pós-venda; avaliações (classificação, número, plataforma e data; padrões só de avaliações reais); horários; canais de contacto.

Fontes: sites dos dois stands, Perfil de Empresa no Google, portais. Nunca: clientes-mistério, informação privada, contas ou volumes adivinhados, nomes de funcionários.

## Regra de justiça

- **A:** cada modelo ganha onde os dados o mostram. Se um ganha tudo, revê o âmbito (versões equivalentes?) antes de publicar e, se se mantiver, diz porque é que alguém escolhe o outro (preço, oferta, gosto).
- **B:** diz para quem cada opção faz sentido, incluindo a que o stand não vende (um stand só de usados admite quando um novo compensa).
- **C:** o concorrente vence ou é mais forte em pelo menos uma dimensão quando os dados o mostram. Teste: o responsável do concorrente leria a página sem encontrar um facto falso. Sem diferença, é empate.
- Sem prova suficiente num critério: "não foi possível confirmar", sem conclusão.
- Declara o interesse: "Esta página foi escrita pelo [stand], que vende [uma das opções / ambas]."

## Publicidade comparativa: lista de controlo

O Código da Publicidade (Decreto-Lei n.º 330/90) regula a publicidade comparativa num artigo próprio (crê-se que o 16.º), na linha da Directiva 2006/114/CE. Confirma a versão em vigor. A comparação deve:

- comparar bens ou serviços que respondem às mesmas necessidades;
- comparar objectivamente características essenciais, pertinentes, comprováveis e representativas, e o preço pode ser uma;
- não gerar confusão entre o stand e o concorrente, nem entre marcas;
- não desacreditar nem denegrir marcas, nomes, produtos ou actividades de terceiros;
- não tirar partido indevido da notoriedade de uma marca;
- não apresentar um bem como imitação de outro com marca protegida.

Nomes de marcas e modelos só para identificar. Sem logótipos nem imagens oficiais sem autorização; usa fotos das viaturas do próprio stand.
