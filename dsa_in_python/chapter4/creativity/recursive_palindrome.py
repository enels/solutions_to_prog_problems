def recursive_palindrome(s, is_palindrome=False):
    """
    recursively checks if a string is palindrome
    :param s: string to check
    :param is_palindrome: True is palindrome otherwise false
    :return: True if is palindrome otherwise false
    """

    # base case
    # even string length case
    if s[len(s) - 1] == s[0]:
        return True
    # odd string length case
    elif len(s) == 1:
        return True

    # if characters from both ends of the string are equal
    if s[0] == s[len(s) - 1] and is_palindrome:
        is_palindrome = True
        # pass a slice version of the string
        # removing the beginning and end characters
        return recursive_palindrome(s[1: len(s) - 1], is_palindrome)
    else:
        return False

if __name__ == "__main__":
    print(recursive_palindrome("racecar"))
    print(recursive_palindrome("ygohangasalamiimalasagnahogy"))

    assert recursive_palindrome("racecar") == True
    assert recursive_palindrome("gohangasalamiimalasagnahog") == True
    #assert recursive_palindrome("abragadabra") == False