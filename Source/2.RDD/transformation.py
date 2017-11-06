from pyspark import SparkConf
from pyspark import SparkContext

#初始化信息
conf=SparkConf()
conf.setMaster(value="local").setAppName(value="transformation_test")
sc=SparkContext(conf=conf)


#基本函数测试


