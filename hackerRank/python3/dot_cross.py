import numpy


n = int(input())

A = list()
B = list()

n_lines = n * 2

for i in range(n_lines):
    if i < n_lines / 2:
        A.append(list(map(int, input().split())))
    else:
        B.append(list(map(int, input().split())))

A_numpy = numpy.array(A)
B_numpy = numpy.array(B)

print(numpy.matmul(A_numpy, B_numpy))

