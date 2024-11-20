import psycopg2
import csv

# Função para exportar dados para CSV
def export_to_csv(db_config, table_name, csv_file_name):
    # Conectando ao banco de dados PostgreSQL
    conn = psycopg2.connect(
        host=db_config['host'],
        port=db_config['port'],
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = conn.cursor()

    # Executando a consulta para pegar todos os dados da tabela
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Pegando os nomes das colunas
    columns = [desc[0] for desc in cursor.description]

    # Escrevendo os dados no arquivo CSV
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Escreve os nomes das colunas no CSV
        writer.writerow(columns)

        # Escreve as linhas de dados no CSV
        writer.writerows(rows)

    # Fechando a conexão com o banco de dados
    conn.close()


db_config = {
    'host': 'localhost',  
    'port': 5432,         
    'dbname': 'postgres',  
    'user': 'admin',          
    'password': 'admin'       
}

# Exemplo de uso
table_name = 'cliente'         
csv_file_name = 'dados_exportados.csv'  

export_to_csv(db_config, table_name, csv_file_name)
