#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):

    new_s = ""
    prev_space = True
    prev_char = ""
    for c in s:
        if c.isalpha() and prev_space and prev_char.isdigit() == False:
            new_s += c.upper()
            prev_space = False
            prev_char = c

        else:
            new_s += c
            if c.isspace():
                prev_space = True
            prev_char = c

    return new_s

if __name__ == '__main__':
    print(solve("1 w 2 r 3g"))