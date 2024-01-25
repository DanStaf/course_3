import os.path
import json

def get_5_operations():

    file_name = os.path.join('..', 'operations.json')

    with open(file_name, 'r', encoding='utf-8') as f:
        result = f.read()

    data_json = json.loads(result)






get_5_operations()
