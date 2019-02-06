#!/usr/bin/env python3

"""
f68edd00dd3451ef3fa44f14ad0564c4
oopython
lab1
v2
jelf18
2019-01-21 13:27:42
v3.1.3 (2018-09-13)

Generated 2019-01-21 14:27:42 by dbwebb lab-utility v3.1.3 (2018-09-13).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb
from classes import Cat
from classes import Duration



# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Objects and classes
#
# Basic object oriented python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a new file, for creating classes in, call it **classes.py**. In
# classes.py create the class Cat. Add the following instance attributes in
# the Cat class constructor:
# - `eye_color`
# - `name`
# Add a paramater for each attribute in the constructor definition.
# Create a *get*-method for each attribute.
#
# Dont forget to import the file!
#
# In the code below create a new variable called `cat1` and initiate it with
# a new *Cat object*.
# Give the object the eye color "black" and the name "Basion".
#
# Answer with the string "My cats name is `name` and has `eye_color` eyes.",
# use the get-methods to retrieve the values from the object in cat1.
#
# Write your code below and put the answer into the variable ANSWER.
#

cat1 = Cat('black', 'Basion')

ANSWER = ("My cats name is " + cat1.get_name() + " and has "
          + cat1.get_eye_color() + " eyes.")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Expand your Cat class with the instance attribute `lives_left`.
# Also add a *set*- and *get*-method for the attribute.
# In the constructor, give `lives_left` a default value of `-1` if no other
# value is sent to the constructor.
#
# In the code below use the set-method on cat1 to change the value to `5`.
#
# Answer with number of lives cat1 has left.
#
# Write your code below and put the answer into the variable ANSWER.
#

cat1.set_lives_left(5)


ANSWER = cat1.set_lives_left(5)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a new method in the Cat class, called `description`. The method
# should return the string "My cats name is `name`, has `eye_color` eyes and
# `lives_left` lives left to live.". Use `self` to access the values for each
# attribute.
#
# Answer with the result returned from `cat1.description()`.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = cat1.description()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a static attribute in the Cat class, "nr_of_paws", that contains the
# number of paws a cat have.
# Assign its value to `4` in the declaration.
#
# Create a get method in the Cat class that returns "self.nr_of_paws".
#
# Answer with the string "`cat1.get_name()` has `cat1.get_nrof_paws()` paws".
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = cat1.get_name() + " has " + str(cat1.get_nr_of_paws()) + " paws"

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# In the code below assign `2` to cat1's nr_of_paws.
#
# Answer with the string "`cat.get_name` has `cat1.get_nrof_paws` paws but
# cats have `Cat.nr_of_paws` paws.".
#
# Write your code below and put the answer into the variable ANSWER.
#


cat1.set_nr_of_paws(2)


ANSWER = (
    cat1.get_name() + " has " + str(cat1.get_nr_of_paws()) +
    " paws but cats have " + str(Cat.nr_of_paws) + " paws.")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a new variable called `cat2` and initiate it with a new Cat objekt.
# Give cat2 the name "Nova" and eye color "green".
#
# Put cat1 and cat2 variables in a list. Iterate through the list and
# concatenate the result from their description methods together in a string,
# without any seperation between the two string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#
cat2 = Cat("green", "Nova")

list_of_cats = [cat1, cat2]
res = ""

for cat in list_of_cats:
    res += cat.description()


ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a new class named Duration.
# Declare the following instance attributes in the constructor:
# - `hours`
# - `minutes`
# - `seconds`
# Add a parameter for each attribute to the function heading and assign each
# parameter to respective attribute.
#
# Add the method `info` to the class, it should return the duration as a
# string with the format "h-m-s".
# Numbers below 10 should have a leading zero in the string.
#
# Initialize a new *Duration object* and assign it to a variable called
# `duration1`. Give it hours `24`, minutes `5` and seconds `10`.
#
# Answer with the result from the info method.
#
# Write your code below and put the answer into the variable ANSWER.
#


duration1 = Duration(24, 5, 10)


ANSWER = duration1.info()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8 (1 points)
#
# Create a static method in the Duration class, name it `duration_to_sec`.
# The method should take one argument, a string in the format as the one
# `info` returns, "h-m-s".
# The method should return the duration it represents converted to number of
# seconds.
#
# Answer with `Duration.duration_to_sec(duration1.info())`.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = Duration.duration_to_sec(duration1.info())

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.8", ANSWER, True)

# --------------------------------------------------------------------------
# Section 2. Overriding methods
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Overload the `add operator(+)` in the Duration class.
# It should return the duration of two objects added together, in seconds.
#
# Initialize a new Duration object to a variable called `duration2` , give it
# hours `32`, minutes `19` and seconds `2`.
#
# Answer with `duration1+duration2`.
#
# Write your code below and put the answer into the variable ANSWER.
#

duration2 = Duration(32, 19, 2)
print(duration1+duration2)

ANSWER = duration1+duration2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Overload the `iadd operator(+=)` in the Duration class to update the own
# object with the sum of its own units and the other objects units,
# hours+other.hours, minutes+other.minutes and seconds+other.seconds.
#
# Initialize a new Duration object to a variable called `duration3` , give it
# hours `3`, minutes `4` and seconds `36`.
# In the code use "+=" to update `duration2` with `duration3`.
#
# Answer with `duration2`s info method.
#
# Write your code below and put the answer into the variable ANSWER.
#

duration3 = Duration(3, 4, 36)

duration2 += duration3

ANSWER = duration2.info()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Overload the `smaller than operator(<)` in the Duration class.
# It should return True if the duration is shorter than the other.
#
# Answer with `duration1<duration2`.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = duration1 < duration2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)


dbwebb.exit_with_summary()
