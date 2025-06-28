import numpy


nm_list = list(map(int, input().split()))

n = nm_list[0]
m = nm_list[1]

arr = list()

for i in range(n):
    #arr.append(list())
    arr.append(list((map(int, input().split()))))

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round((numpy.std(arr, axis=None)),11))

