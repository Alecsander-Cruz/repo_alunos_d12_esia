# AV1.1 — Escolher o modo

**Individual — registro consolidado em 35min — B1, 16/10/2026, prática 20h30–21h35 (Brasília).** Integra AV1, que vale 20% da nota pela média simples dos registros dos blocos com presença. Consulte a [avaliação e rubrica pública](../../avaliacao.md).

## Objetivo

Quero escolher o modo de interação com IA para três tarefas de desenvolvimento, executar uma delas em dois modos e registrar o que verifiquei e o que a IA errou.

## Contexto e insumos

MiniLoja é o caso fictício de pedidos. Trabalhe com o contrato (`caso/regras.md`, regra **R3**) e com as verificações do caso. Todos os dados são fictícios.

- **R3.2:** o `cpf` deve ter dígitos verificadores válidos e não pode ter todos os dígitos iguais.
- **R3.4:** cadastro inválido responde `422` com a lista de **todos** os erros.
- [Contrato completo](../../caso/regras.md) · [template individual](template-registro.md) · [dados de CPF](../../caso/dados/cpfs.json).

| Cartão | Tarefa e informações disponíveis | Resultado solicitado |
| --- | --- | --- |
| T1 | Validar o CPF no cadastro de cliente (`caso/miniloja/cadastro.py`). As verificações `v08` e `v09` falham hoje | Código que faz `v08` e `v09` passarem, sem quebrar as demais |
| T2 | O cadastro inválido deve responder `422` com a lista de todos os erros, em vez de `400` com mensagem única. A verificação `v10` falha hoje | Código que faz `v10` passar |
| T3 | **Hipotética, sem executar:** lentidão em produção às 02h. Você tem métricas e logs, e um agente que poderia rodar comandos | Decisão sobre o modo e as permissões que você concederia |

Comando de verificação: `python -B testes/test_miniloja.py --codigo caso`. Sem ferramenta ou ambiente, analise as respostas simuladas em [apoio/respostas-simuladas/](../../apoio/respostas-simuladas/) (b1-cpf-completar.md e b1-cpf-agente.md) e identifique-as como simuladas.

## Passos — 35min

1. **Ler — 5min.** Leia R3 e rode (ou leia a transcrição de) as verificações. Defina o critério de aceite de T1 e T2 antes de escolher o modo.
2. **Produzir individualmente — 20min.** Execute **T1 em dois modos diferentes** (por exemplo, completar no editor e agente) e T2 em um modo à sua escolha. Registre, para cada execução, o tempo até a primeira versão e até "pronto e verificado", as idas e vindas, a fração que você corrigiu à mão, o que a IA errou e como você verificou. Alterne a ordem dos modos em relação ao seu colega de grupo. Em T3, decida modo e permissões **sem executar**, com base em raio de impacto, existência de oráculo e reversibilidade.
3. **Revisar pela rubrica — 5min.** Confira se cada modo está ligado ao pedido e se o registro mede "pronto verificado", não só "primeira versão".
4. **Entregar — 5min.** Finalize um único registro individual de até uma página, usando o template. O canal acadêmico será informado pelo professor; este material não presume endereço de envio.

## Entrega e checklist

- [ ] Execuções de T1 (dois modos) e T2 registradas, com tempos, idas e vindas, correção e erro da IA.
- [ ] Evidência: comando de verificação e trecho relevante da saída (ou "análise manual; execução não realizada").
- [ ] T3 decidida com raio de impacto, oráculo e permissões.
- [ ] Origem das respostas simuladas e declaração de IA, se utilizada.
- [ ] Se alterou algum teste existente, o motivo registrado (a tarefa muda o contrato de `400` para `422`).

**Critério de conclusão:** outra pessoa consegue relacionar cada modo ao pedido e localizar a verificação que sustenta "pronto". A entrega escrita é suficiente e não depende de fala ou câmera.

| Critério AV1 | Peso | Indicadores deste registro |
| --- | --- | --- |
| Aplicação/decisão | 30% | Modo justificado para cada execução; T3 decidida com raio de impacto, oráculo e permissões concedidas. |
| Evidência | 40% | Comando e saída (ou análise declarada) para ao menos uma execução; erros da IA descritos de forma específica; tempo até "verificado". |
| Limites/alternativa | 30% | Limite da comparação (uma execução não prova nada) e condição concreta para mudar o modo. |

**Dica:** o tempo da primeira versão engana. Meça até estar **verificado**. Uma execução não prova nada sobre a ferramenta: ela serve para calibrar o seu julgamento. Não inclua dados do empregador.
