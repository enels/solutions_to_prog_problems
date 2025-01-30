import math

x = int(input())
y = int(input())

# get the value of the hypotenus
m = math.sqrt(x**2 + y**2)

# get the base angle
ans = math.degrees(math.asin(x / m))

# round off the answer and print out
round_ans = round(ans)

print("{}\u00b0".format(round_ans))
