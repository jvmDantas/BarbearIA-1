from .usuario import Usuario


class Cliente(Usuario):
    """Classe que representa um cliente no sistema"""
    
    def __init__(self, id=None, email=None, senha=None, foto=None, telefone=None):
        super().__init__(id, email, senha, foto)
        self.telefone = telefone
    
    def to_dict(self):
        """Converte o objeto para dicionário (sem a senha)"""
        data = super().to_dict()
        data['telefone'] = self.telefone
        return data
    
    def to_dict_with_password(self):
        """Converte o objeto para dicionário (com a senha)"""
        data = super().to_dict_with_password()
        data['telefone'] = self.telefone
        return data
