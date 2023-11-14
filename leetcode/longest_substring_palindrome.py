def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    # length of string
    s_len = len(s)

    # stores current maximum length of sub palindrome
    max_len_sub_palin = 0
    max_palin_str = max_sub_palin = ""


    for n in range(s_len):
        start_c = s[n]
        inner_c = ""
        for c in s[n + 1:]:
            if c != start_c:
                inner_c += c
            else:
                inner_c += c
                start_c += inner_c

                # check if it's a palindrome
                start_c_len = len(start_c)
                mid = start_c_len // 2

                # assumgin it's a palindrome
                is_palindrome = True
                for n in range(mid):
                    start_c_len -= 1
                    if start_c[n] == start_c[start_c_len] and is_palindrome:
                        pass
                    else:
                        is_palindrome = False
                        break

                if max_len_sub_palin < len(start_c) and is_palindrome:
                    max_palin_str = start_c
                    max_len_sub_palin = len(start_c)

    return max_palin_str

if __name__ == "__main__":
    print(longestPalindrome("bbabbbcdea"))
