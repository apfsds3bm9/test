import dataiku

# Đọc biến partition từ Scenario (lấy từ custom variables)
current_make = dataiku.get_custom_variables()["current_make"]

# Đọc dataset đầu vào
mydataset = dataiku.Dataset("norway_new_car_sales_by_make_filtered_2")
myoutputdataset = dataiku.Dataset("Test_Python")
print(f"---------------------------------------------------------{current_make}--------------------------------------------------------")
# Lọc dữ liệu theo partition (Make) hiện tại
df = mydataset.get_dataframe()
partition_df = df[df['Make'] == current_make]

# Ghi dữ liệu ra dataset đầu ra
with myoutputdataset.get_writer() as writer:
    writer.write_dataframe(partition_df)
