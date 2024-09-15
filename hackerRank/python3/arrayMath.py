# Enter your code here. Read input from STDIN. Print output to STDOUT
# get the number of rows and columns
import numpy

user_input = input()
n = int(user_input[0])
m = int(user_input[2])

# create the list to store the array values
arr_list = list()

n += 1
# collect the array values
for i in range(n):
    arr_list.append(input())

arr_list_2 = list()

# get the number of rows
for i in range(n):
    arr_list_2.append(list())

m += m - 1
print(arr_list_2)
# cast the integer string in the array into a pure int
for i in range(n):
    for j in range(m):
        if arr_list[i][j].isdigit():
            arr_list_2[i].append(int(arr_list[i][j]))

print(arr_list_2)
# create a list to store the various results
result = list(list())

# convert to numpy array and add
for i in range(n-1):
    result.append(numpy.array(arr_list_2[0]) - numpy.array(arr_list_2[i+1]))

print("[" + str(result[0]) + "]")
