# Execução acompanhada do bloco 3

Roteiro para verificar, na sua cópia do caso, se a suíte existente **perceberia** um erro. Sem ambiente, leia a coluna "Observado na preparação": é o que o professor viu ao executar. Não declare como observado por você.

## Antes de começar
Copie a pasta `caso/` para uma cópia de trabalho (por exemplo `trabalho/`) e use `--codigo trabalho` nos comandos. Confira a linha de base: `python -B testes/test_miniloja.py --codigo trabalho --existentes` deve terminar com `OK` (26 testes).

## Sabotagens sugeridas (arquivo `miniloja/calculo.py` e `miniloja/estoque.py`)

| # | Sabotagem (uma por vez) | Observado na preparação | O que isso ensina |
| --- | --- | --- | --- |
| 1 | `total = total * 0.9` → `total = total * 0.91` (cupom `PROMO10`) | **Falhou**: a suíte percebeu | Há teste com asserção real para `PROMO10` |
| 2 | `frete = 21.5` → `frete = 22.5` (RJ) | **Continuou verde** | Nenhum teste exercita o frete do RJ |
| 3 | `total = total * 0.8` → `0.79` (`NATAL`) | **Continuou verde** | O teste do `NATAL` só verifica `is not None` |
| 4 | `if disponivel < qtd:` → `if disponivel <= qtd:` (`estoque.py`) | **Continuou verde** | Falta o teste de borda (pedir exatamente o saldo) |
| 5 | `if total > 200:` → `if total >= 200:` | **Falhou** | Aqui o teste falhou por um motivo curioso: ele **grava o valor atual**. Confira o contrato (R1.3) antes de concluir que o código estava certo |

Registre cada resultado e **desfaça a sabotagem** antes da próxima.

## Mutação automática
`python -B testes/mutacao_manual.py` repete esse processo com 31 falhas. Na preparação: 23 mortos, 8 sobreviventes, escore de 74%; a cobertura de linhas da mesma suíte é de cerca de 90%. Dos sobreviventes, um é **equivalente** (não muda o comportamento). Para cada um dos outros, escreva o teste que o mataria.

## Registro
Sem entrega nem nota adicional: use este roteiro para preencher a AV1.3.
