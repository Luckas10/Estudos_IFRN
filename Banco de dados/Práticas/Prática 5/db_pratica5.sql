use db_estoque;

# 1. Atualize o status para 'indisponível' e aumente o preço em 15% para produtos da categoria 'Cereais' ou 'bebidas' que têm pro_quantidade_estoque menor que 100 e pro_preco menor que 15.00.

UPDATE tb_produtos
SET pro_status = 'indisponível',
pro_preco = pro_preco * 1.15
WHERE pro_categoria IN ('Cereais', 'bebidas')
AND pro_quantidade_estoque < 100
AND pro_preco < 15.00;

# 2. Exclua todos os produtos com data de validade vencida e cujo preço é maior que 50.00 da tabela tb_produtos.

DELETE FROM tb_produtos
WHERE pro_data_validade < CURDATE()
AND pro_preco > 50.00;

# 3. Aumente a quantidade em estoque em 50 unidades e defina a marca como 'Novo Produto' para produtos da categoria 'Produtos de Limpeza' que foram cadastrados há mais de 6 meses e cujo pro_preco é menor que 10.00.

UPDATE tb_produtos
SET pro_quantidade_estoque = pro_quantidade_estoque + 50,
pro_marca = 'Novo Produto'
WHERE pro_categoria = 'Limpeza'
AND pro_data_cadastro < CURDATE() - INTERVAL 6 MONTH
AND pro_preco < 10.00;

# 4. Reduza o valor em 15 % de todos os produtos da categoria 'Chocolates' que têm pro_quantidade_estoque menor que 100 e foram cadastrados há mais de três meses e quinze dias.

UPDATE tb_produtos
SET pro_preco = pro_preco * 0.85
WHERE pro_categoria = 'Chocolates'
AND pro_quantidade_estoque < 100
AND pro_data_cadastro < curdate() - INTERVAL 3 MONTH - INTERVAL 15 DAY;

# 5. Aumente o preço em 20% e defina a data de validade como 3 meses a partir da data atual para produtos da categoria 'Alimentos' que têm pro_quantidade_estoque maior que 50 e pro_data_validade menor que a data atual.

UPDATE tb_produtos
SET pro_preco = pro_preco * 1.20,
pro_data_validade = CURDATE() + INTERVAL 3 MONTH
WHERE pro_categoria = 'Alimentos'
AND pro_quantidade_estoque > 50
AND pro_data_validade < CURDATE();

# 6. Exclua todos os produtos da categoria 'Produtos de Limpeza' que têm validade vencida, peso menor que 1kg e seja da marca Omo ou Ariel.

DELETE FROM tb_produtos
WHERE pro_categoria = 'Limpeza'
AND pro_data_validade < CURDATE()
AND pro_peso < 1
AND pro_marca IN ('Omo', 'Ariel');

# 7. Atualize a descrição para 'Promoção Especial' e defina o status como 'disponível' para produtos com quantidade entre 50 e 100 e preço maior que 20.00.

UPDATE tb_produtos
SET pro_descricao = 'Promoção Especial',
pro_status = 'disponível'
WHERE pro_quantidade_estoque BETWEEN 50 AND 100
AND pro_preco > 20.00;

# 8. Exclua todos os produtos da categoria 'Bebidas' ou 'Papelaria' cujo cadastro foi feito há mais de três meses e o preço menor que 2.00.

DELETE FROM tb_produtos
WHERE pro_categoria IN ('Bebidas', 'Papelaria')
AND pro_data_cadastro < CURDATE() - INTERVAL 3 MONTH
AND pro_preco < 2.00;

# 9. Defina a marca como 'Super Marca' e aumente o peso em 0.5 kg para produtos da categoria 'Utensílios Domésticos' que têm o preço maior que 50.00 e o peso menor que 2.00 kg.

UPDATE tb_produtos
SET pro_marca = 'Super Marca',
pro_peso = pro_peso + 0.5
WHERE pro_categoria = 'Utensílios Domésticos'
AND pro_preco > 50.00
AND pro_peso < 2.00;

# 10. Exclua todos os produtos que têm preço menor que 2.00 e quantidade em estoque maior que 200.

DELETE FROM tb_produtos
WHERE pro_preco < 2.00
AND pro_quantidade_estoque > 200;

# 11. Aumente o preço dos produtos da categoria 'Chocolates' em 25% onde validade é maior que a data atual e quantidade em estoque é maior que 50.

UPDATE tb_produtos
SET pro_preco = pro_preco * 1.25
WHERE pro_categoria = 'Chocolates'
AND pro_data_validade > CURDATE()
AND pro_quantidade_estoque > 50;

# 12. Exclua todos os produtos que têm peso maior que 5.00 kg e preço maior que 10.00.

DELETE FROM tb_produtos
WHERE pro_peso > 5.00
AND pro_preco > 10.00;