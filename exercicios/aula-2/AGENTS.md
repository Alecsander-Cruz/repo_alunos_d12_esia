# AGENTS.md — MiniLoja (AV1.2)

- **Verificar toda mudança:** `python -B exercicios/aula-2/golden_master.py comparar`; `python -B testes/test_miniloja.py --codigo caso`; `... --codigo caso --existentes`; `git diff main --stat`.
- **Nunca alterar:** `testes/` e `caso/regras.md`; não presumir aceite de impacto nem fazer commit sem pedido explícito.
- **Pare e pergunte se:** algo parecer bug, o tipo de retorno ou o tratamento de algum tipo de entrada mudar, ou for preciso mexer em outro módulo.
- **Golden master preserva bugs de propósito:** se ele acusar diferença ao "consertar" algo, reporte e não corrija.
- **`testes/mutacao_manual.py` depende do texto literal de `calculo.py`:** refatorar esse arquivo a quebra (usada na aula 3).
- **UF e cupom só com `==`:** `dict.get`, `[]` ou `in` exigem hash e fazem entrada não texto (ex.: lista) gerar `TypeError`.
