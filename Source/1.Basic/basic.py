from pyspark import SparkConf
from pyspark import SparkContext

#初始话pyspark
conf=SparkConf()
conf.setMaster(value="local").setAppName(value="Leo")
sc=SparkContext(conf=conf)


file=sc.textFile("../../Notes/1.Basic.md")
print(file.count())