# Guia do fim de semana 1 — AV1.1, AV1.2, AV1.3 e AV2

Consulta individual e impressão. Cada seção resume o enunciado; o enunciado completo e o modelo estão em `exercicios/aula-N/`.

## AV1.1 — Escolher o modo (16/10, prática 20h30–21h35)
- **Dados:** contrato R3 (`caso/regras.md`), verificações v07 a v11, CPFs fictícios em `caso/dados/cpfs.json`.
- **Passos:** defina o critério de aceite → execute **T1 em dois modos** e T2 em um → decida **T3** (hipotética) sem executar → registre.
- **Exemplo de preenchimento (outra tarefa, não copie):** "Tarefa: validar e-mail. Modo A (completar): 3min até 1ª versão, 9min até verificado, 1 ida e volta, 20% corrigido; a IA aceitou `a@b`. Verifiquei com 3 casos de borda. Modo B (agente): 6min, 14min, 3 idas e voltas, 40% corrigido; o agente alterou um teste existente."
- **Rubrica:** aplicação/decisão 30% · evidência 40% · limites/alternativa 30%.

## AV1.2 — Declarar escopo antes de mudar (17/10, prática 10h10–11h30)
- **Dados:** `caso/miniloja/calculo.py`, contrato R1.
- **Passos:** passo zero (golden master com igualdade exata) → rodada 1 sem escopo → desfazer → rodada 2 com seis campos e plano revisado → comparar → `AGENTS.md` mínimo.
- **Exemplo de escopo (outro módulo):** "Objetivo: extrair a taxa de `calcular_total` para uma função. Pode tocar: `calculo.py`. Não pode tocar: assinatura pública, outros módulos. Invariantes: mesmas saídas do golden master. Pronto: verificações e golden verdes. Pare e pergunte se precisar mudar tipo numérico ou achar algo que pareça bug."
- **Rubrica:** mesma da AV1.

## AV1.3 — Testes que falhariam (17/10, prática 15h10–16h30)
- **Dados:** `caso/testes_existentes/`, `testes/mutacao_manual.py`, contrato R1 e R2; [execução acompanhada](execucao-acompanhada-b3.md).
- **Passos:** classifique 3 testes → trate 2 mutantes → derive 3 casos do contrato e compare → ADR curto.
- **Exemplo de caso derivado (outra regra):** "Entrada: 1 item de R$ 10,00, UF XX, sem cupom. Esperado pelo contrato: (10,00 + 29,90) × 1,08 = 43,092 → 43,09. Observado: ___."
- **Rubrica:** mesma da AV1.

## AV2 — Refatoração e testes verificáveis (prazo 21/10, 23h59)
- **Passos:** escopo e plano → mudança pequena com comportamento preservado → suíte com prova de que falharia → documentação → registro de até duas páginas.
- **Critérios:** escopo e plano 20% · comportamento preservado 25% · suíte com verificação real 35% · documentação e ADR 20%.
