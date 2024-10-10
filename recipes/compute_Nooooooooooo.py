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

Nooooooooooo_df = norway_new_car_sales_by_make_df # For this sample code, simply copy input to output


# Write recipe outputs
Nooooooooooo = dataiku.Dataset("Nooooooooooo")
Nooooooooooo.write_with_schema(Nooooooooooo_df)
