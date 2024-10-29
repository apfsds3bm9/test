import dataiku
import pandas as pd
from flask import Response, request
import logging
import json
from dataikuapi.dss.scenario import DSSScenario

@app.route('/first_form', methods=['POST', 'PUT'])
def first_form():
    """
    Process the request sent from the front end.

    :return: a response containing the data coming from the request.
    """
    request_body = request.get_json()
    name = request_body["name"]
    email = request_body["email"]
    client = dataiku.api_client()
    project_handle = dataiku.api_client().get_project(dataiku.default_project_key())
    vars = project_handle.get_variables()
    PROJECT_KEY = dataiku.default_project_key()
    vars["standard"]["sum"] = int(name)
    vars["standard"]["mul"] = int(email)
    project_handle.set_variables(vars)
    project = client.get_default_project()
    base_scenario = project.get_scenario('TEST_RUNSTEP')
    settings = base_scenario.get_settings()
    temp_scenario = project.create_scenario('my_temp_scenario', 'step_based', {'params' : settings.data['params']})
    
    temp_scenario.run_and_wait()
    # remove your temporary scenario 
    temp_scenario.delete()
    base_scenario.run()
    return {'status': 200, 'reason_1': name, 'reason_2': email}


