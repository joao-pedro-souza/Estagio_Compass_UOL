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

# Lê os arquivos json
df_movies = spark.read.json('s3://data-lake-do-jp/Raw/Local/TMDB/JSON/2023/05/30/*.json')

# Escreve o arquivo parquet
df_movies.write.parquet('s3://data-lake-do-jp/Trusted/Local/Parquet/JSON/2023/05/30/')

job.commit()
