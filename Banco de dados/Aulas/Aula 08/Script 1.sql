SELECT * FROM tb_jogadores;
SELECT * FROM tb_alunos WHERE alu_genero='M';
SELECT * FROM tb_alunos WHERE alu_cidade='New York';
SELECT alu_nome, alu_data_nascimento FROM tb_alunos WHERE alu_cidade='Mississippi' OR alu_cidade='California';

# 1. Quais são os jogadores de nacionalidade brasileira e do gênero masculino? 
SELECT * FROM tb_jogadores 
WHERE jog_nacionalidade='Brasil' 
AND jog_genero='M';

# 2. Quais são os jogadores que nasceram em 1995 e têm o gênero masculino? 
SELECT * FROM tb_jogadores 
WHERE year(jog_data_nascimento)='1995' 
AND jog_genero='M';

# 3. Quais são os jogadores que têm a posição 'Atacante' ou 'Goleiro'? 
SELECT * FROM tb_jogadores 
WHERE jog_posicao='Atacante' 
OR jog_posicao='Goleiro';

# 4. Quais são os jogadores do time com ID 1 ou ID 2? 
SELECT * FROM tb_jogadores 
WHERE jog_time_id=1 
OR jog_time_id=2;

# 5. Quais são os jogadores com o número da camisa 10?
SELECT * FROM tb_jogadores 
WHERE jog_numero_camisa=10;

# 6. Quais são os jogadores de nacionalidade brasileira, do gênero masculino e que jogam como 'Zagueiro'?
SELECT * FROM tb_jogadores 
WHERE jog_nacionalidade='Brasil' 
AND jog_genero='M' 
AND jog_posicao='Zagueiro';

# 7. Quais são os jogadores que nasceram em 1995, têm o gênero masculino e estão no time com ID 5?
SELECT * FROM tb_jogadores 
WHERE YEAR(jog_data_nascimento)='1995' 
AND jog_genero='M' 
AND jog_time_id =5;

# 8. Quais são os jogadores que têm a posição 'Atacante' ou 'Goleiro', e que têm o número da camisa 1?
SELECT * FROM tb_jogadores 
WHERE jog_posicao='Atacante' 
OR jog_posicao='Goleiro' 
AND jog_numero_camisa=1;

# 9. Quais são os jogadores do time com ID 1 ou ID 2, e que são do gênero masculino e têm a posição 'Meio-campo'?
SELECT * FROM tb_jogadores 
WHERE (jog_time_id=1 or jog_time_id=2) 
AND jog_genero='M' 
AND jog_posicao='Meio-campo';

# 10. Quais são os jogadores com o número da camisa 10, que nasceram antes do ano 2000 e jogam no time com ID 6?
SELECT * FROM tb_jogadores 
WHERE jog_numero_camisa=10 
AND YEAR(jog_data_nascimento)<2000 
AND jog_time_id=6;

# 11. Quais são os jogadores que têm nacionalidade brasileira e atuam na posição 'Atacante' ou 'Goleiro'?
SELECT * FROM tb_jogadores 
WHERE jog_nacionalidade='Brasil' 
AND (jog_posicao='Atacante' 
OR jog_posicao='Goleiro');