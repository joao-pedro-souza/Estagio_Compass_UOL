-- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem 
-- crescente.

SELECT DISTINCT au.nome
FROM
	autor AS au
	LEFT JOIN livro AS li
		ON au.codautor = li.autor
WHERE li.autor IS NULL 
ORDER BY nome ASC