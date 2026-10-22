"""Testes de calcular_total derivados do contrato (caso/regras.md, R1), não do código.

Cada esperado foi calculado à mão a partir de R1; a conta está no comentário do teste.
Os dois bugs conhecidos (R1.3 e R1.5) ficam como expectedFailure: o esperado é o do
contrato, e a suíte acusa "unexpected success" quando o bug for corrigido.

Uso, a partir da raiz do pacote:
  python -B avaliacoes/av2/test_calculo_contrato.py
  MINILOJA_CODIGO=caminho/da/copia python -B avaliacoes/av2/test_calculo_contrato.py
"""
import os
import sys
import unittest
from unittest import mock

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.abspath(os.environ.get("MINILOJA_CODIGO", os.path.join(RAIZ, "caso"))))

from miniloja.calculo import calcular_total  # noqa: E402

FLAG = "MINILOJA_PROMO_NATAL"


def um_item(preco):
    return [{"preco": preco, "qtd": 1}]


class TestCalculoContrato(unittest.TestCase):
    def setUp(self):
        # campanha NATAL desligada por padrão; cada teste liga se precisar
        patcher = mock.patch.dict(os.environ, {FLAG: "0"})
        patcher.start()
        self.addCleanup(patcher.stop)

    # R1.1 subtotal
    def test_subtotal_soma_preco_vezes_qtd_de_varios_itens(self):
        # 3 x 19,99 + 2 x 10,00 = 79,97; + 21,50 (RJ) = 101,47; x 1,06 = 107,5582 -> 107,56
        itens = [{"preco": 19.99, "qtd": 3}, {"preco": 10.0, "qtd": 2}]
        self.assertEqual(calcular_total(itens, None, "RJ"), 107.56)

    # R1.2 desconto
    def test_promo10_desconta_10_por_cento(self):
        # 100 x 0,90 = 90,00; + 19,90 (SP) = 109,90; x 1,07 = 117,593 -> 117,59
        self.assertEqual(calcular_total(um_item(100.0), "PROMO10", "SP"), 117.59)

    def test_vip15_desconta_15_por_cento(self):
        # 100 x 0,85 = 85,00; + 21,50 (RJ) = 106,50; x 1,06 = 112,89
        self.assertEqual(calcular_total(um_item(100.0), "VIP15", "RJ"), 112.89)

    def test_natal_com_campanha_ativa_desconta_20_por_cento(self):
        # 100 x 0,80 = 80,00; + 29,90 (demais) = 109,90; x 1,08 = 118,692 -> 118,69
        os.environ[FLAG] = "1"
        self.assertEqual(calcular_total(um_item(100.0), "NATAL", "BA"), 118.69)

    def test_natal_com_campanha_inativa_nao_desconta(self):
        # sem desconto: 100 + 29,90 (demais) = 129,90; x 1,08 = 140,292 -> 140,29
        self.assertEqual(calcular_total(um_item(100.0), "NATAL", "BA"), 140.29)

    def test_fretegratis_zera_frete_sem_alterar_valor(self):
        # 50,00 sem desconto; frete 0; x 1,07 (SP) = 53,50
        self.assertEqual(calcular_total(um_item(50.0), "FRETEGRATIS", "SP"), 53.5)

    def test_cupom_desconhecido_e_ignorado(self):
        # como sem cupom: 100 + 19,90 (SP) = 119,90; x 1,07 = 128,293 -> 128,29
        self.assertEqual(calcular_total(um_item(100.0), "XYZ", "SP"), 128.29)

    # R1.3 frete e R1.4 taxa
    def test_pe_sem_desconto_paga_frete_e_taxa_de_pe(self):
        # 100,10 + 12,90 (PE) = 113,00; x 1,05 = 118,65
        self.assertEqual(calcular_total(um_item(100.10), None, "PE"), 118.65)

    def test_subtotal_abaixo_de_200_paga_frete(self):
        # 199,99 + 12,90 (PE) = 212,89; x 1,05 = 223,5345 -> 223,53
        self.assertEqual(calcular_total(um_item(199.99), None, "PE"), 223.53)

    @unittest.expectedFailure  # bug conhecido: código usa > 200; R1.3 diz >= (ADR da AV1.3)
    def test_subtotal_exatamente_200_tem_frete_gratis(self):
        # 200,00 >= 200 -> frete 0; x 1,05 (PE) = 210,00
        self.assertEqual(calcular_total(um_item(200.0), None, "PE"), 210.0)

    def test_desconto_que_leva_a_200_ou_mais_tem_frete_gratis(self):
        # 222,23 x 0,90 = 200,007 >= 200 -> frete 0; x 1,07 (SP) = 214,00749 -> 214,01
        self.assertEqual(calcular_total(um_item(222.23), "PROMO10", "SP"), 214.01)

    # R1.5 arredondamento
    @unittest.expectedFailure  # bug conhecido: round() em float não arredonda meio para cima
    def test_arredonda_meio_para_cima(self):
        # 10,00 + 12,90 (PE) = 22,90; x 1,05 = 24,045 -> meio para cima 24,05
        self.assertEqual(calcular_total(um_item(10.0), None, "PE"), 24.05)

    # R1.6 ordem
    def test_frete_e_decidido_depois_do_desconto(self):
        # 210 x 0,90 = 189,00 < 200 -> paga frete; + 19,90 (SP) = 208,90; x 1,07 = 223,523 -> 223,52
        # (frete decidido antes do desconto daria 210 >= 200 -> 189 x 1,07 = 202,23)
        self.assertEqual(calcular_total(um_item(210.0), "PROMO10", "SP"), 223.52)


if __name__ == "__main__":
    unittest.main()
