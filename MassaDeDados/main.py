import csv
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()


def data_ultimo_ano():
    hoje = datetime.today()
    tres_anos_atras = hoje - timedelta(days=3*365)
    return fake.date_between(start_date=tres_anos_atras, end_date=hoje)

dados_cliente = []
dados_imovel = []
dados_seguradora = []
dados_corretor = []
dados_cobertura = []
dados_apolice_seguro = []

for i in range(10000):  
    
    cliente = {
        'cliente_id': i + 1,
        'nome_cliente': fake.name(),
        'endereco_cliente': fake.address(),
        'telefone_cliente': fake.phone_number(),
        'email_cliente': fake.email(),
    }
    dados_cliente.append(cliente)

    imovel = {
        'imovel_id': i + 1,
        'cliente_id': i + 1,  
        'endereco_imovel': fake.address(),
        'tipo_imovel': fake.random_element(elements=('Casa', 'Apartamento', 'Sobrado')),
        'valor_imovel': round(fake.random_number(digits=5), 2),
    }
    dados_imovel.append(imovel)

    seguradora = {
        'seguradora_id': i + 1,
        'nome_seguradora': fake.company(),
        'endereco_seguradora': fake.address(),
        'telefone_seguradora': fake.phone_number(),
        'email_seguradora': fake.email(),
    }
    dados_seguradora.append(seguradora)

    corretor = {
        'corretor_id': i + 1,
        'nome_corretor': fake.name(),
        'numero_registro': fake.random_number(digits=5),
        'seguradora_id': i + 1,  
        'telefone_corretor': fake.phone_number(),
        'email_corretor': fake.email(),
    }
    dados_corretor.append(corretor)

    cobertura = {
        'cobertura_id': i + 1,
        'descricao': fake.sentence(),
        'premio': round(fake.random_number(digits=4), 2),
        'limite_indenizacao': round(fake.random_number(digits=5), 2),
        'seguradora_id': i + 1,  
        'obrigatorio': fake.boolean(),
    }
    dados_cobertura.append(cobertura)

    apolice = {
        'apolice_id': i + 1,
        'cliente_id': i + 1,  
        'imovel_id': i + 1,  
        'seguradora_id': i + 1,  
        'corretor_id': i + 1, 
        'data_inicio': data_ultimo_ano(),
        'data_termino': data_ultimo_ano(),
    }
    dados_apolice_seguro.append(apolice)

def salvar_csv(nome_arquivo, dados, fieldnames):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dados)

salvar_csv('clientes.csv', dados_cliente, ['cliente_id', 'nome_cliente', 'endereco_cliente', 'telefone_cliente', 'email_cliente'])
salvar_csv('imoveis.csv', dados_imovel, ['imovel_id', 'cliente_id', 'endereco_imovel', 'tipo_imovel', 'valor_imovel'])
salvar_csv('seguradoras.csv', dados_seguradora, ['seguradora_id', 'nome_seguradora', 'endereco_seguradora', 'telefone_seguradora', 'email_seguradora'])
salvar_csv('corretores.csv', dados_corretor, ['corretor_id', 'nome_corretor', 'numero_registro', 'seguradora_id', 'telefone_corretor', 'email_corretor'])
salvar_csv('coberturas.csv', dados_cobertura, ['cobertura_id', 'descricao', 'premio', 'limite_indenizacao', 'seguradora_id', 'obrigatorio'])
salvar_csv('apolices_seguro.csv', dados_apolice_seguro, ['apolice_id', 'cliente_id', 'imovel_id', 'seguradora_id', 'corretor_id', 'data_inicio', 'data_termino'])

print('Arquivos CSV salvos com sucesso!')

