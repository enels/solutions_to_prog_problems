import numpy

n = int(input())

# create the list
a = list()

# collect the elements and split them into seperate list element to form a 2D list
for _ in range(n):
    a.append(input().split())

# convert each element in the 2D list in to a float
for i in range(n):
    for j in range(n):
        a[i][j] = float(a[i][j])

print(numpy.round(numpy.linalg.det(a), decimals=3))
