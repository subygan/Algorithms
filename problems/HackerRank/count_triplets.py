import math
import os
import random
import re
import sys
'''
https://www.hackerrank.com/challenges/count-triplets-1/problem
'''

# Complete the countTriplets function below.
def countTriplets(arr, r):
    my_dict = {}
    count = 0
    for index, value in enumerate(arr):
        if value in my_dict:
            my_dict[value].append(index)
        else:
            my_dict[value] = [index]
    for index, number in enumerate(arr):
        x = number * r
        y = x * r
        if x in my_dict and y in my_dict:
            for di, dv in enumerate(my_dict[x]):
                if dv > index:
                    b = my_dict[x][di:]
                    my_dict[x] = b
                    # print(my_dict)
                    break
            for di, dv in enumerate(my_dict[y]):
                if dv > index:
                    c = my_dict[y][di:]
                    my_dict[y] = c
                    break
            if r == 1:

                n = len(b)
                count += (n * (n - 1)) // 2
            else:
                for bi, bv in enumerate(b):
                    for ci, cv in enumerate(c):
                        if cv > bv:
                            count += len(c[ci:])
                            break
    return count

def countTriplets1(arr, r):
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
        if i * r in dictPairs:
            count += dictPairs[i * r]
        if i * r in dict:
            dictPairs[i] = dictPairs.get(i, 0) + dict[i * r]

        dict[i] = dict.get(i, 0) + 1

    return count

with open("/rough/myfile.txt") as fp:
    Lines = fp.readlines()
    for line in Lines:
       arr = list(map(int, line.rstrip().split()))
       break
    r = 1
    print(countTriplets(arr,r))