from itertools import groupby

# get user's input
sample_input = input()

# location to store the keys and the orderly frequency
keys = list()
order_freq = list()

# get the keys and the iterable values
for k,v in groupby(sample_input):
    keys.append(k)
    order_freq.append(list(v))

# iterate through the keys and order frequency
counter = 0
for idx in range(len(keys)):
    for _ in order_freq[idx]:
        counter += 1
    print("({}, {})".format(counter, keys[idx]), end=" ")
    
    # re-initialize the counter
    counter = 0
