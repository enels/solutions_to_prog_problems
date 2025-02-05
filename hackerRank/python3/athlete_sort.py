#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    # Sort the array based on the k-th attribute using a lambda function
    arr.sort(key=lambda x: x[k])

    # print out sorted array based on k
    column_length = len(arr[0])
    for i in range(len(arr)):
        for j in range(column_length):
            print(arr[i][j], end=" ")
        print()
