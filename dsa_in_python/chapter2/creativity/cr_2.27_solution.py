class Range:
    """
    A class that mimic's the built-in class range
    """
    def __init__(self, start, stop=None, step=1):
        """
        Initializes Range class

        Semantics is similar to built-in class
        """

        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None:            # special case of rnage(n)
            start, stop = 0, start  # should be treated as if range(0, n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step -1 ) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __contains__(self, val):
        """ A more efficient method of the contains method
            to check for the existence of a value in a range
        """

        # if the value to find is 1 and less than stop value
        if self._step == 1 and val < self._stop:
            return True
        # if the value to find is divisible by the step and
        # less than the stop value
        elif val % self._step and val < self._stop == 0:
            return True
        # if the value to find is nto divisible by the step value.
        # not in range
        elif val % self._step != 0:
            return False

if __name__ == "__main__":
    r = Range(0, 100, 2)
    if 100 in r:
        print(True)
    else:
        print(False)