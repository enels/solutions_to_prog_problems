class Vector:
    """
    Represents a vector in a multidimentional space
    """

    def __init__(self, d):
        """
        Create d-dimensional vectors of zeros
        """
        self._coords = [0] * d

    def __len__(self):
        """
        Return the dimension of the vector
        """
        return len(self._coords)

    def __getitem__(self, j):
        """
        Return the jth item of the vector
        """
        return self._coords[j]

    def __setitem__(self, j, val):
        """
        Set the jth item of the vector to a given val
        """

        self._coords[j] = val

    def __add__(self, other):
        """
        Return sum of two vectors
        """
        if len(self) != len(other):
            raise ValueError("dimensions must agree!")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        """
        Performs subtraction of two vectors

        Returns an instance of the resulting vector
        """
        len_of_self = len(self._coords)
        if len_of_self != len(other._coords):
            print("Unequal length")
            return -1

        result = [self._coords[c] - other._coords[c] for c in range(len_of_self)]

        return result

    def __eq__(self, other):
        """
        Return True if vectors have the same coordinates
        """
        return self._coords == other._coords

    def __ne__(self, other):
        """
        Return True if vectors differs from other
        """
        return not self == other

    def __neg__(self):
        """
        Returns the negative values of the vectors
        """
        len_of_self = len(self)

        for c in range(len_of_self):
            self._coords[c] *= -1

        return self._coords

    def __mul__(self, val):

        v_len = len(self)
        for i in range(v_len):
            self._coords[i] *= 3

        return self._coords

    def __str__(self):
        """
        Produce string representation of vector"
        """
        return '<' + str(self._coords)[1:-1] + '>'

if __name__ == "__main__":
    my_vector = Vector(8)

    for i in range(1, 9):
        my_vector[i-1] = i

    print(my_vector * 3)