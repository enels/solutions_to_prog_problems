from Progression import Progression


class DifferenceProgression(Progression):
    """ Iterator producing a generic progression

    Default iterator produces the whole numbers 0, 1, 2, 3
    """

    def __init__(self, start=2, next=200):
        self._current = next
        self._previous = start

    def _advance(self):

        self._current = self._current - self._previous

        if self._current < 0:
            self._current *= -1

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
    prog = DifferenceProgression()
    prog.print_progression(10)