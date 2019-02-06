#!/usr/bin/env python3

"""
28944054638d34cb1901552387ef3d42
oopython
lab2
v2
jelf18
2019-01-28 12:45:49
v3.1.3 (2018-09-13)

Generated 2019-01-28 13:45:49 by dbwebb lab-utility v3.1.3 (2018-09-13).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a *get* method for both "name" and "ssn". Only Create a *set* method
# for "name".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `Badgerlock` and ssn `502075-3392`.
#
#
# Answer with per\'s get method for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#


class Person():
    """create objects persons"""

    def __init__(self, name, ssn, adress=""):
        self.name = name
        self.ssn = ssn
        self.adress = adress

    def get_name(self):
        """returns name"""
        return self.name

    def get_ssn(self):
        """returns ssn"""
        return self.ssn

    def get_adress(self):
        """returns adress"""
        return self.adress

    def set_name(self, new_name):
        """set and return name"""
        self.name = new_name
        return self.name

    def set_adress(self, new_adress):
        """set and return adress using sub Adress()"""
        self.adress = new_adress
        return self.adress

    def to_string(self):
        """returns string with name, ssn, adress"""
        return "Name: {name} SSN: {ssn} Address: {city} {state} {country}"\
        .format(
            name=self.name,
            ssn=self.ssn,
            city=self.adress.city,
            state=self.adress.state,
            country=self.adress.country
            )


per = Person('Badgerlock', '502075-3392')


ANSWER = per.get_ssn()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
# Create a method, in Address, called **to_string**, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Add the instance attribute **address** to class Person. It's value should
# be sent as argument to constructor, give it a default value of and empty
# string, `""`.
# Create a set method for attribute "address".
# Create a method, in Person, called **to_string**, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"`. Use Address'
# to_string method to get address data.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Katar`, the state `Skane` and the country `Commonwealth`.
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Adress():
    """create adress objects"""

    def __init__(self, city, state, country):
        """create object"""
        self.city = city
        self.state = state
        self.country = country


adr = Adress('Katar', 'Skane', 'Commonwealth')
per.set_adress(adr)

ANSWER = per.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person". In
# the constructor add the instance attribute "courses" and initiate it to and
# empty list.
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
# Create the method **remove_course**, it should take one argument and remove
# if from the course list attribute.
# Overload the **to_string** method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Tip, use `super(Teacher, self)` to access base
# method.
#
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Renere`, the state `Blekinge` and the country `Six Duchies`.
#
# Create a new instance of the class Teacher. Initiate it with the name
# `Buster` and ssn `516518-3442` and the aforementioned Address object.
# Use the add_course method to add the following courses, `design`, `python`
# and `webapp`.
#
#
# Answer with the Teacher object's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Teacher(Person):
    """Create object inherit name and ssn from Person"""

    def __init__(self, name, ssn):
        """create object to Teacher"""
        super().__init__(name, ssn)
        self.courses = []

    def add_course(self, new_course):
        """add courses to Teacher object attribute list courses"""
        return self.courses.append(new_course)

    def remove_course(self, old_course):
        """remove course, only first object in list equal to old_course"""
        return self.courses.remove(old_course)

    def get_courses(self):
        """returns string with commasepareated courses
        also if course is other than string
        """
        return ", ".join(map(str, self.courses))

    def to_string(self):
        return "{Person} Courses: {courses}".format(
            Person=super().to_string(),
            courses=self.get_courses()
        )

bus = Teacher('Buster', '516518-3442')
adr2 = Adress('Renere', 'Blekinge', 'Six Duchies')
bus.set_adress(adr2)

bus.add_course('design')
bus.add_course('python')
bus.add_course('webapp')

ANSWER = bus.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person". In
# the constructor add the instance attribute "courses_grades" and initiate it
# to and empty list.
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Tear`, the state `Vansterland` and the country
# `Commonwealth`.
# Create a new instance of the class Student. Initiate it with the name
# `Goliat` and ssn `228474-2825` and the aforementioned Address object.
# Use the add_course_grade method to add the following courses, `ramverk2`
# with grade `3`, `javascript1` with grade `-` and `ramverk1` with grade `2`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Student(Person):
    """create student objects, inherit from  Person """

    def __init__(self, name, ssn):
        """init attribute to object = grades """
        super().__init__(name, ssn)
        self.courses_grades = []

    def add_course_grade(self, course, grade):
        """add course and grade and append to object attribute"""
        new_course_grade = (course, grade)
        return self.courses_grades.append(new_course_grade)
        #courses_grades = [(course, grade), (course, grade)]

    def average_grade(self):
        """
        returns average grade
        """
        num_grades = 0
        avr = 0

        for course_grade in self.courses_grades:
            grade = course_grade[1]

            if isinstance(grade, int):
                avr += grade
                num_grades += 1

        return avr/num_grades

adr3 = Adress('Tear', 'Vansterland', 'Commonwealth')
stu = Student('Goliat', '228474-2825')
stu.set_adress(adr3)

stu.add_course_grade('ramverk2', 3)
stu.add_course_grade('javascript1', '-')
stu.add_course_grade('ramverk1', 2)


ANSWER = stu.average_grade()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)


dbwebb.exit_with_summary()
