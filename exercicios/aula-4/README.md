# AV1.4 — Ler legado com prova

**Individual — registro consolidado em 35min — B4, 23/10/2026, prática 20h05–21h25 (Brasília).** Integra AV1, que vale 20% da nota pela média simples dos registros dos blocos com presença. Consulte a [avaliação e rubrica pública](../../avaliacao.md).

## Objetivo

Quero usar IA para entender um código que ninguém do time escreveu e provar cada afirmação apontando o trecho, e depois planejar uma mudança segura.

## Contexto e insumos

O professor libera o **repositório desconhecido** em `caso/legado/` na hora do bloco (veja o aviso em [caso/legado/LEIA-ME.md](../../caso/legado/LEIA-ME.md)). **Não leia o README do repositório antes**: ele pode estar desatualizado. Modo de rodar: instruções do próprio repositório, sem rede.

Cinco perguntas, com apoio do agente (ou da leitura direta):
1. Onde começa a ingestão e quais caminhos a disparam?
2. Quem escreve na tabela `trabalhos`?
3. Como o sistema classifica trabalhos e autores por área, e do que isso depende da API externa?
4. Que relatórios existem e quem os dispara?
5. Que configurações mudam o comportamento por ambiente, e qual de fato vale no agendamento?

Formato de cada resposta: **afirmação | trecho (arquivo:linha) | contraevidência buscada | status** (confirmada, refutada ou incerta). Para toda afirmação do tipo "só X faz Y" ou "nunca é chamado", busque o contraexemplo. [Template individual](template-registro.md).

## Passos — 35min

1. **Ler — 5min.** Leia as cinco perguntas e escreva, antes de abrir o código, onde você procuraria cada resposta.
2. **Produzir individualmente — 20min.** Responda as cinco perguntas com prova. Registre **uma resposta do assistente que parecia certa e estava errada** e como você a refutou. Antes de qualquer mudança, **grave a saída** de dois relatórios (caracterização mínima). Depois escreva um **plano de migração** para a API atual do serviço externo (consulte a documentação oficial), em fatias pequenas, separando o que um codemod resolve do que exige decisão humana.
3. **Revisar pela rubrica — 5min.** Confira se nenhuma resposta ficou sem trecho e se o plano indica a verificação de cada fatia.
4. **Entregar — 5min.** Finalize um único registro individual de até uma página, usando o template. O canal acadêmico será informado pelo professor; este material não presume endereço de envio.

## Entrega e checklist

- [ ] Cinco linhas com afirmação, trecho (arquivo:linha), contraevidência e status.
- [ ] Uma resposta errada com aparência de certa, com a refutação.
- [ ] Caracterização mínima: comando e saída gravada antes de mudar.
- [ ] Plano de migração em fatias, mecânico × decisão humana, com a verificação de cada fatia.
- [ ] Origem e declaração de IA, se utilizada.

**Critério de conclusão:** outra pessoa consegue abrir cada trecho citado e confirmar ou refutar a afirmação. O plano diz o que automatizar e o que decidir.

| Critério AV1 | Peso | Indicadores deste registro |
| --- | --- | --- |
| Aplicação/decisão | 30% | Respostas com status honesto; plano que separa mudança mecânica de decisão humana. |
| Evidência | 40% | Trecho e linha para cada afirmação; contraevidência buscada; saída gravada antes de mudar. |
| Limites/alternativa | 30% | O que a leitura não cobre (código dinâmico, configuração por ambiente, consumidores externos) e condição para reabrir uma resposta. |

**Dica:** pergunte a si mesmo, para cada "só" e cada "nunca": que busca derrubaria isso? Se não consegue formular a busca, você ainda não pode agir.
