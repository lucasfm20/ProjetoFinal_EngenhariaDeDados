#landing-zone
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text
from azure.storage.blob import BlobServiceClient
import os
from azure.core.exceptions import AzureError

# Configurações do Banco de Dados PostgreSQL
db_host = "-"
db_port = "5432"
db_name = "Banco"
db_user = "-"
db_password = "-"

# Configuração do Azure Blob Storage
azure_connection_string = "-"

# Conectar ao Banco de Dados PostgreSQL
conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)

# Conectar ao Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)

# Criar URL de conexão para o PostgreSQL
db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

# Função para buscar dados de uma tabela do banco de dados
def fetch_table_data(table_name):
    query = text(f"SELECT * FROM {table_name}")
    with engine.connect() as connection:
        return pd.read_sql(query, con=connection)

# Buscar dados das tabelas e armazenar em DataFrames
clientes_df = fetch_table_data('cliente')
imovel_df = fetch_table_data('imovel')
cobertura_df = fetch_table_data('cobertura')
apolice_seguro_df = fetch_table_data('apolice_seguro')
corretor_df = fetch_table_data('corretor')
seguradora_df = fetch_table_data('seguradora')

# Função para salvar DataFrame como CSV no Azure Blob Storage
def save_to_azure_blob(df, file_name):
    try:
        # Garantir que o nome do arquivo seja válido para o Azure Blob Storage
        file_name = file_name.lower().replace(" ", "_")  # Converte para minúsculas e substitui espaços por underscores

        # Criação de um caminho temporário simplificado no sistema local
        local_temp_path = f"/tmp/{file_name}"
        os.makedirs(os.path.dirname(local_temp_path), exist_ok=True)  # Cria o diretório se não existir
        df.to_csv(local_temp_path, index=False)

        # Nome do container
        container_name = "landing-zone"  # Certifique-se de que o nome do container seja válido

        # Obter o cliente do container
        container_client = blob_service_client.get_container_client(container_name)

        # Carregar o arquivo CSV no Azure Blob Storage
        blob_client = container_client.get_blob_client(file_name)
        with open(local_temp_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"Arquivo {file_name} carregado no Azure Blob Storage.")
    
    except AzureError as e:
        print(f"Ocorreu um erro ao tentar carregar o arquivo no Azure Blob Storage: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Salvar as tabelas como arquivos CSV
save_to_azure_blob(clientes_df, "clientes.csv")
save_to_azure_blob(imovel_df, "imovel.csv")
save_to_azure_blob(cobertura_df, "cobertura.csv")
save_to_azure_blob(apolice_seguro_df, "apoliceseguro.csv")
save_to_azure_blob(corretor_df, "corretor.csv")
save_to_azure_blob(seguradora_df, "seguradora.csv")
