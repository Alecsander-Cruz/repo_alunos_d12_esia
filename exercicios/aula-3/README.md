# AV1.3 — Testes que falhariam

**Individual — registro consolidado em 35min — B3, 17/10/2026, prática 15h10–16h30 (Brasília).** Integra AV1, que vale 20% da nota pela média simples dos registros dos blocos com presença. Consulte a [avaliação e rubrica pública](../../avaliacao.md).

## Objetivo

Quero distinguir teste que verifica de teste que só repete a implementação, tratar mutantes que sobrevivem e derivar casos de teste do contrato, e não do código.

## Contexto e insumos

Insumos: a suíte existente em `caso/testes_existentes/` (26 testes, que **passam**), o código refatorado (ou o original) e o contrato **R1** e **R2** em `caso/regras.md`. [Execução acompanhada](../../apoio/execucao-acompanhada-b3.md) (passo a passo) · [template individual](template-registro.md).

- **Sabotagem:** quebre o código de propósito (inverta um `if`, troque `*` por `+`, devolva uma constante) e rode a suíte. Se continuar verde, o teste é suspeito.
- **Mutação:** `python -B testes/mutacao_manual.py` injeta 31 falhas pequenas e lista as que **sobrevivem**. Sem ambiente, use a transcrição em [apoio/resultado-textual.md](../../apoio/resultado-textual.md).
- **Derivar do contrato:** o "esperado" vem de `regras.md`, calculado à mão. Se o código discordar, não "conserte o teste para passar": decida se o código ou a leitura do contrato está errada.
- Tipos de teste tautológico: espelho (recalcula a fórmula), afirma o mock, sem asserção real, snapshot do próprio código, super-mockado, passa com o corpo esvaziado.

## Passos — 35min

1. **Ler — 5min.** Leia R1 e R2. Defina, antes de rodar qualquer coisa, o que seria um teste que **falharia** para um erro real.
2. **Produzir individualmente — 20min.** **(a)** Escolha **3 testes** da suíte existente que você suspeita serem tautológicos; classifique-os e mostre a sabotagem (ou o raciocínio) que o prova. **(b)** Escolha **2 mutantes sobreviventes** e escreva o teste que o mataria. **(c)** Derive **3 casos do contrato** (inclua ao menos um na fronteira do frete grátis e um em que o arredondamento importe), calcule o esperado à mão e compare com o código. **(d)** Se houver divergência, decida qual lado está errado e escreva um ADR de 4 linhas (contexto, decisão, consequências, alternativa).
3. **Revisar pela rubrica — 5min.** Confira se cada afirmação tem uma sabotagem ou um cálculo que outra pessoa consegue repetir.
4. **Entregar — 5min.** Finalize um único registro individual de até uma página, usando o template. O canal acadêmico será informado pelo professor; este material não presume endereço de envio.

## Entrega e checklist

- [ ] Três testes classificados, com sabotagem ou raciocínio.
- [ ] Dois mutantes tratados, com o teste proposto (ou justificativa de equivalente).
- [ ] Três casos derivados do contrato: entrada, esperado calculado, observado, decisão.
- [ ] ADR curto, com contexto real.
- [ ] Origem e declaração de IA, se utilizada.

**Critério de conclusão:** outra pessoa consegue repetir a sabotagem ou o cálculo e chegar à mesma conclusão. A decisão de quem está errado (código ou leitura do contrato) está justificada.

| Critério AV1 | Peso | Indicadores deste registro |
| --- | --- | --- |
| Aplicação/decisão | 30% | Classificação correta dos testes; decisão fundamentada sobre divergências; ADR ligado ao que você observou. |
| Evidência | 40% | Sabotagem/mutante verificável; esperado calculado à mão a partir do contrato; comando e saída (ou análise declarada). |
| Limites/alternativa | 30% | Limite do que a suíte garante mesmo depois dos novos testes; mutante equivalente identificado e justificado; condição para rever o ADR. |

**Dica:** nunca altere o esperado para o valor que o código devolve. Se o esperado vem do código, o teste é espelho. Se a IA propuser um teste que passa de primeira, desconfie.
