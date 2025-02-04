# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = map(int, input().split())

equation = input()

result = eval(equation)

print(result==k)
