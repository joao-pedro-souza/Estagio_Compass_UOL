# Desafio - Parte III

## Processamento da Trusted

Meu objetivo neste desafio era juntar as informações que eu peguei do TMDB na Sprint 8, e junta-lás ao arquivo movies.csv da Sprint 7, 
para dar origem a arquivos *.parquet* na camada Trusted.

Comecei o desafio criando um job ETL no Glue com base no Spark

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/380a8f5b-8646-4147-8e4d-2a46a99e6efb)

Após isso, criei uma IAM Role para que o job Glue tivesse todas as permissões necessárias para a sua execução.

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/1122f99d-47ee-4075-9cba-3b02f9f61d3e)

Adicionei a política S3 FullAcess, para que o job pudesse ler os arquivos .csv e .json dentro do bucket S3, e para poder escrever os arquivos .parquet,
adicionei também a política CloudWatchFullAcess, para ter acesso detalhado aos logs de execução do job.

Com todas as configurações feitas, comecei a desenvolver meu código.

Criei um dataframe no Spark usando a função read.csv para fazer a leitura do arquivo movies.csv dentro do S3:

`df_movies = spark.read.csv('s3://data-lake-do-jp/Raw/Local/CSV/Movies/2023/05/25/movies.csv', header=True, inferSchema=True, sep='|')`

Após isso usei a função write.parquet para escrever os arquivos no formato parquet dentro da camada Trusted dentro do S3:

`df_movies.write.parquet('s3://data-lake-do-jp/Trusted/Local/Parquet/Movies/2023/05/25/')`

Repeti os processos de configuração e criei um novo job dentro do Glue: 

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/e44bc57d-1714-4985-bd5a-e25712860f4b)

Dessa vez para ler os arquivos JSON dentro do S3, usei a função read.json, passando o caminho da pasta e usando *.json, para que todos
os arquivos fossem lidos e transformados em um só dataframe.

`df_movies = spark.read.json('s3://data-lake-do-jp/Raw/Local/TMDB/JSON/2023/05/30/*.json')`

Mais uma vez usei a função write.parquet para salvar os arquivos na camada Trusted:

`df_movies.write.parquet('s3://data-lake-do-jp/Trusted/Local/Parquet/JSON/2023/05/30/')`

Executei os dois jobs com sucesso:

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/9bbd07d5-2bf3-4aa9-b357-a5642c8969d2)

E os arquivos parquet foram escritos dentro do S3:

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/5a59d51f-7baa-4740-be44-740cd52568a8)
![image](https://github.com/joaopedrocompass/Compass/assets/126081326/ee6c28a0-0f8f-4b75-96ca-f0273b7c3b14)

## Modelagem de Dados da Refined

Meu objetivo nessa tarefa era modelar os dados da Trusted e deixar tudo pronto para que os dados fossem inseridos na camada Refined.

O primeiro passo foi adicionar a permissão AWSGlueServiceRole, para permitir ao Glue escrever tabelas no Data Catalog

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/541ec16a-b92f-4f5f-a075-510fed2a6898)


Após isso criei dois *crawlers* (um para as informações do CSV e outro para os JSON) no Glue, para ler os arquivos parquet dentro da camada Trusted:

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/242231fe-d958-49f9-bfe5-e4a58637b7d0)

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/813d1513-549b-4802-9544-67819ed04d06)

Criei o *Banco de Dados* movies_db, onde as tabelas criadas pelo crawler seriam salvas.

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/d7d2a004-017d-4d31-9680-0a81ca84bd71)

Executei os dois crawlers com sucesso:

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/987bc002-eb57-4e9b-b60f-b254b632274c)

E duas tabelas foram criadas no movies_db:

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/56362461-0767-432c-a023-8b097d174348)

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/f61c22e1-fcc3-438a-bbe3-34b7e3449a12)

Com as tabelas prontas, pude começar a modelagem do Banco de Dados, para isso usei o Athena. Defini o seguinte modelo para o movies_db:

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/298db424-5c1d-4e7f-a504-439533a4ba76)

E comecei a desenvolver as queries:

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/30f5d91f-ba9a-4230-9f5e-a1f07eb64355)

Após a execução das queries fiquei com as seguintes tabelas no Data Catalog:

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/95cac31f-293a-427d-b499-fe471afff3a3)

## Processamento da Refined

Meu objetivo nesse desafio era processar as tabelas e salvar os dados na camada Refined

Com as tabelas criadas, criei um novo job Spark, que lê as tabelas (que ficam salvas no S3) e guarda as informações na Refined no formato Parquet
![image](https://github.com/joaopedrocompass/Compass/assets/126081326/d77e6606-41ec-42cd-b55d-2df6840200d2)
