# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

# collect the input from user
string = input().split()

# extract the words into words and size to split the words
word, size = string[0], int(string[1])

# permuatate the words in the specified length(size)
obj = combinations(word, size)

# stores the character combination
result = []

# stores the word from each tuple
s = ""

# print out the unique possible charcters
# stores the unique characters
char_set = set()

for char in word:
    char_set.add(char)

# append the result
for value in char_set:
    result.append(value)

# get the length of the unique characters
result_len = len(result)

# sort the unique characters
result.sort()


# converts the iteratable object to a list
obj_list = list(obj)

result2 = list()

# store the
for obj_idx in range(len(obj_list)):
    for char in obj_list[obj_idx]:
        # concat each character in the tuples
        s += char

        # convert the string to list obj
        s_list = list(s)

        # sort the list
        s_list.sort()

        # reinitialize the string to collec the sorted list
        s = ""

        # re-concantenate the new sorted list in a string
        for c in s_list:
            s += c

    # stores the word in the result
    result2.append(s)

    # reinitializes the string container to store the tuple values
    s = ""

result2.sort()

# append the sorted result to the previous one
for r in result2:
    result.append(r)

#result[result_len:].sort()

# print out the result
for w in result:
    print(w)