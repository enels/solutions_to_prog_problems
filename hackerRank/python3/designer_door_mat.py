# Enter your code here. Read input from STDIN. Print output to STDOUT
digits = input().split()

inputed_cols = int(digits[1])
rows = int(digits[0])
cols = inputed_cols
mid_row = rows // 2 + 1

# factor = cols / rows
# half_col = factor / 2

mid_pattern = ".|."
dash = "-"

# stores the first half of the output
first_half_output_dict = dict()


# keeps track of the index of the ouput strings
index = -1

n_mid_patterns = 0
current_row = 0
for row in range(1,rows+1):
    n_mid_patterns = current_row + row
    current_row += 1

    # check the number of half dashes columns if it's odd or even
    j = (inputed_cols - row) // 2
    if (inputed_cols - row) % 2 == 0:
         n_half_cols = j
    else:
         n_half_cols = j + 1

    if row < mid_row:
        index += 1
        first_half_output_dict[index] = ""
    if row == mid_row:
        # subtract the number of characters that makes up WELCOME
        cols = inputed_cols - 7

        # midline to print out the WELCOME text
        for n in range(cols+1):
            if n == cols // 2:
                print("WELCOME", end="")

            else:
                print(dash, end="")

        print()

    elif row < mid_row:
        # subtract the number of mid patters to print out from the total columns
        # this helps to print out the correct number of dashes on both sides of the mid pattern
        cols = inputed_cols - n_mid_patterns*3

        for n in range(cols+1):
            # when it gets to half of the columns
            if n == n_half_cols:
                # prints out the middle pattern
                for _ in range(n_mid_patterns):
                    print(mid_pattern, end="")
                    first_half_output_dict[index] += mid_pattern
            else:
                print(dash, end="")
                first_half_output_dict[index] += dash
        print()
    # begin the other half of the shape patter after the
    # middle with "WELCOME"
    elif row > mid_row:
        # iterate through the rows backwardly
        print(first_half_output_dict[index])
        index -= 1








