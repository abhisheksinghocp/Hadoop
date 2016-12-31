#####################################################################################
IMPL Link																			#
https://spark.apache.org/docs/2.0.0/api/python/pyspark.sql.html#pyspark.sql.Row		#
Life cycle of Spark																	#

1) create datafrom from external or collection like array,list						#
2)Lazily Transfromation (action only when requested)								#
3)cache() for future if needed														#
4)Transform & action, save result													#
#####################################################################################
python life cycle
1)Most of python code run driver (means utility node)
a=a+1 
2)Transfromation run on excuter side
linedf.filter(in india)
3)Action run on excuter & driver
commentdf.count() 

#####################################################################################
>>> linedf=sqlContext.read.text('/home/user/Desktop/ml-1m/usr.dat')  ## file loaded
	16/12/30 03:51:11 INFO TextRelation: Listing file:/home/user/Desktop/ml-1m/usr.dat on driver

>>> linedf.take(5) ## display 5 records
	[Row(value=u'1::F::1::10::48067'), Row(value=u'2::M::56::16::70072'), Row(value=u'3::M::25::15::55117'), Row(value=u'4::M::45::7::02460'), Row(value=u'5::M::25::20::55455')]
	
>>> linedf.first()
	Row(value=u'1::F::1::10::48067')
filterdf=linedf.filter('F')

>> linedf.describe()
   DataFrame[summary: string]

>>> linedf.show()
	+--------------------+
	|               value|
	+--------------------+
	|  1::F::1::10::48067|
	| 2::M::56::16::70072|
	| 3::M::25::15::55117|
	|  4::M::45::7::02460|
	| 5::M::25::20::55455|
	|  6::F::50::9::55117|
	|  7::M::35::1::06810|
	| 8::M::25::12::11413|
	| 9::M::25::17::61614|
	| 10::F::35::1::95370|
	| 11::F::25::1::04093|
	|12::M::25::12::32793|
	| 13::M::45::1::93304|
	| 14::M::35::0::60126|
	| 15::M::25::7::22903|
	| 16::F::35::0::20670|
	| 17::M::50::1::95350|
	| 18::F::18::3::95825|
	| 19::M::1::10::48073|
	|20::M::25::14::55113|
	+--------------------+
	only showing top 20 rows

>>> linedf.filter(linedf.value > '02460').show()
	--------------------+
	|               value|
	+--------------------+
	|  1::F::1::10::48067|
	| 2::M::56::16::70072|
	| 3::M::25::15::55117|
	|  4::M::45::7::02460|
	| 5::M::25::20::55455|
	|  6::F::50::9::55117|
	|  7::M::35::1::06810|
	| 8::M::25::12::11413|
	| 9::M::25::17::61614|
	| 10::F::35::1::95370|
	| 11::F::25::1::04093|
	|12::M::25::12::32793|
	| 13::M::45::1::93304|
	| 14::M::35::0::60126|
	| 15::M::25::7::22903|
	| 16::F::35::0::20670|
	| 17::M::50::1::95350|
	| 18::F::18::3::95825|
	| 19::M::1::10::48073|
	|20::M::25::14::55113|
	+--------------------+
	only showing top 20 rows
>>> linedf.cache() ## full data in momory if you cache same data set in 2 parameter you will get warning "data is already cache"
