// Databricks notebook source
import org.apache.spark.sql.SparkSession

// COMMAND ----------

val spark = SparkSession.builder.appName("Scala Spark Data Frames").getOrCreate()

// COMMAND ----------

val df = spark.read.option("header",true).csv("/FileStore/tables/data.csv")
df.show()

// COMMAND ----------


