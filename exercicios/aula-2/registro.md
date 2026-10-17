# Registro individual — AV1.2

**Limite: uma página, incluindo evidências essenciais.** Estudante: Alecsander D. Cruz — Data: 17/10/2026
Origem: `caso/miniloja/calculo.py` fictício; modalidade: **execução própria**.

**Golden master:** 369 entradas (3 carrinhos de `carrinhos.json` + 10 de fronteira — R$ 199,99/200,00/200,01, desconto cruzando R$ 200, arredondamento 15,645, vazio, qtd 0 — × 7 cupons, incluindo NATAL com flag 0/1 × 4 UFs, + 5 variações de texto/omissão); gerado por `exercicios/aula-2/golden_master.py gravar` sobre o código antes da rodada 1; comparação exata por `assertEqual` de valor e tipo, sem tolerância (`assertAlmostEqual`/`isclose` descartados: esconderiam diferença de centavo). Resultado: linha de base 369/369 idênticos (`OK`, 0 divergências); mutação de teste `> 200`→`>= 200` acusa 16 divergências.

| Medida | Rodada 1 (sem escopo) | Rodada 2 (com escopo) |
| --- | --- | --- |
| Linhas adicionadas/removidas | +24 / −61 |  |
| Arquivos alterados (e quais estavam fora do esperado) | 1 (`calculo.py`); fora do pedido: 4 constantes públicas novas e 2 funções auxiliares |  |
| Mudou comportamento? (golden master) | 369/369 idênticos (rodado por mim); porém UF/cupom não texto (ex.: lista) passou a gerar `TypeError` — fora da cobertura |  |
| Tempo de revisão | 10 min (agente executou em 2 min, 12:46–12:48) |  |
| Idas e vindas | 2 permissões, 0 perguntas de conteúdo |  |

**Escopo da rodada 2 (escrito antes de abrir o agente):** objetivo remover código morto e condicionais repetidas de `calcular_total`, separando desconto, frete e taxa em funções auxiliares, sem mudar nenhum resultado; pode tocar só `caso/miniloja/calculo.py`, incluindo funções privadas (`_`) e constantes novas nesse arquivo; não pode tocar a assinatura `calcular_total(itens, cupom=None, uf="PE")`, outros módulos de `caso/miniloja/`, `caso/testes_existentes/`, `testes/` e `caso/regras.md`; invariantes golden master com igualdade exata, ordem desconto → frete → taxa e mesmo comportamento também fora do golden master (ex.: UF/cupom não texto não pode passar a gerar exceção — furo visto na rodada 1); pronto quando (escrito antes de qualquer pedido ao agente) `calcular_total` estiver sem código morto e sem condicionais repetidas, com diff só em `caso/miniloja/calculo.py`, mesma assinatura pública, golden master 100% idêntico (igualdade exata) e `python -B testes/test_miniloja.py --codigo caso` e `... --existentes` com saída `0`; pare e pergunte se algo parecer bug, se o tipo de retorno ou o tratamento de algum tipo de entrada mudar, ou se for preciso mexer em outro módulo.
**Plano do agente: o que eu cortei ou corrigi antes de executar:** ___
**Algo que parecia bug e eu apenas reportei:** ___
**`AGENTS.md` mínimo:** ___

**Trecho essencial de evidência:** ___ **Limite e condição para rever o escopo:** ___

**Procedência/IA:** não utilizada / ferramenta e modelo visíveis: ___; tarefa delegada e contexto: ___; trecho aproveitado: ___; minha verificação/intervenção: ___. Use "não informado" para metadados indisponíveis. O raciocínio e a decisão registrados são meus.

**Revisão:** [ ] golden master; [ ] duas rodadas com números; [ ] seis campos; [ ] AGENTS.md; [ ] até uma página.
