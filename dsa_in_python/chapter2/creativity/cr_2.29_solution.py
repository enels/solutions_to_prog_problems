from codeFragment21 import CreditCard

class PredatoryCreditCard(CreditCard):
    """ An extension to CreditCard that compounds interest and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._minimum_monthly_payment = self._balance % 0.2
        self._late_fee = 10 # if customer does not pay the minimum monthly balance

        # get the current month
        self._start_month = dt.date.isoformat(dt.datetime.now()).split('-')[1]

    def charge(self, price):
        """ Charge a given price to the card, assuming sufficient credit limit"""

        current_month = dt.date.isoformat(dt.datetime.now()).split('-')[1]

        # convert the start and current month to int
        s_month = int(self._start_month)
        c_month = int(current_month)

        # increment the count charge for that month
        self._charge_count += 1

        # charge count exceeds the maximum allowed within the same month
        if c_month - s_month == 1:
            if self._balance != self.balance + self._minimum_monthly_payment:
                price += self._late_fee

        success = super().charge(price)
        if not success:
            self._balance += 5   # assess penalty
        return success          # caller expects return value

    def process_month(self):
        """ Assess monthly interest on outstanding balance"""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

if __name__ == "__main__":
    credit_card = PredatoryCreditCard("Emmanuel", "Access", "234323983", 5000, 0.08)
    credit_card.charge(1000)
    credit_card.charge(1000)
    credit_card.charge(1000)
    credit_card.charge(1000)
    print("Accnt. No. {0}".format(credit_card.get_account()))
    print("Bank {0}".format(credit_card.get_bank()))
    print("Limit {0}".format(credit_card.get_limit()))
    print("Balance {0}".format(credit_card.get_balance()))