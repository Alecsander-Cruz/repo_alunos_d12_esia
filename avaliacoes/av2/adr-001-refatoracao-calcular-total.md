# ADR-001 — Refatorar `calcular_total` sem corrigir os desvios do contrato

**Status:** aceito (AV2, 21/10/2026) · **Arquivo:** `caso/miniloja/calculo.py`

## Contexto
- `calcular_total` tinha código morto: a variável `desconto_aplicado`, lida só em `if desconto_aplicado: pass`, os ramos de cupom sem efeito e um comentário de 2023. Também repetia os valores de frete e taxa por UF em dois `if/elif`, enquanto `FRETE_POR_UF`/`TAXA_POR_UF` existiam e não eram usadas. Para mudar um valor, era preciso mexer em dois lugares.
- O código diverge do contrato (`caso/regras.md`) em dois pontos, já registrados na AV1.3:
  - R1.3: usa `> 200` em vez de `>= 200`;
  - R1.5: `round()` em float não arredonda meio para cima.
- Na AV1.2, uma refatoração com `FRETE_POR_UF[uf]` passou a levantar `TypeError` para `uf=["PE"]` (lista não é hashable). O original devolvia o valor de "demais UFs".

## Decisão
- Refatorar sem mudar comportamento: remover o código morto e usar as tabelas existentes por meio de `_valor_por_uf`.
- `_valor_por_uf` compara com `==`, sem `dict.get` nem `in`, para que a UF não hashable continue caindo no padrão.
- Manter os dois desvios do contrato e documentá-los na docstring.
- A prova de equivalência é o golden master: 384 casos, igualdade exata de valor, tipo e tipo da exceção.

## Consequências
- O golden master fica em 0 divergências, e a assinatura e o tipo de retorno não mudam.
- Os testes do contrato (`avaliacoes/av2/test_calculo_contrato.py`) marcam os dois desvios com `expectedFailure`. Se alguém corrigir um deles, a suíte acusa *unexpected success*, e o decorador precisa ser retirado conscientemente.
- `testes/mutacao_manual.py` procura o texto literal do código original. Por isso, a mutação passa a rodar sobre o original, e o código novo é coberto por sabotagens manuais.

## Alternativas descartadas
- **Corrigir `>= 200` e o arredondamento junto com a refatoração:** misturaria mudança de comportamento com refatoração. O golden master deixaria de provar equivalência (16 divergências só no `>= 200`).
- **`tabela.get(uf, padrao)`:** é mais curto, mas muda a exceção para UF não hashable. É o erro da rodada 1 da AV1.2.
- **Tornar `uf` obrigatória ou mudar o padrão `"PE"`:** R1 não define UF padrão, mas `pedidos.py` e outros chamadores dependem dele. Seria mudança de API.

## Condição para rever
- Quando houver uma tarefa com escopo próprio para corrigir R1.3 e R1.5. Nela, as divergências do golden master passam a ser esperadas, são revisadas caso a caso e só então a linha de base é regravada.
- Também quando uma nova versão de `regras.md` mudar R1.3 ou R1.5, ou definir uma UF padrão.
