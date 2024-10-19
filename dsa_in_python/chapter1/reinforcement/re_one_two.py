def is_even(k):
    '''
    checks if the variable k is even without using the multiplication,
    division, or modulos operator
    :param k: variable to check
    :return: True if even, else False
    '''

    k -= 2
    while (k != 0 or k != 1):
        if k == 1:
            return False # is false
        elif k == 0:
            return True # is even
        k -= 2 # reduce k by two