# Algorithm
"""
functionname(m, n)
    # set the base case
    if n decreases to 0:
        return 0

    # return the function while reducing the value of n by 1 and adding m
    return functionname(m, reduce n by 1) + m
"""

# Python code
def productbyaddition(m, n):
    """
    :param m: first variable
    :param n: recursive variable count
    :return: sum of m with itself n times
    """

    # base case
    if n == 0:
        return 0
    return productbyaddition(m, n - 1) + m

if __name__ == "__main__":
    # test
    print(productbyaddition(2, 3))

    assert (productbyaddition(2, 3) == 6)
    #assert (productbyaddition(4, 3) == 13)
    assert (productbyaddition(2, 4) == 8)
    assert (productbyaddition(9, 9) == 81)