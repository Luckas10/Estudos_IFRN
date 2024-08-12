# 1. Selecione todos os jogadores do Brasil cujo nome comece com "A".

SELECT * 
FROM tb_jogadores 
WHERE jog_nacionalidade = 'Brasil' 
AND jog_nome LIKE 'A%';

# 2. Selecione todos os jogadores cuja nacionalidade seja Brasil e que tenham "e" no nome.

SELECT * 
FROM tb_jogadores 
WHERE jog_nacionalidade = 'Brasil' 
AND jog_nome LIKE '%e%';

# 3. Selecione todos os jogadores com número de camisa maior que 10 e menor ou igual a 20.

SELECT * 
FROM tb_jogadores 
WHERE jog_numero_camisa > 10 
AND jog_numero_camisa <= 20;

# 4. Selecione todos os jogadores cuja posição seja "Atacante" ou "Meio-campo" e que tenham contrato registrado após 2023-01-01.

SELECT * 
FROM tb_jogadores 
WHERE jog_posicao IN ('Atacante', 'Meio-campo') 
AND jog_data_contrato > '2023-01-01';

# 5. Selecione todos os jogadores cujo número de camisa está entre 5 e 15, e que sejam do Brasil ou da Argentina.

SELECT * 
FROM tb_jogadores 
WHERE jog_numero_camisa BETWEEN 5 AND 15 
AND jog_nacionalidade IN ('Brasil', 'Argentina');

# 6. Selecione todos os jogadores que jogam como "Meio-campo" ou "Zagueiro" e que tenham contrato registrado antes de 2024-01-01.

SELECT * 
FROM tb_jogadores 
WHERE jog_posicao IN ('Meio-campo', 'Zagueiro') 
AND jog_data_contrato < '2024-01-01';

# 7. Selecione todos os jogadores cujo nome comece com "J" e que sejam do Brasil e cuja posição não seja "Goleiro".

SELECT * 
FROM tb_jogadores 
WHERE jog_nome LIKE 'J%' 
AND jog_nacionalidade = 'Brasil' 
AND jog_posicao != 'Goleiro';

# 8. Selecione todos os jogadores que não sejam do Brasil, cuja posição seja "Atacante" e cujo número de camisa esteja entre 10 e 20.

SELECT * 
FROM tb_jogadores 
WHERE jog_nacionalidade != 'Brasil' 
AND jog_posicao = 'Atacante' 
AND jog_numero_camisa BETWEEN 10 AND 20;

# 9. Selecione todos os jogadores cujo número de camisa seja 11 ou 22, e cuja nacionalidade seja "Brasil" ou "Argentina".

SELECT * 
FROM tb_jogadores 
WHERE jog_numero_camisa IN (11, 22) 
AND jog_nacionalidade IN ('Brasil', 'Argentina');

# 10. Selecione todos os jogadores cujo nome termina com "o" e que sejam do Brasil ou da Argentina.

SELECT * 
FROM tb_jogadores 
WHERE jog_nome LIKE '%o' 
AND jog_nacionalidade IN ('Brasil', 'Argentina');

# 11. Selecione todos os jogadores cuja nacionalidade seja Brasil e que tenham "R" no nome, ordenando-os por número de camisa.

SELECT * 
FROM tb_jogadores 
WHERE jog_nacionalidade = 'Brasil' 
AND jog_nome LIKE '%R%' 
ORDER BY jog_numero_camisa;

# 12. Selecione todos os jogadores do Brasil ou da Argentina cujo nome comece com "A" e que joguem como "Goleiro".

SELECT * 
FROM tb_jogadores 
WHERE jog_nome LIKE 'A%' 
AND jog_nacionalidade IN ('Brasil', 'Argentina') 
AND jog_posicao = 'Goleiro';

# 13. Selecione todos os jogadores que não sejam zagueiros, cujo número de camisa esteja entre 5 e 15, e que tenham "S" no nome.

SELECT * 
FROM tb_jogadores 
WHERE jog_posicao != 'Zagueiro' 
AND jog_numero_camisa BETWEEN 5 AND 15 
AND jog_nome LIKE '%S%';

# 14. Selecione todos os jogadores cujo nome não contenha "R" e que sejam do Brasil ou Uruguai, e cuja posição seja "Meio-campo".

SELECT * 
FROM tb_jogadores 
WHERE jog_nome NOT LIKE '%R%' 
AND jog_nacionalidade IN ('Brasil', 'Uruguai') 
AND jog_posicao = 'Meio-campo';

# 15. Selecione todos os jogadores com um número de camisa entre 1 e 11, cuja nacionalidade seja brasileira ou argentina, mas que não tenham "a" no nome.

SELECT * 
FROM tb_jogadores 
WHERE jog_numero_camisa BETWEEN 1 AND 11 
AND jog_nacionalidade IN ('Brasil', 'Argentina') 
AND jog_nome NOT LIKE '%a%';

# 16. Selecione todos os jogadores que jogam como "Atacante" ou "Meio-campo", cujo nome termine com "o" e que não sejam do Brasil.

SELECT * 
FROM tb_jogadores 
WHERE jog_posicao IN ('Atacante', 'Meio-campo') 
AND jog_nome LIKE '%o' 
AND jog_nacionalidade != 'Brasil';

# 17. Selecione todos os jogadores que tenham um número de camisa entre 10 e 30, que tenham "e" no nome, ou que não sejam da Argentina ou do Uruguai.

SELECT * 
FROM tb_jogadores 
WHERE (jog_numero_camisa BETWEEN 10 AND 30 
AND jog_nome LIKE '%e%') 
OR jog_nacionalidade NOT IN ('Argentina', 'Uruguai');

# 18. Selecione todos os jogadores cuja data de nascimento esteja entre 1985 e 1995, que sejam do Brasil ou Uruguai, e cujo nome não contenha "s", ordenando os resultados pelo número de camisa em ordem crescente.

SELECT * 
FROM tb_jogadores 
WHERE jog_data_nascimento BETWEEN '1985-01-01' AND '1995-12-31' 
AND jog_nacionalidade IN ('Brasil', 'Uruguai') 
AND jog_nome NOT LIKE '%s%' 
ORDER BY jog_numero_camisa;

# 19. Selecione todos os jogadores que jogam como "Zagueiro" ou "Goleiro", cujo número de camisa esteja entre 1 e 20, e cujo nome não contenha a letra "i", ordenando-os por nacionalidade.

SELECT * 
FROM tb_jogadores 
WHERE jog_posicao IN ('Zagueiro', 'Goleiro') 
AND jog_numero_camisa BETWEEN 1 AND 20 
AND jog_nome NOT LIKE '%i%' 
ORDER BY jog_nacionalidade;
