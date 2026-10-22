"""Golden master de calcular_total (AV1.2, ampliado na AV2) — somente biblioteca padrão.

Grava o comportamento ATUAL (inclusive bugs e exceções) e compara com igualdade
exata de valor e tipo, sem tolerância; exceção é comparada pelo tipo. Uso, a
partir da raiz do pacote:
  python -B exercicios/aula-2/golden_master.py gravar     # antes da rodada 1
  python -B exercicios/aula-2/golden_master.py comparar   # depois de cada rodada
  python -B exercicios/aula-2/golden_master.py comparar --codigo caminho/da/copia
"""
import argparse
import json
import os
import sys
import unittest

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
ARQUIVO = os.path.join(AQUI, "golden_master.json")
FLAG = "MINILOJA_PROMO_NATAL"

# (cupom, flag NATAL): None = sem cupom; NATAL com a campanha desligada e ligada
CUPONS = [
    (None, "0"), ("PROMO10", "0"), ("VIP15", "0"), ("FRETEGRATIS", "0"),
    ("NATAL", "0"), ("NATAL", "1"), ("INVALIDO", "0"),
]
UFS = ["PE", "SP", "RJ", "BA"]  # BA representa "demais UFs"

# fronteiras: R$ 200 (código usa > 200, contrato diz >= 200), desconto cruzando o
# limite, arredondamento "meio para cima" e carrinhos degenerados
FRONTEIRAS = {
    "F_200_00": [{"preco": 200.0, "qtd": 1}],
    "F_199_99": [{"preco": 199.99, "qtd": 1}],
    "F_200_01": [{"preco": 200.01, "qtd": 1}],
    "F_222_22": [{"preco": 222.22, "qtd": 1}],  # PROMO10 -> 199.998
    "F_222_23": [{"preco": 222.23, "qtd": 1}],  # PROMO10 -> 200.007
    "F_235_00": [{"preco": 235.0, "qtd": 1}],   # VIP15 -> 199.75
    "F_arred_2_00": [{"preco": 2.0, "qtd": 1}],  # PE sem cupom -> 15.645 antes do round
    "F_arred_1_60": [{"preco": 1.6, "qtd": 1}],  # SP sem cupom -> 23.005 antes do round
    "F_vazio": [],
    "F_qtd_zero": [{"preco": 80.0, "qtd": 0}],
}


def carregar_carrinhos():
    with open(os.path.join(RAIZ, "caso", "dados", "carrinhos.json"), encoding="utf-8") as f:
        carrinhos = json.load(f)["carrinhos"]
    carrinhos.update(FRONTEIRAS)
    return carrinhos


def gerar_casos():
    """Lista de casos: matriz carrinho x cupom x UF, mais variações de texto/omissão."""
    casos = []
    for nome, itens in CARRINHOS.items():
        for cupom, natal in CUPONS:
            for uf in UFS:
                sufixo = cupom or "SEM_CUPOM"
                if cupom == "NATAL":
                    sufixo += "_flag" + natal
                casos.append({"id": f"{nome}|{sufixo}|{uf}", "natal": natal,
                              "itens": itens, "kwargs": {"cupom": cupom, "uf": uf}})
    c1 = CARRINHOS["C1_camisa_e_bola"]
    extras = [
        ("uf_minuscula_pe", {"cupom": None, "uf": "pe"}),
        ("cupom_minusculo_promo10", {"cupom": "promo10", "uf": "PE"}),
        ("cupom_vazio", {"cupom": "", "uf": "PE"}),
        ("uf_omitida", {"cupom": "PROMO10"}),
        ("cupom_e_uf_omitidos", {}),
        # UF/cupom não texto: a rodada 1 da AV1.2 passou a levantar TypeError com
        # lista (não hashable) e o golden master não via; só valores nativos de JSON
        ("uf_none", {"cupom": None, "uf": None}),
        ("uf_vazia", {"cupom": None, "uf": ""}),
        ("uf_int", {"cupom": None, "uf": 26}),
        ("uf_lista", {"cupom": None, "uf": ["PE"]}),
        ("uf_dict", {"cupom": None, "uf": {"uf": "PE"}}),
        ("cupom_int", {"cupom": 10, "uf": "PE"}),
        ("cupom_lista", {"cupom": ["PROMO10"], "uf": "PE"}),
        ("cupom_dict", {"cupom": {"cupom": "PROMO10"}, "uf": "SP"}),
        ("fretegratis_uf_lista", {"cupom": "FRETEGRATIS", "uf": ["SP"]}),
    ]
    for nome, kwargs in extras:
        casos.append({"id": f"C1_camisa_e_bola|{nome}", "natal": "0", "itens": c1, "kwargs": kwargs})
    # itens malformados: hoje levantam exceção; o golden master exige o mesmo tipo
    # de exceção depois da refatoração (o contrato é omisso aqui)
    malformados = {
        "item_sem_qtd": [{"preco": 80.0}],
        "item_sem_preco": [{"qtd": 1}],
        "preco_texto": [{"preco": "80.0", "qtd": 1}],
        "preco_none": [{"preco": None, "qtd": 1}],
        "qtd_float": [{"preco": 80.0, "qtd": 1.5}],
        "itens_none": None,
    }
    for nome, itens in malformados.items():
        casos.append({"id": f"M_{nome}|SEM_CUPOM|PE", "natal": "0", "itens": itens,
                      "kwargs": {"cupom": None, "uf": "PE"}})
    return casos


def executar(calcular_total, caso):
    anterior = os.environ.get(FLAG)
    os.environ[FLAG] = caso["natal"]
    itens = caso["itens"]
    if itens is not None:
        itens = [dict(i) for i in itens]
    try:
        return calcular_total(itens, **caso["kwargs"])
    finally:
        if anterior is None:
            os.environ.pop(FLAG, None)
        else:
            os.environ[FLAG] = anterior


def importar_calcular_total(codigo):
    sys.path.insert(0, os.path.abspath(codigo))
    from miniloja.calculo import calcular_total
    return calcular_total


def observar(calcular_total, caso):
    """Resultado comparável: valor e tipo, ou só o tipo da exceção (a mensagem pode mudar)."""
    try:
        valor = executar(calcular_total, caso)
    except Exception as e:
        return {"erro": type(e).__name__}
    return {"saida": valor, "tipo": type(valor).__name__}


def gravado(caso):
    return {k: caso[k] for k in ("saida", "tipo", "erro") if k in caso}


def gravar(calcular_total):
    saida = []
    for caso in gerar_casos():
        saida.append({**caso, **observar(calcular_total, caso)})
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump({"total_casos": len(saida), "casos": saida}, f, ensure_ascii=False, indent=1)
    print(f"Gravados {len(saida)} casos em {os.path.relpath(ARQUIVO, RAIZ)}")


class TestGoldenMaster(unittest.TestCase):
    """Igualdade exata (valor e tipo, ou tipo da exceção), sem tolerância: um centavo já é divergência."""

    calcular_total = None

    def test_comportamento_identico_ao_gravado(self):
        with open(ARQUIVO, encoding="utf-8") as f:
            casos = json.load(f)["casos"]
        self.assertEqual(len(casos), len(gerar_casos()), "lista de casos mudou desde a gravação")
        divergencias = 0
        for caso in casos:
            with self.subTest(caso=caso["id"]):
                atual = observar(type(self).calcular_total, caso)
                if atual != gravado(caso):
                    divergencias += 1
                self.assertEqual(atual, gravado(caso))
        print(f"\nGolden master: {len(casos)} casos, {divergencias} divergência(s)")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("modo", choices=["gravar", "comparar"])
    p.add_argument("--codigo", default=os.path.join(RAIZ, "caso"), help="pasta com o pacote miniloja")
    a = p.parse_args()
    calcular_total = importar_calcular_total(a.codigo)
    if a.modo == "gravar":
        if os.path.exists(ARQUIVO):
            sys.exit(f"{os.path.relpath(ARQUIVO, RAIZ)} já existe; apague-o para regravar de propósito.")
        gravar(calcular_total)
        return
    TestGoldenMaster.calcular_total = staticmethod(calcular_total)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGoldenMaster)
    resultado = unittest.TextTestRunner(verbosity=1).run(suite)
    sys.exit(0 if resultado.wasSuccessful() else 1)


CARRINHOS = carregar_carrinhos()

if __name__ == "__main__":
    main()
