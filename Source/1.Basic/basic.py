from pyspark import SparkConf
from pyspark import SparkContext

#初始化过程
conf=SparkConf()
conf.setMaster(value="local").setAppName(value="Leo")
sc=SparkContext(conf=conf)

print("****************result**************")
file=sc.textFile("/home/xierhacker/WorkSpace/SparkTutorial/Notes/1.Basic.md")
num=file.count()
print("success!!!!")
print(num)
print(file.first())
print("*************************************")
