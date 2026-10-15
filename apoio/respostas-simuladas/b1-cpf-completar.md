> **RESPOSTA SIMULADA.** Texto construído pelo professor para análise, identificado como simulação. Não é saída real de um modelo e não mede desempenho de nenhuma ferramenta. Quem a usa **não deve declarar ter executado** a tarefa.

# Bloco 1 · T1 em modo "completar no editor" (simulado)

**Situação:** você digita em `caso/miniloja/cadastro.py` a assinatura `def cpf_valido(cpf):`. O editor sugere:

```python
def cpf_valido(cpf):
    d = [int(c) for c in cpf if c.isdigit()]
    if len(d) != 11:
        return False
    for n in (9, 10):
        soma = sum(d[i] * (n + 1 - i) for i in range(n))
        if (soma * 10) % 11 % 10 != d[n]:
            return False
    return True
```

**Tempo simulado até a primeira versão:** 2min. **Idas e vindas:** 0.

**Para você analisar:** a sugestão está correta para o CPF `529.982.247-25`. Ela cobre a regra de que **todos os dígitos iguais** são inválidos (`111.111.111-11`)? Rode mentalmente o caso e diga se a verificação `v09` passaria. Que verificação extra você faria antes de aceitar?
