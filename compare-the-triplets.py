#https://www.hackerrank.com/challenges/compare-the-triplets

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    scoreAlice = 0
    scoreBob = 0
    for rep in range(3):
        if a[rep] > b[rep]:
            scoreAlice += 1
        elif b[rep] > a[rep]:
            scoreBob += 1
    
    return [scoreAlice, scoreBob]

if __name__ == '__main__':
    fptr = open("output.txt", "w")

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
