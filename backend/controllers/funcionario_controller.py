from fastapi import APIRouter
from managers.funcionario_manager import funcionario_manager


class FuncionarioController:
    """Controller para rotas de Funcionario"""
    
    def __init__(self):
        """
        Inicializa o controller
        """
        self.funcionario_manager = funcionario_manager
        self.router = APIRouter(prefix='/funcionarios', tags=['Funcionarios'])
        self._registrar_rotas()
    
    def _registrar_rotas(self):
        """Registra as rotas do controller"""
        
        @self.router.get('')
        async def listar_funcionarios():
            """Lista todos os funcionários"""
            return self.funcionario_manager.listar_funcionarios()
        
        @self.router.post('', status_code=201)
        async def criar_funcionario(dados: dict):
            """Cria um novo funcionário"""
            return self.funcionario_manager.criar_funcionario(dados)


# Instância singleton
funcionario_controller = FuncionarioController()
