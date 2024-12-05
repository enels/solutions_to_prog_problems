def print_formatted(number):
    # adjustment
    align = len(bin(number).split("b")[1])

    for i in range(1, number+1):
        # decimal
        print(str(i).rjust(align), end=" ")

        # octal
        res = oct(i).split("o")[1]
        print(res.rjust(align), end=" ")

        # hex
        res = hex(i).split("x")[1].upper()
        print(res.rjust(align), end=" ")

        # binary
        res = bin(i).split("b")[1]
        print(res.rjust(align), end=" ")

        print()

if "__main__" == __name__:
    print_formatted(17)