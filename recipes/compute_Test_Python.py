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
myoutputdataset = dataiku.Dataset("norway_new_car_sales_by_make_partitioned")

# Initialize writer for output dataset
with myoutputdataset.get_writer() as writer:
    # Loop through each partition from the input dataset
    for p in mydataset.list_partitions():
        # Set partition to read from
        mydataset.read_partitions = [p]
        
        # Get dataframe for the current partition
        df = mydataset.get_dataframe()
        
        # Set partition to write to in the output dataset
        myoutputdataset.set_write_partition(str(p))
        
        # Write dataframe to the corresponding partition
        writer.write_dataframe(df)

    # Close the writer after all partitions are written
    writer.close()
