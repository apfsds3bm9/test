# This sample code helps you get started with the custom scenario API.
#For more details and samples, please see our Documentation
from dataiku.scenario import Scenario

# The Scenario object is the main handle from which you initiate steps
scenario = Scenario()

# A few example steps follow

# Building a dataset
list_partitions = ["2009", "2010"]
for z in list_partitions:
    scenario.build_dataset(f"customers_prepared_{z}", partitions=z)
    


