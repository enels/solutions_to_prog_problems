class ReverseSequenceIterator:
    """
    An iterator of any of Python's sequence types
    """

    def __init__(self):

        self._seq = [2, 3, 9, 1, 4, 10, 12]
        self._k = len(self._seq)          # will increment to 0 on first call to next

    def __next__(self):
        """
        Return the next element, or else raise StopIterator
        """
        self._k -= 1

        if self._k >= 0:
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        """
        By convention, an iterator must return itself as an iterator
        """
        return self


if __name__ == "__main__":

    seq = ReverseSequenceIterator()
    for n in seq:
        print(n, end=" ")