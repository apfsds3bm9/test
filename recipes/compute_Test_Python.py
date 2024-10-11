import dataiku

# Read the input dataset
mydataset = dataiku.Dataset("norway_new_car_sales_by_make_filtered_2")
myoutputdataset = dataiku.Dataset("Test_Python")

#df = mydataset.get_dataframe()

# Lấy danh sách các giá trị duy nhất của cột 'year'
#unique_years = df['Year'].unique()

# Lưu dữ liệu theo partition từng năm
#with myoutputdataset.get_writer() as writer:
#    for year in unique_years:
        # Lọc dữ liệu của từng năm
#        partition_df = df[df['Year'] == year]
        
        # Thiết lập partition theo năm
#        myoutputdataset.set_write_partition(str(year))
        
        # Ghi dữ liệu của partition đó
#        writer.write_dataframe(partition_df)
df = mydataset.get_dataframe()

# Lấy danh sách các giá trị duy nhất của cột 'year'
unique_Maker = df['Make'].unique()

# Lưu dữ liệu theo partition từng năm
with myoutputdataset.get_writer() as writer:
    for Make in unique_Maker:
        # Lọc dữ liệu của từng năm
        partition_df = df[(df['Make'] == Make)]
        myoutputdataset.set_write_partition(str(Make))
        # Không cần gọi set_write_partition, chỉ cần ghi dataframe
        writer.write_dataframe(partition_df)