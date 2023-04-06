from random import shuffle

'''
    outputs all possible string possible by the string combination
    'c', 'a', 't', 'd', 'o', 'g' exactly once
'''
# store the characters in a list
s = ['c', 'a', 't', 'd', 'o', 'g']

# get the factorial of the len of s
s_len = len(s)

# number of possible word to be formed
ntimes = 1

for n in range(1, s_len + 1):
    ntimes *= n

# container to store the possible strings
s2 = list()

for n in range(ntimes):
    # randomize the chars in list
    shuffle(s)
    # str handle to store the newly formed string
    s3 = ""
    for c in s:
        s3 += c
    if s3 in s2:
        pass
    else:
        s2.append(s3)

print(s2)