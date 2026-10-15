> **RESPOSTA SIMULADA.** Texto construído pelo professor para análise, identificado como simulação. Não é saída real de um modelo e não mede desempenho de nenhuma ferramenta. Quem a usa **não deve declarar ter executado** a tarefa.

# Bloco 2 · Rodada 1, sem escopo (simulada)

**Pedido:** "Refatore `calcular_total`."

**Resumo do diff simulado:** 9 arquivos alterados, +412 e −187 linhas.
- `calculo.py` dividido em seis funções; **valores monetários passam de `float` para `Decimal`**.
- Novo arquivo `utils.py` com helpers.
- Assinatura pública alterada: `calcular_total(pedido)` em vez de `calcular_total(itens, cupom, uf)`; `pedidos.py` e `handlers.py` ajustados.
- Ramo do cupom `NATAL` **removido** por "parecer código morto".
- `testes_existentes/test_calculo.py` editado: valores esperados ajustados "para refletir o novo cálculo".

**Para você analisar:**
1. Quais mudanças são de **comportamento**, e não de estrutura? Dê um exemplo numérico: para 2 itens de R$ 1,00 em PE, o código atual devolve 15,64; com `Decimal` e arredondamento meio para cima, 15,65. O golden master perceberia?
2. O ramo `NATAL` é morto? (Veja `flags.py` e o contrato R1.2.) O golden master perceberia a remoção se a flag estiver desligada?
3. Quanto tempo você levaria para revisar 9 arquivos? O que você aceitaria e o que rejeitaria?
