def sum_of_squares(n):
    '''
    Takes a positive integer n and find the sum of all positive integer
    less than n
    :param n: positive argument
    :return: sum of squares of numbers less than n
    '''

    sum = 0
    for num in range(n):
        sum += num ** 2

    return sum