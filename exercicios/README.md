# Como fazer e entregar os exercícios dos blocos

Cada bloco tem uma atividade individual da AV1. Você lê a situação, trabalha no caso (executando, ou analisando as respostas simuladas) e registra suas respostas em **um único documento de até uma página por bloco**, incluindo a evidência pedida. A evidência faz parte da resposta; não é uma segunda entrega.

## Por onde começar

1. Abra o enunciado do bloco na tabela abaixo. Os exercícios ficam em `exercicios/aula-1/` a `exercicios/aula-6/`, a partir da raiz do pacote. A pasta `avaliacoes/` reúne o índice geral, a AV2 e a AV3.
2. Leia a situação e as regras indicadas. "Contrato" significa o documento que define como o sistema fictício MiniLoja deve funcionar (`caso/regras.md`).
3. Faça uma cópia do `template-registro.md` do bloco. Esse é o modelo de resposta: preencha as tabelas e substitua os espaços `___` pelo seu texto. Você também pode copiar o conteúdo para um editor de texto, mantendo os campos pedidos.
4. Siga as etapas do enunciado e registre suas justificativas no próprio modelo. Use frases curtas.
5. Confira o checklist e o limite de uma página. Envie o documento preenchido pelo canal e no formato informados pelo professor. O repositório não recebe nem envia sua atividade automaticamente.

**Sobre os arquivos:** o `README.md` contém o enunciado e o `template-registro.md` contém os campos da resposta. As versões `.html` servem para leitura no navegador e não são formulários. Você não precisa editar o HTML, preencher as duas versões, criar fork nem enviar commit.

| Bloco | O que você vai fazer | Modelo de resposta |
| --- | --- | --- |
| [1 — Escolher o modo](aula-1/README.md) | Resolver a mesma tarefa em dois modos de interação e decidir o modo de uma terceira | [Preencher AV1.1](aula-1/template-registro.md) |
| [2 — Declarar escopo](aula-2/README.md) | Refatorar `calcular_total` sem e com escopo declarado e comparar | [Preencher AV1.2](aula-2/template-registro.md) |
| [3 — Testes que falhariam](aula-3/README.md) | Caçar testes tautológicos, tratar mutantes e derivar casos do contrato | [Preencher AV1.3](aula-3/template-registro.md) |
| [4 — Ler legado com prova](aula-4/README.md) | Responder cinco perguntas sobre um código desconhecido, provando cada uma | [Preencher AV1.4](aula-4/template-registro.md) |
| [5 — Revisar PR de agente](aula-5/README.md) | Revisar um pull request gerado por agente e decidir o merge | [Preencher AV1.5](aula-5/template-registro.md) |
| [6 — Medir e automatizar](aula-6/README.md) | Desenhar uma medição honesta e apontar uma tarefa a automatizar com verificação | [Preencher AV1.6](aula-6/template-registro.md) |

## O que significa "evidência" nestas atividades

É a parte da resposta que permite a outra pessoa conferir sua conclusão. Em vez de escrever apenas "está correto", mostre a regra usada, o comando executado ou o trecho analisado e a comparação que você fez. **Um comando com a saída relevante, um cálculo explicado ou um trecho de código com arquivo e linha, acompanhado de justificativa, pode ser a evidência.** Não é obrigatório produzir print, vídeo ou a conversa completa com a IA.

Exemplo de formato, com valores diferentes dos que você analisa nos blocos:
> Regra: R1.4 manda aplicar a taxa de serviço sobre subtotal com desconto mais frete. Entrada: 1 item de R$ 60,00, UF "XX", sem cupom. Cálculo: 60,00 + 29,90 = 89,90; 89,90 × 1,08 = 97,092; arredondado, 97,09. Origem: cálculo manual a partir do contrato; executei o código e observei 97.09 com `python -B testes/test_miniloja.py --codigo caso`. Esse caso confere uma combinação, mas não prova o comportamento para todas as entradas.

| Expressão do enunciado | O que escrever |
| --- | --- |
| Critério de aceite | A condição que precisa ser atendida para considerar o resultado adequado. Ex.: "CPF com dígito verificador errado deve responder 422" |
| Saída esperada | O resultado que o contrato determina, calculado por você. Isso não significa que o código foi executado |
| Resultado inferido por inspeção | O que você deduziu ao ler o código, explicando o caminho seguido |
| Resultado observado em execução | O que você obteve ao realmente rodar. Registre o comando e o trecho relevante da saída |
| Trecho essencial de evidência | Somente os dados, comandos, cálculos ou linhas necessários para conferir sua justificativa |
| Procedência | De onde vieram os dados: contrato fictício, cálculo próprio, leitura de código, execução própria ou resposta simulada |
| Limite da análise | O que a sua verificação ainda não permite concluir |
| Condição para rever a decisão | Uma informação nova ou um resultado que faria você mudar de ideia |

Os dados fornecidos são fictícios. Se não executou nada, escreva "análise manual; execução não realizada". Se usou uma resposta simulada de `apoio/respostas-simuladas/`, **identifique-a como simulada**: ela não é uma execução sua.

## Preciso usar IA ou programar?

As seis atividades podem ser resolvidas por escrito com os materiais fornecidos. Quem executa as práticas com ferramenta de IA e código segue os mesmos critérios que quem usa o caminho textual. São duas informações diferentes: a **modalidade que você recomenda** para a situação e a **assistência que você efetivamente usou** ao preparar seu registro.

Ao final, escreva **"Não utilizei IA para elaborar este registro"** ou informe ferramenta/modelo visível, tarefa e contexto fornecidos, trecho aproveitado e como você o conferiu. Se o modelo não estiver identificado, escreva "não informado". **Se a prática usou IA sobre o código, registre também o que ela errou.** Utilize apenas os dados fictícios fornecidos.

## Entrega e avaliação

O checklist é uma conferência final do documento; cada item não corresponde a um arquivo separado. O registro é produzido ao longo da prática do bloco e consolidado nos 35min finais: 5 de leitura do enunciado, 20 de elaboração, 5 de revisão e 5 de entrega. Horários, pesos e critérios estão no [índice das avaliações](../avaliacoes/README.md) e na [rubrica da disciplina](../avaliacao.md). Os enunciados da [AV2](../avaliacoes/av2/README.md) e da [AV3](../avaliacoes/av3/README.md) têm entregas e limites próprios; o limite de uma página deste guia se aplica à AV1.
