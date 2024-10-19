def is_distinct_pair(data):
    '''
        Determins if there's a distinct pair of numbers in the sequence whose product is odd
    :param data:
    :return: true if pair found, false otherwise
    '''

    data_len = len(data)  # get the length of the data
    for val in range(0, data_len - 1):
        # compare the values adjacent to each other
        # if the products are odd
        if (data[val] * data[val+1]) % 2 != 0:
            return True

    return False