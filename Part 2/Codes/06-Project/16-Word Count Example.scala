// Databricks notebook source
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf

// COMMAND ----------

val conf = new SparkConf().setAppName("Word Count")

// COMMAND ----------

val sc = SparkContext.getOrCreate(conf)

// COMMAND ----------

val data = sc.textFile("/FileStore/tables/sample_text_data.txt")

// COMMAND ----------

data.collect()

// COMMAND ----------

val splitData = data.flatMap(line => line.split(" "))
splitData.collect()

// COMMAND ----------

val mapdata = splitData.map(word => (word,1))
mapdata.collect()

// COMMAND ----------

val reduceData = mapdata.reduceByKey(_+_)

// COMMAND ----------

reduceData.collect()
