# Registro individual — AV1.1

**Limite: uma página, incluindo evidências essenciais.** Estudante: Alecsander D. Cruz — Data: 16/10/2026
Origem: tarefas T1–T3 fictícias do enunciado; modalidade: **execução própria**.

| Tarefa | Modo | Tempo até 1ª versão | Tempo até pronto e verificado | Idas e vindas | % corrigido à mão | O que a IA errou | Como verifiquei |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | A: Chat (1º) — tarefa pequena e conhecida; comparar tempo até verificado entre modos | ~6 min (00:01→00:07) | ~19 min (→00:20) | 0 (1 pedido; código colado como veio) | 0% | Nenhum erro no escopo. Manteve o CPF opcional (`if "cpf" in payload`): escolha aceitável, pois T1 trata só da R3.2 (validade); a obrigatoriedade (R3.1) fica para T2, junto com `nome` e `email` | Aceite (R3.2): v08 e v09 passam (rejeita DV inválido e dígitos iguais); CPF válido aceito com e sem pontuação; v01–v07 e v11 seguem passando; suíte `--existentes` (26) passa. Resultado: v01–v09 e v11 ok (v10 é T2); existentes 26/26 ok; `_cpf_valido` testada à mão com 4 válidos e 4 inválidos, com/sem pontuação → todos corretos (comando sugerido pela IA; verificado na função, não no endpoint) |
| T1 | B: Agente (2º) — edições automáticas, comandos aprovados à mão; 3ª tentativa (2 descartadas: o pedido expunha o resultado do modo A) | <1 min (00:58→00:58) | ~9 min (→01:07) | 0 (1 plano aprovado, sem correções) | 0% | Nenhum erro no escopo. Mesma escolha de CPF opcional, mas explicitou sozinho o conflito com R3.1/R3.4 e os 2 testes existentes que quebrarão em T2. Implementação diferente da do A (só remove `.`/`-`; rejeita não-`str`) | Mesmo aceite do modo A. Resultado: v01–v09 e v11 ok (v10 é T2); existentes 26/26 ok (rodado por mim e pelo agente); CPFs de `cpfs.json` testados pelo agente no cadastro (201/422, com/sem pontuação) |
| T2 | Agente — escopo definido, mudança em vários trechos e em testes existentes; v10 + suíte como oráculo |  |  |  |  |  | Aceite (R3.4): inválido → 422 com `{"erros": [{"campo", "erro"}]}`, um item por erro detectado, incluindo `nome`, `email` e `cpf` ausentes (R3.1); válido segue 201; v01–v11 passam; testes existentes que contradizem o contrato (400 em vez de 422; cadastro sem CPF aceito) ajustados, com motivo registrado |

**Trecho essencial de evidência (comando e saída que sustentam "verificado"):** ___

**T3 (hipotética): raio de impacto ___; oráculo disponível ___; permissões que concederia ___; modo e por quê ___.**

**Alternativa para ___:** ___ **Comparação com minha escolha (restrição e consequência):** ___ **Limite da comparação e condição para rever a escolha:** ___

**Procedência/IA:** não utilizada / ferramenta e modelo visíveis: ___; tarefa delegada e contexto: ___; trecho aproveitado: ___; minha verificação/intervenção: ___. Use "não informado" para metadados indisponíveis. O raciocínio e a decisão registrados são meus.

**Revisão:** [ ] dois modos em T1; [ ] evidência localizada; [ ] T3 decidida; [ ] alternativa e limite; [ ] até uma página.
