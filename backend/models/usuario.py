class Usuario:
    """Classe base para representar um usuário no sistema"""
    
    def __init__(self, id=None, email=None, senha=None, foto=None):
        self.id = id
        self.email = email
        self.senha = senha
        self.foto = foto
    
    def to_dict(self):
        """Converte o objeto para dicionário (sem a senha)"""
        return {
            'id': self.id,
            'email': self.email,
            'foto': self.foto
        }
    
    def to_dict_with_password(self):
        """Converte o objeto para dicionário (com a senha)"""
        return {
            'id': self.id,
            'email': self.email,
            'senha': self.senha,
            'foto': self.foto
        }
