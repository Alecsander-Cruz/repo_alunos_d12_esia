# MiniLoja — apoio à disciplina D1.2

Este pacote apoia os seis blocos de **Desenvolvimento Assistido por IA (24h)**. MiniLoja é um caso fictício de pedidos de uma loja de material esportivo. Você o usa nas práticas: escolhe o modo de interação com IA, declara escopo, refatora, verifica com testes de verdade, lê um código desconhecido, revisa um pull request e mede o seu contexto. Toda prática roda em código que você precisa **verificar depois**.

O caso e suas verificações já podem ser executados. O professor conduz as demonstrações; cada bloco reserva a segunda metade da aula a uma **prática** com registro individual (AV1). As instruções indicam insumos próprios, entregável e rubrica. Não há entrega coletiva obrigatória.

## Orientação das atividades

O [guia do fim de semana 1](apoio/guia-atividades-fds1.md) (AV1.1 a AV1.3, e AV2) e o [guia do fim de semana 2](apoio/guia-atividades-fds2.md) (AV1.4 a AV1.6, e AV3) reúnem dados, passos, exemplos de preenchimento e rubricas. Servem para consulta individual e impressão.

## Preparação do ambiente

Obtenha o pacote disponibilizado pelo professor e abra esta pasta. A execução local usa **Python 3.11 ou superior e somente a biblioteca padrão**; o pacote foi verificado com **Python 3.12.3**. Não há dependências adicionais. Um assistente de IA (no editor, no navegador ou um agente de codificação) apoia as práticas; a ferramenta é intercambiável. Se não houver acesso à ferramenta ou ao ambiente local, use as **respostas simuladas** de `apoio/respostas-simuladas/` e a transcrição de `apoio/resultado-textual.md`. A instalação local não é condição para demonstrar os objetivos da disciplina.

**Regras do jogo:** trabalhe em uma **cópia sua** do pacote, em uma **branch por tarefa** se usar git, com a árvore limpa antes de cada execução de agente. **Nenhum código ou dado do seu empregador** entra nas práticas em sala. Use apenas os dados fictícios fornecidos.

## Navegação

| Pasta | Conteúdo |
| --- | --- |
| `caso/` | Contrato (`regras.md`), código em `caso/miniloja/`, suíte existente em `caso/testes_existentes/`, dados sintéticos em `caso/dados/` |
| `testes/` | Onze verificações do caso e a ferramenta de mutação |
| `apoio/` | Guias, respostas simuladas identificadas, transcrição de execução e execução acompanhada do bloco 3 |
| `exercicios/aula-1/` a `aula-6/` | Enunciados e modelos de registro de cada bloco |
| `avaliacoes/` | Índice, AV2 e AV3 |

As pastas `caso/legado/` (bloco 4) e `apoio/pr-bloco5/` (bloco 5) contêm apenas um aviso: o professor libera o conteúdo na data da aula, para que o código **continue desconhecido** até lá.

## Comece pelos exercícios do seu bloco

Leia o [guia de preenchimento e entrega](exercicios/README.md). Ele explica qual arquivo preencher, o que é evidência e como registrá-la.

AV1: [bloco 1 — escolher o modo](exercicios/aula-1/README.md) · [bloco 2 — declarar escopo](exercicios/aula-2/README.md) · [bloco 3 — testes que falham](exercicios/aula-3/README.md) · [bloco 4 — ler legado com prova](exercicios/aula-4/README.md) · [bloco 5 — revisar PR de agente](exercicios/aula-5/README.md) · [bloco 6 — medir e automatizar](exercicios/aula-6/README.md).

1. Leia o enunciado (`README.md`) do bloco e os dados indicados.
2. Faça uma cópia do `template-registro.md` desse bloco ou copie o conteúdo para um editor de texto. O HTML é uma versão de leitura, não um formulário.
3. Preencha as respostas e as evidências no mesmo documento, com até uma página. Informe se a análise foi manual ou se houve execução, e declare eventual uso de IA.
4. Confira o checklist e envie o registro pelo canal e no formato informados pelo professor. Não é necessário enviar commit nem alterar este repositório para entregar.

## Execução do código do caso

Execute na raiz desta pasta:

```
python -B testes/test_miniloja.py --codigo caso
```

Há **onze verificações**. No material inicial, **oito passam e três falham**; as três são as tarefas do bloco 1. O processo retorna código de saída `1` quando há falha e `0` quando todas passam. Elas verificam o material e não atribuem nota. **Uma execução verde se limita ao que foi testado.**

Para rodar a suíte existente do caso (26 testes, parte deles tautológica de propósito) e a mutação:

```
python -B testes/test_miniloja.py --codigo caso --existentes
python -B testes/mutacao_manual.py
```

Consulte [testes/README.md](testes/README.md) para executar uma verificação isolada e [apoio/resultado-textual.md](apoio/resultado-textual.md) para ler a transcrição de uma execução.

## Avaliações da pós-graduação

- [Índice dos enunciados e modelos: AV1, AV2 e AV3](avaliacoes/README.md)
- [AV2 — refatoração e testes verificáveis](avaliacoes/av2/README.md)
- [AV3 — entrega final: PR assistido e medição](avaliacoes/av3/README.md)

Composição proposta: AV1 20% (média dos registros dos blocos com presença), AV2 30%, AV3 50%. As 6h autônomas são leitura L0 2h + AV2 2h + AV3 2h. As rubricas avaliam aplicação, evidência e argumentação individuais.

## Documentos da disciplina

- [Plano de ensino da turma](ementa.md)
- [Boas-vindas e preparação](boas-vindas.md)
- [Avaliação e critérios](avaliacao.md)
- [Estudo autônomo e prazos](estudo-autonomo.md)
- [Glossário](glossario.md)
- [Diagnóstico sem nota](diagnostico.md)

Datas: 16–17/10 e 23–24/10/2026. As aulas e entregas usam horário de Brasília. O pacote funciona localmente; o canal acadêmico de envio será informado pelo professor.
