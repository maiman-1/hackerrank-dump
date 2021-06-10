"""
Left rotation: Move all elements in an array one unit to the left. The
leftmost element becomes the rightmost element.

[1,2,3,4,5] -> Left rotated twice -> [3,4,5,1,2]

Given an array a of integers n and a number, d, perform d left rotations on the
array. Return the updated array to be printed as a single line of space-separated integers.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    """
    :param a: int a[n]: the array to rotate
    :param d: int a[n]: the array to rotate
    :return: a'[n]: the rotated array
    """
    # Don't need to loop through d
    a_copy = list(a)
    for i in range(len(a)):
        a[i] = a_copy[(i+d) % len(a)]
    return a

if __name__ == '__main__':
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    """
    a = [41, 73, 89, 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51]
    d = 4
    print(rotLeft(a,d))

