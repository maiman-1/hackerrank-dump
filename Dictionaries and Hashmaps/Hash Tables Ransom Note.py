"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be
traced back to him through his handwriting. He found a magazine and wants to
know if he can cut out whole words from it and use them to create an
untraceable replica of his ransom note. The words in his note are
case-sensitive and he must use only whole words available in the magazine. He
cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if
he can replicate his ransom note exactly using whole words from the magazine;
otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack
at dawn". The magazine has all the right words, but there's a case mismatch.
The answer is No.
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    """

    :param magazine: an array of strings, each a word in the magazine
    :param note: an array of strings, each a word in the ransom note
    :return: str: Yes/No
    """
    # Add all words in magazine to defaultdict
    a_dict = defaultdict(int)
    for word in magazine:
        a_dict[word] += 1
    for word in note:
        if a_dict[word] == 0:
            print("No")
            return False
        elif a_dict[word] > 0:
            a_dict[word] -= 1
    print("Yes")


if __name__ == '__main__':
    """
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
    """
    magazine = "two times three is not four"
    magazine = magazine.strip().split()
    note = "two times two is four"
    note = note.strip().split()
    print(magazine, note)
    checkMagazine(magazine,note)

