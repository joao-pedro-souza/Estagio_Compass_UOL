# Modelagem de Dados
## Modelagem Relacional

Meu objetivo nesse exercício era fazer a modelagem dimensional, e normalizar o banco de dados concessionaria

Comecei o exercício exportando o arquivo concessionaria.sqlite para o DBeaver.


Após isso selecionei tudo da tabela tb_locacao, para enteder a estrutura do banco de dados, e obtive o seguinte resultado:

|idLocacao|idCliente|nomeCliente|cidadeCliente|estadoCliente|paisCliente|idCarro|kmCarro|classiCarro|marcaCarro|modeloCarro|anoCarro|idcombustivel|tipoCombustivel|dataLocacao|horaLocacao|qtdDiaria|vlrDiaria|dataEntrega|horaEntrega|idVendedor|nomeVendedor|sexoVendedor|estadoVendedor|
|---------|---------|-----------|-------------|-------------|-----------|-------|-------|-----------|----------|-----------|--------|-------------|---------------|-----------|-----------|---------|---------|-----------|-----------|----------|------------|------------|--------------|
|1|2|Cliente dois|São Paulo|São Paulo|Brasil|98|25412|AKJHKN98JY76539|Fiat|Fiat Uno|2000|1|Gasolina|20,150,110|10:00|2|100|20,150,112|10:00|5|Vendedor cinco|0|São Paulo|

Desenvolvi então um diagrama de como eu modelaria esse banco de dados, para depois só fazer a modelagem física com código SQLite

![modelagem_relacional](https://github.com/joaopedrocompass/Compass/assets/126081326/30b3a35a-8661-49aa-838d-c70035d4f733)

Comecei então a criar as tabelas:

CREATE TABLE combustiveis (
	idCombustivel INTEGER PRIMARY KEY,
	tipoCombustivel VARCHAR(255)
);

E popula-las com os dados da tabela tb_locacao, usando a função **INSERT INTO**:

```
INSERT INTO 
	combustiveis (idcombustivel, tipoCombustivel)
SELECT DISTINCT 
	idcombustivel, 
	tipoCombustivel
FROM tb_locacao;
```

Para fazer a relação entre as tabelas usei FOREIGN KEYS:

```
CREATE TABLE carros (
    idCarro INTEGER PRIMARY KEY,
    classiCarro VARCHAR(255),
    marcaCarro VARCHAR(255),
    modeloCarro VARCHAR(255),
    anoCarro INTEGER,
    idCombustivel INTEGER,
    FOREIGN KEY (idCombustivel) REFERENCES combustiveis (idCombustivel)
);
```

Algumas tabelas não tinham id, para isso usei a função ROW_NUMBER:

```
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
```

A função ROW_NUMBER não funciona bem com o DISTINCT, então precisei usar o GROUP BY para evitar repetições.

Assim ficaram as tabelas:

### carros
|idCarro|classiCarro|marcaCarro|modeloCarro|anoCarro|idCombustivel|
|-------|-----------|----------|-----------|--------|-------------|
|1|AAAKNS8JS76S39|Toyota|Corolla XEI|2023|3|

### cidades

|idEstado|estado|
|--------|------|
|1|Acre|

### clientes

|idCliente|nomeCliente|idCidade|
|---------|-----------|--------|
|2|Cliente dois|9|

### combustiveis

|idCombustivel|tipoCombustivel|
|-------------|---------------|
|1|Gasolina|

### estados

|idEstado|estado|
|--------|------|
|1|Acre|

### locacoes

|idLocacao|dataLocacao|horaLocacao|qtdDiaria|vlrDiaria|dataEntrega|horaEntrega|idCarro|kmCarro|idCliente|idVendedor|
|---------|-----------|-----------|---------|---------|-----------|-----------|-------|-------|---------|----------|
|1|20150110|10:00|2|100|20150112|10:00|98|25412|2|5|

### vendedores

|idVendedor|nomeVendedor|sexoVendedor|estadoVendedor|
|----------|------------|------------|--------------|
|5|Vendedor cinco|0|9|

## Modelagem Dimensional

Meu objetivo nesse exercício era fazer a modelagem dimensional, a partir do modelo relacional que fiz no exercício anterior. Comecei a desenvolver o diagrama para facilitar a modelagem física com código SQLite.

![modelagem_dimensional](https://github.com/joaopedrocompass/Compass/assets/126081326/e1c81651-06cb-4790-ac5e-c204011e3b8c)

Minha ideia foi ter uma tabela principal onde todas as tabelas se conectam a ela, além da criação de uma dimensão exlusiva para informações de data.

Comecei a desenvolver o código, para fazer a modelagem dimensional usei **VIEWS** no lugar DE **TABLES**

```
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
```

Como diminui o número de tabelas precisei fazer JOIN e pegar informações de várias tabelas em todas as VIEWS criadas.

Após a modelagem física, o resultado foi esse:

### dim_carros

|idCarro|placa|marca|modelo|combustivel|
|-------|-----|-----|------|-----------|
|1|AAAKNS8JS76S39|Toyota|Corolla XEI|Flex|

### dim_clientes

|idCliente|nome|cidade|estado|pais|
|---------|----|------|------|----|
|2|Cliente dois|São Paulo|9|Brasil|

### dim_data

|idData|dataLocacao|horaLocacao|dataEntrega|horaEntrega|kmCarro|
|------|-----------|-----------|-----------|-----------|-------|
|1|20150110|10:00|20150112|10:00|25412|

### dim_locacoes

|idLocacao|quantidade|valor|idData|idCarro|idCliente|idVendedor|
|---------|----------|-----|------|-------|---------|----------|
|1|2|100|1|98|2|5|

### dim_vendedores

|idVendedor|vendedor|sexo|estado|
|----------|--------|----|------|
|5|Vendedor cinco|0|São Paulo|
