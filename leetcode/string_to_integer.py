class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # store the possible digits
        possible_digits = "0123457689"

        result = 0
        char_index = 0  # starts counting when inside the string
        in_string = False
        negative = False
        for c in s:
            if c.isspace():
                if in_string:
                    break
                continue
            elif c in possible_digits:
                if c == "0":
                    pass
                elif c == "1":
                    result += 1
                elif c == "2":
                    result += 2
                elif c == "3":
                    result += 3
                elif c == "4":
                    result += 4
                elif c == "5":
                    result += 5
                elif c == "6":
                    result += 6
                elif c == "7":
                    result += 7
                elif c == "8":
                    result += 8
                elif c == "9":
                    result += 9
            elif c not in possible_digits:
                if c == "-":
                    # first character is -
                    if char_index == 0:
                        negative = True
                    else:
                        break
                elif c == "+":
                    # first character occurrence
                    if char_index == 0:
                        pass
                    else:  # within the string
                        break
                else:
                    break
            result *= 10
            char_index += 1
            in_string = True

        # remove the last zero
        result /= 10

        # iterate pow(2, 32) - allowed range
        allowed_range = 2
        for n in range(31):
            allowed_range *= 2

        allowed_range /= 2  # divide by 2 since it's unsigned.
        if negative == True:
            allowed_range *= -1
            result *= -1
            if result <= allowed_range:
                return allowed_range
        elif negative == False:
            if result >= allowed_range:
                return allowed_range - 1

        return result