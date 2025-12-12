from .usuario import Usuario


class Funcionario(Usuario):
    """Classe que representa um funcionário no sistema"""
    
    def __init__(self, id=None, email=None, senha=None, foto=None, 
                 eh_barbeiro=False, eh_admin=False):
        super().__init__(id, email, senha, foto)
        self.eh_barbeiro = eh_barbeiro
        self.eh_admin = eh_admin
    
    def to_dict(self):
        """Converte o objeto para dicionário (sem a senha)"""
        data = super().to_dict()
        data['eh_barbeiro'] = self.eh_barbeiro
        data['eh_admin'] = self.eh_admin
        return data
    
    def to_dict_with_password(self):
        """Converte o objeto para dicionário (com a senha)"""
        data = super().to_dict_with_password()
        data['eh_barbeiro'] = self.eh_barbeiro
        data['eh_admin'] = self.eh_admin
        return data
