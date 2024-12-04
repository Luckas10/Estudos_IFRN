-- Qual é o total gasto por cada cliente em todas as suas compras?
SELECT cli_nome, SUM(ven_total) AS total_gasto
FROM tb_vendas
JOIN tb_clientes ON ven_cli_id = cli_id
GROUP BY cli_nome;

-- Quais produtos foram vendidos em mais de uma venda e quantas vezes cada um foi vendido?
SELECT pro_nome, COUNT(vpr_id) AS qtd_vendas
FROM tb_vendas_produtos
JOIN tb_produtos ON vpr_pro_id = pro_id
GROUP BY pro_nome
HAVING COUNT(vpr_id) > 1;

-- Qual é a média de quantidade vendida por produto para cada categoria?
SELECT cat_nome, pro_nome, AVG(vpr_quantProduto) AS media_quant_vendida
FROM tb_vendas_produtos
JOIN tb_produtos ON vpr_pro_id = pro_id
JOIN tb_categorias ON pro_categoria_id = cat_id
GROUP BY cat_nome, pro_nome;

-- Quais clientes realizaram mais de uma compra?
SELECT cli_nome, COUNT(ven_id) AS num_compras
FROM tb_vendas
JOIN tb_clientes ON ven_cli_id = cli_id
GROUP BY cli_nome
HAVING COUNT(ven_id) > 1;

-- Qual é a média de preço dos produtos vendidos em cada categoria?
SELECT cat_nome, AVG(vvpr_precoProduto) AS media_preco
FROM tb_vendas_produtos
JOIN tb_produtos ON vpr_pro_id = pro_id
JOIN tb_categorias ON pro_categoria_id = cat_id
GROUP BY cat_nome;

-- Quais categorias tiveram um total de vendas superior a um valor específico? (Exemplo: 10000)
SELECT cat_nome, SUM(vvpr_quantProduto * vpr_precoProduto) AS total_vendas
FROM tb_vendas_produtos
JOIN tb_produtos ON vpr_pro_id = pro_id
JOIN tb_categorias ON pro_categoria_id = cat_id
GROUP BY cat_nome
HAVING SUM(vpr_quantProduto * vpr_precoProduto) > 10000;

-- Qual é a data e o valor da compra mais cara de cada cliente?
SELECT ven_cli_id, MAX(ven_total) AS maior_valor, ven_data
FROM tb_vendas
GROUP BY ven_cli_id;

-- Quais produtos têm uma quantidade total vendida superior a um valor específico? (Exemplo: 100)
SELECT pro_nome, SUM(vpr_quantProduto) AS total_vendido
FROM tb_vendas_produtos
JOIN tb_produtos ON vpr_pro_id = pro_id
GROUP BY pro_nome
HAVING SUM(vpr_quantProduto) > 100;

-- Qual foi a média de valor gasto em cada mês?
SELECT EXTRACT(YEAR_MONTH FROM ven_data) AS mes, AVG(ven_total) AS media_valor
FROM tb_vendas
GROUP BY EXTRACT(YEAR_MONTH FROM ven_data);

-- Quais clientes compraram produtos de categorias diferentes em suas compras?
SELECT DISTINCT cli_nome
FROM tb_vendas
JOIN tb_clientes ON ven_cli_id = cli_id
JOIN tb_vendas_produtos ON ven_id = vpr_ven_id
JOIN tb_produtos ON vpr_pro_id = pro_id
JOIN tb_categorias ON pro_categoria_id = cat_id
GROUP BY cli_nome
HAVING COUNT(DISTINCT cat_nome) > 1;

-- -------------------------------------------------------------

-- Qual é o nome do cliente que realizou a compra mais cara?
SELECT cli_nome
FROM tb_vendas
JOIN tb_clientes ON ven_cli_id = cli_id
WHERE ven_total = (SELECT MAX(ven_total) FROM tb_vendas);

-- Quais produtos nunca foram vendidos?
SELECT pro_nome
FROM tb_produtos
LEFT JOIN tb_vendas_produtos ON pro_id = vpr_pro_id
WHERE vpr_pro_id IS NULL;

-- Quais clientes nunca realizaram uma compra?
SELECT cli_nome
FROM tb_clientes
LEFT JOIN tb_vendas ON cli_id = ven_cli_id
WHERE ven_cli_id IS NULL;

-- Qual é o nome e o e-mail do cliente que mais gastou em todas as suas compras?
SELECT cli_nome, cli_email
FROM tb_vendas
JOIN tb_clientes ON ven_cli_id = cli_id
GROUP BY cli_nome, cli_email
ORDER BY SUM(ven_total) DESC
LIMIT 1;

-- Quais produtos foram vendidos pelo menor preço em relação ao seu preço original?
SELECT pro_nome, MIN(vpr_precoProduto) AS preco_vendido
FROM tb_vendas_produtos
JOIN tb_produtos ON vpr_pro_id = pro_id
GROUP BY pro_nome
HAVING MIN(vpr_precoProduto) < pro_preco;

-- Qual é o segundo maior valor total de uma venda?
SELECT MAX(ven_total) AS segundo_maior_valor
FROM tb_vendas
WHERE ven_total < (SELECT MAX(ven_total) FROM tb_vendas);

-- Quais são os nomes dos clientes que compraram apenas uma vez?
SELECT cli_nome
FROM tb_vendas
JOIN tb_clientes ON ven_cli_id = cli_id
GROUP BY cli_nome
HAVING COUNT(ven_id) = 1;

-- Quais categorias de produtos nunca foram vendidas?
SELECT cat_nome
FROM tb_categorias
LEFT JOIN tb_produtos ON cat_id = pro_categoria_id
LEFT JOIN tb_vendas_produtos ON pro_id = vpr_pro_id
WHERE vpr_pro_id IS NULL;

-- Qual foi o mês com o maior valor total de vendas em todo o histórico?
SELECT EXTRACT(YEAR_MONTH FROM ven_data) AS mes, SUM(ven_total) AS total_vendas
FROM tb_vendas
GROUP BY EXTRACT(YEAR_MONTH FROM ven_data)
ORDER BY total_vendas DESC
LIMIT 1;

-- Quais clientes compraram o produto mais caro vendido na loja?
SELECT cli_nome
FROM tb_vendas
JOIN tb_clientes ON ven_cli_id = cli_id
JOIN tb_vendas_produtos ON ven_id = vpr_ven_id
JOIN tb_produtos ON vpr_pro_id = pro_id
WHERE vpr_precoProduto = (SELECT MAX(vpr_precoProduto) FROM tb_vendas_produtos)
GROUP BY cli_nome;
