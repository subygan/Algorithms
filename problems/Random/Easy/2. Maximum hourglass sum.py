import math
import os
import random
import re
import sys

#logic for the hourglass problems
def hourglassSum(arr):
    max_sum = -10000
    for i in range (len(arr)-2):
        for j in range (len(arr)-2):
            total = (arr[i][j]+arr[i][j+1]+arr[i][j+2])+ (arr[i+1][j+1])+(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]);
            max_sum = max(max_sum, total)
    return max_sum

my_arr = []

my_arr.append(input().split(' '))

for _ in range(len(my_arr)-1) :

    my_arr.append(input().split(' '))

hourglassSum(my_arr)

'''
#source: https://www.hackerrank.com/challenges/2d-array/problem

Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

For example, given the 2D array:

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
We calculate the following  hourglass values:

-63, -34, -9, 12, 
-10, 0, 28, 23, 
-27, -11, -2, 10, 
9, 17, 25, 18
Our highest hourglass value is  from the hourglass:

0 4 3
  1
8 6 6

'''
