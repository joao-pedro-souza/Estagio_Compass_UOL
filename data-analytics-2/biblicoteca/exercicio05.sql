-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO 
-- situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não 
-- podem haver nomes repetidos em seu retorno.

SELECT DISTINCT au.nome
FROM 
	autor AS au
	LEFT JOIN livro AS li
		ON au.codautor = li.autor 
WHERE editora != 13
ORDER BY nome ASC