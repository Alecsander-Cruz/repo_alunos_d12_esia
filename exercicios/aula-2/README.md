# AV1.2 — Declarar escopo antes de mudar

**Individual — registro consolidado em 35min — B2, 17/10/2026, prática 10h10–11h30 (Brasília).** Integra AV1, que vale 20% da nota pela média simples dos registros dos blocos com presença. Consulte a [avaliação e rubrica pública](../../avaliacao.md).

## Objetivo

Quero refatorar `calcular_total` em duas rodadas, uma sem escopo e outra com escopo e plano revisados, e comparar o tamanho do diff e o esforço de revisão.

## Contexto e insumos

Arquivo: `caso/miniloja/calculo.py`. Contrato: **R1** (`caso/regras.md`). A refatoração deve **preservar o comportamento**.

- **Passo zero:** grave o comportamento atual (golden master): uma lista de entradas variadas (carrinhos, cupons `PROMO10`, `VIP15`, `FRETEGRATIS`, `NATAL`, inválido, UFs PE, SP, RJ e outra) e as saídas atuais, e crie uma comparação com **igualdade exata**, sem tolerância.
- **Regra de ouro:** se a IA achar algo que pareça bug, ela **reporta, não corrige**. Corrigir mistura mudança de comportamento com mudança de estrutura.
- Sem ferramenta ou ambiente, analise [b2-rodada1-sem-escopo.md](../../apoio/respostas-simuladas/b2-rodada1-sem-escopo.md) e [b2-rodada2-com-escopo.md](../../apoio/respostas-simuladas/b2-rodada2-com-escopo.md) e identifique-as como simuladas.
- [Contrato](../../caso/regras.md) · [template individual](template-registro.md).

**Os seis campos do escopo:** objetivo · pode tocar · não pode tocar · invariantes · critério de pronto · critério de parada.

## Passos — 35min

1. **Ler — 5min.** Leia R1 e o código. Escreva o critério de pronto antes de pedir qualquer coisa.
2. **Produzir individualmente — 20min.** **Rodada 1:** peça ao agente "refatore `calcular_total`", sem declarar escopo; registre linhas e arquivos alterados, o que mudou de comportamento (use o golden master) e quanto tempo levou para revisar; desfaça tudo. **Rodada 2:** escreva os seis campos, peça o **plano**, revise-o antes de executar (corte o que não pediu) e execute; registre as mesmas medidas. Escreva um `AGENTS.md` mínimo (5 a 8 linhas: comandos, limites, uma convenção não óbvia).
3. **Revisar pela rubrica — 5min.** Confira se a comparação mostra diferença objetiva e se o escopo foi escrito **antes**.
4. **Entregar — 5min.** Finalize um único registro individual de até uma página, usando o template. O canal acadêmico será informado pelo professor; este material não presume endereço de envio.

## Entrega e checklist

- [ ] Golden master descrito (quantas entradas, como foi gerado, comparação exata).
- [ ] Rodadas 1 e 2 comparadas com números (linhas, arquivos, comportamento, tempo de revisão).
- [ ] Os seis campos do escopo e o que você alterou no plano do agente.
- [ ] `AGENTS.md` mínimo.
- [ ] Origem simulada, se usada, e declaração de IA.

**Critério de conclusão:** outra pessoa consegue ver que a rodada 2 teve escopo escrito antes e conferir a diferença de diff e de comportamento entre as rodadas.

| Critério AV1 | Peso | Indicadores deste registro |
| --- | --- | --- |
| Aplicação/decisão | 30% | Escopo escrito antes, plano revisado com cortes justificados e uma regra de parada. |
| Evidência | 40% | Números das duas rodadas e o resultado do golden master (comando e saída, ou análise declarada). |
| Limites/alternativa | 30% | Limite do golden master (preserva o comportamento atual, inclusive erros) e condição para ampliar ou reduzir o escopo. |

**Dica:** o golden master **preserva o erro**. Se você "consertar" algo durante a refatoração, o teste vai acusar, e isso é o desejado. Registre o que parecia bug e não corrigiu.
