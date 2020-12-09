#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    num2 , num1 = 0 , 0 
    for i in range(len(apples)):
        apples[i] += a  
        if  s <= apples[i] <= t:
            num1 += 1
            
    for i in range(len(oranges)):
        oranges[i] += b
        if  s <= oranges[i] <= t:
            num2 += 1
    print(num1)
    print(num2)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
