class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # assuming it's possitive
        negative = False

        # check if x is negative
        if x < 0:
            x = x * -1
            negative = True

        # get the number of digits
        x_value = x
        n_digits = 0
        while x_value != 0:
            x_value /= 10
            n_digits += 1

        # get the reverse string
        # initialize result tozero
        result = 0
        for digit in range(n_digits):
            # divide 10
            rem = x % 10
            result += rem
            result *= 10
            x /= 10

        # remove the last zero
        result /= 10

        # iterate pow(2, 32)
        allowed_range = 2
        for n in range(31):
            allowed_range *= 2

        # get the allowed range in the machien
        # 32bit machine
        allowed_range /= 2
        if negative == True:
            allowed_range *= -1
            result *= -1
            if result <= allowed_range:
                return 0
        elif result >= allowed_range:
            return 0

        return result