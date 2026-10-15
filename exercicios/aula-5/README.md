# AV1.5 — Revisar um PR de agente

**Individual — registro consolidado em 35min — B5, 24/10/2026, prática 10h10–11h30 (Brasília).** Integra AV1, que vale 20% da nota pela média simples dos registros dos blocos com presença. Consulte a [avaliação e rubrica pública](../../avaliacao.md).

## Objetivo

Quero revisar um pull request gerado por agente com critério, sustentando tecnicamente o que aprovo e o que rejeito, e decidir sobre o merge.

## Contexto e insumos

O professor libera o **pull request** em `apoio/pr-bloco5/` na hora do bloco (veja [apoio/pr-bloco5/LEIA-ME.md](../../apoio/pr-bloco5/LEIA-ME.md)), com a descrição escrita pelo agente. O texto do PR é uma **alegação**, não uma evidência: verifique rodando e lendo.

- **Plenária (25min):** a turma constrói o checklist de revisão para código assistido (cada um cita um defeito que já viu; agrupamos; cada falha vira uma pergunta verificável; marcamos o que **bloqueia** o merge).
- **Funil de revisão:** intenção e escopo → testes primeiro → contratos e superfície pública → segurança e dependências → estrutura e manutenção → execução independente.
- **Contrato:** `caso/regras.md` (inclui **R4**, acesso).
- [Template individual](template-registro.md).

## Passos — 35min

1. **Ler — 5min.** Leia a descrição do PR e liste as alegações que ela faz (por exemplo, "testes passam", "sem mudança de comportamento").
2. **Produzir individualmente — 20min.** Aplique o checklist ao PR e rode você mesmo o que a descrição diz que rodou. Registre **ao menos quatro achados**, cada um com: onde (arquivo), por que importa (impacto), severidade (**bloqueia** o merge ou **comenta**) e a correção sugerida com o **teste que falharia** sem ela. Confira cada alegação do texto do PR contra o que você observou. Decida o merge.
3. **Revisar pela rubrica — 5min.** Confira se cada achado bloqueante tem impacto explicado e um teste, e se o parecer não depende do texto do PR.
4. **Entregar — 5min.** Finalize um único registro individual de até uma página, usando o template. O canal acadêmico será informado pelo professor; este material não presume endereço de envio.

## Entrega e checklist

- [ ] Pelo menos quatro achados com onde, impacto, severidade e correção com teste.
- [ ] Alegações da descrição do PR conferidas (confirmada ou refutada, com evidência).
- [ ] Decisão sobre o merge e condição para aprovar.
- [ ] Dependência nova checada (existe? quem mantém? é necessária?).
- [ ] Origem e declaração de IA, se utilizada.

**Critério de conclusão:** outra pessoa consegue reproduzir cada achado e entender por que ele bloqueia ou não o merge. A decisão não depende de confiar no texto do PR.

| Critério AV1 | Peso | Indicadores deste registro |
| --- | --- | --- |
| Aplicação/decisão | 30% | Severidade coerente (bloqueia versus comenta); decisão de merge fundamentada; responsabilidade de quem aprova explicitada. |
| Evidência | 40% | Achados reproduzíveis (arquivo, comando ou teste); alegações do PR conferidas. |
| Limites/alternativa | 30% | O que a revisão não cobre (por exemplo, análise estática e testes de abuso) e condição para aprovar. |

**Dica:** revisar não é concordar com o PR. Um comentário técnico diz o problema, o impacto e a correção, com um teste. "Parece arriscado" não é parecer.
