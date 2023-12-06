CREATE TABLE idiomas AS
SELECT DISTINCT
    ROW_NUMBER() OVER (
		ORDER BY original_language 
	) AS id,
	original_language
FROM json30
GROUP BY original_language;

CREATE TABLE generos AS
SELECT DISTINCT
    ROW_NUMBER() OVER (
		ORDER BY genero 
	) AS id,
    genero
FROM csv25
WHERE genero LIKE 'Action,Adventure%'
GROUP BY genero;

CREATE TABLE filmes AS
SELECT DISTINCT
    csv.id,
    csv.titulopincipal AS tituloprincipal,
	csv.titulooriginal,
	csv.anolancamento,
	csv.tempominutos,
	ge.id AS genero,
	csv.notamedia,
	csv.numerovotos,
	idi.id AS idioma,
	json.budget AS orcamento,
	json.revenue AS receita
FROM csv25 AS csv
JOIN json30 AS json
ON csv.id = json.imdb_id
JOIN idiomas AS idi
ON json.original_language = idi.idioma
JOIN generos AS ge
ON csv.genero = ge.genero
WHERE csv.genero LIKE 'Action,Adventure%'

CREATE TABLE profissoes AS
SELECT DISTINCT
    ROW_NUMBER() OVER (
		ORDER BY profissao 
	) AS id,
	profissao
FROM csv25
GROUP BY profissao;

CREATE TABLE atores AS
SELECT 
    csv.generoartista,
    csv.personagem,
    csv.id AS filme,
    csv.nomeartista,
    csv.anonascimento,
    csv.anofalecimento,
    pr.id AS profissao,
    csv.titulosmaisconhecidos
FROM csv25 AS csv
JOIN profissoes AS pr
ON csv.profissao = pr.profissao
WHERE csv.genero LIKE 'Action,Adventure%'
