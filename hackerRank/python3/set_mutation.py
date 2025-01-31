# Enter your code here. Read input from STDIN. Print output to STDOUT

# number of elements in A
n_A = int(input())

# A elements
A = set(map(int, input().split()))

# number of other sets
nOthers = int(input())

# collect the
for _ in range(nOthers):
    
    # get the operation and the number of elements in the next set
    operation_n_items = input().split()
    
    # get the space seperated elements
    next_set = set(map(int, input().split()))
    
    if operation_n_items[0] == "intersection_update":
        A.intersection_update(next_set)
    elif operation_n_items[0] == "update":
        A.update(next_set)
    elif operation_n_items[0] == "symmetric_difference_update":
        A.symmetric_difference_update(next_set)
    elif operation_n_items[0] == "difference_update":
        A.difference_update(next_set)
        

print(sum(A))
