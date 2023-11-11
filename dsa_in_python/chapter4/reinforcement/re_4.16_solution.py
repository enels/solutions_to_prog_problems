def string_reverse(s, rev_s="", n=0):
    """
    reverse a string using recursion

    :param s: string to reverse
    :param rev_s: store the reverse string
    :param n: number of character remaining to be reversed
    :return: reversed string
    """
    n += 1
    if n > len(s):
        return rev_s
    #print(s[len(s) - n])
    rev_s += s[len(s) - n]

    return string_reverse(s, rev_s, n)

if __name__ == "__main__":
    print("reversed string: " + str(string_reverse('pots&pans')))

    assert (string_reverse('pots&pans') == 'snap&stop')