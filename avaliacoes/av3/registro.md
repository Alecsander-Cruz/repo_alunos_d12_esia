# Registro individual — AV3

**Limite: três páginas + até duas de evidências.** Estudante: Alecsander D. Cruz — Data: 28/10/2026 — Caminho: B (MiniLoja) — B1: acesso a pedidos de outro usuário (R4), com teste negativo

**Modo de interação usado e por quê (raio de impacto, oráculo, familiaridade):** editar com escopo, revisando o plano da IA antes da execução. Raio de impacto pequeno (uma função de `handlers.py` e um arquivo de teste novo), mas em controle de acesso, onde um erro vaza dados de clientes; revisar o plano antes permite conferir se a IA pretende tocar algo fora do escopo e se a abordagem faz sentido. Oráculo: a R4 do contrato ("um usuário só pode ver os próprios pedidos"); o status 404 é decisão minha, registrada no escopo, porque o contrato não define o status. Familiaridade média: conheço o caso pelas atividades anteriores (AV1.1 a AV2, em `cadastro.py`, `calculo.py` e na suíte existente), mas nunca tinha alterado `handlers.py`. Escolhi a B1 por ser a tarefa de escopo menor. **Alternativa comparada:** delegar a um agente. Mesmo com o escopo declarado, o agente poderia fazer algo fora dele sem que eu revisasse antes, gerando retrabalho; e, como a mudança mexe em controle de acesso, um erro não revisado poderia causar vazamento de dados.

**Escopo declarado antes (seis campos):** objetivo: corrigir `get_pedido` em `caso/miniloja/handlers.py` para cumprir a R4 ("um usuário só pode ver os próprios pedidos") e criar um teste negativo que confirme a negação; pedido de outro usuário responde **404** (mesma resposta de pedido inexistente: como os IDs são sequenciais, um 403 revelaria quais pedidos existem); pode tocar: a função `get_pedido` de `caso/miniloja/handlers.py` e um arquivo de teste **novo** em `caso/testes_existentes/`; não pode tocar: nenhum outro arquivo de `caso/` (inclusive `regras.md` e os testes existentes), `testes/` e o golden master; invariantes: testes existentes sem alteração e passando (o dono continua vendo o próprio pedido com 200 e o pedido inexistente continua 404, cobertos por `test_handlers.py`), golden master com igualdade exata, contrato inalterado; pronto quando: `python -B testes/test_miniloja.py --codigo caso` (11 OK), `python -B testes/test_miniloja.py --codigo caso --existentes` (26 + novos, OK) e `python -B exercicios/aula-2/golden_master.py comparar` (384 casos, 0 divergências); o novo teste passa na branch e falha no código da `main`; e `git diff --stat main...HEAD -- caso/` mostra apenas `handlers.py` e o novo teste; pare e pergunte se: aparecer qualquer outro bug fora da R4, o golden master divergir, for preciso alterar outro arquivo, a assinatura ou o tipo de retorno; nesses casos, registrar e não corrigir. **Cumprido? Como verifiquei (comando ou barreira):** ___

**Verificação:** teste que falharia sem a mudança ___; prova (execução antes e depois, sabotagem ou mutação) ___

| O que a IA errou (o quê, onde) | Como detectei | O que corrigi e por quê (causa e impacto) |
| --- | --- | --- |
| ___ |  |  |
| ___ |  |  |
| ___ |  |  |

**Dependências novas (se houver) e checagem:** ___

| Medição do meu time | Meu desenho |
| --- | --- |
| Pergunta e decisão | ___ |
| Métrica primária e guardrail | ___ |
| Baseline, período e método | ___ |
| Risco de manipulação e contramedida | ___ |
| Tarefa recorrente a automatizar e verificação exigida | ___ |

**Limites e condição para rever:** ___

**Procedência/IA:** não utilizada / ferramenta e modelo visíveis: ___; tarefa delegada e contexto: ___; trecho aproveitado: ___; minha verificação/intervenção: ___. O raciocínio e a decisão registrados são meus.

**Revisão:** [ ] modo; [ ] escopo; [ ] verificação; [ ] erros da IA; [ ] medição e automação; [ ] procedência.
