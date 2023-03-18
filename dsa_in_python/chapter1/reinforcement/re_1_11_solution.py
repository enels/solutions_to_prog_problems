values_needed = [1, 2, 4, 8, 16, 32, 64, 128, 256]

# python's comprehension
result = [value for value in range(257) if value in values_needed]

print("Using comprehension {} ".format(result))
l = list()
# without python's comprehension
for r in range(1, 257):
    # initialize with values 1 and 2
    if r == 1 or r == 2:
        l.append(r)

        # store the next element which helps to store
        # the value after 2 as 4
        next_element = r * 2
        # check if the next_element is equal to the current iterated element
    elif r == next_element:
        l.append(next_element)
        # agian store the next expected element
        next_element = r * 2

print("Without comprehension {} ".format(l))