class FirstDerivative:
    """
    Calculate the first derivative of the equation
    Equation input format:  2x^3 + x^2 + 4x + 5
    """
    def __init__(self, equation_string):
        self._equation = equation_string
        self._third_order = ""
        self._second_order = ""
        self._first_order = ""
        self._constant = ""

    def _split_equation(self, equation_string):
        """
        Splits the equation into different parts of degrees
        """
        # split the equation using the + sign
        equation_list = self._equation.split()



        self._third_order = equation_list[0]  # 2x^3
        self._first_sign = equation_list[1] # - or +
        self._second_order = equation_list[2]
        self._second_sign = equation_list[3] # - or +
        self._first_order = equation_list[4]  # 4x
        self._constant = equation_list[3]     # 5

    def _split_order(self, order):
        """
        Splits the order of the equation
        """

        # collect the last index value in order
        last_index_value = order[-1]
        first_index_value = order[0]

        # if last index value is a digit
        if last_index_value != "x": # it's a digit
            # convert to an int
            power = int(last_index_value)
        else:
            power = 1

        # if the first index value is a digit
        if first_index_value != "x": # it has a coefficient
            coefficient = int(first_index_value)
        else:
            coefficient = 1  # absence of a coefficient

        # return the coefficient, middle letter("x"), and the power
        order_list = [coefficient, "x", power]

        return order_list

    def _derivate(self, order):
        """
        Calculate the derivative(differential calculus) of the order
        """

        power = order[-1]

        coefficient = order[0] * power
        power -= 1

        if power != 0:
            if power == 1:
                return str(coefficient) + "x"
            else:
                return str(coefficient) + "x^" + str(power)
        else:
            return str(coefficient)

    def derivative(self):
        """
        Get the derivative of each part of the equation seperately
        """
        # split the equation
        self._split_equation(self._equation)
        third_order_list = self._split_order(self._third_order)
        second_order_list = self._split_order(self._second_order)
        first_order_list = self._split_order(self._first_order)

        answer = ""
        # get the derivative
        answer = self._derivate(third_order_list) + " {} ".format(self._first_sign)
        answer += self._derivate(second_order_list) + " {} ".format(self._second_sign)
        answer += self._derivate(first_order_list) + " "

        return answer

if __name__ == "__main__":
    equation = "2x^3 - 6x^2 + x + 5"
    equ = FirstDerivative(equation)

    print(equ.derivative())