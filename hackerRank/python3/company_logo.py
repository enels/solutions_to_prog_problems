#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    
    # get the unique characters
    name_set = set(s)

    d = dict()

    for c in name_set:
        d[c] = 0
        for c2 in s:
            if c == c2:
                d[c] += 1

    sorted(d.values())

    d2 = dict()
    
    for k, v in d.items():
        d2[k] = v
    
    # sort the 2nd dictionary based on their keys.
    # shifting the values with their respective keys
    d2 = dict(sorted(d2.items(), key=lambda item: item[1], reverse=True))
    
    # print out the final dictionary
    for k,v in d2.items():
        print(k, v)

