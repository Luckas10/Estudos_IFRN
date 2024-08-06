CREATE DATABASE db_pratica5;
USE db_pratica5;

CREATE TABLE tb_empresa (
    emp_id INT (11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    emp_cnpj VARCHAR (20) NOT NULL,
    emp_nome_fantasia VARCHAR (50) NOT NULL,
    emp_endereco VARCHAR (200) NOT NULL,
    emp_telefone VARCHAR (20) NOT NULL,
    emp_emp_id INT (11),
    FOREIGN KEY (emp_emp_id) REFERENCES tb_empresa(emp_id)
);

CREATE TABLE tb_cargo (
    car_id INT (11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    car_nome VARCHAR (45) NOT NULL
);

CREATE TABLE tb_funcionario (
    fun_id INT (11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    fun_nome VARCHAR (100) NOT NULL,
    fun_cpf VARCHAR (20) NOT NULL,
    fun_data_nascimento DATE NOT NULL,
    fun_endereco VARCHAR (20) NOT NULL,
    fun_telefone VARCHAR (20) NOT NULL,
    fun_car_id INT (11),
    FOREIGN KEY (fun_car_id) REFERENCES tb_cargo(car_id),
    fun_emp_id INT (11),
    FOREIGN KEY (fun_emp_id) REFERENCES tb_empresa(emp_id)
);

CREATE TABLE tb_riscos_ocupacionais (
    rio_id INT (11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    rio_nome VARCHAR (45) NOT NULL
);

CREATE TABLE tb_tipo_exame (
    tex_id INT (11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    tex_tipo VARCHAR (45) NOT NULL
);

CREATE TABLE tb_resultado_exame (
    rex_id INT (11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    rex_tipo VARCHAR (30) NOT NULL
);

CREATE TABLE tb_exame (
    exa_id INT (11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    exa_especialidade VARCHAR (50) NOT NULL,
    exa_data_realizacao DATE NOT NULL,
    exa_tex_id INT (11),
    FOREIGN KEY (exa_tex_id) REFERENCES tb_tipo_exame(tex_id),
    exa_rex_id INT (11),
    FOREIGN KEY (exa_rex_id) REFERENCES tb_resultado_exame(rex_id)
);

CREATE TABLE tb_funcionario_has_exame (
    fex_exa_id INT (11),
    FOREIGN KEY (fex_exa_id) REFERENCES tb_exame(exa_id),
    fex_fun_id INT (11),
    FOREIGN KEY (fex_fun_id) REFERENCES tb_funcionario(fun_id),
    PRIMARY KEY (fex_exa_id, fex_fun_id)
);

CREATE TABLE tb_empresa_has_exame (
    emx_exa_id INT (11),
    FOREIGN KEY (emx_exa_id) REFERENCES tb_exame(exa_id),
    emx_emp_id INT (11),
    FOREIGN KEY (emx_emp_id) REFERENCES tb_empresa(emp_id),
    PRIMARY KEY (emx_exa_id, emx_emp_id)
);

CREATE TABLE tb_cargo_has_risco_ocupacionais (
    cro_car_id INT (11),
    FOREIGN KEY (cro_car_id) REFERENCES tb_cargo(car_id),
    cro_rio_id INT (11),
    FOREIGN KEY (cro_rio_id) REFERENCES tb_riscos_ocupacionais(rio_id),
    PRIMARY KEY (cro_car_id, cro_rio_id)
);

CREATE TABLE tb_medico (
    med_id INT (11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    med_crm INT (11) NOT NULL,
    med_nome VARCHAR (100) NOT NULL,
    med_cpf VARCHAR (20) NOT NULL,
    med_especialidade VARCHAR (50) NOT NULL,
    med_data_nascimento DATE NOT NULL,
    med_endereco VARCHAR (200) NOT NULL,
    med_telefone VARCHAR (20)
);

CREATE TABLE tb_atestado (
    ate_id INT (11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    ate_resultados_riscos VARCHAR (100) NOT NULL,
    ate_resultado VARCHAR (100) NOT NULL,
    ate_observacoes VARCHAR (300) NOT NULL,
    ate_med_id INT (11),
    FOREIGN KEY (ate_med_id) REFERENCES tb_medico(med_id)
);

CREATE TABLE tb_exame_has_atestado (
    atx_exa_id INT (11),
    FOREIGN KEY (atx_exa_id) REFERENCES tb_exame(exa_id),
    atx_ate_id INT (11),
    FOREIGN KEY (atx_ate_id) REFERENCES tb_atestado(ate_id),
    PRIMARY KEY (atx_exa_id, atx_ate_id)
);