# Registro individual — AV2

**Limite: duas páginas de análise + anexo técnico curto.** Estudante: Alecsander D. Cruz — Data: 21/10/2026 — Caminho: B (MiniLoja) — refatoração refeita do zero a partir da `main`, aproveitando o golden master da AV1.2 (ampliado para 384 casos)

**Escopo (seis campos, escrito antes de abrir o agente):** **objetivo** refatorar `calcular_total` sem alterar comportamento, removendo código morto e duplicação; bugs conhecidos (`> 200` contra R1.3, `round` contra R1.5) **não** devem ser corrigidos; **pode tocar** apenas `caso/miniloja/calculo.py`; **não pode tocar** a assinatura pública `calcular_total(itens, cupom=None, uf="PE")` (`pedidos.py` chama por posição), nada do golden master (`exercicios/aula-2/golden_master.*`), nenhum outro arquivo (inclusive `testes/`, `caso/regras.md` e `caso/testes_existentes/`, que ficam para mim, numa etapa separada); sem commit nem merge; não alterar nem **ler** outras branches (as `av1.2-*` têm a solução antiga); **invariantes** para qualquer entrada, a função refatorada devolve o mesmo valor, do mesmo tipo (`float`), com igualdade exata, ou levanta a mesma exceção (tipo e mensagem); ordem desconto → frete → taxa; nenhum bug existente corrigido. Verificação: golden master de 384 casos (valor, tipo e tipo da exceção); **pronto quando** `git diff --stat` lista só `caso/miniloja/calculo.py`; não existem mais os ramos de cupom sem efeito (FRETEGRATIS no bloco de desconto, `else` do NATAL e do cupom desconhecido), a variável `desconto_aplicado` (l. 19, 71–72) e o comentário morto (l. 16); cada valor de frete e taxa por UF aparece uma única vez (usando `FRETE_POR_UF`/`TAXA_POR_UF`, l. 4–5); `python -B testes/test_miniloja.py --codigo caso` → `Ran 11 tests … OK`, saída 0; `… --existentes` → `Ran 26 tests … OK`, saída 0; `python -B exercicios/aula-2/golden_master.py comparar` → `Golden master: 384 casos, 0 divergência(s)` e `OK`, saída 0; **pare e pergunte se** achar algo que pareça bug, o golden master divergir, for preciso alterar outro arquivo, a assinatura ou o tipo de retorno.
**Plano do agente: o que cortei ou corrigi:** ___

**Comportamento preservado:** método ___; entradas ___; resultado (comando e saída) ___

| Teste (derivado de qual regra do contrato) | Como provei que falharia (sabotagem, mutação ou diferencial) | Resultado |
| --- | --- | --- |
| ___ |  |  |
| ___ |  |  |
| ___ |  |  |

**Mutantes sobreviventes e tratamento (ou equivalentes justificados):** ___
**Documentação (contrato e motivo) ou ADR:** ___
**O que a IA errou (o quê, onde, como detectei):** ___
**Limite da verificação e condição para rever:** o golden master cobre só as entradas geradas: uma entrada fora da amostra (como `uf=["PE"]` na rodada 1 da AV1.2, antes da ampliação) pode divergir sem que ele perceba; e compara só o **tipo** da exceção, não a mensagem. ___

**Procedência/IA:** não utilizada / ferramenta e modelo visíveis: ___; tarefa delegada e contexto: ___; trecho aproveitado: ___; minha verificação/intervenção: ___. O raciocínio e a decisão registrados são meus.

**Anexo:** resumo do diff (arquivos, linhas) e trechos dos testes.
**Revisão:** [ ] escopo; [ ] comportamento; [ ] testes com prova; [ ] documentação; [ ] erros da IA; [ ] limite.
