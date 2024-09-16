n = int(input())
arr = map(int, input().split())
    
arr_list = list(arr)
    
# create a set to collect the unique values
arr_set = set()
for i in arr_list:
    arr_set.add(i)

# cast it to a list
arr_list = list(arr_set)

# sort the list
arr_list.sort()

# collect the second to the last sorted element
# using list slicing
print(arr_list[len(arr_list) - 2])
