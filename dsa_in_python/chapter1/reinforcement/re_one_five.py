def sum_of_squares(n):
    '''
    Takes a positive integer n and find the sum of all positive integer
    less than n using list python's comprehension
    :param n: positive argument
    :return: sum of squares of numbers less than n
    '''

    result = sum([num**2 for num in range(n)])
    return result