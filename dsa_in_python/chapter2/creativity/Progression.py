class Progression:
    """ Iterator producing a generic progression

    Default iterator produces the whole numbers 0, 1, 2, 3
    """

    def __init__(self, start=0):
        self._current = start

    def _advance(self):

        """ This should be overriden by subclass to customize progression"""
        self._current += 1

    def __next__(self):
        """ Return the next element, or else raise StopIteration error"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self     # By convention, an iterator returns itself

    def print_progression(self, n):
        """ Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))