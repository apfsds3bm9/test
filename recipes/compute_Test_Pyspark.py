# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

# Import required PySpark functions
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.getOrCreate()

# Read the input dataset norway_new_car_sales_by_make
df = spark.sql("SELECT * FROM norway_new_car_sales_by_make")

# Filter for Year == 2009
df_2009 = df.where(col('Year') == 2009)

# Filter for Year == 2010
df_2010 = df.where(col('Year') == 2010)

# Write the 2009 dataset to the output dataset for Year 2009
df_2009.write.mode("overwrite").saveAsTable("norway_new_car_sales_by_make_2009")

# Write the 2010 dataset to the output dataset for Year 2010
df_2010.write.mode("overwrite").saveAsTable("norway_new_car_sales_by_make_2010")

