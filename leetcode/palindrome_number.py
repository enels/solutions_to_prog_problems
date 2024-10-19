class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        total_digits = 0
        digits_list = list()

        # store the digits in x in a reverse order
        y = 0 # store the value of x after division
        while x > 0:
            digits_list.append(x % 10)
            total_digits += 1
            x //= 10

        
        # last digit in x
        digits_list.append(x % 10)
        total_digits += 1

        mid_index = total_digits / 2
        total_digits_end = total_digits - 1

        is_palindrome = True
        for n in range(mid_index):
            total_digits_end -= 1
            if digits_list[n] == digits_list[total_digits_end] and is_palindrome:
                pass
            else:
                is_palindrome = False
                break
        
        return is_palindrome
