import os.path
import json
from operation import Operation

def load_operations_from_file():
    """function load json data from operations.json
    parse data to list
    create list with items of class <Operation>"""

    file_name = os.path.join('..', 'operations.json')

    with open(file_name, 'r', encoding='utf-8') as f:
        result = f.read()

    data_json = json.loads(result)

    list_of_operations = [Operation(item['id'],
                                 item['date'],
                                 item['state'],
                                 item['operationAmount'],
                                 item['description'],
                                 item['from'] if 'from' in item else None,
                                 item['to']) for item in data_json if item]
    # print(len(operations_list))
    # print(operations_list[50])

    return list_of_operations


def chose_sorted_executed_operations(list_of_operations):
    """function chose 'EXECUTED' operation from the list
    sort by date in reversed order"""

    executed_operations = [item for item in list_of_operations if item.state == 'EXECUTED']
    executed_operations.sort(key=lambda oper: oper.date, reverse='true')
    #[print(item.date) for item in executed_operations]
    return executed_operations


def get_last_operations(number=5):
    """function call loading data from file
    call chose of 'EXECUTED' operations
    print the requested number of last operations"""

    operations_list = load_operations_from_file()
    sorted_executed_operations = chose_sorted_executed_operations(operations_list)

    if len(sorted_executed_operations) < number:
        number = len(sorted_executed_operations)

    [print(item) for item in sorted_executed_operations[:number]]


#get_last_operations()

##############
