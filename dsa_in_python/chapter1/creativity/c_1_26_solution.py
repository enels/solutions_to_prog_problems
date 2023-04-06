a = int(input("first digit "))
b = int(input("second digit "))
c = int(input("third digit "))

if a + b == c or a == b - c or a * b == c:
    print(True)
else:
    print(False)