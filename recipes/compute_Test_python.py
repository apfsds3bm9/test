import dataiku
import pandas as pd

# Đọc dataset từ Dataiku
df = dataiku.Dataset("norway_new_car_sales_by_make").get_dataframe()

# Lọc dữ liệu cho năm 2009
df_2009 = df[df['Year'] == 2009]

# Lọc dữ liệu cho năm 2010
df_2010 = df[df['Year'] == 2010]

# Ghi dữ liệu ra hai dataset
output_2009 = dataiku.Dataset("norway_new_car_sales_by_make_2009")
output_2009.write_with_schema(df_2009)

output_2010 = dataiku.Dataset("norway_new_car_sales_by_make_2010")
output_2010.write_with_schema(df_2010)
