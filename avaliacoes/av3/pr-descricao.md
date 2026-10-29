# AV3 — B1: `get_pedido` nega pedido de outro usuário (R4)

## Intenção e escopo
Cumprir a R4 do contrato ("um usuário só pode ver os próprios pedidos"). Hoje, `handlers.get_pedido(usuario_id, pedido_id)` ignora `usuario_id` e devolve o pedido de qualquer usuário.

**Decisão:** o contrato não define o status de resposta. O pedido de outro usuário responde **404 `{"erro": "não encontrado"}`**, exatamente como um pedido inexistente. Como os IDs são sequenciais, um 403 revelaria quais pedidos existem.

Escopo declarado e commitado **antes** do código (`d9e60fa`, seis campos em [registro.md](registro.md)):
- **Pode tocar:** `get_pedido` em `caso/miniloja/handlers.py` e um arquivo de teste novo em `caso/testes_existentes/`.
- **Não pode tocar:** nenhum outro arquivo de `caso/`, nem `testes/`, `caso/regras.md` ou o golden master.
- **Invariantes:** assinatura e retorno `(status, corpo)` iguais; o dono continua vendo o próprio pedido com 200; o pedido inexistente continua 404.

## Plano e commits
1. `d9e60fa`: escopo e modo declarados.
2. `f12576d`: teste negativo `caso/testes_existentes/test_acesso.py`, **falhando** no código atual.
3. `848a3ec`: correção de uma linha em `handlers.py:37`.

```diff
-    if pedido is None:
+    if pedido is None or pedido["usuario_id"] != usuario_id:
         return 404, {"erro": "não encontrado"}
```

O pedido alheio e o inexistente passam pelo mesmo `return`, então a resposta é idêntica e nenhum campo do pedido aparece.

## Teste que falharia sem a mudança
| Caso | Afirma | Sem a correção | Com a correção |
| --- | --- | --- | --- |
| C1 `test_outro_usuario_recebe_404_ao_pedir_pedido_alheio` | O usuário 20 pede um pedido do usuário 10 → 404 | **FAIL** `200 != 404` | ok |
| C2 `test_pedido_alheio_responde_igual_a_pedido_inexistente` | Status e corpo iguais aos de `id + 1` (inexistente); sem `itens`, `total`, `total_fmt` nem `usuario_id` | **FAIL**: o pedido alheio vaza por inteiro | ok |
| C3 `test_dono_ve_o_proprio_pedido` | O dono vê o próprio pedido com 200 | ok (proteção contra regressão) | ok |

## Como verificar (na raiz do pacote)
```
git checkout f12576d -- caso/miniloja/handlers.py   # opcional: volta ao código sem a correção
python -B testes/test_miniloja.py --codigo caso --existentes
#   sem a correção: Ran 29 tests ... FAILED (failures=2), código de saída 1
git checkout HEAD -- caso/miniloja/handlers.py

python -B testes/test_miniloja.py --codigo caso                # Ran 11 tests ... OK (saída 0)
python -B testes/test_miniloja.py --codigo caso --existentes   # Ran 29 tests ... OK (saída 0)
python -B exercicios/aula-2/golden_master.py comparar          # 384 casos, 0 divergências (saída 0)
git diff --stat main...HEAD -- caso/                           # só handlers.py e test_acesso.py
```

## Dependências novas
Nenhuma. `caso/requirements.txt` continua igual; o teste importa apenas `unittest` e `miniloja`.

## Modo de interação
**Editar com escopo, com revisão do plano antes da execução.** Usei dois agentes em sessões separadas, um para o teste e outro para a correção, para que o teste não se moldasse à correção. O raio de impacto é pequeno, mas a mudança é em controle de acesso, onde um erro vaza dados. A alternativa, delegar a um agente sem revisar o plano, foi descartada por esse risco. O oráculo é a R4 mais a decisão do 404.

## O que a IA errou
Cinco itens, com detecção, causa e impacto, em [registro.md](registro.md). Os principais:
- No plano do teste, `ID_INEXISTENTE = 0`, que troquei por `id + 1`, e um `assert` dentro de um `if`, que removi.
- No relato da correção, afirmou que os três testes falhavam antes (eram dois) e entregou a saída editada como "completa". Por isso, toda a evidência acima vem de execução minha, independente.

## Fora do escopo (registrado, não corrigido)
Em `PedidoService.criar`, as reservas de estoque não são desfeitas quando o pagamento é recusado ou quando falta estoque de um item (R2.2, tarefa B3).

## Limites
Comparação estrita de tipo (`"10"` e `10` são diferentes, então nega o acesso); o C2 supõe IDs inteiros sequenciais; a autenticação não é verificada, porque o contrato não a prevê; qualquer novo endpoint que exponha pedidos precisa do mesmo teste. Detalhes em [registro.md](registro.md).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
