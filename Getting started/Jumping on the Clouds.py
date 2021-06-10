"""
There is a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus. The player can
jump on any cumulus cloud having a index that is equal to the index of the
current cloud plus 1 or 2.

The player must avoid the thunderheads. Determine the minimum number of jumps
it will take to jump from the starting position to the last cloud. It is
always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1
 if they must be avoided.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    """

    :param c: List(Integer): A list of numbers (can only be one or zero)
    :return: Integer: Number of minimum path

    Idea: Check index + 2: If 0: continue on this, if 1: check index + 1,
    if 0: continue on this, if 1: halts

    Pseudocode:
    i = 0
    path = 0
    # Code for length == 3
    if len(c) == 3:
        return 1
    elif len(c) == 2:
        return 1
    while i < len(c) - 2:
        if c[i+2] == 0:
            path += 1
            i += 2
        elif c[i+2] == 1:
            if c[i+1] == 0:
                path += 1
                i += 1
            elif c[i+1] == 1:
                return path
    """
    # Initialize all the variables
    i = 0
    num_jumps = 0
    while i < len(c) - 2:
        print(i, c[i+2], bool(c[i+2]))
        if c[i+2]:
            i += 1
        else:
            i += 2
        num_jumps += 1
    if i < len(c) - 1:
        num_jumps += 1
    return num_jumps

if __name__ == '__main__':
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
    """
    print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
