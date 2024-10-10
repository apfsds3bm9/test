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
Check_df = norway_new_car_sales_by_make_df # For this sample code, simply copy input to output

# Write recipe outputs
Check = dataiku.Dataset("Check")
dkuspark.write_with_schema(Check, Check_df)
