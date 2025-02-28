#!/bin/python3
#https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    positionApples = []
    positionOranges = []

    for i in apples:
        positionApples += [a + i]
    
    for i in oranges:
        positionOranges += [b + i]
    
    countApples = 0
    countOranges = 0

    for i in positionApples:
        if ( s <= i <= t):
            countApples += 1

    for i in positionOranges:
        if (s <= i <= t):
            countOranges += 1

    print(countApples)
    print(countOranges)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
