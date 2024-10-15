from project.models.endereco import Endereco
from abc import ABC,abstractmethod

class Funcionario(ABC):
    def __init__(self,nome: str,telefone: str,email: str,endereco: Endereco) -> None:
        super().__init__()
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salarioFinal(self, salario) -> float:
        if not isinstance(salario, (int, float)):
            raise TypeError("O valor não pode ser em texto.")

        if salario < 0:
            raise ValueError("O valor não pode ser negativo.") 
        pass

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereço: {self.endereco}"
                )