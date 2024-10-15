from project.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome, telefone, email, endereco, crm: str):
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    
    def salarioFinal(self, salario) -> float:
        if salario < 0:
            raise ValueError("Valor não pode ser negativo")
        BONUS = 1.2

        return salario * BONUS
            
        