import pytest
from project.models.medico import Medico
from project.models.endereco import Endereco

@pytest.fixture
def medico_valido():
    return Medico("Wagner", "9191919", "wagnersi@gmail.com",
        Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),"123")

"""VALIDAÇÕES DOS DADOS DO USUARIO"""
def test_validar_nome(medico_valido):
    assert medico_valido.nome == "Wagner"


def test_validar_telefone(medico_valido):
    assert medico_valido.telefone ==  "9191919"

def test_validar_email(medico_valido):
    assert medico_valido.email == "wagnersi@gmail.com"

def test_salario_negativo():
    medico = Medico("Wagner", "9191919", "wagnersi@gmail.com",
        Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),"123")
    with pytest.raises(ValueError, match="Valor não pode ser negativo"):
        medico.salarioFinal(-1)