from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
sc = SparkContext(appName="parquet_Read")
sqlContext = SQLContext(sc)

path = 'B:\hadoop_py\work\csv_to_parq\*'  # reading files
parq = sqlContext.read.parquet(path)  # system to implicit partition
parq.printSchema()
# without Print you can't see the output
# print(parq.select('*').collect()) or  print(parq.select('*').count())
#           or
print('File/Dir which was read', path)
print('\nTotal Record count', parq.count())
print('\nTotal unique Records count', parq.drop_duplicates().count())
print('\nsample output\n')
parq.select('*').show()
# you can use this command to save output but for next run you need to delete give output folder location
# otherwise system will give error "location is already exits"
# parq.write.parquet(path="B:\hadoop_py\work\est")
#                           or
# you can use this command to save output and from next run it will overwrite same location with new output"
parq.write.format('csv').mode('overwrite').save("B:\hadoop_py\work\parq_to_txt")