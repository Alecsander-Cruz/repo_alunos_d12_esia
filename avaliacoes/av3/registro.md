# Registro individual — AV3

**Limite: três páginas + até duas de evidências.** Estudante: Alecsander D. Cruz — Data: 28/10/2026 — Caminho: B (MiniLoja) — B1: acesso a pedidos de outro usuário (R4), com teste negativo

**Modo de interação usado e por quê (raio de impacto, oráculo, familiaridade):** editar com escopo, revisando o plano da IA antes da execução. Raio de impacto pequeno (uma função de `handlers.py` e um arquivo de teste novo), mas em controle de acesso, onde um erro vaza dados de clientes; revisar o plano antes permite conferir se a IA pretende tocar algo fora do escopo e se a abordagem faz sentido. Oráculo: a R4 do contrato ("um usuário só pode ver os próprios pedidos"); o status 404 é decisão minha, registrada no escopo, porque o contrato não define o status. Familiaridade média: conheço o caso pelas atividades anteriores (AV1.1 a AV2, em `cadastro.py`, `calculo.py` e na suíte existente), mas nunca tinha alterado `handlers.py`. Escolhi a B1 por ser a tarefa de escopo menor. **Alternativa comparada:** delegar a um agente. Mesmo com o escopo declarado, o agente poderia fazer algo fora dele sem que eu revisasse antes, gerando retrabalho; e, como a mudança mexe em controle de acesso, um erro não revisado poderia causar vazamento de dados.

**Escopo declarado antes (seis campos):** objetivo: corrigir `get_pedido` em `caso/miniloja/handlers.py` para cumprir a R4 ("um usuário só pode ver os próprios pedidos") e criar um teste negativo que confirme a negação; pedido de outro usuário responde **404** (mesma resposta de pedido inexistente: como os IDs são sequenciais, um 403 revelaria quais pedidos existem); pode tocar: a função `get_pedido` de `caso/miniloja/handlers.py` e um arquivo de teste **novo** em `caso/testes_existentes/`; não pode tocar: nenhum outro arquivo de `caso/` (inclusive `regras.md` e os testes existentes), `testes/` e o golden master; invariantes: testes existentes sem alteração e passando (o dono continua vendo o próprio pedido com 200 e o pedido inexistente continua 404, cobertos por `test_handlers.py`), golden master com igualdade exata, contrato inalterado; pronto quando: `python -B testes/test_miniloja.py --codigo caso` (11 OK), `python -B testes/test_miniloja.py --codigo caso --existentes` (26 + novos, OK) e `python -B exercicios/aula-2/golden_master.py comparar` (384 casos, 0 divergências); o novo teste passa na branch e falha no código da `main`; e `git diff --stat main...HEAD -- caso/` mostra apenas `handlers.py` e o novo teste; pare e pergunte se: aparecer qualquer outro bug fora da R4, o golden master divergir, for preciso alterar outro arquivo, a assinatura ou o tipo de retorno; nesses casos, registrar e não corrigir. **Cumprido? Como verifiquei (comando ou barreira):** ___

**Verificação:** teste que falharia sem a mudança: `caso/testes_existentes/test_acesso.py`, escrito antes da correção, a partir da R4 e da decisão do 404: C1 `test_outro_usuario_recebe_404_ao_pedir_pedido_alheio` (usuário 20 pede pedido do usuário 10 → 404), C2 `test_pedido_alheio_responde_igual_a_pedido_inexistente` (resposta, status e corpo, idêntica à de um pedido inexistente, `id + 1`, e sem `itens`, `total`, `total_fmt` e `usuario_id` no corpo) e C3 `test_dono_ve_o_proprio_pedido` (dono continua vendo o próprio pedido com 200; proteção contra regressão); prova: **antes** (código da `main`, `handlers.py` sem alteração), `python -B testes/test_miniloja.py --codigo caso --existentes` → 29 testes, `FAILED (failures=2)`, código de saída 1: C1 `AssertionError: 200 != 404`; C2 `(200, {'id': 3, 'itens': [...], 'status': 'pago', 'total': 66.05, 'total_fmt': 'R$ 66,05', 'usuario_id': 10}) != (404, {'erro': 'não encontrado'})`, ou seja, o pedido alheio vaza por inteiro; C3 e os 26 existentes passam. Depois: ___

| O que a IA errou (o quê, onde) | Como detectei | O que corrigi e por quê (causa e impacto) |
| --- | --- | --- |
| Agente de teste, no plano: atribuiu os bugs de estoque (R2.2/R2.3) às "tarefas do bloco 1" | Conferi com `testes/README.md`: as tarefas do bloco 1 são v08 a v10 (CPF, R3); a R2.2 é a tarefa B3 da AV3 | Corrigi a observação na aprovação do plano. Causa: afirmação sobre o contexto sem conferir a fonte. Impacto: nenhum no teste, mas o achado fora do escopo ficaria registrado com origem errada |
| Agente de teste, no plano do C2: usou `ID_INEXISTENTE = 0` como pedido inexistente | Revisão do plano: 0 é um ID que nunca existiria, e não o que um atacante tentaria | Troquei por `id + 1`. Causa: escolheu o valor seguro para a implementação atual, não o realista. Impacto: se uma validação futura respondesse 400 para o ID 0, o C2 falharia pelo motivo errado; `id + 1` tem formato válido e é exatamente o ID testado por quem percorre pedidos em sequência |
| Agente de teste, no plano do C2: conferência dos campos vazados só "se o corpo for dict" | Revisão do plano: `assert` dentro de `if` pode ser pulado sem aviso | Tirei a condição; a conferência roda sempre. Causa: programação defensiva no lugar errado (no teste). Impacto: uma verificação desligada em silêncio dá falsa confiança |

**Dependências novas (se houver) e checagem:** ___

| Medição do meu time | Meu desenho |
| --- | --- |
| Pergunta e decisão | ___ |
| Métrica primária e guardrail | ___ |
| Baseline, período e método | ___ |
| Risco de manipulação e contramedida | ___ |
| Tarefa recorrente a automatizar e verificação exigida | ___ |

**Achado fora do escopo (registrado, não corrigido, conforme o campo "pare e pergunte"):** em `PedidoService.criar` (`caso/miniloja/pedidos.py`), as reservas de estoque não são desfeitas quando o pagamento é recusado ou quando falta estoque de um item, o que viola a R2.2 e corresponde à tarefa B3. Apontado pelo agente de teste no plano.

**Limites e condição para rever:** ___

**Procedência/IA:** não utilizada / ferramenta e modelo visíveis: ___; tarefa delegada e contexto: ___; trecho aproveitado: ___; minha verificação/intervenção: ___. O raciocínio e a decisão registrados são meus.

**Revisão:** [ ] modo; [ ] escopo; [ ] verificação; [ ] erros da IA; [ ] medição e automação; [ ] procedência.
