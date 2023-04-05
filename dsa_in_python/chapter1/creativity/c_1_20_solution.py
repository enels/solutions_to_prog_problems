from random import randint

def my_shuffle(data):
    '''
        Implementation of Python's inbuilt function shuffle
    :param data: 
    :return: the shuffled data
    '''

    # get the min and max of the data
    min_val = min(data)
    max_val = max(data)

    # container to store the randomized values
    rand_data = list()

    # continue looping under all values in data have been randomly picked
    # by the randint function
    while True:
        val = randint(min_val, max_val)
        if val in data: # checks if generated random int is in passed data
            if val in rand_data: # checks if generated random int is in random data
                pass
            else:
                rand_data.append(val)
                if len(rand_data) == len(data):
                    break

    return rand_data