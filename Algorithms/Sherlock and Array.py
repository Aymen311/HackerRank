#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    sum_arr = sum(arr)
    left = 0
    for i in range(0, len(arr)):
        current = arr[i]
        sum_arr -= current 
        if left == sum_arr:
            return 'YES'
            break  
        left += current
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
