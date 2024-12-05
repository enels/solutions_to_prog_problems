'''
Program to check for the validation of a string. It checks for the presence
of an alphanumeric char, an alphabet char, a digit, an upper case, a lower case
'''
s = input()

print(s.isalnum())

state = False
for c in s:
    if (c.isalpha()):
        state = True
        print(state)
        break;

if (state == False):
    print("False")
state = False
for c in s:
    if (c.isdigit()):
        state = True
        print(state)
        break

if (state == False):
    print("False")

state = False
for c in s:
    if (c.islower()):
        state = True
        print(state)
        break

if (state == False):
    print("False")

state = False
for c in s:
    if (c.isupper()):
        state = True
        print(state)
        break

if (state == False):
    print("False")