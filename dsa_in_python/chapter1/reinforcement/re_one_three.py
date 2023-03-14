def minmax(data):
    '''
    Takes a sequence of one or more numbers, and returns the smallest
    and largest numbers, in the form of a tuple of length two.
    :param data: sequence of numbers
    :return: smallest and largest numbers in tuple
    '''

    # get the data length
    data_len = len(data)

    # sort the data from smallest to largest
    for sort_index in range(data_len):
        for index in range(data_len):
            if data[sort_index] < data[index]:
                # swap the values
                data[index], data[sort_index] = data[sort_index], data[index]

    # assign the smallest and largest
    least, largest = data[0], data[data_len - 1]
    # return tuple
    return least, largest