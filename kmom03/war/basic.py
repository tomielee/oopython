#! usr/local/bin/env python3
"""
    Basic functions for re-use
"""

from random import randint, random, shuffle


def rand_int(minval, maxval):
    """return random int. between min and max"""

    return randint(minval, maxval)

def shuff_list(lst):
    """return shuffled list"""
    shuffle(lst)
    return lst


# test = [1,2,3,4]
# print(shuff_list(test))
