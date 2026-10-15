# Verificações do caso

As onze verificações usam `unittest` e a biblioteca padrão do Python (**3.11 ou superior**; verificado com 3.12.3). Execute os comandos a partir da raiz do pacote, onde está o `README.md` principal.

```
python -B testes/test_miniloja.py --codigo caso
```

`--codigo` recebe a pasta que contém o pacote `miniloja`. Pode apontar para uma **cópia de trabalho**; quando omitido, usa `caso`. A opção `-B` evita arquivos auxiliares de cache.

Para selecionar uma verificação pelo nome de comportamento:

```
python -B testes/test_miniloja.py --codigo caso --teste TestMiniLoja.test_v08_cpf_com_digito_verificador_errado
```

Para rodar a **suíte existente do caso** (26 testes, em `caso/testes_existentes/`) em vez das verificações:

```
python -B testes/test_miniloja.py --codigo caso --existentes
```

Para a **mutação mínima** (31 falhas injetadas na suíte existente, só biblioteca padrão):

```
python -B testes/mutacao_manual.py
python -B testes/mutacao_manual.py calculo.py estoque.py     # só alguns arquivos
```

| Regra | Cobertura |
| --- | --- |
| R1 | Total simples, cupom `PROMO10`, cupom `FRETEGRATIS` e pedido bem acima de R$ 200,00 (v01 a v04) |
| R2 | Pedido sem itens e estoque insuficiente (v05 e v06) |
| R3 | CPF válido, dígito verificador errado, dígitos iguais, resposta `422` com a lista de todos os erros e cadastro válido (v07 a v11) |
| R4 | **Revisão humana**, não automatizada por esta suíte |

No material inicial, **oito verificações passam e três falham** (v08, v09 e v10, as tarefas do bloco 1). `ok` indica verificação satisfeita; `FAIL` indica divergência da expectativa e `ERROR` indica impedimento para executar. O processo retorna `0` quando o conjunto executado passa e `1` se há falha ou erro.

A suíte existente passa por inteiro, mas **passar não é estar certo**: ela contém dívida de propósito. A saída é evidência sobre este material, não nota de aluno. Sucesso nos testes não demonstra segurança completa, qualidade geral ou produtividade da IA. Não se verifica comportamento de um modelo de linguagem. A transcrição acessível está em [resultado-textual.md](../apoio/resultado-textual.md).

**Não altere os arquivos desta pasta.** Se um teste precisa mudar, mude o seu, em uma cópia, e registre o motivo.
