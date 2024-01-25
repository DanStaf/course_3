class Operation():

    def __init__(self, ident, date, state, operationAmount, description, sent_from, sent_to):

        self.ident = ident
        self.date = date
        self.state = state
        self.operationAmount = operationAmount
        self.sent_from = sent_from
        self.sent_to = sent_to

    def __repr__(self):
        return "Class <<Operation>>, id: " + str(self.ident)
