class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str):
        self._verificar_logradouro(logradouro)
        self._verificar_numero(numero)
        self._verificar_complemento(complemento)
        self._verificar_cep(cep)
        self._verificar_cidade(cidade)

    
    """Método para verificação de logradouro"""
    def _verificar_logradouro(self, valor):
        self._verificar_logradouro_tipo_invalido(valor)
        self._verificar_logradouro_vazio(valor)
        
        self.logadouro = valor
        return self.logadouro

    def _verificar_logradouro_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O logradouro deve ser um texto.")
        
    def _verificar_logradouro_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O logradouro não deve estar vazio.")

    """Método para verificação de número"""
    def _verificar_numero(self, valor):
        self._verificar_numero_tipo_invalido(valor)
        self._verificar_numero_vazio(valor)
        
        self.numero = valor
        return self.numero

    def _verificar_numero_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O número deve ser um texto.")
        
    def _verificar_numero_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O número não deve estar vazio.")

    """Método para verificação de complemento"""
    def _verificar_complemento(self, valor):
        self._verificar_complemento_tipo_invalido(valor)
        
        self.complemento = valor
        return self.complemento

    def _verificar_complemento_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O complemento deve ser um texto.")

    """Método para verificação de CEP"""
    def _verificar_cep(self, valor):
        self._verificar_cep_tipo_invalido(valor)
        self._verificar_cep_vazio(valor)
        
        self.cep = valor
        return self.cep

    def _verificar_cep_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CEP deve ser um texto.")
        
    def _verificar_cep_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O CEP não deve estar vazio.")


    """Método para verificação de cidade"""
    def _verificar_cidade(self, valor):
        self._verificar_cidade_tipo_invalido(valor)
        self._verificar_cidade_vazio(valor)
        
        self.cidade = valor
        return self.cidade

    def _verificar_cidade_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A cidade deve ser um texto.")
        
    def _verificar_cidade_vazio(self, valor):
        if not valor.strip():
            raise ValueError("A cidade não deve estar vazia.")
        