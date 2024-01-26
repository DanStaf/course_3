import os.path
import json
from operation import Operation

def load_operations_from_file():

    file_name = os.path.join('..', 'operations.json')

    with open(file_name, 'r', encoding='utf-8') as f:
        result = f.read()

    data_json = json.loads(result)

    operations_list = [Operation(item['id'],
                                 item['date'],
                                 item['state'],
                                 item['operationAmount'],
                                 item['description'],
                                 item['from'] if 'from' in item else None,
                                 item['to']) for item in data_json if item]
    # print(len(operations_list))
    # print(operations_list[50])

    return operations_list


def get_5_operations():

    operations_list = load_operations_from_file()






get_5_operations()
