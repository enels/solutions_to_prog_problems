def factor(n):
    # get half the number
    k = n // 2
    # make sure division with number is less than zero
    while k != 0:
        # if its a factor
        if n % k == 0:
            yield k
            # if it's a perfect square
            if k * k != n:
                yield n // k
        k -= 1