#https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    sum = len(arr)
    countPozitive = 0
    countNegative = 0
    countZero = 0
    for i in arr:
        if (i > 0):
            countPozitive += 1
        if (i < 0):
            countNegative += 1
        if (i == 0):
            countZero += 1
    print(countPozitive / sum)
    print(countNegative / sum)
    print(countZero / sum)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
