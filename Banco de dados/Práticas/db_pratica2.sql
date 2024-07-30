CREATE DATABASE db_pratica2;
USE db_pratica2;

CREATE TABLE tb_categorias (
    cat_id INT PRIMARY KEY AUTO_INCREMENT,
    cat_nome VARCHAR(45) NOT NULL,
    cat_descricao VARCHAR(45) NOT NULL
);

CREATE TABLE tb_autores (
    aut_id INT PRIMARY KEY AUTO_INCREMENT,
    aut_nome VARCHAR(45) NOT NULL
);

CREATE TABLE tb_livros (
    liv_id INT PRIMARY KEY AUTO_INCREMENT,
    liv_titulo VARCHAR(45) NOT NULL,
    liv_cat_id INT,
    liv_aut_id INT,
    FOREIGN KEY (liv_cat_id) REFERENCES tb_categorias(cat_id),
    FOREIGN KEY (liv_aut_id) REFERENCES tb_autores(aut_id)
);
