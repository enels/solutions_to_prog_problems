# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

# collect the input from user
string = input().split()

# extract the words into words and size to split the words
word, size = string[0], int(string[1])

# permuatate the words in the specified length(size)
obj = permutations(word, size)

# stores the character combination
result = []

# stores the word from each tuple
s = ""

# covverts the iteratable object to a list
obj_list = list(obj)

# store the
for obj_idx in range(len(obj_list)):
    for char in obj_list[obj_idx]:
        # concat each character in the tuples
        s += char

    # stores the word in the result
    result.append(s)

    # reinitializes the string container to store the tuple values
    s = ""

# sorted the result
result.sort()

# print out the result
for w in result:
    print(w)