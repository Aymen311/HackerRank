#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    periode = s[-2:]
    s = s.replace(periode, '')
    hours = s[:2]
    
    if periode == 'AM' and hours == '12' :
        s = s.replace(s[:2], '')
        s = '00' + s
    elif periode == 'PM' and (1 <= int(hours) <= 11):
        s = s.replace(s[:2], '')
        s = str(int(hours) +  12 ) + s
    return s 

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
