#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    # use pointers first
    i = k % len(c)
    energy = 100 - (c[i] * 2 + 1)
    #print(energy)
    # Improved codes
    # the cost for each cloud could be seen as c[i] * 2 + 1 (plus one for step)
    while i != 0:
        i = (i+k) % len(c)
        energy -= c[i] * 2 + 1
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
