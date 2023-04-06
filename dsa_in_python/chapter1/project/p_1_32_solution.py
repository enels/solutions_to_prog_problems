def calculate(rvalue, op, lvalue):
    '''
        perform the calculation based on the operation - op
    :param rvalue: right value
    :param op: operation to carry out
    :param lvalue: left value
    :return: integer of float
    '''

    if op == "+":
        return rvalue + lvalue
    elif op == "-":
        return rvalue - lvalue
    elif op == "*":
        return rvalue * lvalue
    elif op == "/":
        return rvalue / lvalue

def simple_calculator():
    '''
        program that simulates a simple calculator
    :return: result obtained
    '''

    # set the possible operators
    ops = ["+", "-", "*", "/", "="]

    # container for storing user's input
    user_input = list()

    # get the user's inputs - values and operators
    while True:
        ui = input(": ")
        # alphabet keyed in
        if ui.isalpha():
            print("Input Error")
            return -1
        # user is done and needs an output(answer)
        if ui == "=":
            break
        # stores users inputs
        user_input.append(ui)

    user_input_len = len(user_input)

    # get initial result
    result = calculate(int(user_input[0]), user_input[1], int(user_input[2]))

    # perform calculation
    for i in range(3, user_input_len):
        # get user operator
        op = user_input[i]
        if op in ops:
            result = calculate(result, user_input[i], int(user_input[i+1]))

    return result
