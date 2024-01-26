from src.operation import Operation

first_operation = Operation(ident=441945886,
                            date="2019-08-26T10:50:58.294041",
                            state="EXECUTED",
                            operation_amount={
                                "amount": "31957.58",
                                "currency": {
                                    "name": "руб.",
                                    "code": "RUB"
                                }
                            },
                            description="Перевод организации",
                            sent_from="Maestro 1596837868dhsk705199",
                            sent_to="Счет 6468647367889477958"
                            )
    # wrong No of sent_from and sent_to

second_operation = Operation(ident=441945886,
                            date="2019-08-26T10:50:58.294041",
                            state="EXECUTED",
                            operation_amount={
                                "amount": "31957.58",
                                "currency": {
                                    "name": "руб.",
                                    "code": "RUB"
                                }
                            },
                            description="Перевод организации",
                            sent_from="Maestro 1596837868705199",
                            sent_to="Счет 64686473678894779580"
                            )

def test_get_account_in_format():

    assert second_operation.get_account_in_format(second_operation.sent_from) == 'Maestro 1596 83** **** 5199'
    assert second_operation.get_account_in_format(second_operation.sent_to) == 'Счет **9580'

def test_get_account_in_format_ERROR():

    assert first_operation.get_account_in_format(first_operation.sent_from) == 'ERROR in reading of account number'
    assert first_operation.get_account_in_format(first_operation.sent_to) == 'ERROR in reading of account number'

def test_get_date_in_format():

    assert first_operation.get_date_in_format() == "26.08.2019"
