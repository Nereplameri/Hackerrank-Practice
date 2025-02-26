#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
#I didnt pass this one

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    arr = s.split(":")
    lastP = arr[-1]
    del(arr[-1])
    arr += [lastP[0:2]]
    format = lastP[2:4]
    
    print(type(format))
    #arr : Saat, format: AM/PM
    if (format == "AM" and arr[0] == "12"):
        arr[0] = "0"
    
    if (format == "PM" and arr[0] != "12"):
        arr[0] = str(int(arr[0]) + 12)
    string = arr[0] + ":" + arr[1] + ":" + arr[2] 

    print(string)

    return string


if __name__ == '__main__':
    fptr = open("output.txt", "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
