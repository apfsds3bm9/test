# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# Read recipe inputs
norway_new_car_sales_by_make = dataiku.Dataset("norway_new_car_sales_by_make")
norway_new_car_sales_by_make_df = dkuspark.get_dataframe(sqlContext, norway_new_car_sales_by_make)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
check_df = norway_new_car_sales_by_make_df # For this sample code, simply copy input to output

# Write recipe outputs
check = dataiku.Dataset("check")
dkuspark.write_with_schema(check, check_df)


import dataiku
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Tạo Spark session
spark = SparkSession.builder.appName("Create Partitioned Datasets").getOrCreate()

# Đọc dataset từ Dataiku
df = dataiku.Dataset("norway_new_car_sales_by_make").get_dataframe()

# Chuyển đổi DataFrame sang Spark DataFrame
spark_df = spark.createDataFrame(df)

# Lọc dữ liệu cho năm 2009
df_2009 = spark_df.filter(F.col('Year') == 2009)

# Lọc dữ liệu cho năm 2010
df_2010 = spark_df.filter(F.col('Year') == 2010)

# Định nghĩa đường dẫn lưu dataset với partition
output_path_2009 = "norway_new_car_sales_by_make_2009"
output_path_2010 = "norway_new_car_sales_by_make_2010"

# Lưu dataset cho năm 2009 với partition
df_2009.write.partitionBy("Year").format("parquet").mode("overwrite").save(output_path_2009)

# Lưu dataset cho năm 2010 với partition
df_2010.write.partitionBy("Year").format("parquet").mode("overwrite").save(output_path_2010)
