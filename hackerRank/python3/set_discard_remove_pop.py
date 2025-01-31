n = int(input())
s = set(map(int, input().split()))

# catches the return key
n_commands = int(input())

for _ in range(n_commands):
    # get operation
    user_input = input().split()
    
    # catches the return key
    #input()
    
    # pop command
    if user_input[0] == 'pop':
        s.pop()
        
    # remove command
    elif user_input[0] == 'remove':
        value = int(user_input[1])
        s.remove(value)
    
    # discard command
    elif user_input[0] == 'discard':
        value = int(user_input[1])
        s.discard(value)

print(sum(s))

