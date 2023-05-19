from random import randint

def birthday_paradox():
    '''
        Test the birthday paradox by a series of experiments to see if its true
        True: probability >= 0.5
        False: probability < 0.5
    :return: the probability
    '''

    n_people = dict()
    persons_with_same_birthday = dict()  # stores the total person and number of same birthday

    days = (1, 32)
    month = (1, 13)

    for current_n_persons in range(25, 101, 5):
        for each_person in range(current_n_persons+1):
            # container to store the randomly generated birthdays
            birthday = (randint(days[0], days[1]), randint(month[0], month[1]))
            n_people[each_person] = birthday
        total_current_persons = each_person

        # set the current total person to zero
        persons_with_same_birthday[total_current_persons] = 0

        # use exhaustive search to search for equal birthdays
        for single in range(total_current_persons):
            # check each one of the birthdays if they are equal
            for total in range(single+1, total_current_persons):
                if n_people[single] == n_people[total]:
                    persons_with_same_birthday[total_current_persons] += 1

    # get the probability that 2 persons in a room with population greater than 23
    num_of_required_outcome = 0
    for key, value in persons_with_same_birthday.items():
        # add up the value for each number of persons in the room
        num_of_required_outcome += value

    num_of_total_outcome = len(persons_with_same_birthday) * 2

    probability = num_of_required_outcome / num_of_total_outcome

    return probability

if __name__ == "__main__":
    print(birthday_paradox())