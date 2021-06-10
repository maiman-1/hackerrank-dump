"""
Given two strings, determine if they share a common substring. A substring may
be as small as one character.
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    """

    :param s1: a string
    :param s2: another string
    :return: Yes/No
    """
    char_list = defaultdict(int)
    for letters in s1:
        char_list[letters] += 1
    for letters in s2:
        if char_list[letters] > 0:
            return "Yes"
    return "No"

if __name__ == '__main__':
    """
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
    """
    s1 = "hi"
    s2 = "world"
    print(twoStrings(s1,s2))