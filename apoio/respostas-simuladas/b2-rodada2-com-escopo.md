> **RESPOSTA SIMULADA.** Texto construído pelo professor para análise, identificado como simulação. Não é saída real de um modelo e não mede desempenho de nenhuma ferramenta. Quem a usa **não deve declarar ter executado** a tarefa.

# Bloco 2 · Rodada 2, com escopo (simulada)

**Escopo declarado:** objetivo, separar desconto, frete e taxa em funções; pode tocar só `calculo.py`; não pode tocar assinatura pública nem outros arquivos; invariantes: golden master exato; pronto: verificações e golden verdes; pare e pergunte se achar algo que pareça bug.

**Plano do agente (simulado):**
1. Extrair `_aplicar_desconto(total, cupom)`.
2. Extrair `_calcular_frete(total, cupom, uf)`.
3. Extrair `_aplicar_taxa(total, uf)`.
4. Manter `calcular_total` com a mesma assinatura, chamando as três em ordem.
5. Rodar o golden master e as verificações.
6. **Reportar, sem corrigir,** qualquer divergência com o contrato.

**Resumo do diff simulado:** 1 arquivo, +58 e −41 linhas. Golden master verde.

**Relato do agente (simulado):** "Observei que o limite do frete grátis usa `> 200`, e o contrato R1.3 diz 'maior ou igual a R$ 200,00'. **Não alterei**, porque mudaria o comportamento."

**Para você analisar:** o que o plano tinha de bom? O que você cortaria ou acrescentaria ao plano? O relato final está certo em reportar sem corrigir? Onde isso deveria ser registrado?
