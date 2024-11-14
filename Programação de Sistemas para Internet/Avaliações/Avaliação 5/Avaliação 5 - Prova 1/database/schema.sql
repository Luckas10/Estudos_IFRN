create database db_projeto;
USE db_projeto;

CREATE TABLE tb_usuarios (
    usr_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    usr_nome VARCHAR(90),
    usr_email TEXT,
    usr_senha TEXT,
    usr_idade INT
);

select * from tb_usuarios;