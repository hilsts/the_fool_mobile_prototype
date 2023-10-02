import os
import json


def verify_path_exists(path):

    return os.path.exists(path)

def get_file_data(path):
    with open(path) as file:
        data = json.loads(file.read())

    return data

def create_file_from_data(data, path):

    json_obj = json.dumps(data)

    with open(path, 'w') as file:
        file.write(json_obj)

