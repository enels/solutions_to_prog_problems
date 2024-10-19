# Algorithm to recursively find the maximum number in a sequence without using any loops.
"""
def findmax(Sequence, next_index):
    if next_index is equal to length of Sequence:
        return Sequence[0]
    if Sequence[0] is less than Sequence[next_index]:
        Sequence[0] = Sequence[next_index]
    return findmax(Sequence, next_index + 1)

Running Time: O(n-1)
"""