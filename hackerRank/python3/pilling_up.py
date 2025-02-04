# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque


n_test_cases = int(input())

for _ in range(n_test_cases):
    # number of block item in block array
    n_blocks = int(input())
    
    # block array
    blocks = list(map(int, input().split()))
    
    # assuming the blocks will fit
    result = 'Yes'
    
    # maximum movement count - 4 - left->right, right->left
    # right-end->left-end, left-end->right-end
    max_movement = 4
    
    reversed_blocks = list(reversed(blocks))
    
    # move from right down to left in order
    for i in range(len(reversed_blocks)-1):
        if i > reversed_blocks[i+1]:
            pass
        else:
            result = 'No'
    
    # move from left to right
    for i in range(len(blocks)-1):
        if i > blocks[i+1]:
            pass
        else:
            result = 'No'
    
    # move right_end->left_end
    blocks_deck = deque(blocks)
    
    
    
    # move left_end->right_end
    
    

print(result)
