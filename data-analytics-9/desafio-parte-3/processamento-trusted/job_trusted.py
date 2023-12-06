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

# Lê o arquivo movies.csv
df_movies = spark.read.csv('s3://data-lake-do-jp/Raw/Local/CSV/Movies/2023/05/25/movies.csv', header=True, inferSchema=True, sep='|')

# Escreve o arquivo parquet
df_movies.write.parquet('s3://data-lake-do-jp/Trusted/Local/Parquet/Movies/2023/05/25/')

job.commit()
