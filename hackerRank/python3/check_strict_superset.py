# Enter your code here. Read input from STDIN. Print output to STDOUT

# get the spaced elements of set A
setA = set(map(int, input().split()))

# get how many is other sets
n = int(input())

# store the final result - True or False
res = True

# get the spaced elements of other sets
for _ in range(n):
    other_set = set(map(int, input().split()))
    
    if len(other_set.difference(setA)) == 0 and other_set.issubset(setA):
        pass
    else:
        res = False
        break


print(res)
