#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    size = len(arr)
    sumDiagonal = 0
    sumRevDiagonal = 0
    for i in range(size):
        sumDiagonal += arr[i][i]
        sumRevDiagonal += arr[i][size-i-1]
    return abs(sumDiagonal - sumRevDiagonal)


if __name__ == '__main__':
    fptr = open("output.txt", "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
