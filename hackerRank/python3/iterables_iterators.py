# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

# length of the list n
list_len = int(input())

# n spaced-seperated lowercase letters
letters = input().split()

# the numeber of indices to be selected
n_indices = int(input())

s = ""
# iterate through tthe letters to get the index of the letters
for i in range(list_len):
    s += str(i + 1)

# get the possible combination
combination_res = list(combinations(s, n_indices))

print(combination_res)

# iterate through the letter to find where letter 'a' exists
a_indexes = list()
for i in range(list_len):
    if letters[i] == 'a':
        a_indexes.append(str(i+1))

# frequency to count the number of occurrences of letter 'a' indexes
# in the combination
counter = 0

print(a_indexes)

# # iterate through the letters to get the possible combination of the
# indices of letter a position
a_index_set = set(a_indexes)
for value in combination_res:
    # iterate through the 'a' indexes
    value_set = set(value)
    if len(a_index_set.intersection(value_set)) >= 1 or \
    len(value_set.intersection(a_index_set)) >= 1:
        counter += 1

# get the probability
probability = counter / len(combination_res)

print(probability)

