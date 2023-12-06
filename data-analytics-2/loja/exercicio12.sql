-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com
-- menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser 
-- cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.

SELECT 
	dep.cddep,
	dep.nmdep,
	dep.dtnasc,
	SUM(qtd * vrunt) AS valor_total_vendas
FROM 
	tbdependente AS dep
	LEFT JOIN tbvendas AS  ven
		ON dep.cdvdd = ven.cdvdd 
WHERE status = 'Concluído'
GROUP BY ven.cdvdd
ORDER BY valor_total_vendas ASC
LIMIT 1