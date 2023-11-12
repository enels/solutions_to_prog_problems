def ranking(s, k, less_than_k=[], greater_than_k=[], next_index=0):
    """
    rearranges sequence of a integer values to seperate even from odd numbers
    :param s: integer values to be arranged
    :param less_than_k: numbers less than k
    :param less_than_k: numbers greater than k
    :param k: a bridge between the numbers (< k on left, > k on the right)
    :param next_index: next integer index in s
    :return: arranged integer values
    """

    # base case
    if len(s) == next_index:
        return less_than_k + greater_than_k

    if s[next_index] < k:
        less_than_k.append(s[next_index])
        return ranking(s, k, less_than_k, greater_than_k, next_index + 1)
    elif s[next_index] == k:
        return ranking(s, k, less_than_k, greater_than_k, next_index + 1)
    else:
        greater_than_k.append(s[next_index])
        return ranking(s, k, less_than_k, greater_than_k, next_index + 1)


if __name__ == "__main__":
    l = [20, 3, 1, 3, 21, 12, 15, 7, 19, 49, 7, 23, 1, 10]
    print(ranking(l, 10))