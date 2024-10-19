if __name__ == '__main__':
    N = int(input())
    
    result = list()
    command = list()

    # initialize the result to zero
    for i in range(N):
        #result.append(0)
        command.append(list())


    # collect input, split each input into
    # the command array index
    for i in range(N):
        s = input()
        command[i] = s.split()

    for i in range(N):
        if command[i][0] == 'insert':
            result.insert(int(command[i][1]), int(command[i][2]))
        elif command[i][0] == 'print':
            print(result)
        elif command[i][0] == 'remove':
            result.remove(int(command[i][1]))
        elif command[i][0] == 'append':
            result.append(int(command[i][1]))
        elif command[i][0] == 'sort':
            result.sort()
        elif command[i][0] == 'pop':
            result.pop()
        elif command[i][0] == 'reverse':
            result.reverse()
