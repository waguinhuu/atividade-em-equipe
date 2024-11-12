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

def test_validar_crm(medico_valido):
    assert medico_valido.crm == "123"

def test_validar_endereco(medico_valido):
    assert medico_valido.endereco.logadouro == "Rua A"
    assert medico_valido.endereco.numero == "91"
    assert medico_valido.endereco.complemento == "casa"
    assert medico_valido.endereco.cidade == "Salvador"
    assert medico_valido.endereco.cep == "4300202-00"

"""TESTES PARA VERIFICAÇÂO DO SALÁRIO"""
def test_salario_negativo():
    medico = Medico("Wagner", "9191919", "wagnersi@gmail.com",
        Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),"123")
    with pytest.raises(ValueError, match="O valor não pode ser negativo."):
        medico.salarioFinal(-1)

def test_salario_tipo_invalido():
    medico = Medico("Wagner", "9191919", "wagnersi@gmail.com",
        Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),"123")
    with pytest.raises(TypeError, match="O valor não pode ser em texto."):
        medico.salarioFinal("2000")

"""TESTES PARA CLASSE MEDICO"""
def test_crm_vazio():
    with pytest.raises(ValueError, match="O CRM não deve estar vazio"):
        Medico("Wagner", "9191919", "wagnersi@gmail.com",
            Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),"")

def test_crm_tipo_invalido():
    with pytest.raises(TypeError, match="O CRM deve ser em texto"):
        Medico("Wagner", "9191919", "wagnersi@gmail.com",
            Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),123)