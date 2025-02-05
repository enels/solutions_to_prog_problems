# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()

# lower case characters
lower_case = []

for c in s:
    if c.islower():
        lower_case.append(c)

# uppercasecharcters
upper_case = []

for c in s:
    if c.isupper():
        upper_case.append(c)

# numerals
# even
even = []
for c in s:
    if c.isdigit():
        if int(c) % 2 == 0:
            even.append(c)

#odd
odd = []
for c in s:
    if c.isdigit():
        if int(c) % 2 != 0:
            odd.append(c)

# sort each one of them
lower_case.sort()
upper_case.sort()
even.sort()
odd.sort()


# finally append all of them
lower_case.extend(upper_case)
lower_case.extend(odd)
lower_case.extend(even)

for c in lower_case:
    print(c, end="")
