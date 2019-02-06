#!/usr/bin/env python3
"""
person classification
"""
# # Importera relevanta moduler
# from flask import Flask, render_template

class Person():
    """Create person object with name, age, courses"""

    def __init__(self, name, sir, age):
        self.name = name
        self.sir = sir
        self.age = age
        self.courses = []


    def add_courses(self, new_course):
        """add courses to object"""
        self.courses.append(new_course)

    def get_img_path_jpg(self):
        """create img path name for person object"""
        img_path = "img/{}.jpg".format(self.name.lower())
        return img_path
