def revert_list(l):
    '''
        Function to revert a list in oppostion order which it
        was arranged
    :return: nothing
    '''

    start = len(l) - 1  # initialize the start index
    end = start  # 2 # half the list index to initialize where it ends
    step = -1  # step to take
    swap_index = 0  # index to swap with the index to iterate
    for i in range(start, end, step):
        temp = l[i]
        l[i] = l[swap_index]
        l[swap_index] = temp
        swap_index += 1

    return l