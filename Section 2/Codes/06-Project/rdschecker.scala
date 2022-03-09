import org.apache.spark.sql.SparkSession
object GlueApp {
    
  def main(sysArgs: Array[String]) {
        val jarPath = "s3://scalasparketl/postgresql-42.2.18.jar"
        val spark = SparkSession.builder.appName("Scala Spark Data Frames").config("spark.jars",jarPath).getOrCreate()
        val df = spark.read.format("jdbc").option("url", "jdbc:postgresql://database-1.cs8ljxah3rgm.us-east-1.rds.amazonaws.com:5432/").option("dbtable", "dummyTable").option("user", "postgres").option("password", "qwerasdfzxcv123").load()
        df.show()
        
  }
}