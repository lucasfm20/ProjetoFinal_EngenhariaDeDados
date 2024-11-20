import psycopg2
import pandas as pd
from sqlalchemy import create_engine

from config import DATABASE_CONFIG

try:
    conn = psycopg2.connect(**DATABASE_CONFIG)
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar: {e}")


db_url = f"postgresql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"

engine = create_engine(db_url)

def fetch_table_data(table_name):
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, con=engine)

clientes_df = fetch_table_data('cliente')
print(clientes_df.head())