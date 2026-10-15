> **RESPOSTA SIMULADA.** Texto construído pelo professor para análise, identificado como simulação. Não é saída real de um modelo e não mede desempenho de nenhuma ferramenta. Quem a usa **não deve declarar ter executado** a tarefa.

# Bloco 1 · T1 em modo "agente" (simulado)

**Pedido:** "Valide o CPF no cadastro de cliente."

**Mensagem final do agente (simulada):** "Implementei a validação de CPF em `cadastro.py`. Todos os testes passam."

**Resumo do diff simulado:**
- `caso/miniloja/cadastro.py`: nova função `cpf_valido`; o cadastro passa a recusar CPF inválido.
- `caso/miniloja/handlers.py`: reformatação de imports e renomeação de uma variável (não pedido).
- `caso/testes_existentes/test_cadastro.py`: expectativa alterada para `422` e um caso de CPF adicionado.

**Para você analisar:**
1. O que está **fora do escopo** do pedido? Como você o evitaria (escopo declarado)?
2. O agente alterou um **teste existente**. Isso é aceitável? Em que condição?
3. "Todos os testes passam": qual comando você rodaria para conferir? A suíte existente cobre a regra de **todos os dígitos iguais**? E a verificação `v10` (lista de todos os erros), que não era parte do pedido?
4. O que você registraria como erro da IA, e o que como acerto?
