# AV3 — Entrega final: PR assistido e medição

**Individual — 2h autônomas — prazo 30/10/2026, 23h59 (Brasília).** Vale 50% da nota. Consulte a [rubrica pública](../../avaliacao.md).

## Objetivo
Quero entregar um pull request assistido por IA que outra pessoa consiga revisar e verificar, com o registro honesto do que a IA errou, e a medição que desenhei para o meu time.

## Insumos
- **Caminho A (seu código):** uma mudança pequena no **seu próprio** repositório pessoal ou de estudo. Nada do empregador.
- **Caminho B (MiniLoja):** uma das tarefas abaixo, no seu fork do pacote.
  - **B1.** Corrigir o acesso a pedidos de outro usuário (R4), com **teste negativo**.
  - **B2.** Migrar valores monetários de `float` para `Decimal` (R1.5), com golden master atualizado de propósito e um ADR.
  - **B3.** Corrigir a reserva de estoque que não é desfeita quando um item falha (R2.2), com teste de regressão.
- Seus registros AV1.1 a AV1.6 e a AV2.

## O que entregar
1. **O pull request** (ou diff equivalente): descrição com intenção e escopo, plano, como foi verificado (comandos e saída), o teste que **falharia sem a mudança**, dependências novas (se houver) e o modo de interação usado, **e por quê**.
2. **Registro do que a IA errou e do que você corrigiu**, e por quê.
3. **Meia página com a medição** desenhada no bloco 6 e a tarefa recorrente candidata a automação, com a verificação que exigiria.

## Checklist
- [ ] Modo de interação justificado, com alternativa comparada.
- [ ] Escopo declarado **antes** e cumprido; mudança revisável.
- [ ] Teste que falharia sem a mudança, com evidência.
- [ ] Honestidade na descrição do que a IA errou; justificativa técnica das correções.
- [ ] Medição (pergunta, métrica, baseline, guardrail, risco de manipulação) e automação com verificação.
- [ ] Procedência e declaração de IA.

**Critério de conclusão:** outra pessoa consegue revisar o diff, rodar a verificação e confrontar o registro de erros da IA com o que você entregou. Rubrica: modo 10% · escopo 15% · mudança revisável 15% · verificação efetiva 20% · honestidade sobre a IA 15% · justificativa das correções 10% · medição e automação 15%. [Modelo de registro](template-registro.md).
