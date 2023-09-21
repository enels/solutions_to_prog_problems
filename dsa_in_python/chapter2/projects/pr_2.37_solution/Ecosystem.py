import time
from random import choice
from Fish import Fish
from Bear import Bear


class Ecosystem:

    def __init__(self, total):

        self._total_animals = total
        self._river = list()

        # initialize the animals in the river putting them in random positions
        for n in range(self._total_animals):
            # randomly get the animal to insert in river index
            position = choice([0, 1, 2])
            if position == 0:
                self._river.append(Bear(n))
            elif position == 1:
                self._river.append(Fish(n))
            else:
                self._river.append(None)

        """for n in range(self._total_animals):
            if self._river[n] != None:
                print(str(n) + ": " + str(self._river[n].get_position()))"""
        #exit()

    def _set_new_position(self, n):
        """
        Sets new position for animal
        """

        new_position = self._river[n].get_position() + self._river[n].get_step()
        self._river[n].set_position(new_position)

    def _take_step_back_front(self):
        """
        iterate through the animals in the river in order to ...
        ...randomly take a step backward or forward
        """
        river_len = len(self._river)

        for n in range(river_len):

            if self._river[n] != None:
                self._river[n].move_one_step()
                # change the instance position of the animal with the step taken (animal's decision making move)
                self._set_new_position(n)

    def _destroy_lower_strength_animal(self, n, m):
        # find the one with the highest strength
        if self._river[n].get_strength() > self._river[m].get_strength():
            # destroy the one with a lesser strength
            self._river[m] = None

    def _create_new_animal(self, same_gender, n, m):
        """
        Change the position of the animals if they are the same
        """

        change = False
        animal_position_index = -1  # index position for animal in river list
        while change == False:
            animal_position_index += 1
            if self._river[animal_position_index] == None and animal_position_index < river_len:
                # get the type of animal that coincided
                if isinstance(self._river[m], Bear):
                    self._river[animal_position_index] = Bear(animal_position_index)  # creates a new Bear
                else:
                    self._river[animal_position_index] = Fish(animal_position_index)  # creates a new Fish
                # a signal that a position with None type has change to an instance of the collided animals
                change = True

    def move_animals(self):
        """
        Move the qquatic animals
        """
        # length of river
        river_len = len(self._river)

        # take step backward or forward
        self._take_step_back_front()

        # check if each instance position coincides with another one
        # n: current animal position
        # m: next adjacent animal position
        for n in range(river_len):
            next_adjacent_position = n + 1  # forward position (Progresively)
            for m in range(next_adjacent_position, river_len):
                if self._river[n] != None and self._river[m] != None:
                    # check if they coincides
                    if self._river[n].get_position() == self._river[m].get_position():  # they coincides
                        # checks if they are of different type of animal
                        if type(self._river[n]) != type(self._river[m]):
                            # checks which of them is a fish in order to destroy it
                            if isinstance(self._river[n], Fish):
                                self._river[n] = None   # destroy it
                            elif isinstance(self._river[m], Fish):
                                self._river[m] = None   # destroy it

                        # if both animals that coincided are the same type
                        elif type(self._river[n]) == type(self._river[m])
                            # different gender
                            if self._river[n].get_gender() != self._river[m].get_gender():
                                # if they are of the same type and the gender are different
                                # keep them in their previous position create a new instance of that type
                                # iterate through the list to find an empty position

                                # Keep them in their previous position
                                self._river[n].set_position(n)
                                self._river[m].set_position(m)

                                # create a new instance of the animal
                                self._create_new_animal(False, n, m)

                            # the same gender
                            elif self._river[n].get_gender() == self._river[m].get_gender():
                                # destroy animal with a lower strength
                                self._destroy_lower_strength_animal(False, n, m)

            else:
                # put animal in the new position if there are no coincidence
                new_position = n
                self._river[new_position] = self._river[n]

    def print_river(self):
        river_len = len(self._river)

        for n in range(river_len):
            print("[ " + str(self._river[n]) + " ]", end=" ")

        # let the two animals that coincides remain in their various positions


if __name__ == "__main__":
    ecosys = Ecosystem(20)
    ecosys.move_animals()
    ecosys.print_river()