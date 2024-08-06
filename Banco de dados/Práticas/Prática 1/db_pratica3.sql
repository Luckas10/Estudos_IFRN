CREATE DATABASE db_pratica3;
USE db_pratica3;

CREATE TABLE tb_medicos (
    med_cod INT PRIMARY KEY AUTO_INCREMENT,
    med_nome VARCHAR(45) NOT NULL,
    med_crm INT NOT NULL,
    med_especialidade VARCHAR(45) NOT NULL
);

CREATE TABLE tb_pacientes (
    pac_cod INT PRIMARY KEY AUTO_INCREMENT,
    pac_nome VARCHAR(45) NOT NULL,
    pac_cpf VARCHAR(45) NOT NULL,
    pac_nascimento DATE NOT NULL
);

CREATE TABLE tb_consultas (
    con_cod INT PRIMARY KEY AUTO_INCREMENT,
    con_data DATE NOT NULL,
    con_med_cod INT,
    con_pac_cod INT,
    FOREIGN KEY (con_med_cod) REFERENCES tb_medicos(med_cod),
    FOREIGN KEY (con_pac_cod) REFERENCES tb_pacientes(pac_cod)
);
