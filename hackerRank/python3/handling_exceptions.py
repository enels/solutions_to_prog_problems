# Enter your code here. Read input from STDIN. Print output to STDOUT

n_test_cases = int(input())

for _ in range(n_test_cases):
    values = input().split()
    try:
        values[0] = int(values[0])
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: '{}'".format(values[0]))
        continue
        
    
    try:
        values[1] = int(values[1])            
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: '{}'".format(values[1]))
        continue
        
    # try division by zero if it passes the value test
    try:
        print(values[0] // values[1])
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
        
