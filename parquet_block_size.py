from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
conf = (SparkConf().setMaster("local"))
sc = SparkContext(appName="parquet_block_size", conf=conf)
sqlContext = SQLContext(sc)
sc._jsc.hadoopConfiguration().set("dfs.block.size", "128m")
# txt = sc.parallelize(("Hello", "world", "!"))
# txt.saveAsTextFile("B:\hadoop_py\work\output")  # saving output with 128MB block size

path = 'B:\hadoop_py\work\parquet\*'  # reading files
parq = sqlContext.read.parquet(path)  # system to implicit partition
parq.printSchema()
print('\nTotal Record count', parq.count())
parq.write.format('parquet').mode('overwrite').save("B:\hadoop_py\work\parq_to_parq_128")
parq.write.format('csv').mode('overwrite').save("B:\hadoop_py\work\parq_to_csv_128")  # saving output with 128MB block size