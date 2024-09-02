use db_inst;

# 1. Liste o nome do aluno, o nome da disciplina e a nota, de todos os alunos matriculados.

SELECT alu_nome, dis_nome, not_valor
FROM tb_matriculas
JOIN tb_alunos ON mat_alu_id = alu_id
JOIN tb_disciplinas ON mat_dis_id = dis_id
JOIN tb_notas ON mat_id = not_mat_id;

# 2. Mostre a quantidade de alunos com nota superior a 5;

SELECT COUNT(DISTINCT alu_id)
FROM tb_matriculas
JOIN tb_notas ON mat_id = not_mat_id
JOIN tb_alunos ON mat_alu_id = alu_id
WHERE not_valor > 5;

# 3. Liste o nome do aluno, o nome da disciplina e a nota, de todos os alunos com nota superior a 7 e matriculados em alguma das disciplinas  (Algoritmos e Estruturas de Dados, Computação em Nuvem e Banco de Dados);

SELECT alu_nome, dis_nome, not_valor
FROM tb_matriculas
JOIN tb_alunos ON mat_alu_id = alu_id
JOIN tb_disciplinas ON mat_dis_id = dis_id
JOIN tb_notas ON mat_id = not_mat_id
WHERE not_valor > 7
AND dis_nome 
IN ('Algoritmos e Estruturas de Dados', 'Computação em Nuvem', 'Banco de Dados');

# 4. Liste o nome do curso, nome do aluno, o nome da disciplina e a nota  de todos os alunos do curso Ciência da Computação ou Engenharia de Software, que estão com notas entre 4 e 8;

SELECT cur_nome, alu_nome, dis_nome, not_valor
FROM tb_matriculas
JOIN tb_alunos ON mat_alu_id = alu_id
JOIN tb_disciplinas ON mat_dis_id = dis_id
JOIN tb_notas ON mat_id = not_mat_id
JOIN tb_cursos ON alu_cur_id = cur_id
WHERE cur_nome IN ('Ciência da Computação', 'Engenharia de Software')
AND not_valor BETWEEN 4 AND 8;


# 5. Liste  o nome do professor, nome do curso, nome do aluno, o nome da disciplina e a nota de todos os alunos do Redes de Computadores ou Análise e Desenvolvimento de Sistemas, que começam com a letra (E ou C ou D ou G), e que estão com notas entre 3 e 9;

SELECT pro_nome, cur_nome, alu_nome, dis_nome, not_valor
FROM tb_matriculas
JOIN tb_alunos ON mat_alu_id = alu_id
JOIN tb_disciplinas ON mat_dis_id = dis_id
JOIN tb_notas ON mat_id = not_mat_id
JOIN tb_cursos ON dis_cur_id = cur_id
JOIN tb_professores ON dis_pro_id = pro_id
WHERE cur_nome IN ('Redes de Computadores', 'Análise e Desenvolvimento de Sistemas')
AND (alu_nome LIKE 'E%' OR alu_nome LIKE 'C%' OR alu_nome LIKE 'D%' OR alu_nome LIKE 'G%')
AND not_valor BETWEEN 3 AND 9;
