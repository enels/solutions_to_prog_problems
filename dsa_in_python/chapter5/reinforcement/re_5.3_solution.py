import sys
data = []
n = 10

for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    # pop out the value when index is a factor of 3
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    if k % 3 == 0 and len(data) != 0:
        data.pop()
        b = sys.getsizeof(data)
        print('After popping: Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)