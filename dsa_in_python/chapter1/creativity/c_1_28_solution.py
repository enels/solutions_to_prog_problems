from math import ceil

def norm(v, p=2):
    '''
        Gives the p-norm of a vector and the euclidean norm
        in a polymorphic way
    :param v: vector
    :param p: p value
    :return: p-norm value or euclidean norm value
    '''

    sum_power = 0
    for val in v:
        # sum up the squares of the numbers
        sum_power += val**p

    # get the nth root of the sum power
    return ceil(sum_power**(1/p))