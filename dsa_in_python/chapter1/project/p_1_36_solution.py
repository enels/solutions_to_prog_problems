def word_count():
    '''
        counts the umber of word in each sentence keyed in by the user
    :return: a dictionar of words with their respective times of occurrence.
    '''

    punctuations = "~@!#$%^&*()[];:-_+=}?,.{|\/\'\"<>"
    # prompt user for input
    user_input = input("Enter sentence: ")

    # remove punctuations
    new_user_input = ""
    for c in user_input:
        if c in punctuations:
            pass
        else:
            new_user_input += c

    # store the sentence in a list
    words = new_user_input.split()

    # store each word uniquely in a set in lowercases
    word_set = set()
    new_words = ""
    for word in words:
        word_set.add(word.lower())
        new_words += word.lower()
        new_words += " "

    # split the new words into a list
    new_words = new_words.split()

    # store each unique word in the set in a dictionary
    # and initialize their count to zero
    word_dict = dict()
    for word in word_set:
        word_dict[word] = 0

    # count each word in the word list using the dictionary
    for word in new_words:
        word_dict[word] += 1

    # print each word in the word dict with their count
    for word, count in word_dict.items():
        print("{}: {}".format(word, count))

    # return the dict for external usage
    return word_dict

if __name__ == "__main__":
    word_count()