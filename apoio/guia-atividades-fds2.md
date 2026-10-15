# Guia do fim de semana 2 — AV1.4, AV1.5, AV1.6 e AV3

## AV1.4 — Ler legado com prova (23/10, prática 20h05–21h25)
- **Dados:** repositório desconhecido liberado pelo professor em `caso/legado/`.
- **Passos:** escreva onde procuraria cada resposta → responda cinco perguntas com trecho → registre uma resposta errada com aparência de certa → grave a saída de dois relatórios → plano de migração em fatias.
- **Exemplo de linha (outro sistema):** "Afirmação: só `Pagamento.cobrar` escreve em `transacoes`. Trecho: `pagamento.py:42`. Contraevidência: busquei `INSERT INTO transacoes` e achei também `scripts/estorno.sql:3`. Status: **refutada**."
- **Rubrica:** aplicação/decisão 30% · evidência 40% · limites/alternativa 30%.

## AV1.5 — Revisar um PR de agente (24/10, prática 10h10–11h30)
- **Dados:** PR liberado pelo professor em `apoio/pr-bloco5/`; contrato R4.
- **Passos:** liste as alegações do PR → aplique o checklist da turma → rode você mesmo o que o PR diz que rodou → ao menos quatro achados com severidade e teste → decida o merge.
- **Exemplo de achado (outro PR):** "Onde: `relatorio.py`. Problema: SQL montado por concatenação com parâmetro do usuário; impacto: injeção. Severidade: **bloqueia**. Correção: consulta parametrizada; teste: entrada com aspas simples deve ser tratada como texto."

## AV1.6 — Medir e escolher o que automatizar (24/10, prática 15h10–16h25)
- **Passos:** pergunta e decisão → métrica primária e guardrail → baseline → risco de manipulação → tarefa candidata com verificação.
- **Exemplo (outro time):** "Pergunta: o agente para atualizar dependências reduz o tempo da CVE ao merge sem aumentar reversões? Primária: mediana de dias. Guardrail: taxa de revert. Baseline: 8 semanas anteriores. Risco: aceitar atualização sem ler *breaking changes*."

## AV3 — Entrega final (prazo 30/10, 23h59)
- **Entregáveis:** PR assistido (descrição, plano, verificação, teste que falharia) + registro do que a IA errou + meia página de medição e automação.
- **Critérios:** modo 10% · escopo 15% · mudança revisável 15% · verificação 20% · honestidade sobre a IA 15% · justificativa das correções 10% · medição e automação 15%.
