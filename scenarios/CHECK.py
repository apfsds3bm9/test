from dataiku.scenario import Scenario, BuildFlowItemsStepDefHelper
import dataiku

# Lấy danh sách tất cả các project
client = dataiku.api_client()
project_keys = client.list_projects()
# Lấy key của từng project
z = [project['projectKey'] for project in project_keys]
# Handling our scenario.
for i in range(2):
    s = Scenario()
    # Khởi tạo bước xây dựng
    step = BuildFlowItemsStepDefHelper("Data Preparation")
    step.add_dataset("job_postings_prepared", "QS_MLOPS_2")
    step.add_dataset("job_postings_python", "QS_MLOPS_2")

    # Chạy bước này
    s.run_step(step.get_step())