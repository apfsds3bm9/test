# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
norway_new_car_sales_by_make_filtered_1_prepared = dataiku.Dataset("norway_new_car_sales_by_make_filtered_1_prepared")
norway_new_car_sales_by_make_filtered_1_prepared_df = norway_new_car_sales_by_make_filtered_1_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Test_sum_and_mul_df = norway_new_car_sales_by_make_filtered_1_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
Test_sum_and_mul = dataiku.Dataset("Test_sum_and_mul")
Test_sum_and_mul.write_with_schema(Test_sum_and_mul_df)
