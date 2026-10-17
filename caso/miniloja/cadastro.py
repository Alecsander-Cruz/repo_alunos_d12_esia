"""Cadastro de clientes."""

_CLIENTES = []


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


def cadastrar_cliente(payload):
    """Cadastra um cliente."""
    if not payload.get("nome"):
        return 400, {"erro": "payload inválido"}
    if not payload.get("email"):
        return 400, {"erro": "payload inválido"}
    if "cpf" in payload and not _cpf_valido(payload["cpf"]):
        return 422, {"erros": [{"campo": "cpf", "erro": "cpf inválido"}]}
    cliente = dict(payload, id=len(_CLIENTES) + 1)
    _CLIENTES.append(cliente)
    return 201, cliente


def limpar():
    _CLIENTES.clear()
