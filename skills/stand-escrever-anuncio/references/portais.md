# Escrever para cada destino

Os portais mudam campos, limites e regras sem aviso. Tudo o que aqui está sobre a interface de cada um é para confirmar no dia da publicação. O que não muda é a lógica de cada destino e a regra de que o mesmo facto tem o mesmo valor em todos.

## Princípios comuns

- **Coerência:** preço, quilómetros, versão, ano, garantia e regime de IVA iguais em todos os destinos. Um anúncio que diz 54 300 km no site e 53 000 km no portal perde confiança e pode ser lido como engano.
- **O essencial primeiro:** marca, modelo, versão, ano, quilómetros, combustível, caixa e preço são o que o comprador filtra e compara.
- **Texto para quem lê no telemóvel:** parágrafos de duas ou três linhas, listas para o equipamento, uma ideia por linha nos destaques.
- **Sem enchimento repetido** em todos os anúncios. Um parágrafo curto sobre o stand pode repetir-se; o resto tem de ser desta viatura.
- **Contacto:** o canal que o stand quer (telefone, WhatsApp, formulário) e a referência interna da viatura, para quem atende saber de que carro se fala.
- **Profissional, não particular:** o anúncio aparece como de um profissional. Dar a impressão de ser um particular é uma prática proibida (Decreto-Lei n.º 57/2008: confirmar a redacção em vigor).

## Fórmula do título

`Marca Modelo Motorização Versão`, mais o que mais pesa na decisão se couber: ano, quilómetros, caixa automática, combustível.

Exemplos com viaturas fictícias:

- `Renault Clio 1.0 TCe Intens, 2021, 54 300 km`
- `Toyota Yaris 1.5 Hybrid Comfort, 2020, automático`

Não metas no título: o preço (tem campo próprio), adjectivos, "oportunidade", emojis, o nome do stand (salvo no título da página do site).

Se não souberes o limite do título, entrega duas versões: a completa e uma curta só com marca, modelo e versão.

## Standvirtual

- Os campos estruturados são o que alimenta os filtros de pesquisa; o texto livre complementa. Preenche todos os campos que tiveres confirmados e deixa vazio o que não tiveres: um campo vazio é melhor do que um errado.
- O texto não pode contradizer os campos (por exemplo, o campo de garantia diz uma coisa e a descrição outra).
- Título: confirma na interface se é escrito pelo stand ou gerado a partir dos campos.
- Estrutura da descrição:
  1. Abertura em duas linhas: a viatura e os destaques mais fortes.
  2. Estado e histórico confirmados: revisões documentadas, número de proprietários se comprovado, defeitos declarados, chaves.
  3. Equipamento por grupos.
  4. Condições: preço com IVA incluído e regime de IVA, garantia com tipo e prazo, financiamento só com a informação completa, retoma se o stand a aceita.
  5. Visita e contacto: concelho ou morada, horário, referência da viatura.
- Confirma na interface: limite de caracteres do título e da descrição; se a descrição aceita quebras de linha e listas; que campos existem para garantia, IVA, origem e financiamento e que valores aceitam; número máximo e ordem das fotografias; regras sobre contactos e ligações no texto.
- Se o stand publica por integração (DMS ou exportador de stock), o texto pode ser substituído na sincronização seguinte. Pergunta onde se edita a descrição para o trabalho não se perder.

## OLX

- Leitura mais rápida e ao lado de anúncios de particulares: o que distingue um stand é a clareza das condições (preço, IVA, garantia, factura, retoma).
- Título curto e directo.
- Estrutura: três ou quatro linhas com o essencial, lista curta com o equipamento que mais pesa, condições, contacto.
- Confirma na interface: categoria e campos da viatura, limites de caracteres, número de fotos, se a conta está configurada como profissional.
- Confirma se o anúncio é criado directamente no OLX ou chega de outra plataforma ou de um exportador, para não haver dois anúncios da mesma viatura com textos diferentes.
- Burlas: o OLX tem avisos próprios sobre pedidos de pagamento por ligações e códigos. O anúncio não pede pagamentos nem sinais por mensagem.

## Site do stand

A página da viatura é a única que o stand controla por inteiro e pode ter o texto mais completo. Entrega:

- **Título da página:** marca, modelo, versão, ano e nome do stand com o concelho.
- **Meta descrição:** uma ou duas frases com quilómetros, combustível, caixa, preço e o destaque principal.
- **H1:** marca, modelo e versão.
- **Texto:** a descrição completa com os blocos do Standvirtual, mais uma linha sobre onde ver a viatura.
- **Texto alternativo das fotos:** o que cada foto mostra ("bancos traseiros rebatidos", "painel com 54 300 km"), sem repetir palavras-chave.
- **URL:** legível, se o site deixar escolher (`/viaturas/renault-clio-1-0-tce-intens-2021`).

Dados estruturados:

- Se o site os gera a partir do DMS, corre `python3 scripts/extrair_sinais_pagina.py <url>` depois de publicado e compara preço, quilómetros e disponibilidade com a ficha.
- Se o stand os mete à mão, entrega um bloco JSON-LD só com campos confirmados, para quem gere o site validar e colocar. Exemplo com a viatura fictícia do exemplo resolvido:

```json
{
  "@context": "https://schema.org",
  "@type": "Car",
  "name": "Renault Clio 1.0 TCe Intens",
  "brand": {"@type": "Brand", "name": "Renault"},
  "model": "Clio",
  "dateVehicleFirstRegistered": "2021-03",
  "mileageFromOdometer": {"@type": "QuantitativeValue", "value": 54300, "unitCode": "KMT"},
  "fuelType": "Gasolina",
  "vehicleTransmission": "Manual",
  "itemCondition": "https://schema.org/UsedCondition",
  "offers": {
    "@type": "Offer",
    "price": 14900,
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock"
  }
}
```

- Vendida: retira a página ou marca-a como vendida no mesmo dia em todos os destinos. Uma vendida activa gera contactos perdidos e desconfiança.
- Para auditar o que o site já publica, usa `stand-rever-anuncios-viaturas`; para a parte técnica de pesquisa, `stand-auditoria-seo`.

## Outros destinos

Facebook Marketplace, portais de marca e outros classificados: usa a mesma ficha e confirma as regras do destino para vendedores profissionais. Para publicações e vídeos nas redes sociais, usa `stand-publicar-redes-sociais`.

## Fotografias

Ordem sugerida, igual em todo o stock para o comprador se orientar:

1. Três quartos frente.
2. Lateral.
3. Três quartos traseira.
4. Frente e traseira.
5. Posto de condução.
6. Painel ligado com os quilómetros.
7. Ecrã central e comandos.
8. Bancos dianteiros e traseiros.
9. Bagageira.
10. Rodas e pneus.
11. Detalhes de equipamento confirmado.
12. Defeitos declarados, um por foto, com a legenda que está no texto.
13. Chaves (quantas existem).

Regras: viatura limpa, luz uniforme, fundo arrumado, sem filtros que mudem a cor. Documentos e livro de revisões só fechados ou com dados tapados. Matrícula conforme a política do stand, aplicada a todas as fotos.

## Coerência antes de publicar

- [ ] Preço, quilómetros, versão e ano iguais em todos os destinos.
- [ ] Campos estruturados e texto dizem o mesmo.
- [ ] Garantia e regime de IVA com o mesmo tipo e prazo em todo o lado.
- [ ] Referência interna presente em todos os destinos.
- [ ] Anúncio publicado como profissional.
- [ ] Contacto e horário certos.
- [ ] Nenhuma outra viatura do stand com o mesmo texto.
