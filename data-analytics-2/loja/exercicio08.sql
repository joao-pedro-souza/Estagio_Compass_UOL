-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas 
-- (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado
-- devem ser, portanto, cdvdd e nmvdd.

SELECT DISTINCT 
	vendedor.cdvdd,
	vendedor.nmvdd
FROM
	tbvendedor AS vendedor
	LEFT JOIN tbvendas AS venda
		ON vendedor.cdvdd = venda.cdvdd
WHERE venda.status = 'Concluído'
GROUP BY venda.vrunt
ORDER BY venda.vrunt DESC
LIMIT 1