import unittest

from miniloja import cadastro


class TestCadastro(unittest.TestCase):
    # Ajustado: esperava 400; o contrato (R3.4) exige 422 com a lista de erros.
    # Payload sem nome e sem cpf: os dois são obrigatórios (R3.1).
    def test_cadastro_sem_nome_e_rejeitado(self):
        cadastro.limpar()
        status, corpo = cadastro.cadastrar_cliente({"email": "a@b.com"})
        self.assertEqual(status, 422)
        self.assertEqual(sorted(e["campo"] for e in corpo["erros"]), ["cpf", "nome"])

    # Ajustado: aceitava cadastro sem cpf; o contrato (R3.1) torna cpf obrigatório.
    # Agora usa um CPF fictício válido (caso/dados/cpfs.json) e continua esperando 201.
    def test_cadastro_valido(self):
        cadastro.limpar()
        status, corpo = cadastro.cadastrar_cliente(
            {"nome": "Ana", "email": "ana@exemplo.com", "cpf": "529.982.247-25"}
        )
        self.assertEqual(status, 201)
        self.assertEqual(corpo["id"], 1)
