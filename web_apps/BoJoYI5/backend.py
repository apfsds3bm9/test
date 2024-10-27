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
    client = dataiku.api_client()
    project_handle = dataiku.api_client().get_project(dataiku.default_project_key())
    vars = project_handle.get_variables()
    PROJECT_KEY = dataiku.default_project_key()
    vars["standard"]["Test"] = request_body["name"]
    project_handle.set_variables(vars)
    project = client.get_default_project()
    #base_scenario = project.get_scenario('TEST_RUNSTEP')
    #settings = base_scenario.get_settings()
    #temp_scenario = project.create_scenario('my_temp_scenario', 'step_based', {'params' : settings.data['params']})
    
    #temp_scenario.run_and_wait()
    #resp = add_json_to_dataset(request_body)

    #response = Response(response=json.dumps(resp),
    #                    status=resp['status'],
    #                    mimetype='application/json')
    #response.headers["Content-Type"] = "text/json; charset=utf-8"
    return {'status': 200, 'reason': json}


def add_content_to_dataset(name, json):
    """
    Add a new row in JSON format to an existing data.
    :param name: Name of the dataset.
    :param json: Value to append.
    """
    dataset = dataiku.Dataset(name)
    df = dataset.get_dataframe()
    df = df.append(json, ignore_index=True)
    logging.info(df.head())
    dataset.write_dataframe(df)


def add_json_to_dataset(json):
    """
    Add a row to a dataset, only if the dataset exists.
    :param json: Value to add.
    :return: a dict representing the result of the addition.
    """
    # This could be a part of data sent by the frontend.
    dataset_name = "L1"
    client = dataiku.api_client()
    project_handle = dataiku.api_client().get_project(dataiku.default_project_key())
    vars = project_handle.get_variables()
    PROJECT_KEY = dataiku.default_project_key()
    vars["standard"]["Test"] = dataset_name
    project_handle.set_variables(vars)
    project = client.get_default_project()
    dataset = project.get_dataset(dataset_name)
    scenario = DSSScenario(client, PROJECT_KEY, "TEST_RUNSTEP")
    print("------------------" + dataset_name + "------------------")
    if dataset.exists():
        add_content_to_dataset(dataset_name, json)
        return {'status': 200, 'name': json.get('name', '')}
    else:
        return {'status': 400, 'reason': json}, scenario.run()