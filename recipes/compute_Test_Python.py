import dataiku

# Đọc biến partition từ Scenario (lấy từ custom variables)
current_make = dataiku.get_custom_variables()["makes_list"]

# Đọc dataset đầu vào
mydataset = dataiku.Dataset("norway_new_car_sales_by_make_filtered_2")
myoutputdataset = dataiku.Dataset("Test_Python")
print(f"--------------------------------------------------------- Name:{current_make}--------------------------------------------------------")
# Lọc dữ liệu theo partition (Make) hiện tại
df = mydataset.get_dataframe()
partition_df = df[df['Make'] == current_make]
print(f"--------------------------------------------------------- Shape: {partition_df.shape}--------------------------------------------------------")
myoutputdataset.write_with_schema(partition_df)