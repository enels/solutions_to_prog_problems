def remove_punctuations(s):
    '''
        Removes punctuations from passed string
    :param s:
    :return: string without punctuations
    '''

    # container to store the punctuationless string
    s2 = ""
    for c in s:
        if c.isalpha() or c.isnumeric() or c == " ":
            # concat c to s2
            s2 += c

    return s2
