from random import choice, random


class Animal:
    """
    Helps move Bear and/or Fish
    """
    def __init__(self, initial_position):
        self._position = initial_position
        self._step = 0

    def set_position(self, val):
        self._position += val

    def get_position(self):
        return self._position

    def set_step(self, step):
        self._step = step

    def get_step(self):
        return self._step

    def move_one_step(self):
        """
        Moves a step backward or forward
        -1: backward
        1: forward
        """
        step = choice([-1, 1])
        self.set_position(step)