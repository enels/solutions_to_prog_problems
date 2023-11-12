def seperate_even_from_odd (s, s_even=[], s_odd=[], next_index=0):
    """
    rearranges sequence of a integer values to seperate even from odd numbers
    :param s: integer values to be arranged
    :param s_even: even integers
    :param s_odd: odd integers
    :param next_index: next integer index in s
    :return: arranged integer values
    """

    # base case
    if len(s) == next_index:
        return s_even + s_odd
    
    if s[next_index] % 2 == 0:
        s_even.append(s[next_index])
        return seperate_even_from_odd(s, s_even, s_odd, next_index + 1)
    elif s[next_index] % 2 == 1:
        s_odd.append(s[next_index])
        return seperate_even_from_odd(s, s_even, s_odd, next_index + 1)

if __name__ == "__main__":
    print(seperate_even_from_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))