import pytest
import src.functions

"""08.12.2019 Открытие вклада
 -> Счет **5907
41096.24 USD

07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
48150.39 USD

19.11.2019 Перевод организации
Maestro 7810 84** **** 5568 -> Счет **2869
30153.72 руб.

13.11.2019 Перевод со счета на счет
Счет **9794 -> Счет **8125
62814.53 руб.

05.11.2019 Открытие вклада
 -> Счет **8381
21344.35 руб.
"""

def test_get_last_operations():

    pass
    #assert src.functions.get_last_operations() == True

def test_load_operations_from_file():

    result = src.functions.load_operations_from_file('operations.json')
    assert len(result) == 100

    result = src.functions.load_operations_from_file('test')
    assert result == None

def test_chose_sorted_executed_operations():

    assert len(src.functions.chose_sorted_executed_operations([])) == 0
