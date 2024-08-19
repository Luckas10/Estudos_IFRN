use db_escola;

# 1. Altere o e-mail do professor "Anitta" para "anitta.silva@exemplo.com".

UPDATE tb_professores
SET pro_email = 'anitta.silva@exemplo.com'
WHERE pro_nome = 'Anitta';

# 2. Atualize o departamento dos professores que lecionam "'Artes Cênicas'" para "Moda".

UPDATE tb_professores
SET pro_departamento = 'Moda'
WHERE pro_departamento = 'Artes Cênicas';

# 3. Corrija o número de telefone do professor cujo ID é 3 para "(11) 99999-8888".

UPDATE tb_professores
SET pro_telefone = '(11) 99999-8888'
WHERE pro_id = 3;

# 4. Reduza em 5% o salário dos professores que trabalham no departamento de "Moda".

UPDATE tb_professores
SET pro_salario = pro_salario * 0.95tb_jogadores
WHERE pro_departamento = 'Moda';

# 5. Atualize a rua e o número dos professores que moram na cidade "São Paulo" para "Rua dos Professores, 123".

UPDATE tb_professores
SET pro_rua = 'Rua dos Professores', pro_numero = 123
WHERE pro_cidade = 'São Paulo';

# 6. Delete todos os professores do departamento "Educação Física".

DELETE FROM tb_professores
WHERE pro_departamento = 'Educação Física';

# 7. Atualize o email dos professores que lecionam "'Artes Cênicas'" para "nome@artes.cenicas".

UPDATE tb_professores
SET pro_email = CONCAT(SUBSTRING_INDEX(pro_nome, ' ', 1), '@artes.cenicas')
WHERE pro_departamento = 'Artes Cênicas';

# 8. Corrija a data de contratação de "Marília Mendonça" para 2022-01-15.

UPDATE tb_professores
SET pro_data_contratacao = '2022-01-15'
WHERE pro_nome = 'Marília Mendonça';

# 9. Atualize a cidade de todos os professores que moram no estado do "RJ" para "Rio de Janeiro".

UPDATE tb_professores
SET pro_cidade = 'Rio de Janeiro'
WHERE pro_estado = 'RJ';

# 10. Delete todos os professores que residem no bairro de "'Medellín'".

DELETE FROM tb_professores
WHERE pro_cidade = 'Medellín';

# 11. Delete todos os professores cujo gênero é "Outro" para fins de simplificação do banco de dados.

DELETE FROM tb_professores
WHERE pro_genero = 'Outro';

# 12. Delete todos os professores do departamento "Música" nascidos antes de 1965.

DELETE FROM tb_professores
WHERE pro_departamento = 'Música'
AND pro_data_nascimento < '1965-01-01';

# 13. Delete todos os professores do bairro "'Ciudad de México'" que sejam do gênero Masculino.

DELETE FROM tb_professores
WHERE pro_bairro = 'Ciudad de México'
AND pro_genero = 'M';

# 14. Delete todos os professores da cidade "'Puerto Rico'" cujo gênero é "Masculino".

DELETE FROM tb_professores
WHERE pro_cidade = 'San Juan'
AND pro_genero = 'M';