CREATE DATABASE db_pratica4;
USE db_pratica4;

CREATE TABLE tb_cliente (
    cli_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    cli_nome VARCHAR(45) NOT NULL,
    cli_telefone VARCHAR(45) NOT NULL,
    cli_email VARCHAR(45) NOT NULL
);

CREATE TABLE tb_categoria (
    cat_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    cat_nome VARCHAR(45) NOT NULL
);

CREATE TABLE tb_fornecedores (
    for_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    for_cnpj VARCHAR(45) NOT NULL,
    for_nome VARCHAR(45) NOT NULL
);

CREATE TABLE tb_produto (
    pro_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    pro_nome VARCHAR(45) NOT NULL,
    pro_preco DECIMAL(10,2) NOT NULL,
    pro_qnt_estoque INT NOT NULL,
    pro_cat_id INT,
    FOREIGN KEY (pro_cat_id) REFERENCES tb_categoria(cat_id),
    pro_for_id INT,
    FOREIGN KEY (pro_for_id) REFERENCES tb_fornecedores(for_id)
);

CREATE TABLE tb_venda (
    ven_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    ven_valor_total DECIMAL(10,2) NOT NULL,
    ven_data DATETIME NOT NULL,
    ven_cli_id INT,
    FOREIGN KEY (ven_cli_id) REFERENCES tb_cliente(cli_id),
    ven_vnd_id int,
    FOREIGN KEY (ven_vnd_id) REFERENCES tb_vendedor(vnd_id),
    ven_pag_id int,
    FOREIGN KEY (ven_pag_id) REFERENCES tb_pagamento(pag_id)
); 

CREATE TABLE tb_vendedor (
    vnd_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    vnd_nome VARCHAR(45) NOT NULL
);

CREATE TABLE tb_pagamento (
    pag_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    pag_forma_pagamento VARCHAR(45) NOT NULL
);

CREATE TABLE tb_venda_has_produto (
    vpr_ven_id INT,
    FOREIGN KEY (vpr_ven_id) REFERENCES tb_venda(ven_id),
    vpr_pro_id INT,
    FOREIGN KEY (vpr_pro_id) REFERENCES tb_produto(pro_id),
    PRIMARY KEY (vpr_ven_id, vpr_pro_id)
);
