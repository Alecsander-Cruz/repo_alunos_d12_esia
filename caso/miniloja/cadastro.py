"""Cadastro de clientes."""

import re

_CLIENTES = []
_EMAIL_RE = re.compile(r"[^@\s.]+(\.[^@\s.]+)*@[^@\s.]+(\.[^@\s.]+)+")


def _cpf_valido(cpf):
    """R3.2: dígitos verificadores válidos, sem todos os dígitos iguais; aceita com ou sem pontuação."""
    if not isinstance(cpf, str):
        return False
    digitos = cpf.replace(".", "").replace("-", "")
    if len(digitos) != 11 or not digitos.isdigit():
        return False
    if len(set(digitos)) == 1:
        return False
    for tamanho in (9, 10):
        soma = sum(int(d) * peso for d, peso in zip(digitos[:tamanho], range(tamanho + 1, 1, -1)))
        dv = (soma * 10) % 11 % 10
        if dv != int(digitos[tamanho]):
            return False
    return True


def _email_valido(email):
    """R3.3: formato texto@texto.texto."""
    return isinstance(email, str) and _EMAIL_RE.fullmatch(email) is not None


def _ausente(valor):
    return valor is None or (isinstance(valor, str) and not valor.strip())


def cadastrar_cliente(payload):
    """Cadastra um cliente (R3): 422 com todos os erros de uma vez, ou 201 com id sequencial."""
    erros = []
    for campo in ("nome", "email", "cpf"):
        if _ausente(payload.get(campo)):
            erros.append({"campo": campo, "erro": "campo obrigatório"})
    if not _ausente(payload.get("nome")) and not isinstance(payload["nome"], str):
        erros.append({"campo": "nome", "erro": "nome inválido"})
    if not _ausente(payload.get("email")) and not _email_valido(payload["email"]):
        erros.append({"campo": "email", "erro": "email inválido"})
    if not _ausente(payload.get("cpf")) and not _cpf_valido(payload["cpf"]):
        erros.append({"campo": "cpf", "erro": "cpf inválido"})
    if erros:
        return 422, {"erros": erros}
    cliente = dict(payload, id=len(_CLIENTES) + 1)
    _CLIENTES.append(cliente)
    return 201, cliente


def limpar():
    _CLIENTES.clear()
