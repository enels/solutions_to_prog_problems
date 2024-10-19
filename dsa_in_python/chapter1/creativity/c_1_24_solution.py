def vowel_count(str_list):
    '''
        count the number of vowels in a string
    :param str_list:
    :return: count of vowels
    '''

    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for s in str_list:
        if s in vowel:
            count += 1

    return count