from pyspark import SparkConf
from pyspark import SparkContext

#初始化信息
conf=SparkConf()
conf.setMaster(value="local").setAppName(value="transformation_test")
sc=SparkContext(conf=conf)


#基本函数测试
num1_RDD=sc.parallelize([1,2,3,4,5,6])
num2_Rdd=sc.parallelize([1,1,2,3,4,5,5,9,11])

#count()
print("num of num1_RDD :",num1_RDD.count())

#collect
print("collect of num1_RDD:",num1_RDD.collect())

#countByValue()
print("countByValue of num2_RDD:",num2_Rdd.countByValue())


#take()
print("take of num2_RDD:",num2_Rdd.take(3))

#takeOerderd()
print("takeOrderd of num2_RDD:",num2_Rdd.takeOrdered(4))





