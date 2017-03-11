# only Aggregation  program
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext   # need for dataframe
import csv
sc = SparkContext(appName="CSV_Read")    # this is IMP
sqlContext = SQLContext(sc)              # This is IMP

path = 'B:\hadoop_py\work\External_data\Telecom\Telecom_Performance-Monthly_jan_feb_2015.csv'  # reading files
lines = sc.textFile(path)  # system to implicit partition
rdd = lines.mapPartitions(lambda x: csv.reader(x))
dataframe = sqlContext.createDataFrame(rdd, ['Parameter', 'Unit', 'Feb-15', 'Jan-15'])  # createDataFrame(rdd, ['name', 'age'])
# register data frame as a temporary table
dataframe.registerTempTable("Phone")
# Select data frame like sql
sqlContext.sql("SELECT * FROM Phone limit 10").show()
sqlContext.sql("SELECT unit, count(Parameter) FROM Phone group by Unit", 5).show()
