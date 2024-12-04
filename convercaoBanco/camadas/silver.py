# silver-zone
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import AzureError



# Nome dos containers para cada camada
bronze_container_name = "bronze"
silver_container_name = "silver"

#

# Função para copiar arquivo de um container para outro
def copy_to_silver(file_name):
    try:
        # Obter o cliente do blob na Bronze Zone
        source_blob = blob_service_client.get_blob_client(container=bronze_container_name, blob=file_name)

        # Obter o cliente do blob na Silver Zone
        target_blob = blob_service_client.get_blob_client(container=silver_container_name, blob=file_name)

        # Copiar o arquivo para a Silver Zone
        target_blob.start_copy_from_url(source_blob.url)
        print(f"Arquivo {file_name} movido para a Silver Zone.")
    except AzureError as e:
        print(f"Ocorreu um erro ao mover o arquivo para a Silver Zone: {e}")

# Lista de arquivos para processar
files_to_process = [
    "clientes.csv",
    "imovel.csv",
    "cobertura.csv",
    "apoliceseguro.csv",
    "corretor.csv",
    "seguradora.csv"
]

# Processar cada arquivo da Bronze para a Silver Zone
for file_name in files_to_process:
    copy_to_silver(file_name)