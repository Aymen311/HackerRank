#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos, neg, zero = 0, 0 , 0 
    for i in range(0, len(arr)):
        if arr[i] > 0 :
            pos +=1
        elif arr[i] < 0 :
            neg += 1
        else :
            zero += 1
    print(str(pos/len(arr)) + "\n" , str(neg/len(arr))+ "\n" , str(zero/len(arr))+"\n")
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)