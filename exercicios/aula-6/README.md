# AV1.6 — Medir e escolher o que automatizar

**Individual — registro consolidado em 35min — B6, 24/10/2026, prática 15h10–16h25 (Brasília).** Integra AV1, que vale 20% da nota pela média simples dos registros dos blocos com presença. Consulte a [avaliação e rubrica pública](../../avaliacao.md).

## Objetivo

Quero desenhar uma medição honesta para o meu time e apontar uma tarefa recorrente candidata a automação, com a verificação que ela exigiria.

## Contexto e insumos

Insumos: seus registros **AV1.1 a AV1.3** (tempo até "verificado", idas e vindas, tamanho de diff, escore de mutação) como um **baseline em miniatura** do curso, e o que você sabe do seu time. Não use dados do empregador: descreva o contexto de forma genérica.

- **Medição honesta:** pergunta e a decisão que depende dela · métrica primária · guardrail de qualidade · baseline (de onde vem) · período e método · confundidores · **risco de a métrica ser manipulada**.
- **Automação:** frequência · custo atual · verificabilidade · variabilidade · raio de impacto · custo de manter. A saída do agente é **proposta**, não ação. Verificação: checagens determinísticas, permissões mínimas, orçamento e tempo-limite, responsável.
- **Risco de CI:** não rode agente com segredos ou escrita sobre conteúdo não confiável (por exemplo, PR de fork).
- [Template individual](template-registro.md).

## Passos — 35min

1. **Ler — 5min.** Leia seus registros anteriores e escolha o contexto de time que você vai medir.
2. **Produzir individualmente — 20min.** Preencha o desenho da medição e a tarefa candidata a automação. Declare como a métrica poderia ser gamificada e qual guardrail protege a qualidade. Para a automação, escreva a verificação que a saída exigiria **antes** de qualquer ação.
3. **Revisar pela rubrica — 5min.** Confira se há baseline (mesmo que pequeno) e se o risco de manipulação está declarado.
4. **Entregar — 5min.** Finalize um único registro individual de até uma página, usando o template. O canal acadêmico será informado pelo professor; este material não presume endereço de envio.

## Entrega e checklist

- [ ] Pergunta, decisão, métrica primária, guardrail, baseline, período e método, confundidores.
- [ ] Risco de manipulação declarado e contramedida.
- [ ] Tarefa recorrente candidata e a verificação que ela exigiria (determinística, permissões, orçamento, responsável).
- [ ] Um limite da medição e uma condição para interromper.
- [ ] Origem e declaração de IA, se utilizada.

**Critério de conclusão:** outra pessoa consegue ver como você saberia se houve ganho e como a automação seria verificada antes de agir.

| Critério AV1 | Peso | Indicadores deste registro |
| --- | --- | --- |
| Aplicação/decisão | 30% | Pergunta ligada a uma decisão; tarefa de automação com filtro (frequência, verificabilidade, raio de impacto). |
| Evidência | 40% | Baseline identificado (mesmo em miniatura); guardrail; verificação da automação descrita. |
| Limites/alternativa | 30% | Risco de a métrica virar meta, confundidores, condição para interromper ou revisar. |

**Dica:** sem baseline não existe ganho, existe impressão. Uma métrica de uso (quantas sugestões aceitas) não é uma métrica de valor.
