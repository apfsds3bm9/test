# This sample code helps you get started with the custom scenario API.
#For more details and samples, please see our Documentation
from dataiku.scenario import Scenario, BuildFlowItemsStepDefHelper
import dataiku

# The Scenario object is the main handle from which you initiate steps
scenario = Scenario()

# A few example steps follow
client = dataiku.api_client()
project_keys = client.list_projects()

# Lấy key của từng project
z = [project['projectKey'] for project in project_keys]
# Building a dataset
list_partitions = [2008]# ,2009, 2010]
for z in list_partitions:
    s = Scenario()
    step = BuildFlowItemsStepDefHelper(f"Data Preparation {z}")
    step.add_dataset("norway_new_car_sales_by_make", "TASKCHUAVAI")  # Thay "QS_MLOPS_2" bằng z[0]
    step.add_dataset("Test_Python", "TASKCHUAVAI")  # Thay "QS_MLOPS_2" bằng z[0]
    # Chạy step với build_mode là RECURSIVE_FORCED_BUILD
    s.build_dataset("Test_Python", 
                    "TASKCHUAVAI", 
                    build_mode="RECURSIVE_BUILD",
                    partitions = z)
    


