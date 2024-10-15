from project.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome, telefone, email, endereco, crm: str):
        super().__init__(nome, telefone, email, endereco)
        self._verificar_crm(crm)

    
    def salarioFinal(self, salario) -> float:
        super().salarioFinal(salario)

        BONUS = 1.2
        return salario * BONUS
    
    def _verificar_crm(self, valor):
        self._verificar_crm_tipo_invalido(valor)
        self._verificar_crm_vazio(valor)

        self.crm = valor
        return self.crm
    
    def _verificar_crm_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CRM deve ser em texto")
    
    def _verificar_crm_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O CRM não deve estar vazio")
            
        