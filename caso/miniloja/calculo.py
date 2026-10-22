"""Cálculo de totais de pedido."""
from miniloja import flags

FRETE_POR_UF = {"PE": 12.9, "SP": 19.9, "RJ": 21.5}
TAXA_POR_UF = {"PE": 0.05, "SP": 0.07, "RJ": 0.06}


def _valor_por_uf(tabela, uf, padrao):
    # busca por igualdade, não por hash: UF não hashable (ex.: lista) cai no padrão
    for chave, valor in tabela.items():
        if uf == chave:
            return valor
    return padrao


def calcular_total(itens, cupom=None, uf="PE"):
    """Calcula o total do pedido."""
    # soma dos itens
    total = 0
    for i in itens:
        preco = i["preco"]
        qtd = i["qtd"]
        total = total + preco * qtd

    # desconto (cupom desconhecido é ignorado; FRETEGRATIS é tratado no frete)
    if cupom == "PROMO10":
        total = total * 0.9
    elif cupom == "VIP15":
        total = total * 0.85
    elif cupom == "NATAL" and flags.promo_natal_ativa():
        # campanha antiga; só vale se a flag estiver ligada
        total = total * 0.8

    # frete
    if cupom == "FRETEGRATIS" or total > 200:
        frete = 0
    else:
        frete = _valor_por_uf(FRETE_POR_UF, uf, 29.9)
    total = total + frete

    # taxa de serviço por UF
    taxa = _valor_por_uf(TAXA_POR_UF, uf, 0.08)
    imposto = total * taxa
    total = total + imposto

    return round(total, 2)
