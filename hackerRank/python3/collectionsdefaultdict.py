# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# get the number of characters in A and B respectively
n_chars = input().split(" ")

# store n and m as integers
n = int(n_chars[0])
m = int(n_chars[1])

# set A and B as string type
A = list()
B = list()

# collect the characters in string A and B
# collect for A
for _ in range(n):
    A.append(input())
    
# collect for B
for _ in range(m):
    B.append(input())

# create a dictionary of list where the list are the elements of B
dd = defaultdict(list)

# store each character index in A into the default dict
for i in range(len(A)):
    # append a 1-index position, hence the +1
    dd[A[i]].append(i+1)

# iterate through each character and print out their various positions
for w in B:
    if w in A:
        for pos in dd[w]:
            print(str(pos) + " ", end="")
    else:
        print(-1, end="")
    print()
