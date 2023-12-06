from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, when, expr, col

spark = SparkSession \
                .builder \
                .master("local[*]")\
                .appName("Exercicio Intro") \
                .getOrCreate()

# Nesta etapa, adicione código para ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv. Carregue-o para dentro de um dataframe chamado df_nomes e, por fim, liste algumas linhas através do método show. Exemplo: df_nomes.show(5)

df_nomes = spark.read.csv('nomes_aleatorios.txt')
df_nomes.show(5)

# Nesta etapa, será necessário adicionar código para renomear a coluna para Nomes, imprimir o esquema e mostrar 10 linhas do dataframe.

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')
df_nomes.printSchema()
df_nomes.show(10)

# Ao dataframe (df_nomes), adicione nova coluna chamada Escolaridade e atribua para cada linha um dos três valores de forma aleatória: Fundamental, Medio ou Superior.

df_nomes = df_nomes.withColumn('Escolaridade', when(rand() < 1/3, 'Fundamental').when(rand() < 2/3, 'Medio').otherwise('Superior'))

# Ao dataframe (df_nomes), adicione nova coluna chamada Pais e atribua para cada linha o nome de um dos 13 países da América do Sul, de forma aleatória.

df_nomes = df_nomes.withColumn('Pais', when(rand() < 1/13, 'Argentina')
                                               .when(rand() < 2/13, 'Bolívia')
                                               .when(rand() < 3/13, 'Brasil')
                                               .when(rand() < 4/13, 'Chile')
                                               .when(rand() < 5/13, 'Colômbia')
                                               .when(rand() < 6/13, 'Equador')
                                               .when(rand() < 7/13, 'Guiana')
                                               .when(rand() < 8/13, 'Guiana Francesa')
                                               .when(rand() < 9/13, 'Paraguai')
                                               .when(rand() < 10/13, 'Peru')
                                               .when(rand() < 11/13, 'Suriname')
                                               .when(rand() < 12/13, 'Uruguai')
                                               .otherwise('Venezuela'))

# Ao dataframe (df_nomes), adicione nova coluna chamada AnoNascimento e atribua para cada linha um valor de ano entre 1945 e 2010, de forma aleatória.

df_nomes = df_nomes.withColumn('AnoNascimento', expr('cast(round(rand() * (2010 - 1945) + 1945) as int)'))

# Usando o método select do dataframe (df_nomes), selecione as pessoas que nasceram neste século. Armazene o resultado em outro dataframe chamado df_select e mostre 10 nomes deste.

df_select = df_nomes.select('Nomes', 'AnoNascimento').filter(col('AnoNascimento') >= 2001)
df_select.show(10)

# Usando Spark SQL repita o processo da Pergunta 6. Lembre-se que, para trabalharmos com SparkSQL, precisamos registrar uma tabela temporária e depois executar o comando SQL.

df_nomes.createOrReplaceTempView("pessoas")
spark.sql("SELECT Nomes, AnoNascimento FROM pessoas WHERE AnoNascimento >= 2001").show()

# Usando o método select do Dataframe df_nomes, Conte o número de pessoas que são da geração Millennials (nascidos entre 1980 e 1994) no Dataset

print(df_nomes.filter(col('AnoNascimento').between(1980, 1994)).count())

# Repita o processo da Pergunta 8 utilizando Spark SQL

spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").show()

# Usando Spark SQL, obtenha a quantidade de pessoas de cada país para uma das gerações abaixo. Armazene o resultado em um novo dataframe e depois mostre todas as linhas em ordem crescente de Pais, Geração e Quantidade

df_geracoes = spark.sql("""
SELECT Pais, 
       CASE 
           WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
           WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geracao X'
           WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
           WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geracao Z'
       END AS Geracao,
       COUNT(*) AS Quantidade
FROM pessoas
GROUP BY Pais, Geracao
ORDER BY Pais, Geracao, Quantidade
""")
df_geracoes.show(52)
