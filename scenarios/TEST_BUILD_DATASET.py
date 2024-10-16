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
# Lấy ra 6 hãng xe trang danh sách Make (các hãng xe).
unique_makes = unique_makes[:6]
# Building a dataset - Lặp qua danh sách các `Make`
for make in unique_makes:
    vars['standard']["makes_list"] = str(make)
    project_handle.set_variables(vars)
    # Chạy step với build_mode là RECURSIVE_FORCED_BUILD cho từng partition
    #scenario.build_dataset("Test_Python", partitions=make, build_mode="RECURSIVE_FORCED_BUILD")
    scenario.build_dataset("Test_Python_filtered", partitions=make, build_mode="RECURSIVE_BUILD")

    