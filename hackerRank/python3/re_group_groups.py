# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()

found = False

for i in range(1, len(s)-1):
    if s[i].isalnum():
        if s[i-1] == s[i]:
            print(s[i])
            found = True
            break

# go repetitive alphanumeric character was found     
if not found:
    print(-1)      
