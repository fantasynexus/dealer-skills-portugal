# Consentimento, oposição e regras de envio

Lista de controlo operacional, não parecer jurídico. Diplomas de referência: RGPD (Regulamento (UE) 2016/679), Lei n.º 58/2019 (execução do RGPD em Portugal) e Lei n.º 41/2004 (privacidade nas comunicações electrónicas). Confirma a versão em vigor de cada um; as dúvidas vão para o encarregado de protecção de dados (DPO) ou para um jurista.

## 1. Transaccional, pré-contratual ou marketing

| Natureza | O que é | Exemplos | Base habitual (confirmar) | Pode levar promoção? |
|---|---|---|---|---|
| Transaccional ou de serviço | necessário para cumprir o que o cliente pediu ou comprou, uma obrigação legal ou um aviso de segurança | confirmação de marcação, documentos, garantia, registo, chamada técnica | execução do contrato ou obrigação legal (RGPD, artigo 6.º, n.º 1, alíneas b) e c)) | Não |
| Pré-contratual a pedido | resposta a um pedido concreto do cliente, por pouco tempo e só sobre esse pedido | seguimento da proposta pedida, do test-drive feito, do orçamento de oficina | diligências pré-contratuais a pedido do titular (alínea b)) | Não |
| Marketing directo | promove o stand, produtos ou serviços | novidades, lembretes que promovem a oficina, retoma, eventos, recomendação, aniversário de compra e, por prudência, pedidos de avaliação | consentimento, ou excepção de cliente da Lei n.º 41/2004, sempre com direito de oposição (RGPD, artigo 21.º) | Sim |

**Teste rápido:** se o cliente se tivesse oposto ao marketing, este email teria de sair na mesma? Sim, é transaccional. Não, é marketing.

**Conteúdo misto:** um email transaccional com destaque de stock, campanha ou "já pensou em trocar?" passa a marketing. Quem se opôs ao marketing deixa de o poder receber, e a confirmação da marcação dessa pessoa falha. Mantém os transaccionais limpos.

**Quantos seguimentos pré-contratuais?** Os do catálogo (até 2 por pedido) são uma sugestão prudente. Quantos são razoáveis antes de passar a marketing decide-se com o DPO.

## 2. Lista de controlo de consentimento e oposição

Preenche com `sim`, `não` ou `N/V` e a prova. Um `não` num item de marketing tira esse fluxo do arranque.

**Base e prova**

- [ ] Cada fluxo tem natureza e base registadas no documento.
- [ ] Marketing por email, SMS ou WhatsApp a pessoas singulares tem consentimento prévio, ou usa a excepção de cliente (Lei n.º 41/2004, artigo 13.º-A: confirmar a redacção em vigor). A excepção exige contacto obtido na venda de um produto ou serviço, marketing só de produtos ou serviços análogos do próprio stand, e possibilidade de recusa no momento da recolha e em cada mensagem.
- [ ] O consentimento é livre, específico, informado e inequívoco (RGPD, artigos 4.º e 7.º): caixa não pré-seleccionada, separada dos termos do contrato, uma por canal e por finalidade.
- [ ] Há prova de cada consentimento: data, origem (formulário, contrato, balcão), texto exacto aceite e quem o recolheu.
- [ ] Contactos vindos de portais são usados para responder àquele pedido. Marketing só com consentimento recolhido pelo stand ou com base confirmada nos termos do portal.
- [ ] Contactos de empresas (pessoas colectivas) estão separados: a Lei n.º 41/2004 trata-os de forma diferente. Confirmar o regime e as listas de oposição aplicáveis antes de os juntar a um fluxo.
- [ ] Confirmado se se aplicam listas de oposição externas e, se sim, como se consultam.

**Oposição e retirada**

- [ ] Cada email de marketing tem uma forma simples e gratuita de oposição, que funciona, e identifica o stand.
- [ ] A oposição chega a todas as plataformas (CRM, email, SMS, WhatsApp) através de uma lista de supressão única.
- [ ] Retirar o consentimento é tão fácil como dá-lo (RGPD, artigo 7.º, n.º 3).
- [ ] A oposição ao marketing não corta transaccionais necessários. "Não me contactem de todo" regista-se como tal: só passam os contactos obrigatórios.
- [ ] O stand fixou um prazo interno curto para aplicar a oposição e testou-o.

**Transparência e dados**

- [ ] A informação aos titulares (RGPD, artigos 13.º e 14.º) cobre estes fluxos, incluindo a segmentação por idade da viatura, quilómetros ou datas de contrato, e o direito de oposição a essa perfilagem (artigo 21.º).
- [ ] Nenhum fluxo usa categorias especiais de dados (artigo 9.º) nem infere vulnerabilidade financeira.
- [ ] Plataformas de envio e CRM têm contrato de subcontratação (artigo 28.º). Se os dados saem do Espaço Económico Europeu, a base da transferência está confirmada.
- [ ] Há prazo de conservação para contactos que não compraram e para clientes inactivos.
- [ ] Os envios e as oposições ficam registados.

## 3. Requisitos de envio

Confirma os requisitos actuais de cada fornecedor de email; mudam com frequência.

- **Domínio autenticado:** domínio próprio com SPF, DKIM e DMARC. Desde 2024, a Google e a Yahoo exigem a quem envia em volume autenticação, cancelamento com um clique nos emails de marketing e uma taxa de queixas baixa: confirma os limiares em vigor.
- **Remetente:** nome de uma pessoa e do stand ("Ana, Stand Exemplo"); endereço de resposta que alguém lê.
- **Identificação:** as comunicações publicitárias identificam-se como tal e identificam o anunciante (Decreto-Lei n.º 7/2004: confirmar). No rodapé: nome do stand, morada, contacto e o motivo por que a pessoa recebe o email.
- **Formato:** versão em texto simples; corpo curto; um CTA; leitura em telemóvel; imagens com texto alternativo; nenhum documento pessoal em anexo.
- **Ligações:** UTM consistentes, segundo o plano de `stand-auditoria-ga4-google-ads`.

## 4. Regras globais do programa

Decisão do stand. São regras de partida desta skill, não limites legais.

- **Frequência de marketing:** no máximo um email de marketing por semana e por pessoa, somando todos os fluxos. Os transaccionais não contam para o limite, mas não saem no mesmo dia que um de marketing para a mesma pessoa.
- **Prioridade** quando dois fluxos caem no mesmo dia: segurança, transaccional, documentação, pré-contratual, serviço, marketing. O de menor prioridade adia.
- **Exclusões mútuas:**
  - reclamação aberta suspende marketing e pedidos de avaliação até ao fecho;
  - venda concluída fecha os seguimentos de proposta e test-drive;
  - cliente em campanha de `stand-campanha-retoma` não recebe os fluxos 12 e 13;
  - cliente no programa de `stand-onboarding-cliente` não recebe os fluxos 5 e 7 nesse período;
  - "comprei noutro lado" fecha os seguimentos e regista o motivo.
- **Supressões comuns:** oposição; email inválido ou devolvido; viatura vendida pelo cliente (para fluxos sobre essa viatura); falecimento comunicado pela família; pedido de apagamento ou de limitação.
- **Horário:** emails em horas razoáveis para o cliente. SMS e WhatsApp em dias úteis e horário de expediente, salvo marcação pedida.

## 5. Quando pedir revisão ao DPO ou a um jurista

- Fluxos que usam datas de crédito, leasing, aluguer de longa duração ou renting (fluxo 12) ou estimam o valor da viatura (fluxo 13).
- Qualquer email que fale de prestação, taxa, "sem entrada" ou crédito. A publicidade a crédito ao consumo tem informação obrigatória, como a TAEG e um exemplo representativo (Decreto-Lei n.º 133/2009, ou o diploma que o substitua na transposição da Directiva (UE) 2023/2225, e regras do Banco de Portugal: confirmar). O stand só a faz dentro do seu estatuto de intermediário de crédito (Decreto-Lei n.º 81-C/2017). Na dúvida, o email não fala de crédito.
- Partilha de dados com a marca, a financeira, a oficina parceira ou plataformas de publicidade (audiências personalizadas).
- Programas de recomendação com incentivo.
- Uso da excepção de cliente em vez de consentimento.
- Fluxos dirigidos a empresas.
- Qualquer fluxo que segmente por algo que não seja a viatura, a compra ou o serviço.

## 6. Erros frequentes a apanhar no modo de revisão

- Newsletter enviada a toda a base, incluindo contactos de portais que só pediram informação sobre uma viatura.
- Confirmação de marcação com destaque de stock ou campanha.
- Ligação de oposição que leva a uma página que pede login, ou que só retira de uma lista.
- Inquérito de satisfação que só mostra o link do Google a quem deu nota alta.
- Lembrete de manutenção com intervalo genérico ("a cada 15 000 km") que não é o do plano da viatura.
- Remetente "noreply" e respostas que ninguém lê.
- Campo vazio a aparecer no texto ("Olá ,", "o seu {viatura}").
