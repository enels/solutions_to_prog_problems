def sum_of_squares(n):
    '''
    Takes a positive integer n and find the sum of all odd positive numbers integer
    less than n using list python's comprehension
    :param n: positive argument
    :return: sum of squares of numbers less than n
    '''

    sum = 0
    for num in range(n):
        if num % 2 != 0:
            sum += num ** 2

    return sum