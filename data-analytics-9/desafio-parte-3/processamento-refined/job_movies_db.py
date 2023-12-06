import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# processa a tabela atores
atores = glueContext.create_dynamic_frame_from_options(connection_type='s3', 
                                                        connection_options={"paths": ['s3://data-lake-do-jp/Athena/create_atores/2023/06/13/tables/581ff5c4-73a1-4cc2-95d7-3c2887f22999/']},
                                                        format='parquet')
atores = atores.toDF()
atores.write.parquet('s3://data-lake-do-jp/Refined/Local/movies_db/atores/')

# processa a tabela filmes
filmes = glueContext.create_dynamic_frame_from_options(connection_type='s3', 
                                                        connection_options={"paths": ['s3://data-lake-do-jp/Athena/create_filmes/2023/06/13/tables/6af5ccab-210c-4f23-a6f2-4c1f8afe8387/']},
                                                        format='parquet')
filmes = filmes.toDF()
filmes.write.parquet('s3://data-lake-do-jp/Refined/Local/movies_db/filmes/')

# processa a tabela generos
generos = glueContext.create_dynamic_frame_from_options(connection_type='s3', 
                                                        connection_options={"paths": ['s3://data-lake-do-jp/Athena/create_generos/2023/06/13/tables/db6fc9d2-e2ad-4d5b-94e4-27531f51def9/']},
                                                        format='parquet')
generos = generos.toDF()
generos.write.parquet('s3://data-lake-do-jp/Refined/Local/movies_db/generos/')

# processa a tabela idiomas
idiomas = glueContext.create_dynamic_frame_from_options(connection_type='s3', 
                                                        connection_options={"paths": ['s3://data-lake-do-jp/Athena/create_idiomas/2023/06/13/tables/f78503f5-7ea5-4f4c-8fc0-1b7e67893316/']},
                                                        format='parquet')
idiomas = idiomas.toDF()
idiomas.write.parquet('s3://data-lake-do-jp/Refined/Local/movies_db/idiomas/')

# processa a tabela profissoes
profissoes = glueContext.create_dynamic_frame_from_options(connection_type='s3', 
                                                        connection_options={"paths": ['s3://data-lake-do-jp/Athena/Unsaved/2023/06/13/tables/06b4b79e-48b7-4ab3-ae0d-61019dbb7a8d/']},
                                                        format='parquet')
profissoes = profissoes.toDF()
generos.write.parquet('s3://data-lake-do-jp/Refined/Local/movies_db/profissoes/')

job.commit()