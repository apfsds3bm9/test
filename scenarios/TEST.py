# This sample code helps you get started with the custom scenario API.
#For more details and samples, please see our Documentation
from dataiku.scenario import Scenario

# The Scenario object is the main handle from which you initiate steps
scenario = Scenario()

# A few example steps follow

# Building a dataset
list_partitions = ["2009", "2010"]
for z in list_partitions:
    s = Scenario()
    step = BuildFlowItemsStepDefHelper(f"Data Preparation {z}")
    step.add_dataset("earnings_by_education", "QS_MLOPS_2")  # Thay "QS_MLOPS_2" bằng z[0]
    step.add_dataset("job_postings_python", "QS_MLOPS_2")  # Thay "QS_MLOPS_2" bằng z[0]
    step.add_dataset("job_postings_prepared_joined", "QS_MLOPS_2") 
    step.add_dataset("unmatched", "QS_MLOPS_2") #unmatched
    # Chạy step với build_mode là RECURSIVE_FORCED_BUILD
    #s.build_dataset("earnings_by_education", "QS_MLOPS_2", build_mode="RECURSIVE_FORCED_BUILD")
    s.build_dataset("job_postings_prepared", "QS_MLOPS_2", build_mode="RECURSIVE_FORCED_BUILD")
    #s.build_dataset("job_postings_prepared_joined", "QS_MLOPS_2", build_mode="RECURSIVE_FORCED_BUILD")
    #s.build_dataset("unmatched", "QS_MLOPS_2", build_mode="RECURSIVE_FORCED_BUILD")
    


