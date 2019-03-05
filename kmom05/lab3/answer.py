#!/usr/bin/env python3

"""
a3238d6f7a04781c958b7a6a0e27e44a
oopython
lab3
v2
jelf18
2019-03-01 10:04:40
v3.1.3 (2018-09-13)

Generated 2019-03-01 11:04:41 by dbwebb lab-utility v3.1.3 (2018-09-13).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - Recursion
#
# If you need to peek at examples or just want to know more, take a look at
# the page: https://docs.python.org/3/library/index.html. Here you will find
# everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Simple recursion
#
# Practice on creating recursive functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers `16` up to `30`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#

def rec_sum(n):
    """ sum numbers recursive """

    #BASE
    if n == 16:
        return 16

    return n + rec_sum(n - 1)


ANSWER = rec_sum(30)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers in the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
# If its an empty list return `0`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#

def sum_list(list_to_sum):
    """sum the numbers in list"""
    tot = 0

    if list_to_sum is None:
        return 0

    for num in list_to_sum:
        tot = tot + num

    return tot


list_ts = [4, 5, 6, 11, 9, 1, 2, 3, 8]


ANSWER = sum_list(list_ts)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a recursive function in the code below that searches a list for a
# number and returns the index of the number.
# Find the index of `3` in the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
# If the number cant be found, return -1.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#

def find_num(list_to_search, value):
    """find a value in list and return the index position"""

    for num in list_to_search:
        if num == value:
            return list_to_search.index(num)

    return -1

list_ts = [4, 5, 6, 11, 9, 1, 2, 3, 8]

ANSWER = find_num(list_ts, 3)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Use the function from the previous assignment to find the number `16` in
# the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = find_num(list_ts, 16)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a recursive function in the code below that calculates `11` to the
# power of `5`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#


def rec_power(x, n):
    """
        return x^n
    """

    #BASE
    if n == 0:
        return 1

    return x * rec_power(x, n-1)

ANSWER = rec_power(11, 5)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a recursive function in the code below that turns a string
# backwards. Turn the string "switcharoo" backwards.
#
# Answer with the backward string.
#
# Write your code below and put the answer into the variable ANSWER.
#

def rec_string(word_to_turn):
    """given a string (word_to_turn) return it (back_word) backwards"""

    # word_to_turn[-1] = last letter
    # word_to_turn[:-1] = the hole word BUT the last
    if word_to_turn == "":
        return word_to_turn

    return word_to_turn[-1] + rec_string(word_to_turn[:-1])


# print(rec_string("ord"))

ANSWER = rec_string("switcharoo")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)


dbwebb.exit_with_summary()
