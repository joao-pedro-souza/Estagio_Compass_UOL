CREATE TABLE combustiveis (
	idCombustivel INTEGER PRIMARY KEY,
	tipoCombustivel VARCHAR(255)
);

INSERT INTO 
	combustiveis (idcombustivel, tipoCombustivel)
SELECT DISTINCT 
	idcombustivel, 
	tipoCombustivel
FROM tb_locacao;

CREATE TABLE carros (
    idCarro INTEGER PRIMARY KEY,
    classiCarro VARCHAR(255),
    marcaCarro VARCHAR(255),
    modeloCarro VARCHAR(255),
    anoCarro INTEGER,
    idCombustivel INTEGER,
    FOREIGN KEY (idCombustivel) REFERENCES combustiveis (idCombustivel)
);

INSERT INTO 
	carros (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel)
SELECT DISTINCT 
	idCarro, 
	classiCarro, 
	marcaCarro,
	modeloCarro,
	anoCarro,
	idCombustivel
FROM tb_locacao; 

CREATE TABLE estados (
	idEstado INTEGER PRIMARY KEY,
	estado VARCHAR(255)
);

INSERT INTO 
	estados (idEstado, estado)
SELECT DISTINCT 
	ROW_NUMBER() OVER (ORDER BY estadoCliente),
	estadoCliente
FROM tb_locacao
GROUP BY estadoCliente; 

CREATE TABLE cidades (
	idCidade INTEGER PRIMARY KEY,
	cidade VARCHAR(255),
	idEstado INTEGER,
	pais VARCHAR(255),
	FOREIGN KEY (idEstado) REFERENCES estados (idEstado)
);

INSERT INTO 
	cidades (idCidade, cidade, idEstado, pais)
SELECT DISTINCT 
	ROW_NUMBER() OVER (ORDER BY cidadeCliente),
	tl.cidadeCliente,
	es.idEstado,
	tl.paisCliente
FROM tb_locacao AS tl
JOIN estados AS es 
ON es.estado = tl.estadoCliente
GROUP BY tl.cidadeCliente;

CREATE TABLE clientes (
	idCliente INTEGER PRIMARY KEY,
	nomeCliente VARCHAR(255),
	idCidade INTEGER,
	FOREIGN KEY (idCidade) REFERENCES cidades (idCidade)
);

INSERT INTO 
	clientes (idCliente, nomeCliente, idCidade)
SELECT DISTINCT 
	tl.idCliente,
	tl.nomeCliente,
	ci.idCidade
FROM tb_locacao AS tl
JOIN cidades AS ci
ON tl.cidadeCliente = ci.cidade;

CREATE TABLE vendedores (
	idVendedor INTEGER PRIMARY KEY,
	nomeVendedor VARCHAR(255),
	sexoVendedor VARCHAR(255),
	estadoVendedor INTEGER,
	FOREIGN KEY (estadoVendedor) REFERENCES estados (idEstado)
);

INSERT INTO 
	vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT 
	tl.idVendedor,
	tl.nomeVendedor,
	tl.sexoVendedor,
	es.idEstado
FROM tb_locacao AS tl
JOIN estados AS es
ON tl.estadoVendedor = es.estado;
	
CREATE TABLE locacoes (
	idLocacao INTEGER PRIMARY KEY,
	dataLocacao VARCHAR(255),
	horaLocacao VARCHAR(255),
	qtdDiaria INTEGER,
	vlrDiaria INTEGER,
	dataEntrega VARCHAR(255),
	horaEntrega VARCHAR(255),
	idCarro INTEGER,
	kmCarro INTEGER,
	idCliente INTEGER,
	idVendedor INTEGER,
	FOREIGN KEY (idCarro) REFERENCES carros (idCarro),
	FOREIGN KEY (idCliente) REFERENCES clientes (idCliente),
	FOREIGN KEY (idVendedor) REFERENCES vendedores (idVendedor)
);

INSERT INTO 
	locacoes (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCarro, kmCarro, idCliente, idVendedor)
SELECT
	idLocacao,
	dataLocacao,
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	dataEntrega,
	horaEntrega,
	idCarro,
	kmCarro,
	idCliente,
	idVendedor
FROM tb_locacao;
