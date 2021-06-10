"""
An avid hiker keeps meticulous records of their hikes. During the last hike
that took exactly steps steps, for every step it was noted if it was an
uphill, U, or a downhill, D step. Hikes always start and end at sea level, and
each step up or down represents a 1 unit change in altitude. We define the
following terms:
    - A mountain is a sequence of consecutive steps above sea level, starting
    with a step up from sea level and ending with a step down to sea level.
    - A valley is a sequence of consecutive steps below sea level, starting
    with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    """
    :param steps: Integer: the number of steps on the hike
    :param path: String: a string describing the path
    :return: Integer: the number of valleys traversed

     Steps:
     1. Initialize height = 0, valleys = 0, mountains = 0
     2. Loop through strings (each character)
     3. If the letters = "D":
        - height -= 1
        - if height == 0:
            - mountains += 1
    4. If letters = "U":
        - height += 1
        - if height == 0:
            - valleys += 1
    5. return valleys


    Pseudocode:
    height, num_valleys, num_mountains = 0
    for i in range(step):
        if path[i] == "D":
            height -= 1
            if height == 0:
                mountains += 1
        else if path[i] == "U":
            height += 1
            if height == 0:
                valleys += 1
    return valleys
    """
    # Initialize variables
    cur_height, num_valleys, num_mountains = 0,0,0
    for i in range(steps):
        if path[i] == "D":
            cur_height -= 1
            if cur_height == 0:
                num_mountains += 1
        elif path[i] == "U":
            cur_height += 1
            if cur_height == 0:
                num_valleys += 1
    return num_valleys

if __name__ == '__main__':
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
    """
    steps = 8
    path = "UDDDUDUU"
    print(countingValleys(steps, path))