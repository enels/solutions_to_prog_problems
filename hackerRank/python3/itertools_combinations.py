# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

# collect the input from user
string = input().split()

# extract the words into words and size to split the words
word, size = string[0], int(string[1])

# stores the word from each tuple
s = ""

# stores the temporary result
temp_result = list()

# stores the final result
final_result = list()

# store the
for obj_idx in range(1, size+1):
    # permuatate the words in the specified length(size)
    obj = combinations(word, obj_idx)
    # converts the iteratable object to a list
    obj_list = list(obj)

    # iterate through each set of tuple value in list
    for chars_tup in obj_list:
        # concat each character in the tuples

        # iterate through each set of character in tuple to form a word
        for char in chars_tup:
            s += char

        # sort the word
        sorted_s = sorted(s)

        # for a new sorted string from the list formed from the sorted string
        s = ""
        for c in sorted_s:
            s += c

        # stores the word in the result
        temp_result.append(s)

        # reinitializes the string container to store the tuple values
        s = ""

    # sort the result
    temp_result.sort()

    # append the result to the final output to maintain the sorted order
    for r in temp_result:
        final_result.append(r)

    # re-initialize the result for fresh input from another combination of the word
    temp_result = list()


# print out the result
for w in final_result:
    print(w)
