from pyspark import SparkContext
from pyspark.sql import SparkSession

appName = "Basic Test"


def main(spark):
    # the comment that starts with 'type: ' are stupid hacks to get type hinting in PyCharm
    # Don't do this in real life - there are better ways to do this
    spark = spark # type: SparkSession
    sc = spark.sparkContext #type: SparkContext
    rdd = sc.parallelize(range(1,1000))
    print(rdd.sum())
    print(rdd.count())


if __name__ == "__main__":
    spark = SparkSession.builder \
                .appName(appName) \
                .master("spark2dock_spark-master_1") \
                .getOrCreate()
    main(spark)