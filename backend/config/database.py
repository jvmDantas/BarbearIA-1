"""
Database Connection - Gerenciador de conexões com MySQL usando PyMySQL
"""
import pymysql
import os
from exceptions import DatabaseConnectionException


class DBConnection:
    """Classe para gerenciar conexões com o banco de dados"""
    
    def __init__(self):
        self.host = os.getenv("MYSQL_HOST", "localhost")
        self.port = int(os.getenv("MYSQL_PORT", "3306"))
        self.user = os.getenv("MYSQL_USER", "barbearia_user")
        self.password = os.getenv("MYSQL_PASSWORD", "")
        self.database = os.getenv("MYSQL_DATABASE", "barbearia_db")
    
    def get_connection(self):
        """Cria e retorna uma nova conexão com o banco de dados"""
        try:
            return pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.OperationalError as e:
            error_code = e.args[0]
            if error_code == 2003:
                raise DatabaseConnectionException("Servidor MySQL não está acessível")
            elif error_code == 1045:
                raise DatabaseConnectionException("Credenciais de acesso inválidas")
            elif error_code == 1049:
                raise DatabaseConnectionException(f"Banco de dados '{self.database}' não existe")
            else:
                raise DatabaseConnectionException(f"Erro ao conectar: {str(e)}")
        except pymysql.Error as e:
            raise DatabaseConnectionException(f"Erro de conexão: {str(e)}")
