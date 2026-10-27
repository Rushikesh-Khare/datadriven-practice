from pyspark.sql.function import *

customer_df = spark.sql("select * from customers")

customer_df = customer_df.withColumn("full_name", 
  concat_ws(" ", col("first_name"), col("last_name")))
customer_df.show()
#apply filters like df have alphabeticle order full name and if names
#if names are identical lower customer id should get priority
final_df = customer_df.orderBy(col("full_name").asc(), col("customer_id").asc())
final_df.select("full_name", "customer_id", "country").show(truncate, False)
