# iterate thru each denomination to cover the quantity needed
# get the floating part, if any, to get the number of cents

def store_balance_currency(bills, bill):
    bills.append(bill)

def get_balance(balance_left, bill):
    balance_left -= bill
    return balance_left

def get_dollar_bills(dollar_bill, balance_left, bills):
    for bill in dollar_bill:
        while get_balance(balance_left, bill) >= 0:
            store_balance_currency(bills, bill)
            balance_left = get_balance(balance_left, bill)

    return bills

def print_change_bills(change_bills, cent_bills):

    #print out the dollar change
    print("Dollars: ")
    for b in change_bills:
        print("${} ".format(b), end="")
    print("\n")

    # print out the cent change
    print("Cent: ")
    if len(cent_bills) != 0:
        for c in cent_bills:
            print("{} ".format(c), end="")
    else:
        print("{}c".format(0))
    print("\n")

def change(charge, given):
    '''
    Determine the minimum amount of currency denomination to give out as change
    :param charge: amount charge on service/product
    :param given: amount paid
    :return: list of currency denomination to be given out
    '''
    # container to store the currency denominations
    change_bills = list()
    cent_bills = list()

    # get the balance(change) left
    balance_left = get_balance(given, charge)

    dollar_bill = [100, 50, 20, 10, 5, 2, 1]
    cent = [50, 25, 10, 5, 1]

    # get the dollar bills to be use as change
    get_dollar_bills(dollar_bill, balance_left, change_bills)

    # check if balance include some cent
    if isinstance(balance_left, float):
        # get the the balance_left in whole number
        balance_left *= 100

        # get the cent left
        cent_left = balance_left % 100

        # get the cent denominations to use as change
        get_dollar_bills(cent, cent_left, cent_bills)

    print_change_bills(change_bills, cent_bills)

    # return the change in tuples of list
    return change_bills, cent_bills

if __name__ == "__main__":
    change(120, 200)