import sys
data = []
n = 10
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
    # pops out the last value when k is even
    # to check the underlying array size
    if k % 2 == 0 and k != 0:
        data.pop()
        data.pop()
        a = len(data)
        b = sys.getsizeof(data)
        print('After removing an element - Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        # restore back the length
        data.append(None)