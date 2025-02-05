n = int(input())

n_ints = list(map(int, input().split()))

# 3 lines solution
res = [i > 0 for i in n_ints] # all positive
res2 = [i < 10 for i in n_ints] # any palindromic integer
print(all(res) and any(res2))
