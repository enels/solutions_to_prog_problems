from random import shuffle
from random import randint

# get the number of lines to print
max_count = 100

# store the sentence to print
sentence = "I will never spam any friends again"

# get the words in a list
word_list = sentence.split()

# get number of words in the list
word_count = len(word_list)

# initiate the random word count
random_word_count = 0

# container to keep track of the random word generated so far
random_word_generated = list()

for line_no in range(1, 101):
    # get the random index to pick the word to artificially create a typo
    rand_index = randint(0, word_count-1)

    # randomize the letters of the word to create the typo
    rand_word = list()
    w = word_list[rand_index]
    for c in w:
        rand_word.append(c)

    # print out the line number first
    print("{} ".format(line_no), end="")

    for word in word_list:
        # word is equal to the generated random word
        if word == w:
            # shuffle the word list to mimic a type
            shuffle(rand_word)
            new_word = ""
            # concatenate the characters again to form a string
            for c in rand_word:
                new_word += c
            # check to make sure it mees teh condition of printing the random number
            # number of uniquely generated random number <= 8
            if len(random_word_generated) < 8 and new_word not in random_word_generated:
                random_word_generated.append(new_word)
                print("{} ".format(new_word), end="")
            else:
                print("{} ".format(word), end="")
        else:
            print("{} ".format(word), end="")

    print("\n")