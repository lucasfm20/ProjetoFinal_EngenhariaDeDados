CREATE TABLE cliente (
    cliente_id INT  PRIMARY KEY,
    nome_cliente VARCHAR(255),
    endereco_cliente VARCHAR(255),
    telefone_cliente VARCHAR(30),
    email_cliente VARCHAR(255)
);

CREATE TABLE imovel (
    imovel_id INT  PRIMARY KEY,
    cliente_id INT,
    endereco_imovel VARCHAR(255),
    tipo_imovel VARCHAR(50),
    valor_imovel DECIMAL(12, 2),
    FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id)
);

CREATE TABLE cobertura (
    cobertura_id INT  PRIMARY KEY,
    descricao VARCHAR(255),
    premio DECIMAL(12, 2),
    limite_indenizacao DECIMAL(12, 2),
    seguradora_id INT,
    obrigatorio BOOLEAN,
    FOREIGN KEY (seguradora_id) REFERENCES seguradora(seguradora_id)
);

CREATE TABLE apolice_seguro (
    apolice_id INT  PRIMARY KEY,
    cliente_id INT ,
    imovel_id INT ,
    seguradora_id INT,
    corretor_id INT,
    data_inicio DATE,
    data_termino DATE,
    FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id),
    FOREIGN KEY (imovel_id) REFERENCES imovel(imovel_id),
    FOREIGN KEY (seguradora_id) REFERENCES seguradora(seguradora_id),
    FOREIGN KEY (corretor_id) REFERENCES corretor(corretor_id)
);



CREATE TABLE corretor (
    corretor_id INT  PRIMARY KEY,
    nome_corretor VARCHAR(255),
    numero_registro VARCHAR(50),
    seguradora_id INT,
    telefone_corretor VARCHAR(30),
    email_corretor VARCHAR(255),
    FOREIGN KEY (seguradora_id) REFERENCES seguradora(seguradora_id)
);

CREATE TABLE seguradora (
    seguradora_id INT  PRIMARY KEY,
    nome_seguradora VARCHAR(255) ,
    endereco_seguradora VARCHAR(255),
    telefone_seguradora VARCHAR(30),
    email_seguradora VARCHAR(255)
);

