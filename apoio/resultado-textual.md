# Resultado textual de execuções (preparação)

Transcrições de execuções feitas na **preparação do material**, com **Python 3.12.3**, na raiz do pacote. Servem a quem não executa o código: leia-as como saídas observadas **pelo professor**, não pelo aluno. Não declare que você observou estas saídas.

## 1. Verificações do caso (material inicial)

```
$ python -B testes/test_miniloja.py --codigo caso
test_v01_total_simples_em_pe ... ok
test_v02_cupom_promo10_aplica_dez_por_cento ... ok
test_v03_cupom_fretegratis_zera_o_frete ... ok
test_v04_pedido_bem_acima_de_200_nao_paga_frete ... ok
test_v05_pedido_sem_itens_e_rejeitado ... ok
test_v06_estoque_insuficiente_responde_409 ... ok
test_v07_cadastro_com_cpf_valido_e_aceito ... ok
test_v08_cpf_com_digito_verificador_errado ... FAIL
test_v09_cpf_com_todos_os_digitos_iguais ... FAIL
test_v10_payload_invalido_lista_todos_os_erros ... FAIL
test_v11_cadastro_valido_recebe_identificador ... ok
AssertionError: 201 != 422
AssertionError: 201 != 422
AssertionError: 400 != 422
Ran 11 tests in 0.004s
FAILED (failures=3)
$ echo $?
1
```

Oito verificações passam e três falham. As três falhas são as **tarefas do bloco 1** (CPF e resposta `422`). `FAIL` indica divergência da expectativa; `ERROR` indicaria impedimento para executar.

## 2. Suíte existente do caso

```
$ python -B testes/test_miniloja.py --codigo caso --existentes
Ran 26 tests in 0.002s
OK
```

A suíte existente passa por inteiro. **Isso não diz que o código está correto**: leia o contrato e compare com os testes.

## 3. Mutação mínima sobre a suíte existente

```
$ python -B testes/mutacao_manual.py
Mutantes: 31 | mortos: 23 | sobreviventes: 8 | escore: 74%
  SOBREVIVEU  calculo.py: NATAL: 20% -> 21%
  SOBREVIVEU  calculo.py: frete RJ
  SOBREVIVEU  calculo.py: variável sem efeito (mutante equivalente)
  SOBREVIVEU  descontos.py: percentual do VIP15
  SOBREVIVEU  estoque.py: limite exato do estoque
  SOBREVIVEU  cadastro.py: e-mail deixa de ser obrigatório
  SOBREVIVEU  pedidos.py: total formatado sempre zero
  SOBREVIVEU  relatorios.py: formatação do relatório
```

A ferramenta injeta 31 pequenas falhas no código e roda a suíte existente. **Sobrevivente** é uma falha que a suíte não percebeu. O mutante "variável sem efeito" é **equivalente** (não altera o comportamento). A cobertura de linhas da mesma suíte, medida por rastreamento da biblioteca padrão, é de cerca de 90%: cobertura alta e mutação mais baixa é exatamente o contraste que o bloco 3 explora.
