import datetime


class Operation:

    def __init__(self, ident, date, state, operation_amount, description, sent_from, sent_to):

        self.ident = ident
        self.date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
        self.state = state
        self.description = description
        self.operation_amount = operation_amount
        self.sent_from = sent_from
        self.sent_to = sent_to

    def __repr__(self):
        #return "Class <<Operation>>, id: " + str(self.ident)

        return f'''{self.get_date_in_format()} {self.description}
{self.get_account_in_format(self.sent_from)} -> {self.get_account_in_format(self.sent_to)}
{self.operation_amount['amount']} {self.operation_amount['currency']['name']}
'''

    def get_date_in_format(self):
        return self.date.strftime("%d.%m.%Y")

    def get_account_in_format(self, account_number):

        if not account_number:
            return ''

        parts_number = account_number.split(' ')
        number = parts_number[-1]
        name = ' '.join(parts_number[:-1])

        if not number.isdigit():
            return 'ERROR in reading of account number'

        if len(number) == 20:
            return name + ' **' + number[-4:]

        elif len(number) == 16:
            new_card_number = " ".join([number[:-12], number[-12:-8], number[-8:-4], number[-4:]])
            replace_line = new_card_number[-12:-5]
            return name + ' ' + new_card_number.replace(replace_line, '** ****')

        else:
            return 'ERROR in reading of account number'

