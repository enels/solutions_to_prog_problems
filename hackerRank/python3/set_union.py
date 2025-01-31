# Enter your code here. Read input from STDIN. Print output to STDOUT

# n students who have subscribed to english
n = int(input())

# english students roll numbers
roll_n = set(map(int, input().split()))

# n students who have subscribed to french
b = int(input())

# french students roll numbers
roll_b = set(map(int, input().split()))

# total number of studetns who have at least one subscription
print(len(roll_n.union(roll_b)))
