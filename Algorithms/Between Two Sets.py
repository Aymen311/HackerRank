#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    res = 0
    for elem in range(1 , max(max(a), max(b))+1):
        bol = False
        for i in range(len(a)):
            if elem % a[i] == 0 :
                bol = True
            else:
                bol = False
                break
        if  bol :
            for i in range(len(b)):   
                if b[i] % elem == 0:
                    bol = True
                else:
                    bol = False
                    break
        if bol:
            res += 1
    return res 
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
