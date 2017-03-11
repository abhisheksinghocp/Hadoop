# only DataFrame program
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext   # need for dataframe
import csv
sc = SparkContext(appName="CSV_Read")
sqlContext = SQLContext(sc)

path = 'B:\hadoop_py\work\External_data\Telecom\Telecom_Performance-Monthly_jan_feb_2015.csv'  # reading files
lines = sc.textFile(path)  # system to implicit partition
rdd = lines.mapPartitions(lambda x: csv.reader(x))
# /*******lines = sc.textFile(path,4)  ## system explicit partition
#print(lines.take(5))  # print RDD Output
dataframe = sqlContext.createDataFrame(rdd, ['Parameter', 'Unit', 'Feb-15', 'Jan-15'])  # createDataFrame(rdd, ['name', 'age'])
# Type of DF selection
print(dataframe.take(2))
print(dataframe.select('*').take(2))
print(dataframe.select('Unit', 'Jan-15').take(2))
dataframe.select(dataframe.Parameter, 'Feb-15').show()  # show will give you table like output
