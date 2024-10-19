# A recursive algorithm to compute the integer part of the base two logarithm of n using only addition and integer
# and integer division

"""
def logbase2(number):
    divide n by 2
    if n is less than 1:
        return 0

    return 1 + logbase2(n / 2)
"""


def logbase2(n):
    n /= 2
    if n < 1:
        return 0

    return 1 + logbase2(n / 2)

if __name__ == "__main__":
    print(logbase2(9))