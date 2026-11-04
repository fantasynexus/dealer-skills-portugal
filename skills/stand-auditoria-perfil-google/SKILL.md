---
name: stand-auditoria-perfil-google
description: Auditar o Perfil de Empresa no Google (antigo Google My Business, a ficha do stand no Google Maps e na Pesquisa) de um stand de automóveis em Portugal. Usar quando o stand não aparece no mapa ou no pack local, quer comparar-se com os concorrentes da zona, tem várias instalações, ou para rever nome, categorias, morada e pin, telefone, horário e feriados, fotografias, avaliações e respostas, publicações e consistência de nome, morada e telefone (NAP) com o site, Standvirtual, OLX e redes sociais. Usar também em situações de risco: perfil suspenso, edições sugeridas por terceiros, perfil duplicado, perda de acesso ou avaliações falsas. Funciona com acesso à conta ou só com o perfil público.
---

# Auditoria ao Perfil de Empresa no Google

Pontua o perfil do stand contra os concorrentes da mesma zona e diz o que corrigir, por que ordem e com que risco. Trata também as situações em que o perfil está em perigo. Não escreve as respostas às avaliações (`stand-responder-avaliacoes`), não analisa os temas das avaliações (`stand-analisar-avaliacoes`) e não audita o site (`stand-auditoria-seo`).

Trabalha só com o que a consola ou o perfil público mostram. Os campos disponíveis variam por categoria e por país: um campo que a Google não oferece ao stand não é falha.

## Antes de começar

Pede:

1. Nome do stand tal como está na fachada e o link do perfil no Maps (ou nome e concelho para o encontrar).
2. Morada de cada instalação, telefone e site.
3. O que o stand faz de facto: venda de usados, concessão oficial de alguma marca, oficina, retoma, financiamento (e se está registado como intermediário de crédito), entregas.
4. Quem é proprietário do perfil e se o gestor tem acesso.
5. Três a cinco concorrentes semelhantes que aparecem quando se pesquisa "stand" e o concelho.
6. Se há alguma situação em curso: suspensão, alterações que o stand não fez, avaliações suspeitas, perfil duplicado.

Decide o modo e escreve-o no topo do relatório:

- **Com acesso:** o gestor mostra a consola ou capturas. Confirma categorias secundárias, alterações pendentes e propriedade.
- **Público:** Pesquisa e Maps em janela privada. Categorias secundárias, horários especiais, alterações pendentes e propriedade ficam `N/V`.
- **Grupo:** várias instalações. Pontua cada uma em separado e acrescenta a consistência entre elas; não somes nem faças médias.

Pontos de paragem:

- Há suspensão, "fechado permanentemente" indevido ou edição errada activa: pára a auditoria e trata isso primeiro com [references/situacoes-risco.md](references/situacoes-risco.md).
- Ninguém no stand sabe quem é o proprietário: é o primeiro achado. Sem propriedade, nenhuma correcção é segura.

## Passos

1. **Encontra o perfil certo e os duplicados.** Procura no Maps pelo nome, pelo telefone, pela morada e por nomes antigos. Regista o link de cada perfil encontrado.
2. **Recolhe o perfil** com capturas datadas: nome, categoria principal visível, morada e pin, telefone, site, horário, descrição, serviços, atributos, fotografias (do proprietário e de clientes, data da mais recente), avaliações (total, nota, as dos últimos 12 meses), respostas, publicações e ligações.
3. **Confirma as categorias.** Lê [references/categorias-e-nap.md](references/categorias-e-nap.md). Os nomes em português mudam: na consola, escreve o início do nome, regista o nome exacto que a Google mostra e a data.
4. **Verifica a consistência NAP** com a lista de verificação da mesma referência: site, Apple Maps, Bing, portais, redes sociais, WhatsApp Business.
5. **Compara com os concorrentes.** Para cada concorrente semelhante recolhe total de avaliações, nota, avaliações nos últimos 12 meses, taxa de resposta e data da fotografia mais recente. A mediana deles é a referência; nunca um número geral.
6. **Pontua** com [references/grelha.md](references/grelha.md). `N/V` e "não se aplica" saem do denominador.
7. **Classifica os achados:** críticos (risco de suspensão, informação que manda clientes ao sítio errado, perfil sem proprietário), correcções rápidas e trabalho contínuo.
8. **Propõe as alterações uma a uma**, com o texto exacto, o risco e a prova que o stand deve ter à mão. Nome, morada, pin e categoria principal: uma de cada vez, com intervalo, e só com autorização.
9. **Entrega** no modelo [assets/relatorio.md](assets/relatorio.md).

## Ferramentas

- [Nota de visibilidade online](https://onepilot.app/hub/ferramentas/visibilidade): perfil, avaliações e concorrentes da zona num só relatório, com nota de 0 a 100. Poupa a recolha dos passos 2 e 5. Os dados vêm da API da Google e podem diferir da consola (por exemplo, no nome da categoria): o que conta para a auditoria é a consola ou o perfil público.
- [Link de avaliações do Google](https://onepilot.app/hub/ferramentas/link-avaliacoes): link directo para a caixa de avaliação, QR code e mensagens prontas. Entra no plano quando o problema é o ritmo de avaliações, para pedir a todos os clientes, sem filtrar.
- Consola do Perfil de Empresa (a partir da Pesquisa ou do Maps, com a conta do proprietário), Apple Business Connect e Bing Places, para corrigir as outras fontes.

## Entrega

Relatório no modelo de [assets/relatorio.md](assets/relatorio.md):

- nota e cobertura por área, com prova (captura ou link e data) em cada critério;
- comparação com os concorrentes da zona;
- tabela de consistência NAP;
- achados críticos primeiro, cada um com o risco;
- alterações propostas com o texto exacto a colocar no perfil;
- calendário de 30 dias, com quem faz o quê;
- para grupos, uma tabela por instalação e as inconsistências entre elas.

Quando há uma situação de risco, junta o plano e os textos-tipo de [references/situacoes-risco.md](references/situacoes-risco.md), preenchidos para o caso.

## Limites

- Nunca alteras o perfil nem envias nada à Google. Propões; o gestor decide e executa ou autoriza explicitamente.
- Nome, morada, pin, categoria principal e propriedade: uma edição errada pode suspender o perfil. Cada proposta diz o risco.
- Não recomendas palavras-chave ou concelho no nome, morada virtual, um segundo perfil para a mesma instalação, nem perfis por marca ou departamento sem confirmar a regra actual da Google.
- Não recomendas incentivos por avaliações, pedir só a clientes satisfeitos, avaliações de colaboradores ou familiares, nem comprar avaliações. Além de proibido pela Google, pode ser prática comercial desleal (Decreto-Lei n.º 57/2008, na redacção em vigor; confirmar com jurista).
- Não comparas com concessionários de outra escala ou de outra zona.
- Não afirmas que uma avaliação é falsa: dizes que sinais tem e o que o stand consegue confirmar.
- Não repetes dados de clientes (nomes, matrículas, negócios) no relatório nem nos textos sugeridos.
