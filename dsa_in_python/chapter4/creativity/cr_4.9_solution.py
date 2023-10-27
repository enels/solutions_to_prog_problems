def find_max_min(s, next_index=1):
    """
        Desc: Finds the maximum and minimum values in a sequence without using loops
        the first and last numbers are assumed to be the minimum and maximum numbers resp.
    :param s: sequence of numbers
    :param next_index: index of next numbers to compare with the assumed min and max
    :return: a tuple of min and max values
    """
    # second to the last number reached
    if next_index == len(s) - 1:
        return s[0], s[len(s) - 1]

    # if minimum number is greater than current number
    if s[0] > s[next_index]:
        # switch them
        s[0], s[next_index] = s[next_index], s[0]

    # if max (last) number less than current number
    if s[len(s) - 1] < s[next_index]:
        # switch them
        s[len(s) - 1], s[next_index] = s[next_index], s[len(s) - 1]

    # if # minim is greater than the less number between the max and the current
    if s[0] > s[next_index]:
        # switch them
        s[0], s[next_index] = s[next_index], s[0]

    # recursively call the function
    return find_max_min(s, next_index + 1)

if __name__ == "__main__":
    s = [7, 17, 2, 28, 12, 6, 500, 1]
    print(find_max_min(s))