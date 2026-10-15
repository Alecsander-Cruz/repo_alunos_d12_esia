# D1.2 — Desenvolvimento Assistido por IA

Plano de ensino da turma · CESAR School · Turma 01 · Revisão pedagógica: prática individual verificável, caso evolutivo e repositório desconhecido.
Escopo deste documento: disciplina D1.2, de 24h, integrante do módulo institucional M1, de 72h. Os canais de aula, envio e acompanhamento de acessibilidade serão comunicados pela organização.

## 1. Ficha técnica do módulo

| Campo | Definição |
| --- | --- |
| Curso | Pós-Graduação Lato Sensu em Engenharia de Software e IA — CESAR School |
| Escopo | D1.2 — Desenvolvimento Assistido por IA, 24h; integra M1 institucional, de 72h |
| Professor/turma | Jamisson Santana de Freitas · Turma 01 |
| Carga | 18h ao vivo (seis blocos de 180min) + 6h autônomas; hora de 60min |
| Método | Exposição aplicada com demonstração, prática individual em código que o aluno precisa verificar, socialização de casos |
| B1 | 16/10/2026, sexta, 19–22h |
| B2/B3 | 17/10/2026, sábado, 9–12h e 14–17h |
| B4 | 23/10/2026, sexta, 19–22h |
| B5/B6 | 24/10/2026, sábado, 9–12h e 14–17h |
| Público | 42 profissionais de software em atuação; remoto ao vivo; um estudante acompanha com intérprete de Libras |
| Pré-requisitos | Leitura de código e noções de testes e git; instalação local não é condição de avaliação |
| Ferramentas | Python e biblioteca padrão para o caso; ao menos um assistente no editor e um agente de codificação com acesso a arquivos e terminal, ou o caminho textual |
| Alternativa de acesso | Respostas simuladas identificadas, transcrição de execução e inspeção textual; sem API paga obrigatória |
| Normas institucionais | Limite de falta de 25%, gravação após 48h por 90 dias sem gerar presença e abono somente pela Secretaria; recuperação, atraso e lançamento ainda aguardam confirmação |

Horários de Brasília. Almoço fora da carga; encerramento dos sábados às 17h.

Ementa de referência: leitura de bases de código, planejamento de mudanças, modificação de arquivos, geração de testes, refatoração, documentação, revisão e automação de tarefas recorrentes, com ênfase em fluxos verificáveis, colaborativos e compatíveis com práticas profissionais de engenharia.

## 2. Contexto: a trilha completa do curso

O curso tem 360h em cinco módulos de 72h: M1 fundamentos e desenvolvimento → M2 arquitetura e integração → M3 agentes e automação → M4 avaliação, segurança e operação → M5 produto e projeto aplicado.

| Disciplina de M1 | Carga | Contribuição e fronteira |
| --- | --- | --- |
| D1.1 — Engenharia de Software na Era da IA Generativa | 24h | Decidir quando usar IA, verificar saídas, reconhecer riscos. Já estabeleceu a régua de verificação e responsabilidade e a política de uso |
| D1.2 — Desenvolvimento Assistido por IA | 24h | **Fluência operacional**: escolher o modo, declarar escopo, testar de verdade, ler legado, revisar, medir. Aqui a pergunta deixa de ser "o que mudou" e passa a ser "como eu faço" |
| D1.3 — Prompting Técnico, Especificação e Contexto | 24h | Prompt como especificação, critérios de aceite, engenharia de contexto e instruções persistentes de projeto |

Aqui o prompt aparece **como meio**. Arquitetura, RAG, agentes como componente de produto e avaliação sistemática são de M2, M3 e M4. O agente é **ferramenta de trabalho do dev**, não peça da solução entregue. Subagentes, hooks e orquestração de automações pertencem a M3.

## 3. Filosofia pedagógica do módulo

**Método antes de ferramenta.** A maioria da turma já usa IA. O que falta é método: escopo declarado, verificação e responsabilidade. A disciplina não depende de uma ferramenta específica, mas depende da categoria: um assistente no editor e um agente de codificação.

**Toda prática roda em código que o aluno precisa verificar depois.** É o antídoto contra a disciplina virar demonstração de ferramenta. O caso tem dívida plantada em cada ponto trabalhado, e a verificação de verdade (teste que falharia) é o critério.

**Ganho real não é ganho percebido.** A evidência empírica sobre produtividade é contraditória. O aluno aprende a ler essa evidência e a medir o próprio contexto, em vez de repetir número de fornecedor.

**Avaliação individual e honesta.** O registro do que a IA errou vale mais do que um resultado perfeito. Avaliam-se decisão, evidência e argumento próprios; não se avalia presença, câmera, quantidade de prompts ou testes verdes.

**Segurança de ambiente.** Nada do empregador em sala. Permissões mínimas para agentes, árvore limpa e branch por tarefa são parte do método.

**Equidade e carga verificável.** Materiais antecipados, instruções escritas, caminho textual com a mesma rubrica. As 6h autônomas não pedem pesquisa nem projeto extra.

## 4. Questões de pesquisa aplicada por bloco

Os recortes abaixo são questões para análise, não afirmações sobre produtos. A bibliografia básica teve título, autoria e registro conferidos; a atualização de 24/02/2026 da METR foi conferida na fonte.

- **B1 — Modos e ambiente.** O que muda de um modo de interação para outro em contexto, verificação e custo? Por que o ambiente (arquivos, comandos, permissões) pesa tanto quanto o modelo, e que riscos de segurança ele traz?
- **B2 — Escopo.** Por que um diff pequeno é decisão de engenharia? O que o plano revisado evita?
- **B3 — Verificação real.** Que diferença há entre cobertura e verificação? Como reconhecer um teste que nunca falharia?
- **B4 — Legado.** Como acelerar a leitura sem terceirizar a conferência? O que é mecânico e o que é decisão humana numa migração?
- **B5 — Revisão e segurança.** O que o revisor costuma deixar passar quando ninguém "pensou" o código linha a linha? Que dependências e vetores novos aparecem com agentes?
- **B6 — Evidência e adoção.** Por que estudos sérios chegam a resultados opostos? O que medir, com que baseline, e quando a métrica vira meta?

## 5. Conceitos-base (glossário operacional)

Ver o [glossário](glossario.md). Os conceitos que sustentam a disciplina: **modo de interação**, **escopo declarado**, **plano revisado**, **oráculo**, **teste tautológico**, **mutação**, **teste de caracterização**, **viés de automação**, **baseline** e **guardrail**.

## 6. Pré-requisitos e setup

- A organização comunicará sala, ambiente da turma, canal de entrega e acompanhamento de acessibilidade quando confirmados.
- Disponibilizar previamente enunciados, glossário, código fictício e pacote de contingência; usar fonte legível e descrever o conteúdo exibido.
- Não pressupor licença de turma, API, conta ou cota; validar antes do encontro. A licença prevista cobre 16/10 a 14/11; aula de reposição fora da janela não está coberta.
- Para a execução local, preparar Python 3.11 ou superior e a biblioteca padrão; o aluno sem instalação acompanha o mesmo código e analisa resultados fornecidos, com origem identificada.
- Não exigir download de modelo local, chave de API, pagamento ou dados do empregador.

**Smoke test de preparação:** abrir o pacote; registrar `python --version`; rodar `python -B testes/test_miniloja.py --codigo caso` (esperado: onze verificações, oito passam e três falham, código de saída `1`); rodar `--existentes` (esperado: 26 testes, OK). Se não houver ambiente, abrir `apoio/resultado-textual.md` e registrar a modalidade.

**Contingência equivalente:** o pacote textual contém todos os insumos, respostas simuladas rotuladas e transcrições de execução. Quem o utiliza analisa critérios, limites e decisões com a mesma rubrica, e **não declara ter feito execuções ou medições que não executou**.

## 7. Mapa de competências e instrumentos

| Objetivo | Desempenho esperado | Instrumentos |
| --- | --- | --- |
| O1 — Escolher o modo | Escolher e justificar o modo de interação para uma tarefa concreta | AV1.1, AV3 |
| O2 — Conduzir com escopo | Gerar e refatorar com plano revisado, escopo declarado, mudança pequena e resultado verificável | AV1.2, AV2 |
| O3 — Testes e documentação | Produzir testes e documentação que acrescentem verificação real; reconhecer teste tautológico, cobertura enganosa e documentação óbvia | AV1.3, AV2 |
| O4 — Ler legado | Verificar no código toda afirmação do assistente antes de agir | AV1.4 |
| O5 — Revisar | Revisar código assistido (correção, segurança, dependências, dívida) e sustentar o que aprova e rejeita | AV1.5, AV3 |
| O6 — Medir e automatizar | Ler evidência de produtividade, propor medição honesta e identificar tarefa recorrente a automatizar com verificação | AV1.6, AV3 |

Fluência em um fornecedor específico não é competência avaliada. A precisão do argumento e a capacidade de auditar sua evidência determinam o nível da rubrica.

## 8. Plano de aulas detalhado

Cada bloco tem 180min, com divisão sugerida de cerca de 60min de exposição aplicada, 80–90min de prática e 30min de fechamento. O professor ajusta. O bloco 1 reserva 20–30min iniciais ao nivelamento de ambiente.

| Etapa | B1 | B2–B6 |
| --- | --- | --- |
| Abertura e nivelamento de ambiente | 25min | — |
| Exposição aplicada (com demonstração) | 55min | 60min |
| Pausa | 10min | 10min |
| Prática individual em salas (inclui transições de 5–8min) | 65min | 80min |
| Socialização de 3–5 casos e fechamento | 25min | 30min |
| **Total** | **180min** | **180min** |

### B1 — Ferramentas, modos de interação e onde cada um entra
**16/10, 19–22h.** Completar, conversar, editar com escopo e delegar a um agente, com o que cada modo pede de contexto e de verificação; o ambiente em volta do modelo (arquivos, comandos, permissões) e a segurança de agentes; MCP e seus riscos; custo cognitivo de revisar mudança grande; critério por tipo de tarefa e maturidade do código. **Prática (AV1.1):** a mesma tarefa pequena do MiniLoja em dois modos, com registro de tempo, idas e vindas e correção. **Fechamento:** o modo errado custa mais do que não usar IA.

### B2 — Geração, edição e refatoração com escopo
**17/10, 9–12h.** Escopo declarado em seis campos; plano revisado como código; escada do raio de impacto; diff pequeno; refatoração com comportamento preservado (golden master); quando o agente insiste em reescrever; git como rede de segurança; regras persistentes mínimas. **Prática (AV1.2):** refatorar `calcular_total` em duas rodadas (sem e com escopo). **Fechamento:** escopo declarado antes separa refatoração de reescrita acidental.

### B3 — Testes e documentação assistidos
**17/10, 14–17h.** Teste como rede e como oráculo do agente; pedir teste de comportamento; teste tautológico; cobertura × mutação; teste diferencial; documentação útil; ADR com apoio de IA. **Prática (AV1.3):** cobrir o código refatorado, caçar na suíte existente o teste que só repete a implementação, derivar casos do contrato. **Fechamento:** teste gerado que não falharia nunca não é teste, é enfeite.

### B4 — Legado: leitura, navegação e mudança segura
**23/10, 19–22h.** Leitura assistida de base grande; pedir mapa com evidência; protocolo afirmação → prova; rede de segurança antes de mudar; migração em escala (codemod × IA × humano). **Prática (AV1.4):** em um repositório desconhecido, cinco perguntas de arquitetura provadas com trecho de código e um plano de migração. **Fechamento:** em legado, a IA acelera a leitura e não substitui a conferência.

### B5 — Revisão, segurança e dívida do código assistido
**24/10, 9–12h.** O que muda no review quando ninguém pensou o código linha a linha; vulnerabilidades recorrentes; falsa sensação de segurança; dependências e cadeia de suprimentos; duplicação e dívida; o que exigir de um PR de agente. **Prática (AV1.5):** checklist em plenária e parecer de revisão de um pull request gerado por agente. **Fechamento:** quem aprova o merge responde pelo código.

### B6 — Produtividade real, medição e uso em time
**24/10, 14–17h.** Por que os estudos divergem; o que medir (DORA, SPACE) e baseline; métrica que vira meta; combinado de time; automação de tarefa recorrente com verificação; ponte para D1.3. **Prática (AV1.6):** desenhar uma medição para o próprio time e apontar uma tarefa candidata a automação. **Fechamento:** sem baseline não existe ganho, existe impressão.

## 9. Projeto integrador do módulo

O caso transversal **MiniLoja** sustenta as práticas dos blocos 1 a 3 e 5; o **repositório desconhecido** do bloco 4 aplica as mesmas habilidades a um legado; o bloco 6 mede e decide. O produto integrador é a **AV3, entrega final**: um pull request assistido com registro do que a IA errou e a medição desenhada.

| Trabalho autônomo | Carga | Entrega | Prazo proposto, Brasília |
| --- | --- | --- | --- |
| L0 — leitura orientada | 2h | Fichamento de duas referências, formativo | 21/10/2026, 23h59 |
| AV2 — refatoração e testes | 2h | Refatoração e suíte verificáveis, com registro | 21/10/2026, 23h59 |
| AV3 — entrega final | 2h | PR assistido + registro de erros da IA + meia página de medição | 30/10/2026, 23h59 |

O [índice de avaliações](avaliacoes/README.md) reúne enunciados e modelos; o [estudo autônomo](estudo-autonomo.md) delimita esforço e procedência.

## 10. Avaliação e rubricas

**AV1 20% + AV2 30% + AV3 50%.** AV1 é a média dos registros dos blocos com presença registrada. Todas as notas estão entre 0 e 10. L0 é formativa e não acrescenta peso. **Pesos e prazos são proposta docente, sujeitos a confirmação da coordenação.**

| Instrumento | Critérios internos, soma 100% |
| --- | --- |
| AV1, cada registro | Aplicação/decisão 30%; evidência 40%; limites/alternativa 30% |
| AV2 | Escopo e plano 20%; comportamento preservado 25%; suíte com verificação real 35%; documentação e ADR 20% |
| AV3 | Modo e justificativa 10%; escopo declarado e cumprido 15%; mudança revisável 15%; verificação efetiva 20%; honestidade sobre os erros da IA 15%; justificativa técnica das correções 10%; medição e automação 15% |

Níveis por critério: 0 ausente, 1 incipiente, 2 adequado, 3 consistente. Nota = 10 × soma(peso × nível/3); todos os níveis 2 produzem 6,67. As [rubricas públicas completas](avaliacao.md) descrevem os níveis, a fórmula, a regra de presença e a devolutiva.

IA é permitida com declaração e julgamento próprios. Execução e inspeção textual são modalidades válidas; a origem do resultado deve estar clara. A avaliação é manual.

**Presença, frequência e gravações:** limite de falta de **25% da carga de 24h (6h)**; acima disso, reprovação por falta, independentemente da nota. Gravações liberadas **48h após a aula**, disponíveis por **90 dias**, só para revisão; **não geram presença**. Abono de falta é atribuição exclusiva da **Secretaria, mediante comprovante**. A regra para quem faltar a um bloco com registro avaliado e a recuperação aguardam confirmação (o PPC prevê nova avaliação em até 5 dias úteis para falta justificada e comprovada, a pedido do aluno).

## 11. Repositório de apoio

O [material do aluno](README.md) contém contrato, dados sintéticos, código, onze verificações, a suíte existente, mutação, respostas simuladas, transcrição de execução e dossiês de avaliação. O material inicial tem **três verificações que falham** (as tarefas do bloco 1). A suíte existente passa por inteiro e **contém dívida de propósito**: descobri-la faz parte da prática.

Duas pastas são liberadas pelo professor no dia do bloco: `caso/legado/` (B4) e `apoio/pr-bloco5/` (B5).

## 12. Referências e fontes

**Bibliografia básica**
- LIANG, Jenny T.; YANG, Chenyang; MYERS, Brad A. *A Large-Scale Survey on the Usability of AI Programming Assistants: Successes and Challenges*. arXiv, 2023. https://arxiv.org/abs/2303.17125
- BECKER, Joel et al. *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*. arXiv, 2025. https://arxiv.org/abs/2507.09089 (ler com a atualização da METR de 24/02/2026)
- PERRY, Neil et al. *Do Users Write More Insecure Code with AI Assistants?* arXiv, 2022. https://arxiv.org/abs/2211.03622

**Complementar**
- PENG, Sida et al. *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. arXiv, 2023. https://arxiv.org/abs/2302.06590
- YANG, John et al. *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*. arXiv, 2024. https://arxiv.org/abs/2405.15793
- WANG, Junjie et al. *Software Testing with Large Language Models: Survey, Landscape, and Vision*. arXiv, 2023. https://arxiv.org/abs/2307.07221
- NIKOLOV, Stoyan et al. *How is Google using AI for internal code migrations?* arXiv, 2025. https://arxiv.org/abs/2501.06972
- PEARCE, Hammond et al. *Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions*. arXiv, 2021. https://arxiv.org/abs/2108.09293
- DORA. *State of AI-assisted Software Development*. Google Cloud, 2025. https://dora.dev/dora-report-2025/

**Referência operacional:** documentação oficial do Python (biblioteca padrão e `unittest`). O runtime de referência é o local do aluno; nenhum fornecedor de IA integra o contrato pedagógico.

## 13. Apêndices: templates e checklists

**Registro de avaliação:** identificação; instrumento; insumo/versão; critério; método; entrada; esperado; encontrado; decisão; alternativa; limite; procedência e assistência. Preencher só os campos pertinentes ao enunciado.

**AV1:** um registro individual até uma página por bloco. **AV2:** escopo → plano → mudança → verificação (teste que falharia) → decisão. **AV3:** PR com escopo, evidência e registro de erros da IA, mais meia página de medição.

**Checklist do estudante:** usar apenas insumos autorizados; aplicar ao caso; identificar fonte e método; separar esperado e encontrado; não atribuir execução à inspeção; justificar a decisão; examinar limite e alternativa; declarar assistência; revisar pela rubrica e entregar no canal institucional.

**Ficha docente de correção:** critério | peso | nível 0–3 | evidência localizada | comentário. Com 42 trabalhos, corrigir por rubrica de níveis, sem comentário longo em cada um.
