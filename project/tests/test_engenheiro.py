import pytest
from project.models.engenheiro import Engenheiro
from project.models.endereco import Endereco

@pytest.fixture
def engenheiro_valido():
    return Engenheiro("Wagner", "9191919", "wagnersi@gmail.com",
        Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),"12345")

"""VALIDAÇÕES DOS DADOS DO USUARIO"""
def test_validar_nome(engenheiro_valido):
    assert engenheiro_valido.nome == "Wagner"

def test_validar_telefone(engenheiro_valido):
    assert engenheiro_valido.telefone ==  "9191919"

def test_validar_email(engenheiro_valido):
    assert engenheiro_valido.email == "wagnersi@gmail.com"

def test_validar_crm(engenheiro_valido):
    assert engenheiro_valido.crea == "12345"

def test_validar_endereco(engenheiro_valido):
    assert engenheiro_valido.endereco.logadouro == "Rua A"
    assert engenheiro_valido.endereco.numero == "91"
    assert engenheiro_valido.endereco.complemento == "casa"
    assert engenheiro_valido.endereco.cidade == "Salvador"
    assert engenheiro_valido.endereco.cep == "4300202-00"

"""TESTES PARA VERIFICAÇÂO DO SALÁRIO"""
def test_salario_negativo():
    engenheiro = Engenheiro("Wagner", "9191919", "wagnersi@gmail.com",
        Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),"12345")
    with pytest.raises(ValueError, match="O valor não pode ser negativo."):
        engenheiro.salarioFinal(-1)

def test_salario_tipo_invalido():
    engenheiro = Engenheiro("Wagner", "9191919", "wagnersi@gmail.com",
        Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),"12345")
    with pytest.raises(TypeError, match="O valor não pode ser em texto."):
        engenheiro.salarioFinal("2000")

"""TESTES PARA CLASSE MEDICO"""
def test_crea_vazio():
    with pytest.raises(ValueError, match="O crea não pode ficar em branco"):
        Engenheiro("Wagner", "9191919", "wagnersi@gmail.com",
            Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),"")

def test_crea_tipo_invalido():
    with pytest.raises(TypeError, match="O crea deve ser preenchido em texto"):
        Engenheiro("Wagner", "9191919", "wagnersi@gmail.com",
            Endereco("Rua A", "91", "casa", "4300202-00","Salvador"),12345)