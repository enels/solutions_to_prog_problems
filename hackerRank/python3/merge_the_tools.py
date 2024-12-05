def merge_the_tools(string, k):
    # your code goes here
    c = ""
    char_count = 0
    for ch1 in string:
        char_count += 1

        # checks if character already exist in current
        # concatenated string
        if ch1 in c:
            pass
        else:
            # new character found
            c += ch1
        # if number of character seen is equal to number required per word
        if char_count == k:
            for ch in c:
                print(ch, end="")

            c = ""
            char_count = 0

            # new line
            print()


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)