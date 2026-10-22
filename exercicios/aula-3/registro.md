# Registro individual — AV1.3

**Limite: uma página, incluindo evidências essenciais.** Estudante: Alecsander D. Cruz — Data: 17/10/2026
Origem: `caso/testes_existentes/` e `caso/regras.md` fictícios; modalidade: execução própria

| Teste suspeito | Tipo de tautologia | Sabotagem que apliquei (ou raciocínio) | Continuou verde? |
| --- | --- | --- | --- |
| `test_calculo::test_cupom_natal_com_flag` | Sem asserção real (`assertIsNotNone`: qualquer número passa) | `calculo.py`: NATAL `total * 0.8` → `0.79` | Sim (26 OK) |
| `test_descontos::test_aplicar_desconto` | Espelho (esperado = `total - total*10/100`, mesma expressão do código; do contrato seria `180.00`) | Raciocínio: erro na fórmula se repete no esperado. Sabotagem: `PERCENTUAIS["VIP15"]` 15 → 5 | Sim (26 OK) |
| `test_pedidos::test_fluxo_chama_colaboradores` | Super-mockado / afirma o mock (só checa `.called`, nunca argumentos) | `pedidos.py`: `gateway.cobrar(total, token)` → `cobrar(0, token)` (cobra R$ 0) | Sim (26 OK) |

| Mutante sobrevivente | Por que sobreviveu | Teste que o mataria (ou "equivalente", com justificativa) |
| --- | --- | --- |
| `estoque.py`: `disponivel < qtd` → `disponivel <= qtd` | Falta fronteira: testes pedem 3 de 10 e 3 de 2; ninguém pede exatamente o saldo | `Estoque({"BOLA-01": 5}).reservar("BOLA-01", 5, "p1")` não levanta e `saldo == 0` (mutante levanta `EstoqueInsuficiente`) |
| `calculo.py`: `desconto_aplicado = True` → `False` | **Equivalente** | Só é lida em `if desconto_aplicado: pass` (l. 71–72): não afeta retorno nem efeito colateral; nenhum teste a distingue |

| Caso derivado do contrato (entrada) | Esperado (cálculo à mão) | Observado no código | Decisão |
| --- | --- | --- | --- |
| Fronteira: 1 × R$ 200,00, sem cupom, PE | 200,00 ≥ 200 → frete 0; 200,00 × 1,05 = **210,00** | **223,55** | Código errado: `if total > 200` contraria R1.3 (≥); `test_cenarios_gravados` grava o erro |
| Arredondamento: 1 × R$ 10,00, sem cupom, PE | (10,00 + 12,90) × 1,05 = 24,045 → meio p/ cima **24,05** | **24,04** | Código errado: float dá 24,04499…, `round()` não é meio p/ cima (R1.5) |
| Desconto + fronteira: 1 × R$ 222,23, PROMO10, SP | 222,23 × 0,9 = 200,007 ≥ 200 → frete 0; × 1,07 = 214,00749 → **214,01** | **214,01** | Concorda |

**ADR curto (fronteira do frete):** contexto: R1.3 manda frete grátis com subtotal c/ desconto **≥** R$ 200,00; `calculo.py:46` usa `> 200`, e 1 × R$ 200,00 (PE) devolve 223,55 em vez de 210,00; `test_cenarios_gravados` grava 223,55 (snapshot do erro); decisão: o código está errado. Corrigir para `>=` e trocar o esperado de `limite_200` por 210.00, calculado do contrato; consequências: o snapshot fica vermelho até ser corrigido; pedidos de exatamente R$ 200 deixam de pagar frete; entra o par de fronteira 199,99 × 200,00; alternativa descartada: alterar o contrato para `>`, porque o contrato é a fonte da verdade e `regras.md` não pode ser alterado.

**Trecho essencial de evidência:** `MINILOJA_TEST_CMD="python -B testes/test_miniloja.py --existentes --codigo caso -x" python -B testes/mutacao_manual.py calculo.py descontos.py estoque.py formatacao.py pedidos.py relatorios.py handlers.py` → `Mutantes: 30 | mortos: 23 | sobreviventes: 7 | escore: 77%`. Nota de ambiente: no Windows, `python -B testes/mutacao_manual.py` falha com `FileNotFoundError` porque o script passa o caminho do Python (`C:\Users\...\python.exe`) por `shlex.split`, que trata `\` como escape e apaga as barras; contornei com a variável `MINILOJA_TEST_CMD`, prevista na docstring do script, sem alterar `testes/`. `cadastro.py` ficou fora porque o trecho mutado não existe mais após a refatoração da AV1.1. Sabotagens da tabela 1: `python -B testes/test_miniloja.py --codigo <cópia> --existentes` → `Ran 26 tests ... OK`. **Limite do que a suíte garante e condição para rever a decisão:** mesmo com os testes novos, continuam vivos frete RJ, NATAL, VIP15, `total_fmt` e formatação do relatório; o arredondamento em float (caso 2) segue sem correção; `cadastro.py` não foi mutado; e a mutação só cobre 31 falhas escolhidas, então escore alto ≠ código correto (cobertura de ~90% conviveu com 7 sobreviventes). Rever o ADR se uma nova versão de `regras.md` alterar R1.3 (limite ou operador do frete grátis).

**Procedência/IA:** ferramenta e modelo visíveis: Claude Code (extensão VS Code), Claude Opus 5.5 (`claude-opus-5-5`); tarefa delegada e contexto: rodar a mutação e as sabotagens em cópia de trabalho, propor os testes candidatos, conduzir um quiz por etapa, obter o observado no código e redigir as células a partir das minhas respostas; trecho aproveitado: comandos e saídas da evidência, redação das tabelas e do ADR; minha verificação/intervenção: escolhi as classificações, os cálculos e as decisões no quiz; calculei os 3 casos à mão antes de ver o observado; li `calculo.py:46`, `:71-72` e `estoque.py`; revisei o texto final; repeti as 3 sabotagens da tabela 1 numa cópia (caso-teste/), aplicadas juntas e com o controle PROMO10 0.9 → 0.91: os 3 testes-alvo continuaram ok e só test_cupom_promo10_sp falhou.. O raciocínio e a decisão registrados são meus.

**Revisão:** [x] três testes; [x] dois mutantes; [x] três casos do contrato; [x] ADR; [ ] até uma página.
