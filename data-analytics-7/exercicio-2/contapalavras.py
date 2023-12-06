from pyspark.sql import SparkSession
from pyspark.sql.functions import split, size

spark = SparkSession.builder.appName("Contagem de Palavras").getOrCreate()

df = spark.read.text("README.md")

words = df.select(split(df.value, " ").alias("words"))

word_counts = words.select(size(words.words).alias("word_count"))

total_words = word_counts.groupBy().sum("word_count").collect()[0][0]

print("Total de palavras:", total_words)

spark.stop()
