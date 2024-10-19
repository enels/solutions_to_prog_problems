def is_all_distinct(data):
    '''
        Checks if all the list elements are distinct
    :param data:
    :return: True if distinct, False if not
    '''

    data_len = len(data)

    for val in range(0, data_len - 1):
        for val2 in range(val+1, data_len):
            if data[val] == data[val2]:
                return False

    return True