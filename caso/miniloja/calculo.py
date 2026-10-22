"""Cálculo de totais de pedido."""
from miniloja import flags

FRETE_POR_UF = {"PE": 12.9, "SP": 19.9, "RJ": 21.5}
TAXA_POR_UF = {"PE": 0.05, "SP": 0.07, "RJ": 0.06}


def _valor_por_uf(tabela, uf, padrao):
    # busca por igualdade, não por hash: UF não hashable (ex.: lista) cai no padrão.
    # tabela.get(uf) levantaria TypeError e mudaria o comportamento (ADR-001)
    for chave, valor in tabela.items():
        if uf == chave:
            return valor
    return padrao


def calcular_total(itens, cupom=None, uf="PE"):
    """Calcula o total do pedido segundo R1 de caso/regras.md, com dois desvios conhecidos.

    itens: lista de dicts com "preco" e "qtd"; subtotal = soma de preco x qtd (R1.1).
        Item sem "preco" ou "qtd" levanta KeyError.
    cupom: "PROMO10" (10%), "VIP15" (15%), "NATAL" (20%, só com MINILOJA_PROMO_NATAL=1)
        ou "FRETEGRATIS" (zera o frete, sem desconto); qualquer outro valor, inclusive
        None, é ignorado sem erro (R1.2).
    uf: define o frete (PE 12,90, SP 19,90, RJ 21,50, demais 29,90; grátis com
        FRETEGRATIS ou subtotal com desconto acima do limite) e a taxa de serviço
        (PE 5%, SP 7%, RJ 6%, demais 8%) (R1.3, R1.4). UF fora da tabela, inclusive
        não texto, cai em "demais", sem erro. O padrão "PE" é decisão do código, não
        do contrato: R1 não define UF padrão.

    Retorna float com duas casas. Ordem: desconto, frete, taxa sobre (subtotal com
    desconto + frete) (R1.6).

    Desvios conhecidos do contrato, mantidos de propósito (ADR-001):
    - frete grátis só acima de R$ 200 (> 200); R1.3 pede >= 200. Ex.: 1 x R$ 200,00
      em PE devolve 223,55, e não 210,00.
    - round() em float não arredonda meio para cima (R1.5). Ex.: 1 x R$ 2,00 em PE
      (15,645 pelo contrato) devolve 15,64, e não 15,65.
    Corrigir qualquer um muda o comportamento: é tarefa própria, não refatoração.
    """
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
