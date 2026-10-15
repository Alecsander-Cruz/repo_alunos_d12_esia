# Avaliação e critérios — D1.2

Referência pública para composição da nota, níveis 0–3 e rubricas completas. **Pesos e prazos são proposta docente**; o canal acadêmico de entrega será informado pelo professor. Horários de Brasília.

## Composição

| Instrumento | Peso | Esforço e entrega | Prazo |
| --- | --- | --- | --- |
| AV1 — seis registros individuais | 20% | Dentro da prática de cada bloco; até uma página; média simples dos blocos com presença | Dentro de B1–B6 |
| [AV2 — refatoração e testes verificáveis](avaliacoes/av2/README.md) | 30% | 2h autônomas; registro curto + diff + testes | 21/10/2026, 23h59 |
| [AV3 — entrega final: PR assistido e medição](avaliacoes/av3/README.md) | 50% | 2h autônomas; PR + registro de erros da IA + meia página de medição | 30/10/2026, 23h59 |

L0 (leitura, 2h) é formativa e não tem nota própria.

## Cálculo
Todas as notas variam de 0 a 10. Níveis por critério: **0 ausente, 1 incipiente, 2 adequado, 3 consistente**. **Nota = 10 × soma(peso × nível/3).** Todos os níveis 2 produzem 6,67. Exemplo: AV1 com pesos 30/40/30 e níveis 3, 2, 2 dá 10 × (0,30×1 + 0,40×0,6667 + 0,30×0,6667) = 7,67.

## Rubrica AV1 (cada registro)

| Critério | Peso | Nível 3 | Nível 2 | Nível 1 |
| --- | --- | --- | --- | --- |
| Aplicação/decisão | 30% | Decisão ligada às condições da tarefa, com responsabilidade clara | Decisão adequada, ligação parcial | Decisão sem relação com a tarefa |
| Evidência | 40% | Evidência localizada que outra pessoa consegue conferir (comando, saída, trecho, cálculo) | Evidência presente, difícil de conferir | Afirmação sem evidência |
| Limites/alternativa | 30% | Limite da verificação e condição concreta para mudar a decisão | Limite genérico | Sem limite |

## Rubrica AV2

| Critério | Peso | Nível 3 | Nível 2 | Nível 1 |
| --- | --- | --- | --- | --- |
| Escopo e plano | 20% | Seis campos antes da mudança e plano revisado | Escopo escrito, plano sem revisão | Só o objetivo |
| Comportamento preservado | 25% | Golden master ou equivalente com igualdade exata | Verificação parcial | Sem verificação de comportamento |
| Suíte com verificação real | 35% | Teste que falharia sem a mudança, com evidência (sabotagem ou mutação); sobreviventes tratados ou justificados | Testes com asserções reais, sem prova de que falhariam | Cobertura sem verificação |
| Documentação e ADR | 20% | Contrato e motivo registrados com contexto real | Documentação correta, mas óbvia | Documentação que repete o código |

## Rubrica AV3

| Critério | Peso | Nível 3 | Nível 2 | Nível 1 |
| --- | --- | --- | --- | --- |
| Modo e justificativa | 10% | Modo escolhido por raio de impacto, oráculo e familiaridade, com alternativa comparada | Modo citado e justificado em parte | Modo sem justificativa |
| Escopo declarado e cumprido | 15% | Seis campos antes; diff dentro do escopo; barreira executada | Escopo escrito depois ou cumprido em parte | Sem escopo |
| Mudança revisável | 15% | PR pequeno, plano anexado, commits atômicos | PR médio ou sem plano | PR grande e misturado |
| Verificação efetiva | 20% | Teste que falharia sem a mudança, com evidência | Testes adequados, sem prova de falha | Testes que só passam |
| Honestidade sobre os erros da IA | 15% | Registro específico (o quê, onde, como detectou) | Registro genérico | Ausente ou contradiz o diff |
| Justificativa técnica das correções | 10% | Cada correção com causa e impacto | Explicação parcial | Sem explicação |
| Medição e automação | 15% | Pergunta, métrica, baseline, guardrail, risco de manipulação e verificação da automação | Métrica sem baseline ou sem risco | Ausente |

## Presença, ausência e cálculo de AV1
AV1 é a **média simples dos registros dos blocos com presença registrada, sem reposição por ausência**. O bloco ausente fica fora da soma e do denominador; a falta permanece registrada para frequência. Presença e entrega são registros distintos: o bloco com presença integra o denominador mesmo sem entrega, e os critérios sem evidência recebem nível 0. Se não houver nenhum bloco com presença, não se calcula média e o lançamento é encaminhado à Secretaria. A regra para quem faltar a um bloco avaliado e a recuperação aguardam confirmação da coordenação e serão comunicadas antes do bloco 1.

## Devolutiva
O professor registra **nível 0–3 e evidência curta por critério** em todos os registros AV1. A devolutiva individual desenvolvida (uma força, uma lacuna e uma ação de melhoria) ocorre em AV1.3 e AV1.6; nos demais, a turma recebe devolutiva coletiva sem identificação. AV2 e AV3 têm devolutiva individual. Pedidos de revisão indicam critério e evidência.

## Autoria e IA
IA é permitida com declaração: ferramenta e modelo visíveis, tarefa delegada, trecho aproveitado e a **sua verificação**. Avalia-se aplicação, evidência localizada, comparação e limite; **não** se avalia aparência da resposta, frequência, câmera, quantidade de prompts ou testes verdes. A via textual e a execução recebem os mesmos critérios. Simulações devem ser identificadas, e execução não realizada não pode ser declarada como observada. Não se exigem câmera, fala ou dados de empregador.
