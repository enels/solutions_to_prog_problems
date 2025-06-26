import re

# Enter your code here. Read input from STDIN. Print output to STDOUT
max_input = int(input())

# list container to store the values
values_list = list()

# collect the string
for _ in range(max_input):
    values_list.append(input())

# validate each string to check for floating string
dot_found = False
all_digit = True


for value in values_list:
    # iterate through each value of the string
    current_index = -1
    n_dots = 0
    for c in value:

        current_index += 1
        # a floating string found
        if c == ".":
            dot_found = True
            n_dots += 1
            
            # if current_index != 0 and current_index != len(value)-1:
            #     if value[current_index-1].isalnum() == False or value[current_index+1].isalnum() == False:
            #         all_digit = False
        
        elif c.isalpha():
            all_digit = False
        
        else:
            pass
            
    # print the value state - if it's float or not
    if (dot_found and all_digit and n_dots == 1):
        print(True)
    else:
        print(False)
    
    # reset the booleans
    dot_found = False
    all_digit = True

