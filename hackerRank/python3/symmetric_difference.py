# Enter your code here. Read input from STDIN. Print output to STDOUT

# get number of M integers
M_ints = int(input())

# M set
M_set = set()

# get M integer values
M_list = input().split()

# catches the return key
input()

for n in M_list:
    M_set.add(int(n))

# get number of N integers
N_list = input().split()

# N set
N_set = set()

# get N integer values
for n in N_list:
    N_set.add(int(n))

# the result set
result_set = set()

# get the differnce between both M_aet and N_set
new_set = M_set.difference(N_set)
new_set.update(N_set.difference(M_set))

#M_set.union(N_set)

# sort the new set
new_set = sorted(new_set)

for i in new_set:
    print(i)
