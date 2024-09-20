
create table if not exists tb_usuarios (
    usr_id INTEGER PRIMARY KEY AUTOINCREMENT,
    usr_tipo_usuario TEXT NOT NULL,
    usr_nome TEXT NOT NULL,
    usr_email TEXT NOT NULL,
    usr_cpf TEXT NOT NULL,
    usr_senha TEXT NOT NULL
);

create table if not exists tb_tecnologias (
    tec_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tec_nome TEXT NOT NULL,
    tec_sigla TEXT NOT NULL,
    tec_descricao TEXT NOT NULL
);