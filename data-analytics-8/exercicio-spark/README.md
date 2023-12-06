Meu objetivo nessa tarefa era ler o arquivo nomesaleatorios.txt, gerado na tarefa anterior, que contém 10 milhões de nomes_aleatorios.txt, 
e usar ele para criar um dataframe no PySpark

Comecei o desafio de Spark importando as biliotecas necessárias

```
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, when, expr, col
```

E iniciando a SparkSession

```
spark = SparkSession \
                .builder \
                .master("local[*]")\
                .appName("Exercicio Intro") \
                .getOrCreate()
```

Então eu li o arquivo txt e o transformei num dataframe, também exibi as 5 primeiras linhas:

```
df_nomes = spark.read.csv('nomes_aleatorios.txt')
df_nomes.show(5)
```
![image](https://github.com/joaopedrocompass/Compass/assets/126081326/ff1f418a-6f3d-40ad-bd72-ec832df18cd0)

Mudei o nome da coluna para nomes, exibi o schema e mosrei as 10 primeiras linhas

```
df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')
df_nomes.printSchema()
df_nomes.show(10)
```

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/776f3c76-999d-4789-8569-bbd88fc2657b)

Então, usando as funções rand e when, adicionei uma nova coluna chamada escolaridade, que gera um entre três escolaridades diferentes para cada um dos nomes:

`df_nomes = df_nomes.withColumn('Escolaridade', when(rand() < 1/3, 'Fundamental').when(rand() < 2/3, 'Medio').otherwise('Superior'))`

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/5fc2472a-e00f-4cc9-a484-7ed41650f38a)

Usando novamente as funções rand e when, adicionei uma outra coluna chamada Pais, que recebe aleatoriamente um dos treze países da América do SUL

```
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
```

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/3da4d170-5e86-4123-a13a-42749a11ddde)

Usando a função expr, criei uma expressão que converte a função rand para um ano entre 1945 e 2010
`df_nomes = df_nomes.withColumn('AnoNascimento', expr('cast(round(rand() * (2010 - 1945) + 1945) as int)'))`

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/f98933b7-0bb5-45ce-9c0d-d88265189721)

A partir do df_nomes, criei um novo dataframe chamado df_select, que seleciona apenas as colunas Nomes e AnoNascimento pessoas nascidas nesse século (depois de 2001)

`df_select = df_nomes.select('Nomes', 'AnoNascimento').filter(col('AnoNascimento') >= 2001)`

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/d370d13d-ee8c-4edc-94a1-9226b0296183)

Usando o Spark SQL repeti o mesmo processo.

```
df_nomes.createOrReplaceTempView("pessoas")
spark.sql("SELECT Nomes, AnoNascimento FROM pessoas WHERE AnoNascimento >= 2001").show()
```

Usando o método select, contei a quantidade de pessoas da geração Millenials (nascidos entre 1980 e 1994)

`print(df_nomes.filter(col('AnoNascimento').between(1980, 1994)).count())`

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/5596fd9e-fc95-43b6-a82f-bfcdf05eeccf)

Fiz o mesmo processo, agora usando Spark SQL

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/63772b0f-f073-490d-b15f-4e43e0bc5ae1)

Por último, criei um dataframe chamado df_geracoes, que contava a quantidade de pessoas de cada geração, separados por países, para isso usei Spark SQL:

```
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
```

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/869af05a-205f-4dfd-8d33-19fa83b2fc96)
