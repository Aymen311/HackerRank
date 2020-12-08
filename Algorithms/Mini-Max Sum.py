#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mini = min(arr)
    maxi = max(arr)
    sum1, sum2 = 0, 0
    for i in range(0 ,len(arr)):
        if arr[i] != maxi :
            sum1 += arr[i]
        if arr[i] != mini :
            sum2 += arr[i]
    if maxi == mini :
         print(str(sum(arr[1:])), str(sum(arr[1:])))
    else:
        print(str(sum1), str(sum2))

         

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
