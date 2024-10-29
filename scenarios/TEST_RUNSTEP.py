import dataiku
from dataiku.scenario import Scenario
from dataiku.scenario import BuildFlowItemsStepDefHelper

# Lấy dataset chứa thông tin `Make`
mydataset = dataiku.Dataset("norway_new_car_sales_by_make")
df = mydataset.get_dataframe()
#dataiku.default_project_key()
print(dataiku.default_project_key())
project_handle = dataiku.api_client().get_project(dataiku.default_project_key())
vars = project_handle.get_variables()
project_key = dataiku.default_project_key()
# Lấy danh sách các giá trị 'Make'
unique_makes = df['Make'].unique()
# The Scenario object is the main handle from which you initiate steps
scenario = Scenario()
unique_makes = unique_makes[:6]
# Building a dataset - Lặp qua danh sách các `Make`
for make in unique_makes:
    vars['standard']["makes_list"] = str(make)
    project_handle.set_variables(vars)
    # Khởi tạo một step mới cho từng `Make`
    step = BuildFlowItemsStepDefHelper(f"Data Preparation for {make}") 
    step.add_dataset("norway_new_car_sales_by_make_filtered_1_prepared", project_key = project_key) 
    step.add_dataset("Test_sum_and_mul", project_key = project_key)
    # Add các dataset đầu vào và đầu ra
    #step.add_dataset("norway_new_car_sales_by_make_filtered_2", project_key = project_key)#, partitions=make)  # Thay partition bằng make
    #step.add_dataset("Test_Python", project_key = project_key, partitions=make)  # Thêm partition vào dataset đầu ra
    #step.add_dataset("Test_Python_filtered", project_key = project_key, partitions=make)
    # Chạy step với build_mode là RECURSIVE_FORCED_BUILD cho từng partition
    scenario.run_step(step.get_step())

    