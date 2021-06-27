#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # store temp so n is preserved
    temp = n
    num_ans = 0
    while temp > 0:
        # get last digit and compare
        print(temp, temp % 10)
        if temp % 10 == 0:
            temp //= 10
            continue
        if n % (temp % 10) == 0:
            num_ans += 1
        temp //= 10
    return num_ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
