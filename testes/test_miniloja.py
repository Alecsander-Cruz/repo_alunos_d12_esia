"""Verificações do caso MiniLoja (somente biblioteca padrão).

Uso, a partir da raiz do pacote:
  python -B testes/test_miniloja.py --codigo caso
  python -B testes/test_miniloja.py --codigo caso --teste TestMiniLoja.test_v08_cpf_com_digito_verificador_errado
  python -B testes/test_miniloja.py --codigo caso --existentes     # roda a suíte existente do caso
"""
import argparse
import os
import sys
import unittest

CPF_VALIDO = "529.982.247-25"
CPF_DV_ERRADO = "529.982.247-24"
CPF_IGUAIS = "111.111.111-11"


class TestMiniLoja(unittest.TestCase):
    """Cada verificação nasce do contrato em caso/regras.md."""

    @classmethod
    def setUpClass(cls):
        from miniloja import cadastro, handlers
        from miniloja.calculo import calcular_total

        cls.cadastro, cls.handlers = cadastro, handlers
        cls.calcular_total = staticmethod(calcular_total)

    def setUp(self):
        self.cadastro.limpar()

    # --- R1 · cálculo do total (valores de entrada fora das fronteiras de arredondamento e de R$ 200,00)
    def test_v01_total_simples_em_pe(self):
        self.assertEqual(self.calcular_total([{"preco": 50.0, "qtd": 2}], None, "PE"), 118.55)

    def test_v02_cupom_promo10_aplica_dez_por_cento(self):
        self.assertEqual(self.calcular_total([{"preco": 80.0, "qtd": 1}], "PROMO10", "SP"), 98.33)

    def test_v03_cupom_fretegratis_zera_o_frete(self):
        self.assertEqual(self.calcular_total([{"preco": 40.0, "qtd": 1}], "FRETEGRATIS", "RJ"), 42.4)

    def test_v04_pedido_bem_acima_de_200_nao_paga_frete(self):
        self.assertEqual(self.calcular_total([{"preco": 250.0, "qtd": 1}], None, "PE"), 262.5)

    # --- R2 · pedido
    def test_v05_pedido_sem_itens_e_rejeitado(self):
        status, _ = self.handlers.post_pedidos(1, {"itens": []})
        self.assertEqual(status, 400)

    def test_v06_estoque_insuficiente_responde_409(self):
        status, corpo = self.handlers.post_pedidos(
            1, {"itens": [{"sku": "CHUTEIRA-42", "preco": 300.0, "qtd": 999}]}
        )
        self.assertEqual(status, 409)
        self.assertEqual(corpo["sku"], "CHUTEIRA-42")

    # --- R3 · cadastro de cliente
    def test_v07_cadastro_com_cpf_valido_e_aceito(self):
        status, corpo = self.handlers.post_clientes(
            {"nome": "Ana Exemplo", "email": "ana@exemplo.com", "cpf": CPF_VALIDO}
        )
        self.assertEqual(status, 201)
        self.assertEqual(corpo["cpf"], CPF_VALIDO)

    def test_v08_cpf_com_digito_verificador_errado(self):
        status, corpo = self.handlers.post_clientes(
            {"nome": "Ana Exemplo", "email": "ana@exemplo.com", "cpf": CPF_DV_ERRADO}
        )
        self.assertEqual(status, 422)
        self.assertIn("cpf", [e["campo"] for e in corpo["erros"]])

    def test_v09_cpf_com_todos_os_digitos_iguais(self):
        status, corpo = self.handlers.post_clientes(
            {"nome": "Ana Exemplo", "email": "ana@exemplo.com", "cpf": CPF_IGUAIS}
        )
        self.assertEqual(status, 422)
        self.assertIn("cpf", [e["campo"] for e in corpo["erros"]])

    def test_v10_payload_invalido_lista_todos_os_erros(self):
        status, corpo = self.handlers.post_clientes({"email": "sem-arroba", "cpf": CPF_DV_ERRADO})
        self.assertEqual(status, 422)
        self.assertEqual(sorted(e["campo"] for e in corpo["erros"]), ["cpf", "email", "nome"])

    def test_v11_cadastro_valido_recebe_identificador(self):
        status, corpo = self.handlers.post_clientes(
            {"nome": "Bia Exemplo", "email": "bia@exemplo.com", "cpf": CPF_VALIDO}
        )
        self.assertEqual(status, 201)
        self.assertEqual(corpo["id"], 1)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--codigo", default="caso", help="pasta que contém o pacote miniloja (padrão: caso)")
    p.add_argument("--teste", help="nome da verificação, por exemplo TestMiniLoja.test_v01_total_simples_em_pe")
    p.add_argument("--existentes", action="store_true", help="roda a suíte existente do caso em vez das verificações")
    p.add_argument("-x", "--failfast", action="store_true")
    a = p.parse_args()
    codigo = os.path.abspath(a.codigo)
    sys.path.insert(0, codigo)
    carregador = unittest.TestLoader()
    if a.existentes:
        suite = carregador.discover(os.path.join(codigo, "testes_existentes"), top_level_dir=codigo)
    elif a.teste:
        suite = carregador.loadTestsFromName(a.teste, sys.modules[__name__])
    else:
        suite = carregador.loadTestsFromTestCase(TestMiniLoja)
    resultado = unittest.TextTestRunner(verbosity=2, failfast=a.failfast).run(suite)
    sys.exit(0 if resultado.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
