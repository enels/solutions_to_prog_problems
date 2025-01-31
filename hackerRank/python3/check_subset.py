# Enter your code here. Read input from STDIN. Print output to STDOUT

# get the number of test cases T
T = int(input())

for _ in range(T):
    # get the number of elements in A
    nA = int(input())
    
    # get n spaced elements in A
    elements_in_A = set(map(int, input().split()))
    
    # get the number of elements in B
    nB = int(input())
    
    # get n spaced elements in B
    elements_in_B = set(map(int, input().split()))
    
    print(elements_in_A.issubset(elements_in_B))
