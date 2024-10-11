import dataiku
from dataiku.scenario import Scenario
from dataiku.scenario import BuildFlowItemsStepDefHelper

# Lấy dataset chứa thông tin `Make`
mydataset = dataiku.Dataset("norway_new_car_sales_by_make_filtered_2")
df = mydataset.get_dataframe()

# Lấy danh sách các giá trị 'Make'
unique_makes = df['Make'].unique()

# Chuyển tất cả các giá trị trong 'Make' thành chuỗi ký tự
unique_makes_str = [str(make) for make in unique_makes]

# Set danh sách này làm biến trong scenario
scenario_variables = {"makes_list": ",".join(unique_makes_str)}
Scenario().set_scenario_variables(breach_list=scenario_variables)

# The Scenario object is the main handle from which you initiate steps
scenario = Scenario()

# Building a dataset - Lặp qua danh sách các `Make`
for make in unique_makes:
    # Khởi tạo một step mới cho từng `Make`
    step = BuildFlowItemsStepDefHelper(f"Data Preparation for {make}")
    
    # Add các dataset đầu vào và đầu ra
    step.add_dataset("norway_new_car_sales_by_make_filtered_2", partitions=make)  # Thay partition bằng make
    step.add_dataset("Test_Python", partitions=make)  # Thêm partition vào dataset đầu ra
    
    # Chạy step với build_mode là RECURSIVE_FORCED_BUILD cho từng partition
    scenario.build_dataset("Test_Python", partitions=make, build_mode="RECURSIVE_FORCED_BUILD")
