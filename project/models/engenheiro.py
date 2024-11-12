from project.models.funcionario import Funcionario
from project.models.endereco import Endereco

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco,crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = self._verificar_crea(crea)

    
    def salarioFinal(self, salario) -> float:
        super().salarioFinal(salario)

        BONUS = 1.2
        return salario * BONUS    

    def _verificar_crea(self, valor):
       self.__verificar_crea_tipo_invalido(valor)
       self.__verificar_crea_vazio_invalido(valor)
       
       self.crea = valor
       return self.crea

    def __verificar_crea_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O crea deve ser preenchido em texto")
        
    def __verificar_crea_vazio_invalido(self, valor):
        if not valor.strip():
            raise ValueError("O crea não pode ficar em branco")
        
