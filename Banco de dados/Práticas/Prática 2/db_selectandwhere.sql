# 1. Selecione todos os resultados de atletas do Brasil.

SELECT * 
FROM atletismo_resultados
WHERE pais = 'Brasil';

# 2. Encontre os resultados dos eventos ocorridos após 2016.

SELECT * 
FROM atletismo_resultados
WHERE ano > 2016;

# 3. Busque os resultados onde o atleta tem o gênero 'F' e a prova é '100 metros rasos'.

SELECT *
FROM atletismo_resultados
WHERE modalidade = 'Feminino' 
AND prova = '100 metros rasos';

# 4. Encontre os resultados onde o atleta tem o gênero 'M' ou a prova é 'Maratona'.

SELECT * 
FROM atletismo_resultados
WHERE modalidade = 'Masculino' 
OR prova = 'Maratona';

# 5. Liste os resultados onde a posição é menor que 4 e a prova é 'Maratona' ou '100 metros rasos'.

SELECT * 
FROM atletismo_resultados
WHERE (posicao < 4 AND (prova = 'Maratona' OR prova = '100 metros rasos'));

# 6. Encontre os resultados dos eventos ocorridos em 2020 e onde o país do atleta é 'Jamaica' ou 'Canadá'.

SELECT * 
FROM atletismo_resultados
WHERE ano = 2020 
AND (pais = 'Jamaica' or pais = 'Canadá');

# 7. Encontre os resultados onde o tempo é menor que 10 segundos e a prova é '100 metros rasos'.

SELECT * 
FROM atletismo_resultados
WHERE tempo < '00:10:00' 
AND prova = '100 metros rasos';

# 8. Liste os resultados de atletas do país 'França' que competiram em 2020 e cuja posição é menor que 8.

SELECT * 
FROM atletismo_resultados
WHERE ano = 2020 
AND pais = 'França' 
AND posicao < 8;

# 9. Busque todos os resultados onde o atleta tem o gênero 'Feminino' ou a prova é 'Revezamento 4x100 metros', e a posição é menor que 4.

SELECT * 
FROM atletismo_resultados
WHERE (modalidade = 'Feminino' OR prova = 'Revezamento 4x100 metros') 
AND posicao < 4;

# 10. Encontre os resultados onde o país do atleta é diferente de 'China' ou 'Brasil', e a posição é entre 1 e 3.

SELECT * 
FROM atletismo_resultados
WHERE (pais != 'China' OR pais != 'Brasil') 
AND (posicao > 1 AND posicao < 3);

# 11. Selecione todos os resultados onde o atleta é 'Nadine Debois' ou 'Usain Bolt', que competiram em eventos diferentes de '200 metros rasos' e 'Revezamento 4x100 metros'.

SELECT * 
FROM atletismo_resultados
WHERE (atleta_nome = 'Nadine Debois' OR atleta_nome = 'Usain Bolt')
AND (prova != '200 metros rasos' AND prova != 'Revezamento 4x100 metros');

# 12. Liste todos os resultados onde a prova é 'Decatlo' e o atleta tem o gênero 'Masculino', e a posição é menor que 8.

SELECT * 
FROM atletismo_resultados
WHERE prova = 'Decatlo' 
AND modalidade = 'Masculino' 
AND posicao < 8;

# 13. Encontre resultados de atletas com o tempo menor que 10 segundos na prova '100 metros rasos', que competiram em 2020.

SELECT * 
FROM atletismo_resultados
WHERE ano = 2020 
AND prova = '100 metros rasos' 
AND tempo < '00:10:00';

# 14. Busque os resultados onde o atleta é 'Elaine Thompson' ou 'Shelly-Ann Fraser-Pryce', que competiram em provas diferentes de '100 metros rasos' e '200 metros rasos', e a posição é menor que 5.

SELECT * 
FROM atletismo_resultados
WHERE (atleta_nome = 'Elaine Thompson' OR atleta_nome = 'Shelly-Ann Fraser-Pryce')
AND (prova != '100 metros rasos' AND prova != '200 metros rasos') 
AND posicao < 5;
