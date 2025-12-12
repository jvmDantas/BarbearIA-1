import hashlib


class SenhaService:
    """Service para operações relacionadas a senha"""
    
    @staticmethod
    def hash_senha(senha):
        """
        Gera o hash SHA256 da senha
        
        :param senha: String com a senha em texto plano
        :return: Hash SHA256 da senha
        """
        return hashlib.sha256(senha.encode()).hexdigest()
    
    @staticmethod
    def verificar_senha(senha, hash_armazenado):
        """
        Verifica se a senha corresponde ao hash armazenado
        
        :param senha: String com a senha em texto plano
        :param hash_armazenado: Hash SHA256 armazenado
        :return: True se a senha está correta, False caso contrário
        """
        hash_senha = SenhaService.hash_senha(senha)
        return hash_senha == hash_armazenado
