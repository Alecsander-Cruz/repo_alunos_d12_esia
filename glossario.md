# Glossário

| Termo | O que significa |
| --- | --- |
| Agente de codificação | Sistema que planeja, lê arquivos, roda comandos e edita código de forma iterativa |
| Modo de interação | Forma de usar a IA: completar no editor, conversar, editar com escopo ou delegar a um agente |
| Harness (ambiente) | O que está em volta do modelo: arquivos que lê, comandos que roda, permissões, sandbox |
| Permissão (allowlist) | Lista do que o agente pode ler, escrever ou executar sem perguntar |
| Prompt injection | Instrução maliciosa escondida em conteúdo que o agente lê (arquivo, issue, página, resposta de ferramenta) |
| MCP | Padrão aberto para conectar aplicações de IA a ferramentas e dados externos |
| Escopo declarado | Texto, escrito antes, do que a mudança pode e não pode tocar e quando parar |
| Critério de parada | Condição em que o agente deve parar e perguntar |
| Plano | Descrição das etapas que o agente pretende executar, revisada antes da execução |
| Diff | Diferença entre duas versões do código |
| Refatoração | Mudar a estrutura sem mudar o comportamento observável |
| Golden master | Gravar as saídas atuais para comparar depois da mudança |
| Teste de caracterização | Teste que registra o que o código faz hoje, certo ou errado |
| Oráculo | Fonte do "resultado esperado" de um teste (contrato, regra, referência) |
| Teste tautológico | Teste que não pode falhar por erro do código, porque a asserção depende do próprio código ou de um dublê |
| Dublê (mock) | Objeto que substitui um colaborador no teste |
| Cobertura | Proporção do código executada pelos testes; não diz se algo foi verificado |
| Mutação | Teste que injeta pequenas falhas no código; mutante sobrevivente = suíte não notou |
| Mutante equivalente | Mutação que não altera o comportamento observável |
| ADR | Registro de decisão arquitetural (contexto, decisão, consequências, alternativas) |
| Legado | Código sem testes ou que ninguém mais entende bem |
| Costura (seam) | Ponto onde dá para alterar comportamento sem editar o código no lugar |
| Codemod | Transformação automática de código, normalmente baseada em árvore sintática |
| Viés de automação | Tendência a confiar demais na saída de um sistema automatizado |
| Slopsquatting | Registro malicioso de nomes de pacotes inventados por IA |
| Baseline | Medida de referência anterior à intervenção |
| Guardrail | Métrica de qualidade que acompanha a métrica principal |
| Lei de Goodhart | Quando uma medida vira meta, deixa de ser boa medida |
| SPACE / DORA | Estruturas para medir produtividade e desempenho de entrega |
| Evidência | Parte da resposta que permite a outra pessoa conferir sua conclusão |
| Procedência | De onde vieram os dados: enunciado, cálculo próprio, leitura de código ou execução própria |
| Saída simulada | Texto construído para análise, identificado como simulação; não é medição real de modelo |
