# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

# collect the input from user
string = input().split()

# extract the words into words and size to split the words
word, size = string[0], int(string[1])

# get the combinations with replace result
comb_result = list(combinations_with_replacement(word, size))

# sort the result
comb_result.sort()

# store each of the string that makes up each tuple value from comb_result
t_str = ""

# list to store the sorted string
t_list = list()

# iterate through each string in the resulting tuple list
for t in comb_result:
    # iterate each character in the tuple word itself
    for c in t:
        # stringify the character
        t_str += c
    
    # sort the result string
    t_str_sorted = sorted(t_str)
    
    # iterate through each sorted characters, for a new string,
    # and then append to the final list
    s = ""
    for c in t_str_sorted:
        s += c
    # extend the sorted list
    t_list.append(s)
    t_str = ""

# sort the final overall list
t_list.sort()

# print the result
for w in t_list:
    print(w)  
