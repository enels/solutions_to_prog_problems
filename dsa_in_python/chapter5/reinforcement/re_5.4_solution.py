import ctypes

def DynamicArray:
    """A dynamic array class akin to a python list"""

    def __init__(self):
        self._n = 0         # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-leval array

    def __len__(self):
        """return number of elements stored in array"""
        return self._n

    def __getitem__(self, k):
        """return element at index k"""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        # including negative index
        elif 0 > k >= self._n * -1:
            return self._A[self._n + k]
        return self._A[k]

    def append(self, obj):
        """add object to the end of the array"""
        if self._n == self._capacity:
            self.resuze(2 * self._capacity)
        self.A[self._n] = obj
        self._n += 1

    def _resize(self, c):       # nonpublic utilit
        """resize internal array to capacity c"""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """return new array with capacity c"""
        return (c * ctypes.py_object)()