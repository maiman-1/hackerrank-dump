#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
   # use edge cases stated by Tze Yang Ng
   # general
    common_length = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break
    differences = len(s) + len(t) - (2 * common_length)
    print(differences)
    # case a: when k is larger than the difference in the two strings
    if  differences > k:
        return "No"
    # case b: if number of different digits is odd and k is odd then it will pass
    elif differences % 2 == k % 2:
        return "Yes"
    # case c: if we are able to completely erased one string and the remaining is still less than k
    elif len(s) + len(t) < k:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
