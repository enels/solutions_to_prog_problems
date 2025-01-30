# Enter your code here. Read input from STDIN. Print output to STDOUT

# collect the number of test cases
n_tests = int(input())

# collect the number of test cases
for _ in range(n_tests):
    
    # collec the block size
    block_size = int(input())
    
    # create the block list
    block = list()
    
    # collect the block values in string format
    str_block_values = input().split()
    
    # convert the string block values format to integer format
    block_values = list()
    for value in str_block_values:
        block_values.append(int(value))
    
    # if the maximum cubes is not at either of both ends of the list
    if max(block_values) != block_values[-1] or max(block_values) != block_values[0]:
        print("No")
        continue
    
    # set if the test case passes or not
    test_pass = True
    
    # Begin arrangement of the cubes
    # check if the arrangement can be done from the right
    if max(block_values) == block_values[-1]:
        for n in range(block_size-2, 0, -1):
            if block_values[n] > block_values[n-1]:
                pass
            else:
                test_pass = False
    
    # check if the arrangement can be done from the left
    if max(block_values) == block_values[0]:
        for n in range(block_size-1):
            if block_values[n] > block_values[n+1]:
                pass
            else:
                test_pass = False
    
    if test_pass == False:
        # compare right to left
        # get the mid value
        mid = block_size / 2
        
        for n in range(mid):
            # moving from the left hand side
            left = block_values[n]
            
            # moving from the right hand side
            right = block_values[block_size-n+1]
        
# first check if the maximum is one either ends
