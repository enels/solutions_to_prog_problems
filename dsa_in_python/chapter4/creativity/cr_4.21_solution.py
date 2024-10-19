def power(m, n):
    """
    get the power of m to n nonrecursively
    :param m: integer
    :param n: power
    :return: power of m ton
    """

    result = 1
    for i in range(n):
        result *= m

    return result

if __name__ == "__main__":
    print(power(2, 6))