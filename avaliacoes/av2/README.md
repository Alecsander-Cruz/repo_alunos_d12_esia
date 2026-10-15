# AV2 — Refatoração e testes verificáveis

**Individual — 2h autônomas — prazo 21/10/2026, 23h59 (Brasília).** Vale 30% da nota. Consulte a [rubrica pública](../../avaliacao.md).

## Objetivo
Quero fechar uma refatoração com escopo declarado e plano revisado, preservando o comportamento, e entregar uma suíte de testes que **falharia** se a mudança estivesse errada.

## Insumos
- **Caminho A (seu código):** um módulo do **seu próprio** projeto pessoal ou de estudo, no seu ambiente. **Código ou dados do empregador não são aceitos como evidência neste pacote.**
- **Caminho B (MiniLoja):** a refatoração de `calcular_total` e a suíte do bloco 3, no seu fork do pacote.
- Os dois caminhos usam a mesma rubrica.

## Passos
1. **Escopo e plano.** Escreva os seis campos e o plano revisado (o que você cortou do plano do agente).
2. **Mudança pequena.** Refatore sem alterar comportamento. Evidência: golden master ou equivalente com igualdade exata.
3. **Suíte com verificação real.** Cubra o código com testes que partem do contrato (não do código). Mostre a prova de que falhariam: sabotagem, mutação ou teste diferencial. Trate os sobreviventes (ou justifique os equivalentes).
4. **Documentação útil.** Contrato e motivo em docstring ou ADR com contexto real.
5. **Registro.** Até duas páginas: escopo, plano, mudança, verificação, decisões. Anexe o diff (resumo) e os testes. Declare a IA.

## Entrega e checklist
- [ ] Seis campos do escopo e plano revisado.
- [ ] Evidência de comportamento preservado.
- [ ] Testes derivados do contrato, com prova de que falhariam.
- [ ] Mutantes tratados ou justificados.
- [ ] ADR ou docstring com contrato e motivo.
- [ ] O que a IA errou, de forma específica.
- [ ] Procedência e declaração de IA.

**Critério de conclusão:** outra pessoa consegue repetir a verificação e ver que os testes falham quando o código é sabotado. Rubrica: escopo e plano 20% · comportamento preservado 25% · suíte com verificação real 35% · documentação e ADR 20%. [Modelo de registro](template-registro.md).
