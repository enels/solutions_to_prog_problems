from Progression import Progression
from math import sqrt

class SquareProgression(Progression):
    """ Iterator producing a generic progression

    Default iterator produces the whole numbers 0, 1, 2, 3
    """

    def __init__(self, start=65536):
        self._current = start

    def _advance(self):

        self._current = sqrt(self._current)

        return self._current

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

if __name__ == "__main__":
    prog = SquareProgression()
    prog.print_progression(10)