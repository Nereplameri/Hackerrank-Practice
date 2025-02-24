#https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(n+1):

        #We dont need "i" to be "0"
        if (i == 0):
            continue

        print(" " * (n-i), end="")
        print("#" * i)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
