CREATE DATABASE db_pratica1;
USE db_pratica1;

CREATE TABLE tb_funcionarios (
    fun_cod INT PRIMARY KEY AUTO_INCREMENT,
    fun_nome VARCHAR(45) NOT NULL,
    fun_cpf VARCHAR(11) NOT NULL,
    fun_rua VARCHAR(45),
    fun_bairro VARCHAR(45),
    fun_cidade VARCHAR(45),
    fun_estado VARCHAR(45)
);

CREATE TABLE tb_telFun (
    tlf_cod INT PRIMARY KEY AUTO_INCREMENT,
    tlf_telefone VARCHAR(45),
    tlf_fun_cod INT,
    FOREIGN KEY (tlf_fun_cod) REFERENCES tb_funcionarios(fun_cod)
);
