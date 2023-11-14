class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # one character string
        if len(s) == 1 or len(s) == 2 and s[0] != s[1]:
            return s[0]

        # length of strin
        s_len = len(s)

        # stores current maximum length of sub palindrome
        max_len_sub_palin = 0
        max_palin_str = max_sub_palin = ""

        for i in range(s_len - 1):
            start_c = s[i]
            inner_c = ""
            for c in s[i + 1:]:
                if c != start_c:
                    inner_c += c
                else:
                    inner_c += c  # last character encountered
                    start_c += inner_c

                    # check if it's a palindrome
                    start_c_len = len(start_c)
                    mid = start_c_len // 2

                    # assigning it's a palindrome
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

                    # reassign it to the beginning of the current substring
                    start_c = s[i]

        if len(max_palin_str) == 0:
            return s[0]

        return max_palin_str