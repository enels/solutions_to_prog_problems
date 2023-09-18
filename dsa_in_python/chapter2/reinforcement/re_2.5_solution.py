class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance
        The initial balance is zero

        customer the name of the customer (e.g., 'John Bowman')
        bank    the name of the bank (e.g., 'California Savings')
        acnt    the account number (e.g, 5391 0375 9387 5309)
        limit   credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """
        Return name of the customer
        """
        return self._customer

    def get_bank(self):
        """
        Return the bank's name
        """
        return self._bank

    def get_account(self):
        """
        Return the card identity number (typically stored as a string)
        """
        return self._account

    def get_limit(self):
        """
        Return the current credit limit
        """
        return self._limit

    def get_balance(self):
        """
        Return the current balance of the customer
        """
        return self._balance

    def charge(self, price):
        """
        Charge given price on the card, assuming sufficient credit limit

        Return true if charge was processed; False if charge was denied
        """
        if not isinstance(price, int):
            raise TypeError("Price not a number")

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """
        Process customer payment that reduces balance
        """
        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer or a float")

        self._balance -= amount


if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("Enoma Uwaifo", "Unity Bank", "0033670233", 4500))
    wallet.append(CreditCard("Newton Uwaifo", "Unity Bank", "0033670233", 7500))
    wallet.append(CreditCard("Enoma Wasy", "Unity Bank", "0033670233", 1000))
    wallet.append(CreditCard("Osas Isiho", "Unity Bank", "0033670233", 3000))

    wallet[0].charge(2300)

    num_of_customers = len(wallet)
    for c in range(num_of_customers):
        print(
            "Name: {0} Bank: {1} accout number: {2} balance: {3}".format(wallet[c].get_customer(), wallet[c].get_bank(),
                                                                         wallet[c].get_account(),
                                                                         wallet[c].get_balance()))