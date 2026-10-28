# Registro individual — AV1.6

**Limite: uma página, incluindo evidências essenciais.** Estudante: Alecsander D. Cruz — Data: 27/10/2026
Origem: meus registros AV1.1 a AV1.3 e um contexto de time descrito de forma genérica.

| Campo da medição | Meu desenho |
| --- | --- |
| Pergunta (uma frase) | O escopo escrito antes reduz o retrabalho nas tarefas com o agente? |
| Decisão que depende da resposta | Exigir (ou não) escopo escrito antes de toda tarefa com o agente |
| Métrica primária | Itens fora do escopo desfeitos por tarefa (arquivo, função, constante ou comportamento alterado que o pedido não previa), contados na revisão do `git diff`, após a execução e antes do aceite |
| Guardrail de qualidade | Verificações `test_miniloja.py` (11/11) e suíte existente (26/26) com saída `0`; em tarefa que não deve mudar comportamento, golden master com 0 divergências (ele preserva bugs, então não vale para mudança de comportamento) |
| Baseline (de onde vem, que período) | Meus registros AV1.1–AV1.3 na MiniLoja (16–17/10/2026; "time" = eu, sozinho): itens fora do escopo R1 sem escopo = 7 (4 constantes públicas, 2 funções, 1 `TypeError` novo) e R2 com escopo = 0, golden master 369/369 nas duas (AV1.2); 0% corrigido à mão em T1/T2 com agente, 11/11 e 26/26 (AV1.1); mutação 23/30 = 77% (AV1.3) |
| Período e método de comparação | 2 semanas, ≥ 10 tarefas com agente de tipo e tamanho parecidos, alternando com e sem escopo (5 + 5), sempre em sessão nova; "reduziu" = mediana de itens fora do escopo menor com escopo, com o guardrail verde em todas as tarefas |
| Confundidores previstos | Aprendizado do código (a tarefa posterior sai melhor por eu já conhecer o caso; mitigado pela alternância); contexto que o agente lê sozinho (`CLAUDE.md`, `AGENTS.md`, READMEs) funciona como escopo implícito, como na R1 do AV1.2, e torna o "sem escopo" menos sem escopo; não determinismo do modelo; dificuldade real diferente entre tarefas de tamanho parecido |
| Como a métrica poderia ser gamificada | Declarar um escopo bem amplo, para que nada conte como "fora do escopo"; ou deixar de registrar o que foi desfeito |

**Contramedida contra a manipulação:** escrever e fixar o escopo antes da execução, listando explicitamente arquivos e funções que podem ser tocados (os seis campos do AV1.2; sem coringa como "qualquer arquivo"), e contar os itens comparando o diff com esse escopo (a parte de arquivos por `git diff --name-only` × lista do escopo), em vez de depender de quem fez a tarefa dizer o que desfez.

| Tarefa recorrente candidata | Frequência e custo atual | Verificação da saída (determinística) | Permissões mínimas e orçamento | Responsável |
| --- | --- | --- | --- | --- |
| Relatório de revisão pós-tarefa (3 verificações + diff × escopo congelado); raio de impacto baixo: no pior caso, um relatório errado que eu reviso, sem alterar o caso | Toda tarefa com agente (≥ 10 em 2 semanas); ~10–15 min manual | Saídas `0` com 11/11 e 26/26; `golden_master.py comparar` com 0 divergências (só sem mudança de comportamento); `git diff --name-only` × lista do escopo commitado; itens de função/constante são candidatos que eu confirmo | Lê o repo, roda só esses comandos, escreve 1 relatório; proibido editar `caso/`, `testes/`, escopo, rodar `gravar`, commit/reset; sessão nova, separada da que executou a tarefa; local, sem segredos, fora da CI; 5 min por execução | Eu (aprovo item a item) |

**Limite da medição e condição para interromper ou rever:** limite: eu executo, escrevo o escopo e conto, então meu viés pode afetar a análise (o diff × lista e o relatório reduzem, mas itens de função/constante ainda dependem de mim); e a amostra é pequena (≥ 10 tarefas, uma pessoa, caso fictício), então o resultado vale para mim na MiniLoja, não para um time real. Interrompo se o guardrail ficar vermelho em tarefa aceita (a qualidade caiu e a primária deixa de valer). Revejo o desenho se escrever o escopo custar mais do que economiza na revisão manual.

**Procedência/IA:** ferramenta e modelo visíveis: Claude Code (extensão VS Code), Claude Opus 5.5 (`claude-opus-5-5`), como tutor; tarefa delegada e contexto: conduzir perguntas por etapa do template, ler meus registros AV1.1–AV1.3 para extrair o baseline, analisar minhas respostas e redigir as células a partir delas; trecho aproveitado: redação das células; correções da IA aceitas por mim: confundidor de contexto reformulado (escopo implícito); complementos sugeridos pela IA e aceitos por mim: confundidores de não determinismo e dificuldade, lista explícita no escopo, raio de impacto, método com ≥ 10 tarefas alternadas e mediana; minha verificação/intervenção: as ideias dos campos partiram de mim (pergunta, decisão, métrica, guardrail, gamificação, contramedida, tarefa de automação com verificação e permissões, limites); revisei o texto redigido; conferi os números do baseline com os registros. O raciocínio e a decisão registrados são meus.

**Revisão:** [x] medição completa; [x] risco de manipulação; [x] automação com verificação; [x] limite; [ ] até uma página.
