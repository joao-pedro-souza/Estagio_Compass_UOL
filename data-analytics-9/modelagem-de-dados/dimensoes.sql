CREATE VIEW dim_carros AS
SELECT 
	ca.idCarro,
	ca.classiCarro AS placa,
	ca.marcaCarro AS marca,
	ca.modeloCarro AS modelo,
	co.tipoCombustivel AS combustivel
FROM carros AS ca
JOIN combustiveis AS co
ON ca.idCombustivel = co.idCombustivel;

CREATE VIEW dim_clientes AS
SELECT 
	cl.idCliente,
	cl.nomeCliente AS nome,
	ci.cidade, 
	ci.idEstado AS estado,
	ci.pais
FROM clientes AS cl
JOIN cidades AS ci
ON cl.idCidade = ci.idCidade;

CREATE VIEW dim_vendedores AS
SELECT 
	ve.idVendedor,
	ve.nomeVendedor AS vendedor,
	ve.sexoVendedor AS sexo,
	es.estado
FROM vendedores AS ve
JOIN estados AS es
ON ve.estadoVendedor = es.idEstado;

CREATE VIEW dim_data AS
SELECT 
	ROW_NUMBER() OVER (ORDER BY dataLocacao) AS idData,
	dataLocacao,
	horaLocacao,
	dataEntrega,
	horaEntrega,
	kmCarro
FROM locacoes;

CREATE VIEW dim_locacoes AS
SELECT 
	lo.idLocacao,
	lo.qtdDiaria AS quantidade,
	lo.vlrDiaria AS valor,
	da.idData,
	lo.idCarro,
	lo.idCliente,
	lo.idVendedor
FROM locacoes AS lo
JOIN dim_data AS da
ON lo.idLocacao = da.idData;
