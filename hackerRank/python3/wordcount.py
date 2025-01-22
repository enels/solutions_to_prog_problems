# Enter your code here. Read input from STDIN. Print output to STDOUT
# stores the number of words to be keyed in by user
n_words = int(input())

# stores all the words
words = list()

# stores the distinct words
#distinct_words = set()
# create dictionary for storing the words and their number of occurrences
word_dict = dict()

# iterate throgh to collect the words
for _ in range(n_words):
    word = input()
    words.append(word)
    word_dict[word] = 0

# store the unique words in a dictionary with a value of zero
# for word in distinct_words:
#     word_dict[word] = 0

# print(distinct_words)
# increase every occurrence of a word by 1    
for word in words:
    word_dict[word] += 1

# print out the results
print(len(word_dict))

for value in word_dict.values():
    print(value, end=" ")
