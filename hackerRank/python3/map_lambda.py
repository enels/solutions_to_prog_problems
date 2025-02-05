cube = lambda x: x * x * x

def fibonacci(n):
    # return a list of fibonacci numbers
    l = []
    
    # check for edge cases
    if n == 1:
        l.append(0)
        return l
    if n == 0:
        return l
        
    # initialize the fibonacci list
    l.append(0)
    l.append(1)
    
    for i in range(2, n):
        l.append(l[i-1] + l[i-2])
    
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
