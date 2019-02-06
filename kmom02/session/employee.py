#! /usr/local/bin/env python3
"""
Class file to handle object/class Employee
"""
import random

class Employee():
    """
    class for object employee
    """

    def __init__(self, firstname, lastname, salary, id_number=None):
        """ init method """
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.id_number = id_number if id_number else \
            random.sample(range(10), 4)

    def get_firstname(self):
        """returns firstname """
        return self.firstname

    def get_lastname(self):
        """returns lastname """
        return self.lastname

    def get_salary(self):
        """returns salary """
        return self.salary

    def get_id(self):
        """returns id-number"""
        return "".join(map(str, self.id_number))

    def get_name(self):
        """returns full name"""
        return self.firstname + " " + self.lastname

    def to_json(self):
        """serialise data"""
        return {
            "fname" : self.firstname,
            "lname" : self.lastname,
            "salary" : self.salary,
            "id" : self.id_number
        }

    @classmethod
    def from_json(cls, json):
        """deserilise data"""
        return cls(json["fname"], json["lname"], json["salary"], json["id"])
