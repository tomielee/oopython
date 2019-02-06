#! usr/local/bin/env python3
"""
Handler file
handle objects between app.py and Employee.py
"""
from employee import Employee

class Handler():
    """
    handle empolyees
    """

    def __init__(self):
        """init, list with employees"""
        self.people = []
        self.add_predefined_employees()

    def get_people(self):
        """returns people"""
        return self.people

    def add_employee(self, form):
        """add person/employee"""
        person = Employee(
            form["firstname"],
            form["lastname"],
            form["salary"]
        )
        self.people.append(person)


    def add_predefined_employees(self):
        """add a couple of predifined people"""

        emil = Employee("Emil", "Folino", 30000)
        mikael = Employee("Mikael", "Roos", 31000)
        kenneth = Employee("Kenneth", "Lewenhagen", 75000)
        andreas = Employee("Andreas", "Arnesson", 12000)

        self.people.append(emil)
        self.people.append(mikael)
        self.people.append(kenneth)
        self.people.append(andreas)

    def write_session(self, session):
        """write data to session"""
        session["employees"] = [e.to_json() for e in self.people]

    def read_session(self, session):
        """read data from session"""
        if session.get("empolyees", []):
            self.people = [Employee.from_json(e) for e in session["employees"]]
