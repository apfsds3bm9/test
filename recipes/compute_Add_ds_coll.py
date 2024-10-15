# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
norway_new_car_sales_by_make = dataiku.Dataset("norway_new_car_sales_by_make")
norway_new_car_sales_by_make_df = norway_new_car_sales_by_make.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.
# Gộp cột Year và Month để tạo thành cột ds
norway_new_car_sales_by_make_df['ds'] = pd.to_datetime(norway_new_car_sales_by_make_df['Year'].astype(str) + '-' + norway_new_car_sales_by_make_df['Month'].astype(str) + '-01')

Add_ds_coll_df = norway_new_car_sales_by_make_df # For this sample code, simply copy input to output


# Write recipe outputs
Add_ds_coll = dataiku.Dataset("Add_ds_coll")
Add_ds_coll.write_with_schema(Add_ds_coll_df)
