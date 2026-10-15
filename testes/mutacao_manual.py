#!/usr/bin/env python3
"""Mutação manual mínima (alternativa leve a mutmut/Stryker/PIT, só biblioteca padrão).

Aplica pequenas falhas ao código-fonte, roda a suíte e informa quais mutantes SOBREVIVERAM
(isto é, a suíte continuou verde). Uso: python -B testes/mutacao_manual.py [arquivo.py ...]
Variável MINILOJA_TEST_CMD permite trocar o comando de teste (padrão: python -B testes/test_miniloja.py --existentes --codigo caso -x).
"""
import os
import shlex
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SRC = RAIZ / "caso" / "miniloja"
CMD = shlex.split(os.environ.get("MINILOJA_TEST_CMD", f"{sys.executable} -B testes/test_miniloja.py --existentes --codigo caso -x"))

MUTACOES = [
    # (arquivo, trecho original, trecho mutado, descrição)
    ("calculo.py", "total = total * 0.9\n", "total = total * 0.91\n", "PROMO10: 10% -> 9%"),
    ("calculo.py", "total = total * 0.85", "total = total * 0.86", "VIP15: 15% -> 14%"),
    ("calculo.py", "total = total * 0.8\n", "total = total * 0.79\n", "NATAL: 20% -> 21%"),
    ("calculo.py", "if total > 200:", "if total >= 200:", "limite do frete grátis: > vira >="),
    ("calculo.py", "if total > 200:", "if total > 300:", "limite do frete grátis: 200 vira 300"),
    ("calculo.py", "frete = 12.9", "frete = 13.9", "frete PE"),
    ("calculo.py", "frete = 19.9", "frete = 20.9", "frete SP"),
    ("calculo.py", "frete = 21.5", "frete = 22.5", "frete RJ"),
    ("calculo.py", "frete = 29.9", "frete = 30.9", "frete UF desconhecida"),
    ("calculo.py", "taxa = 0.05", "taxa = 0.06", "taxa PE"),
    ("calculo.py", "taxa = 0.07", "taxa = 0.08", "taxa SP"),
    ("calculo.py", "taxa = 0.06", "taxa = 0.07", "taxa RJ"),
    ("calculo.py", "taxa = 0.08", "taxa = 0.09", "taxa UF desconhecida"),
    ("calculo.py", "preco * qtd", "preco + qtd", "soma dos itens: * vira +"),
    ("calculo.py", 'elif cupom == "VIP15":', 'elif cupom == "VIP16":', "cupom VIP15 deixa de existir"),
    ("calculo.py", 'if cupom == "FRETEGRATIS":\n        frete = 0', 'if cupom == "XFRETEGRATIS":\n        frete = 0', "FRETEGRATIS deixa de zerar o frete"),
    ("calculo.py", "return round(total, 2)", "return round(total, 3)", "arredondamento em 3 casas"),
    ("calculo.py", "desconto_aplicado = True", "desconto_aplicado = False", "variável sem efeito (mutante equivalente)"),
    ("descontos.py", '"VIP15": 15', '"VIP15": 5', "percentual do VIP15"),
    ("descontos.py", "total - (total * pct / 100)", "total + (total * pct / 100)", "desconto vira acréscimo"),
    ("estoque.py", "if disponivel < qtd:", "if disponivel <= qtd:", "limite exato do estoque"),
    ("estoque.py", "disponivel - qtd", "disponivel + qtd", "reserva aumenta o saldo"),
    ("formatacao.py", '"R$ " + s', '"R$" + s', "espaço após R$"),
    ("formatacao.py", ":,.2f", ":,.1f", "uma casa decimal"),
    ("cadastro.py", 'if not payload.get("email"):', "if False:", "e-mail deixa de ser obrigatório"),
    ("pedidos.py", 'if cobranca["status"] != "aprovado":', 'if cobranca["status"] == "aprovado":', "inverte a checagem do pagamento"),
    ("pedidos.py", '"total_fmt": moeda(total)', '"total_fmt": moeda(0)', "total formatado sempre zero"),
    ("pedidos.py", "if not itens:", "if itens is None:", "pedido sem itens deixa de ser rejeitado"),
    ("relatorios.py", "round(v, 2)", "round(v, 3)", "formatação do relatório"),
    ("relatorios.py", "len(pedidos)", "len(pedidos) + 1", "quantidade de pedidos"),
    ("handlers.py", "return 409,", "return 408,", "status de estoque insuficiente"),
]


def limpar_cache():
    """Evita que um .pyc de outra variante seja reaproveitado (mutações de mesmo tamanho)."""
    for pasta in RAIZ.rglob("__pycache__"):
        for pyc in pasta.glob("*.pyc"):
            pyc.unlink()


def passa():
    limpar_cache()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run(CMD, cwd=RAIZ, capture_output=True, text=True, timeout=120, env=env).returncode == 0


def main(filtro):
    if not passa():
        sys.exit("A suíte já falha sem mutação; corrija antes de rodar.")
    sobreviventes, mortos = [], 0
    for arq, velho, novo, desc in MUTACOES:
        if filtro and arq not in filtro:
            continue
        caminho = SRC / arq
        original = caminho.read_text(encoding="utf-8")
        assert velho in original, f"trecho não encontrado em {arq}: {velho!r}"
        try:
            caminho.write_text(original.replace(velho, novo, 1), encoding="utf-8")
            verde = passa()
        finally:
            caminho.write_text(original, encoding="utf-8")
        if verde:
            sobreviventes.append((arq, desc))
        else:
            mortos += 1
    total = mortos + len(sobreviventes)
    print(f"Mutantes: {total} | mortos: {mortos} | sobreviventes: {len(sobreviventes)} "
          f"| escore: {100 * mortos / total:.0f}%")
    for arq, desc in sobreviventes:
        print(f"  SOBREVIVEU  {arq}: {desc}")


if __name__ == "__main__":
    main(set(sys.argv[1:]))
