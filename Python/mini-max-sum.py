#https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    max = arr[1] +arr[2] +arr[3] +arr[4]
    min = arr[1] +arr[2] +arr[3] +arr[0]
    print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
