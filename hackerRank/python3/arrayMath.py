# Enter your code here. Read input from STDIN. Print output to STDOUT
# get the number of rows and columns
import numpy

user_input = input()
n = int(user_input[0])
m = int(user_input[2])

# create the list to store the array values
arr_list = list()
a_list = list()
b_list = list()

n += 1
# collect the array values
for i in range(n - 1):
    a_list.append(input())

for i in range(n - 1):
    a_list.append(input())

a = list()

for i in range(n - 1):
    for j in range(m):
        if a_list[i][j].isdigit():
            a[i].append(int(a_list[i][j]))
    b_list.append(input())

#(for i in range(n - 1):
#    b_numpy.append(list())
#    a_numpy.appedn(list())

result = list()

for i in range(n - 1):
    result.append(numpy.array(b_list[i]) + numpy.array(a_list[i]))
    print(result);

#for i in range(n - 1):
#    result.append(numpy.array(b_numpy[i]) - numpy.array(b_numpy[i]))
