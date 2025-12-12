from fastapi import APIRouter
from managers.cliente_manager import cliente_manager


class ClienteController:
    """Controller para rotas de Cliente"""
    
    def __init__(self):
        """
        Inicializa o controller
        """
        self.cliente_manager = cliente_manager
        self.router = APIRouter(prefix='/clientes', tags=['Clientes'])
        self._registrar_rotas()
    
    def _registrar_rotas(self):
        """Registra as rotas do controller"""
        
        @self.router.get('')
        async def listar_clientes():
            """Lista todos os clientes"""
            return self.cliente_manager.listar_clientes()
        
        @self.router.post('', status_code=201)
        async def criar_cliente(dados: dict):
            """Cria um novo cliente"""
            return self.cliente_manager.criar_cliente(dados)


# Instância singleton
cliente_controller = ClienteController()
