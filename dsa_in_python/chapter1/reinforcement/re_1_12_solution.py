from random import randrange

def my_choice(data):
    # get the max and min value of data
    # use randrange to iterate thru it with min and max as stop and start resp.
    # check if each value returned by randrange is in data
    # return the first one found
    '''
    Implementation of a custom version of python's choice
    :param data: the data to perform the choice function on
    :return: the first random value found
    '''

    min_value = min(data)  # get min value
    max_value = max(data)  # get max value

    while True:
        result = randrange(min_value, max_value)
        if result in data:
            return result