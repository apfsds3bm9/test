# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
#norway_new_car_sales_by_make_filtered_2 = dataiku.Dataset("norway_new_car_sales_by_make_filtered_2")
#norway_new_car_sales_by_make_filtered_2_df = norway_new_car_sales_by_make_filtered_2.get_dataframe()


import dataiku

# Read the input dataset
mydataset = dataiku.Dataset("norway_new_car_sales_by_make_filtered_2")
myoutputdataset = dataiku.Dataset("Test_Python")

df = mydataset.get_dataframe()

# Kiểm tra schema của dataframe
print("DataFrame Schema:")
print(df.dtypes)

# Kiểm tra schema của dataset đầu ra
myoutputdataset.write_schema_from_dataframe(df)

with myoutputdataset.get_writer() as writer:
    writer.write_dataframe(df)
