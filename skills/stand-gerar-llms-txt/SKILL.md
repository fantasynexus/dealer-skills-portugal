---
name: stand-gerar-llms-txt
description: Gerar ou rever um ficheiro llms.txt para o site de um stand automóvel português. Usar quando o gestor quer dar a agentes de IA um índice curto, factual e actualizado do stand, stock, serviços, financiamento e contactos.
---

# Gerar `llms.txt` para um stand

Cria um índice legível por máquinas em `/<raiz>/llms.txt`. O ficheiro ajuda a descoberta; não é uma norma oficial de indexação nem garante citações.

## Recolha e validação

Pede o URL e os factos essenciais. Quando houver acesso web, abre cada URL antes de a incluir. Nunca inventes rotas. Dá prioridade a páginas canónicas, públicas, indexáveis e com conteúdo útil.

Confirma:

- nome, descrição factual, localização e contactos;
- stock total ou páginas estáveis por tipo, nunca URLs efémeros de pesquisa;
- venda, compra, retoma, financiamento, garantias e pós-venda;
- marcas e categorias realmente trabalhadas;
- políticas, termos e privacidade;
- páginas noutras línguas apenas quando mantidas.

## Formato

Entrega Markdown simples:

```markdown
# Nome do stand

> Uma frase factual sobre o stand, localização e proposta.

## Viaturas
- [Usados](https://exemplo.pt/viaturas): descrição curta.

## Comprar e vender
- [Retomas](https://exemplo.pt/retomas): descrição curta.

## Serviços
- [Oficina](https://exemplo.pt/oficina): descrição curta.

## Sobre e contactos
- [Contactos](https://exemplo.pt/contactos): morada, horário e canais.
```

Mantém 10 a 30 links de alto valor, remove duplicados, parâmetros de campanha, páginas vazias e afirmações promocionais sem prova. Explica como publicar, validar `200 text/plain`, ligar no sitemap ou rodapé e rever quando URLs ou serviços mudarem.

## Entrega

Mostra primeiro URLs inválidos ou por confirmar, depois o ficheiro final num único bloco pronto a copiar e uma lista curta de manutenção. Não substitui `robots.txt`, sitemap, dados estruturados ou conteúdo rastreável.
