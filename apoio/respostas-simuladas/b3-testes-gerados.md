> **RESPOSTA SIMULADA.** Texto construído pelo professor para análise, identificado como simulação. Não é saída real de um modelo e não mede desempenho de nenhuma ferramenta. Quem a usa **não deve declarar ter executado** a tarefa.

# Bloco 3 · Testes gerados por um agente para `calcular_total` (simulados)

**Pedido:** "Gere testes para `calcular_total`." (sem passar o contrato)

```python
# T-A
def test_total_igual_a_formula(self):
    itens = [{"preco": 50.0, "qtd": 2}]
    esperado = round((100.0 + 12.9) * 1.05, 2)
    self.assertEqual(calcular_total(itens, None, "PE"), esperado)

# T-B
def test_retorna_algo(self):
    self.assertIsNotNone(calcular_total([{"preco": 10.0, "qtd": 1}]))

# T-C
def test_cupom_promo10(self):
    with patch("miniloja.calculo.flags") as f:
        f.promo_natal_ativa.return_value = False
        self.assertEqual(calcular_total([{"preco": 80.0, "qtd": 1}], "PROMO10", "SP"), 98.33)

# T-D
def test_frete_gratis_em_200(self):
    self.assertEqual(calcular_total([{"preco": 100.0, "qtd": 2}], None, "PE"), 223.55)

# T-E
def test_carrinho_vazio(self):
    self.assertEqual(calcular_total([], None, "PE"), 13.54)
```

**Para você analisar:** classifique cada teste (espelho, sem asserção real, snapshot do próprio código, com asserção real). Qual deles **grava um comportamento que o contrato contradiz**? O que o agente precisaria ter recebido para derivar o esperado do contrato?
