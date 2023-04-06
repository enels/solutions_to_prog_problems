def twos(n):
    '''
        get the least number that is indivisible by 2
    :param n:
    :return: number of times to half the number
    '''
    if n <= 2:
        return -1
    # count of the number of times
    count = 0
    while n % 2 > 0:
        count += 1
        # decrease the number by half
        n //= 2

    return count