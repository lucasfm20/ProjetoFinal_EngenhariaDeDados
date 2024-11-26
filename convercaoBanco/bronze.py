# bronze-zone
from azure.storage.blob import BlobServiceClient
import os
from azure.core.exceptions import AzureError



# Nome dos containers para cada camada
landing_container_name = "landing-zone"
bronze_container_name = "bronze"



# Função para copiar arquivo de um container para outro
def copy_to_bronze(file_name):
    try:
        # Obter o cliente do blob na Landing Zone
        source_blob = blob_service_client.get_blob_client(container=landing_container_name, blob=file_name)

        # Obter o cliente do blob na Bronze Zone
        target_blob = blob_service_client.get_blob_client(container=bronze_container_name, blob=file_name)

        # Copiar o arquivo para a Bronze Zone
        target_blob.start_copy_from_url(source_blob.url)
        print(f"Arquivo {file_name} movido para a Bronze Zone.")
    except AzureError as e:
        print(f"Ocorreu um erro ao mover o arquivo para a Bronze Zone: {e}")

# Lista de arquivos para processar
files_to_process = [
    "clientes.csv",
    "imovel.csv",
    "cobertura.csv",
    "apoliceseguro.csv",
    "corretor.csv",
    "seguradora.csv"
]

# Processar cada arquivo da Landing para a Bronze Zone
for file_name in files_to_process:
    copy_to_bronze(file_name)
