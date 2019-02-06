#!/usr/bin/env python3
"""Functions for lab1"""

class Cat():
    """Create cat objects"""
    nr_of_paws = 4

    def __init__(self, eye_color, name):
        self.eye_color = eye_color
        self.name = name
        self.lives_left = -1

    def get_eye_color(self):
        """return object attribute eye_color"""
        return self.eye_color

    def get_name(self):
        """return object attribute name """
        return self.name

    def get_lives_left(self):
        """return object attribute lives_left"""
        return self.lives_left

    def get_nr_of_paws(self):
        """return object attribute nr_of_paws"""
        return self.nr_of_paws


    def set_nr_of_paws(self, nr_of_paws):
        """set object attribute nr_of_paws"""
        self.nr_of_paws = nr_of_paws

        return self.nr_of_paws

    def set_lives_left(self, lives_left):
        """set object attribute lives_left"""
        self.lives_left = lives_left

        return self.lives_left

    def description(self):
        """return string of objects attribute in a sentence"""
        return "My cats name is {}, has {} eyes and {} lives left to live.".\
        format(self.get_name(), self.get_eye_color(), self.get_lives_left())


class Duration():
    """Create object of time with hours, minutes, seconds """

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def info(self):
        """return string of object attributes"""
        return "{:02d}-{:02d}-{:02d}".format(\
        self.hours, self.minutes, self.seconds)

    @staticmethod
    def duration_to_sec(duration):
        """return string of objects time in seconds"""
        sec = int(duration[-2:])
        minutes = int(duration[-5:-3])
        hour = int(duration[:-6])

        return hour*3600 + minutes*60 + sec

    def __add__(self, other):
        """operator for addition self + other"""
        return self.duration_to_sec(self.info()) + \
        other.duration_to_sec(other.info())

    def __iadd__(self, other):
        """operatior for adding self += other"""
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds

        return self

    def __lt__(self, other):
        """operator for less than. return if self is less than other"""
        if self.duration_to_sec(self.info()) < \
        other.duration_to_sec(other.info()):
            return True
