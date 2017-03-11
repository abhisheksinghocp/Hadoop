# Only RDD PROGRAM
from pyspark import SparkContext, SparkConf
from pyspark.sql import Row
sc = SparkContext(appName="CSV_Read")
path = 'B:\hadoop_py\work\External_data\Telecom\Telecom_Performance-Monthly_jan_feb_2015.csv'  # reading files
lines = sc.textFile(path)  # system to implicit partition
# /*******lines = sc.textFile(path,4)  ## system explicit partition
print("split file line by line")
linebyline = lines.map(lambda line: line.split('\n'))
print(lines.take(5))  # print RDD Output
print(linebyline.take(5))  # Take only 5 records

print("Now mapp input file with column name")
linebyline_1 = lines.map(lambda x: Row(Paramete=x[0], Unit=x[1], Feb=x[2], Jan=x[3]))
print(linebyline_1.take(3))

print("All above results are RDD")