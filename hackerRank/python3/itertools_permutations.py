# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

string = input().split()

word, size = string[0], int(string[1])

obj = permutations(word, size)

result = []
s = ""

obj_list = list(obj)

for obj_idx in range(len(obj_list)):
    for tup in obj_list[obj_idx]:
        s += tup

    # stores the word in the result
    result.append(s)

    # reinitializes the string container to store the tuple values
    s = ""

result.sort()

for w in result:
    print(w)