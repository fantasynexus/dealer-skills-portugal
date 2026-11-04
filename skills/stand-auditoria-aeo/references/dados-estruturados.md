# Dados estruturados para stands

Os dados estruturados dizem a uma máquina, sem ambiguidade, o que a página já
diz a uma pessoa. Ajudam motores a ler factos (morada, horário, preço,
quilómetros); não garantem resultados enriquecidos, posições nem citações.

## Regras

- **JSON-LD** em `<script type="application/ld+json">`, no HTML que o servidor
  envia. Marcação injectada pelo GTM ou montada no navegador só é vista por
  quem executa JavaScript; o `extrair_sinais_pagina.py` também não a vê.
- **Igual ao visível.** Cada valor tem de estar na página, com o mesmo valor.
  É a regra base das directrizes da Google para dados estruturados e a que
  mais vezes falha nos sites de stands.
- **Um `AutoDealer` por localização**, com um `@id` estável (o URL do site
  mais `#stand`, por exemplo). As fichas apontam para ele em `seller`, em vez
  de repetirem morada e telefone.
- `AutoDealer` é, no Schema.org, um subtipo de `AutomotiveBusiness` e de
  `LocalBusiness`; `Car` é um subtipo de `Vehicle`, que também é `Product`.
  Uma oficina separada pode ser um `AutoRepair` ligado em `department`.

## O que não esperar (confirma na documentação actual da Google)

- Desde Agosto de 2023 a Google só mostra resultados enriquecidos de FAQ para
  sites governamentais e de saúde reconhecidos. Um stand pode usar `FAQPage`
  quando as perguntas estão visíveis, mas não deve esperar destaque por isso.
- A Google não mostra estrelas de avaliações que uma empresa publica sobre si
  própria (`LocalBusiness`, `Organization`). Não copies as avaliações do
  Google para um `aggregateRating` no site.
- Os resultados enriquecidos de anúncios de viaturas da Google estavam
  limitados a alguns países quando esta skill foi escrita. Confirma se
  Portugal está incluído antes de os apresentar como benefício.

## Exemplo 1: AutoDealer

Stand Exemplo, Leiria (fictício): nome, morada, telefone, coordenadas e
horário são inventados para o exemplo. Substitui tudo pelos dados reais e
apaga o que o stand não mostra na página. Os valores entre `<` e `>` são para
preencher.

```json
{
  "@context": "https://schema.org",
  "@type": "AutoDealer",
  "@id": "https://stand-exemplo.pt/#stand",
  "name": "Stand Exemplo",
  "url": "https://stand-exemplo.pt/",
  "logo": "https://stand-exemplo.pt/imagens/logotipo.png",
  "image": "https://stand-exemplo.pt/imagens/fachada.jpg",
  "description": "Stand de automóveis usados multimarca em Leiria, com retoma, financiamento e garantia.",
  "telephone": "+351 244 000 000",
  "email": "geral@stand-exemplo.pt",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rua do Exemplo, 100",
    "postalCode": "2400-000",
    "addressLocality": "Leiria",
    "addressRegion": "Leiria",
    "addressCountry": "PT"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 39.7436,
    "longitude": -8.8071
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "19:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "09:30",
      "closes": "13:00"
    }
  ],
  "areaServed": [
    { "@type": "City", "name": "Leiria" },
    { "@type": "City", "name": "Marinha Grande" },
    { "@type": "City", "name": "Batalha" }
  ],
  "currenciesAccepted": "EUR",
  "sameAs": [
    "<URL do perfil do stand no Facebook>",
    "<URL do perfil do stand no Instagram>",
    "<URL da página do stand no Standvirtual>"
  ]
}
```

| Campo | Regra |
|---|---|
| `name` | O nome comercial que aparece no Perfil de Empresa e na fachada. O nome legal (`legalName`) só se a página o mostrar. |
| `telephone` | Formato internacional (`+351`), o mesmo número do rodapé. |
| `address` | Código postal com o formato `0000-000`; `addressCountry` em código ISO (`PT`). |
| `geo` | Coordenadas da porta do stand, não do centro da cidade. |
| `openingHoursSpecification` | Dias em inglês (valores do Schema.org) e horas em 24 h. Feriados e férias em `specialOpeningHoursSpecification`, se a página os mostrar. |
| `areaServed` | Só concelhos onde o stand trabalha de facto (entrega, clientes habituais). |
| `sameAs` | Perfis do próprio stand. Nunca perfis de outros stands nem a página da marca. |
| `brand` | Só em concessionários oficiais: as marcas que representam, como `Brand`. Não uses o logótipo da marca como `logo` do stand. |

## Exemplo 2: viatura (Car com Offer em EUR)

Ficha de uma viatura usada do Stand Exemplo (fictícia). Cada valor tem de
ser o da ficha publicada.

```json
{
  "@context": "https://schema.org",
  "@type": "Car",
  "@id": "https://stand-exemplo.pt/viaturas/renault-clio-1-0-tce-2021-1234#viatura",
  "name": "Renault Clio 1.0 TCe Intens",
  "url": "https://stand-exemplo.pt/viaturas/renault-clio-1-0-tce-2021-1234",
  "image": [
    "https://stand-exemplo.pt/fotos/1234-frente.jpg",
    "https://stand-exemplo.pt/fotos/1234-interior.jpg"
  ],
  "description": "Renault Clio 1.0 TCe Intens de 2021, gasolina, caixa manual, 48 500 km, com garantia de 18 meses.",
  "brand": { "@type": "Brand", "name": "Renault" },
  "model": "Clio",
  "vehicleConfiguration": "1.0 TCe Intens",
  "vehicleModelDate": "2021",
  "dateVehicleFirstRegistered": "2021-03-15",
  "itemCondition": "https://schema.org/UsedCondition",
  "mileageFromOdometer": {
    "@type": "QuantitativeValue",
    "value": 48500,
    "unitCode": "KMT"
  },
  "fuelType": "Gasolina",
  "vehicleTransmission": "Manual",
  "bodyType": "Utilitário",
  "color": "Cinzento",
  "numberOfDoors": 5,
  "seatingCapacity": 5,
  "vehicleEngine": {
    "@type": "EngineSpecification",
    "enginePower": {
      "@type": "QuantitativeValue",
      "value": 67,
      "unitCode": "KWT"
    }
  },
  "offers": {
    "@type": "Offer",
    "price": 14900,
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/UsedCondition",
    "url": "https://stand-exemplo.pt/viaturas/renault-clio-1-0-tce-2021-1234",
    "seller": { "@id": "https://stand-exemplo.pt/#stand" }
  }
}
```

| Campo | Regra |
|---|---|
| `price` | Número, sem `€` e sem separador de milhares: `14900` ou `14900.00`. Escrito à portuguesa (`"14.900"`) é lido como 14,9. É o preço final que a página mostra ao consumidor. |
| `priceCurrency` | `EUR`, nunca `€`. |
| `availability` | `InStock` à venda; `Reserved` reservada; `SoldOut` vendida. Confirma os valores aceites no Schema.org. |
| `mileageFromOdometer` | Número com `unitCode` `KMT` (quilómetro). Nunca texto como `"48.500 km"`. |
| `dateVehicleFirstRegistered` | Data da primeira matrícula, como na ficha. Se a ficha só mostra mês e ano, confirma no validador como o representar. |
| `vehicleModelDate` | Ano do modelo, só se for conhecido; não é obrigatoriamente o ano da matrícula. |
| `enginePower` | Em kW (`KWT`). Se a ficha mostra cavalos, converte (1 cv = 0,7355 kW) e mostra os dois valores na página. |
| `vehicleIdentificationNumber` | Só se o stand já publica o VIN na ficha. Matrículas não entram nos dados estruturados. |
| `numberOfPreviousOwners` | Só com documento que o prove. Na dúvida, fica de fora. |

Uma viatura importada pode levar a origem na descrição visível ("importada
da Alemanha em 2023"). Não há campo próprio; não inventes um.

## Erros frequentes em sites de stands

- Preço com ponto de milhar, com `€` ou diferente do preço visível.
- Quilómetros como texto, ou sem unidade.
- JSON-LD copiado do tema do site, com morada, telefone ou nome do fornecedor.
- Um `AutoDealer` diferente em cada ficha, com dados que não batem certo.
- `InStock` em viaturas vendidas ou reservadas.
- `aggregateRating` com avaliações copiadas do Google ou escolhidas pelo stand.
- `FAQPage` em páginas sem perguntas visíveis.
- Marcação montada pelo GTM, invisível para quem não executa JavaScript.
- Vários blocos com nomes diferentes para o mesmo stand.

## Como validar

1. `python3 scripts/extrair_sinais_pagina.py <url>`: confirma que o JSON-LD
   está no HTML e resume marca, modelo, quilómetros, preço, moeda,
   disponibilidade, morada e telefone. Avisa quando um bloco é JSON inválido.
   Não mostra horário nem `sameAs`: vê-os no código-fonte.
2. Teste de resultados enriquecidos da Google (Rich Results Test): erros e avisos para o que a
   Google usa.
3. Validador do Schema.org (validator.schema.org): sintaxe e tipos.
4. Compara, campo a campo, com o que a página mostra. Nenhum validador faz
   esta verificação por ti.

## Várias localizações

Um `AutoDealer` por localização, cada um com `@id`, morada, telefone e
horário próprios, na página dessa localização. Se houver uma empresa-mãe,
liga-os com `parentOrganization` a um `Organization`. Nunca juntes duas
moradas no mesmo `AutoDealer`.
