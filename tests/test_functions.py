#import pytest
import src.functions


"""
def test_read_file():

    assert read_file('operations.json')
"""


def test_get_last_operations():

    assert src.functions.get_last_operations() is True
    assert src.functions.get_last_operations(200) is True


def test_load_operations_from_file():

    result = src.functions.load_operations_from_file('operations.json')
    assert len(result) == 100


def test_load_operations_from_file_blank_file():

    result = src.functions.load_operations_from_file('test')
    assert result is None


def test_chose_sorted_executed_operations():

    assert len(src.functions.chose_sorted_executed_operations([])) == 0
