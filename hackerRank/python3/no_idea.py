# Enter your code here. Read input from STDIN. Print output to STDOUT

# get the number of integers in array and A,B respectively
n_m = input().split()

# get the arrays
arr = input().split()

# get A and B
A = input().split()
B = input().split()

# convert A and B into set
A_set = set(A)
B_set = set(B)

# happiness
happiness = 0

# calculate happiness
# if arr value is in A: happiness + 1
# if arr value is in B: happiness - 1
for i in arr:
    if i in A_set:
        happiness += 1
    if i in B_set:
        happiness -= 1

print(happiness)

