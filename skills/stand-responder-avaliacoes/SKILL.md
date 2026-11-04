---
name: stand-responder-avaliacoes
description: Responder a uma avaliação de cliente de um stand automóvel em Portugal no Google, Facebook, Portal da Queixa ou num portal, em PT-PT. Usar quando o gestor pede "responde a esta avaliação", "resposta à review do Google", "deixaram-nos uma estrela", "comentário negativo", "esta pessoa nunca foi nossa cliente", "estão a atacar um vendedor" ou quer agradecer uma avaliação positiva. Classifica a avaliação (positiva, positiva com reparo, negativa com fundamento, negativa sem contexto, possivelmente falsa ou de não cliente, ataque a colaborador) e entrega a resposta pronta, uma alternativa mais curta e o que o stand deve fazer internamente, sem revelar dados do cliente, sem admitir responsabilidade legal e sem oferecer nada em troca de alterar ou retirar a avaliação.
---

# Responder a uma avaliação

Escreve a resposta pública a uma avaliação e diz ao stand o que fazer fora dela. Uma resposta tem dois leitores: quem escreveu e quem a vai ler depois, a decidir se compra no stand. Para tratar muitas avaliações de uma vez e encontrar padrões, usa `stand-analisar-avaliacoes`.

## Antes de começar

1. Pede o texto completo, as estrelas, a plataforma, a data e se já existe resposta do stand. Não trabalhes sobre um resumo.
2. Pede a versão do stand: o que aconteceu, o que já foi feito, se a pessoa é cliente identificável. O gestor verifica no DMS/CRM; tu não precisas do nome, do contacto nem do negócio do cliente e não os pedes.
3. Pede quem assina (nome e função de quem responde, nunca o colaborador visado) e o contacto para o canal privado: telefone ou email geral do stand e a pessoa que atende.
4. Pergunta se há Livro de Reclamações, reclamação formal, advogado, seguradora ou processo em tribunal. Se houver, a resposta pública é mínima e o gestor fala com o jurista antes de publicar.
5. Usa a voz do stand (kit de `stand-posicionamento`, se existir). Sem kit: cordial, directo, sem linguagem de centro de atendimento.

## Passos

1. **Classifica** num dos seis tipos de [references/tipos-de-avaliacao.md](references/tipos-de-avaliacao.md): positiva, positiva com reparo, negativa com fundamento, negativa sem contexto, possivelmente falsa ou de não cliente, ataque a colaborador. Se tiver traços de dois, usa o mais sensível. Resultado: tipo e motivo numa linha.
2. **Separa** o que a pessoa diz, o que o stand sabe e o que se pode dizer em público. Quase nada do que o stand sabe sobre o cliente se pode dizer em público.
3. **Decide se respondes já.** Responde quase sempre. Pára e passa ao gestor quando há ameaça, acusação de crime, dados de saúde, processo em curso ou dados de terceiros expostos na avaliação: nesses casos entregas só uma resposta mínima e o plano interno.
4. **Escreve a resposta pronta** com a estrutura do tipo: agradecer ou reconhecer, responder ao ponto concreto sem detalhes do negócio, passar para o canal privado com nome e contacto, fechar sem fórmula vazia. Quatro a seis frases, raramente mais.
5. **Escreve a alternativa curta**, com duas ou três frases, para quando o gestor prefere menos exposição.
6. **Verifica** com a lista do modelo: sem dados do cliente, sem admissão de responsabilidade, sem oferta em troca de alterar, sem o nome do colaborador visado, sem repetir a resposta de outra avaliação, PT-PT com a grafia do stand.
7. **Plano interno:** quem contacta o cliente e até quando, o que se verifica (processo, colaborador, viatura), o que se regista e se o tema já apareceu noutras avaliações.
8. **Avaliação falsa ou ofensiva:** além da resposta sóbria, prepara a denúncia pelo processo da plataforma, com o motivo da política que se aplica. Os processos mudam: o gestor confirma o caminho actual na ajuda oficial. Detalhe em [references/plataformas-e-regras.md](references/plataformas-e-regras.md).

## Os seis tipos num relance

| Tipo | Sinal | A resposta | Internamente |
|---|---|---|---|
| Positiva | Elogio sem reparos, ou só estrelas | Agradece com uma referência concreta | Partilhar com a equipa |
| Positiva com reparo | Nota boa com uma crítica concreta | Agradece, reconhece o reparo, diz o que muda só se for verdade | Corrigir a causa do reparo |
| Negativa com fundamento | Falha concreta e plausível | Reconhece a experiência, leva para o privado com uma pessoa | Contactar no próprio dia, resolver, registar |
| Negativa sem contexto | Estrelas baixas, texto genérico | Abertura curta, convite ao contacto | Tentar perceber, sem expor ninguém |
| Possivelmente falsa ou de não cliente | Sem registo, serviços que o stand não tem, vaga de perfis novos | Sóbria, sem acusar, diz que não encontra relação | Guardar prova e denunciar |
| Ataque a colaborador | Acusação ou insulto a uma pessoa | Leva a sério, sem nomear nem defender com pormenores | Ouvir o colaborador, apoiar, denunciar se houver insulto |

## Livro de Reclamações

É outro processo. Uma reclamação no Livro de Reclamações, físico ou electrónico, tem destinatário, forma e prazo de resposta próprios, que não se cumprem com uma resposta no Google. Se a avaliação diz que a pessoa também reclamou no Livro, trata as duas coisas em separado e manda confirmar o prazo no Decreto-Lei n.º 156/2005, na redacção em vigor. A resposta pública não discute o conteúdo da reclamação.

## Ferramentas

- [Link de avaliações do Google](https://onepilot.app/hub/ferramentas/link-avaliacoes): link directo, QR code e mensagens para pedir avaliações. Com poucas avaliações, cada negativa pesa mais; a resposta de fundo é pedir mais, a todos os clientes, depois da entrega ou do serviço, sem escolher só os satisfeitos. Pedir só a quem gostou viola as regras do Google e distorce a nota.
- Com muitas avaliações por tratar, usa `stand-analisar-avaliacoes` para priorizar e encontrar temas e volta aqui para escrever as respostas.
- Quando a crítica é feita em comentários nas redes sociais do stand, aplica esta skill da mesma forma; para o resto das redes, `stand-publicar-redes-sociais`.

## Entrega

Preenche [assets/modelo-resposta.md](assets/modelo-resposta.md): tipo e motivo, factos (públicos e internos, sem dados pessoais), resposta pronta, alternativa curta, plano interno, denúncia quando se aplica e a lista de verificação. Para várias avaliações, uma secção por avaliação, cada uma com texto próprio.

## Limites

- Não revela dados do cliente nem do negócio dele: nome completo, viatura, matrícula, preço, financiamento, datas, reparações, conversas. Mesmo o que a pessoa escreveu não se repete com mais pormenor.
- Não admite responsabilidade legal nem reconhece defeitos em público ("a culpa foi nossa", "o carro já vinha com o problema"). Lamenta a experiência, não factos que ainda não se apuraram.
- Não oferece nada em troca de alterar ou retirar a avaliação, nem em público nem em privado.
- Não ataca, não ironiza, não acusa a pessoa de mentir, mesmo quando a avaliação parece falsa.
- Não nomeia nem expõe o colaborador visado e não publica a versão interna dele.
- Não pede avaliações a colaboradores, familiares ou amigos para compensar uma negativa.
- Não publica: entrega o texto para o gestor aprovar e publicar.
