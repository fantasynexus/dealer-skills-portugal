---
name: stand-classificar-chamadas
description: Classificar transcrições de chamadas de um stand em vendas, pós-venda, peças, financiamento ou outros, sem inflacionar leads. Usar com uma chamada, um lote colado ou um ficheiro exportado e, nas chamadas de vendas, extrair intenção e contacto captado.
---

# Classificar chamadas do stand

Lê cada transcrição completa. Trabalha apenas com gravações/transcrições cuja utilização tenha sido autorizada e minimiza dados pessoais no resultado.

## Taxonomia

- **Vendas:** intenção explícita de comprar, trocar, vender ao stand, pedir proposta ou marcar contacto sobre uma viatura.
- **Pós-venda:** oficina, revisão, avaria, garantia, marcação técnica ou acompanhamento de reparação.
- **Peças:** disponibilidade, preço ou encomenda de peças/acessórios.
- **Financiamento:** processo ou documentação financeira sem intenção nova de compra identificável.
- **Outros:** fornecedores, recrutamento, engano, spam, chamada interna ou insuficiente.

Uma chamada sobre garantia, devolução, prestação ou documentação de uma compra passada não é venda só porque menciona uma viatura. Se houver duas intenções, usa a finalidade principal e regista a secundária.

## Campos

Para cada chamada devolve ID, categoria, confiança `alta/média/baixa`, frase de prova curta e motivo. Apenas em `Vendas`, extrai viatura/interesse, novo/usado, retoma, origem declarada, próxima acção e se nome e contacto foram captados. Usa `não referido` em vez de inferir.

## Resumo

Conta todas as categorias e mostra percentagens com denominador. Distingue chamadas, contactos de vendas, leads válidos e marcações; não os trata como sinónimos. Lista chamadas ambíguas para revisão humana.

Não repitas telefone, email, morada ou dados financeiros no relatório. Não avalies desempenho de colaboradores com uma amostra pequena nem tires conclusões disciplinares automáticas.
