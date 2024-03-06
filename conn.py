from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Sua string de conexão
DB_URL = "postgresql+psycopg2://postgres:123@localhost:5435/DEV"

# Criar um engine de conexão
engine = create_engine(DB_URL)

try:
    # Tentar conectar ao banco de dados
    engine.connect()
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro na conexão: {e}")
finally:
    # Fechar a conexão após o teste
    engine.dispose()
