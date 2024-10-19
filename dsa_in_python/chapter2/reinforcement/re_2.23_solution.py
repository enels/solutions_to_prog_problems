from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):

    @abstractmethod
    def __getitem__(self, j):


    def __contains__(self, val):
        """ Returns True if val found in sequence"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        """ Returns the number of elements equal to given value"""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):
        """
        Checks the equalit of two sequences
        """

        seq_len = len(self)
        for c in range(seq_len):
            if self[c] == other[c]:
                continue
            else:
                break

        if c == seq_len - 1:
            return True
        else:
            return False

    def __lt__(self, other):
        """
        lexicographically compare two sequences
        """
        seq_len = len(self) # get length of sequence

        for c in range(seq_len):
            if self[c] < other[c]: # if seq1 is less than seq2
                return True
            elif self[c] > other[c]: # if seq1 is greater than seq2
                return False
            else:
                continue