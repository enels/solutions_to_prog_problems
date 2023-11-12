def sum_pairs(s, k, current_index=0, next_index=1, overall_index=0):
    """
    get the sum of a pair that results in k
    :param s: integer sequence
    :param current_index: current index of sequence
    :param next_index: next index of sequence
    :param overall_index: overall count of the recursive loop
    :return: pair of integers in tuple
    """

    # get to the end of the sequence without finding any pair
    if overall_index == len(s):
        return 0

    # internal recursion got to the end of the sequence
    if current_index == len(s) - 1:
        return sum_pairs(s, k, overall_index+1, overall_index+2, overall_index+1)

    if s[current_index] + s[next_index] == k:
        return s[current_index], s[next_index]
    elif s[current_index] + s[next_index] != k:
        return sum_pairs(s, k, current_index, next_index + 1, overall_index)

if __name__ == "__main__":
    print(sum_pairs([2,3,5,1,4], 7))