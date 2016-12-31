>>> data = [(44,45),(34,35)]
>>> df=sqlContext.createDataFrame(data)  ## how to create datafram
>>> df.collect()
	[Row(_1=44, _2=45), Row(_1=34, _2=35)]

>>> sqlContext.createDataFrame(data,['num1','num2'])
	DataFrame[num1: bigint, num2: bigint]
>>> df_n=sqlContext.createDataFrame(data,['num1','num2'])
>>> df_n.collect()
	[Row(num1=44, num2=45), Row(num1=34, num2=35)]

####char with number
>>>data_s = [('abhishek',45),('dimple',35)]
>>> df_s=sqlContext.createDataFrame(data_s)  ## how to create datafram
>>> df_s.collect()
	[Row(_1=u'abhishek', _2=45), Row(_1=u'dimple', _2=35)]

>>> sqlContext.createDataFrame(data_s,['name','age'])
	DataFrame[name: string, age: bigint]

>>> df_s=sqlContext.createDataFrame(data_s,['name','age'])
>>> df_s.collect()
	[Row(name=u'abhishek', age=45), Row(name=u'dimple', age=35)]

### how to read file
df_f=sqlContext.read.text("/home/user/derby.log")

### cat of derby log

user@chrysaor-info-ubuntu-14041-desktop-amd64:~$ cat derby.log
----------------------------------------------------------------
Thu Dec 29 15:17:10 IST 2016:
Booting Derby version The Apache Software Foundation - Apache Derby - 10.10.1.1 - (1458268): instance a816c00e-0159-49f9-e182-00002e02cfc8 
on database directory /home/user/metastore_db with class loader org.apache.spark.sql.hive.client.IsolatedClientLoader$$anon$1@2886f893 
Loaded from file:/home/user/software/spark-1.6.1-bin-hadoop2.6/lib/spark-assembly-1.6.1-hadoop2.6.0.jar
java.vendor=Oracle Corporation
java.runtime.version=1.8.0_111-8u111-b14-2ubuntu0.16.04.2-b14
user.dir=/home/user
os.name=Linux
os.arch=amd64
os.version=4.4.0-57-generic
derby.system.home=null
Database Class Loader started - derby.database.classpath='

df_f.collect()

[Row(value=u'----------------------------------------------------------------'), Row(value=u'Thu Dec 29 15:17:10 IST 2016:'), Row(value=u'Booting Derby version The Apache Software Foundation - Apache Derby - 10.10.1.1 - (1458268): instance a816c00e-0159-49f9-e182-00002e02cfc8 '), Row(value=u'on database directory /home/user/metastore_db with class loader org.apache.spark.sql.hive.client.IsolatedClientLoader$$anon$1@2886f893 '), Row(value=u'Loaded from file:/home/user/software/spark-1.6.1-bin-hadoop2.6/lib/spark-assembly-1.6.1-hadoop2.6.0.jar'), Row(value=u'java.vendor=Oracle Corporation'), Row(value=u'java.runtime.version=1.8.0_111-8u111-b14-2ubuntu0.16.04.2-b14'), Row(value=u'user.dir=/home/user'), Row(value=u'os.name=Linux'), Row(value=u'os.arch=amd64'), Row(value=u'os.version=4.4.0-57-generic'), Row(value=u'derby.system.home=null'), Row(value=u"Database Class Loader started - derby.database.classpath=''")]
>>> 16/12/29 16:37:27 INFO Executor: Told to re-register on heartbeat
16/12/29 16:37:27 INFO BlockManager: BlockManager re-registering with master
16/12/29 16:37:27 INFO BlockManagerMaster: Trying to register Bl

### column transformation
user=sqlContext.read.load("B:\hadoop_py\work\ml-1m\usr.dat")
#########################
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import udf

data_s = [('abhishek',45),('dimple',35)]
df_t=sqlContext.createDataFrame(data_s,['name','age']) ## give name of column
size = udf (lambda s: len(s), IntegerType())
doubled= udf(lambda s: s*2, IntegerType()) ## creating custom UDF for 
df_t.select(doubled(df_t.age).alias('new_age')) ## applying custom UDF
DataFrame[new_age: int]
df_age=df_t.select(doubled(df_t.age).alias('new_age'))

df_age.collect() ## print result
[Row(new_age=90), Row(new_age=70)]

df_age=df_t.select(doubled(df_t.age).alias('new_age'),df_t.age,size(name)) ### applied UDF & alias
	[Row(new_age=90, age=45), Row(new_age=70, age=35)]

df_age=df_t.select(doubled(df_t.age).alias('new_age'),df_t.age,size(df_t.name),df_t.name)
	[Row(new_age=90, age=45, PythonUDF#<lambda>(name)=8), Row(new_age=70, age=35, PythonUDF#<lambda>(name)=6)]

df_age=df_t.select(doubled(df_t.age).alias('new_age'),df_t.age,size(df_t.name),df_t.name)
	[Row(new_age=90, age=45, PythonUDF#<lambda>(name)=8, name=u'abhishek'), Row(new_age=70, age=35, PythonUDF#<lambda>(name)=6, name=u'dimple')]

df5=df_age.filter(df_age.age >70)  ## filter
df5=df_age.filter(df_age.age >70)
df5.collect()
	[]

df5=df_age.filter(df_age.new_age >70) ## filter on alias
df5.collect()
	[Row(new_age=90, age=45, PythonUDF#<lambda>(name)=8, name=u'abhishek')]

>>> df5=df_age.distinct() ## distint
>>> df5.collect()
	[Row(new_age=70, age=35, PythonUDF#<lambda>(name)=6, name=u'dimple'), Row(new_age=90, age=45, PythonUDF#<lambda>(name)=8, name=u'abhishek')]


dfs5=df_age.sort('age',ascending=False) ## sort
df5.collect()
	[Row(new_age=70, age=35, PythonUDF#<lambda>(name)=6, name=u'dimple'), Row(new_age=90, age=45, PythonUDF#<lambda>(name)=8, name=u'abhishek')]

dfs5=df_age.sort('age',ascending=True)
df5.collect()
	[Row(new_age=70, age=35, PythonUDF#<lambda>(name)=6, name=u'dimple'), Row(new_age=90, age=45, PythonUDF#<lambda>(name)=8, name=u'abhishek')]

dfs5=df_age.sort('age',dscending=True)
	[Row(new_age=70, age=35, PythonUDF#<lambda>(name)=6, name=u'dimple'), Row(new_age=90, age=45, PythonUDF#<lambda>(name)=8, name=u'abhishek')]

dfs5=df_age.sort('age',dscending=False)
dfs5=df_t.sort('age',dscending=True)
dfs5.collect()
	[Row(name=u'dimple', age=35), Row(name=u'abhishek', age=45)]

>>> dfs5=df_t.sort('age',dscending=False)
>>> dfs5.collect()
	Row(name=u'dimple', age=35), Row(name=u'abhishek', age=45)]

############ explode 
data3=[Row(a=1, intlist=[1,2,3])]
df4=sqlContext.createDataFram(data3)
df4.select(explode(df4.intlist).alias('list')

#################group by function
data=[('abhishek',45,1),('dimple',35,2),('buchiya',7,3),('shivani',55,3),('buchiya',6,4)]
df=sqlContext.createDataFrame(data,['name','age','grade'])
one way-------------------->
		df1=df.groupBy(df.name)
								##### if you try below ##################################################
								>>> df1.collect()
								Traceback (most recent call last):
								  File "<stdin>", line 1, in <module>
								AttributeError: 'GroupedData' object has no attribute 'collect'
								##########################################################################
		df1.agg({"*" : "count"}).collect()
		[Row(name=u'dimple', count(1)=1), Row(name=u'buchiya', count(1)=2), Row(name=u'shivani', count(1)=1), Row(name=u'abhishek', count(1)=1)]
		df2=df1.agg({"*" : "count"})
		df2.collect()
		[Row(name=u'dimple', count(1)=1), Row(name=u'buchiya', count(1)=2), Row(name=u'shivani', count(1)=1), Row(name=u'abhishek', count(1)=1)]
second way-------------------->
		df1=df.groupBy(df.name).count()
		df1.collect()
		[Row(name=u'dimple', count=1), Row(name=u'buchiya', count=2), Row(name=u'shivani', count=1), Row(name=u'abhishek', count=1)]

		or
		
		df.groupBy(df.name).count().collect()
		[Row(name=u'dimple', count=1), Row(name=u'buchiya', count=2), Row(name=u'shivani', count=1), Row(name=u'abhishek', count=1)]
		df.groupBy(df.name).count(df.age).collect()
some more  ----------------->
		df.groupBy(df.name,df.age).count().collect()  ## no select opration,count(age) allowed
		[Row(name=u'dimple', age=35, count=1), 
		Row(name=u'shivani', age=55, count=1), 
		Row(name=u'buchiya', age=6, count=1), 
		Row(name=u'buchiya', age=7, count=1), 
		Row(name=u'abhishek', age=45, count=1)]
		
		-------------------->
		df.groupBy().count().collect()
		[Row(count=5)]
		-------------------->
		df.groupBy().avg().collect()
		[Row(avg(age)=29.6, avg(grade)=2.6)]
		-------------------->
		df.groupBy().avg().count().collect() ## error
		df.groupBy().avg().count()
		1
		-------------------->
		possible error 
				>>> df.groupBy(df.name).avg(df.age,df.grade).collect()
					TypeError: 'Column' object is not callable
				>>> df.groupBy(df.name).avg(age,grade).collect()
					NameError: name 'age' is not defined
				>>> df.groupBy(df.name).avg('age','grade').count().collect()  #### wrong collect is again not supported by count
		Correct
		
				df.groupBy(df.name).avg('age','grade').collect()
				input
				[Row(name=u'abhishek', age=45, grade=1), 
				Row(name=u'dimple', age=35, grade=2), 
				Row(name=u'buchiya', age=7, grade=3), 
				Row(name=u'shivani', age=55, grade=3), 
				Row(name=u'buchiya', age=6, grade=4)]

				output
				[Row(name=u'dimple', avg(age)=35.0, avg(grade)=2.0), only 1 record
				Row(name=u'buchiya', avg(age)=6.5, avg(grade)=3.5),
				Row(name=u'shivani', avg(age)=55.0, avg(grade)=3.0), only 1 record
				Row(name=u'abhishek', avg(age)=45.0, avg(grade)=1.0)] only 1 record
		
				df.groupBy(df.name).avg('age','grade').count()
				4
data=[('abhishek',45,1),('dimple',35,2),('buchiya',7,3),('shivani',55,3),('buchiya',6,4)]
df=sqlContext.createDataFrame(data,['name','age','grade'])
df.collect()
	[Row(name=u'abhishek', age=45, grade=1), Row(name=u'dimple', age=35, grade=2), Row(name=u'buchiya', age=7, grade=3), Row(name=u'shivani', age=55, grade=3), Row(name=u'buchiya', age=6, grade=4)]

df.show()
	+--------+---+-----+
	|    name|age|grade|
	+--------+---+-----+
	|abhishek| 45|    1|
	|  dimple| 35|    2|
	| buchiya|  7|    3|
	| shivani| 55|    3|
	| buchiya|  6|    4|
	+--------+---+-----+
>>> df.count()
	5

>>> df.take(2)
	[Row(name=u'abhishek', age=45, grade=1), Row(name=u'dimple', age=35, grade=2)]

>>> df.describe().show()
	+-------+------------------+------------------+
	|summary|               age|             grade|
	+-------+------------------+------------------+
	|  count|                 5|                 5|
	|   mean|              29.6|               2.6|
	| stddev|22.244100341438852|1.1401754250991378|
	|    min|                 6|                 1|
	|    max|                55|                 4|
	+-------+------------------+------------------+

>>> df.describe('age','grade').show()
	+-------+------------------+------------------+
	|summary|               age|             grade|
	+-------+------------------+------------------+
	|  count|                 5|                 5|
	|   mean|              29.6|               2.6|
	| stddev|22.244100341438852|1.1401754250991378|
	|    min|                 6|                 1|
	|    max|                55|                 4|
	+-------+------------------+------------------+

>>> df.describe('age').show()
	+-------+------------------+
	|summary|               age|
	+-------+------------------+
	|  count|                 5|
	|   mean|              29.6|
	| stddev|22.244100341438852|
	|    min|                 6|
	|    max|                55|
	+-------+------------------+
>>> df.describe('age','name').show()
	+-------+------------------+--------+
	|summary|               age|    name|
	+-------+------------------+--------+
	|  count|                 5|       5|
	|   mean|              29.6|    null|
	| stddev|22.244100341438852|    null|
	|    min|                 6|abhishek|
	|    max|                55| shivani|
	+-------+------------------+--------+
