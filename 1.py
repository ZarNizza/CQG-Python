#!/usr/bin/env python3
"""
This is module description.
NOTE:
    You can use Google/Sphinx style for all documentation in the code.
    See https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

    For code formatting use AutoPEP8 https://pypi.org/project/autopep8 (production standart)
    But I use Black (https://pypi.org/project/black/) for my pets :)

    To check errors in the code use Flake8 (https://flake8.pycqa.org/en/latest/).
"""
# Imports in alphabet order
from dataclasses import dataclass

# Data for initialization
# NOTE: Uppercase for global constants (PEP8)
DATA = [
    {"name": "Ivan1", "nick": "Ivanych1"},
    {"name": "Ivan2", "nick": "Ivanych2"},
    {"name": "Ivan3", "nick": "Ivanych3"},
]


@dataclass
class Person:
    """
    Class contains person description (name, nick)
    NOTE: Dataclass is good alternative for collections.nametuple since Python 3.7
    """

    name: str  # First name of person
    nick: str  # Nick name of person

    def __str__(self):
        """Magic method for output class data"""
        return f"Person(name={self.name}, nick={self.nick})"


# If you plan to start this script from command line (instead of including as a module)
if __name__ == "__main__":
    # create List of Person instances
    # NOTE: Please use snake_style not CamelStyle and not both :)
    list_of_persons = []

    # previous version
    # for i in data:
    #    list_of_Persons.append(Person(**i))

    # tadaaaam!..
    # Awesome! :)
    # def p(i):
    #    return Person(**i)
    # list_of_Persons = list(map(p,data))

    # tadabadaaam!..
    # Awesome! This is functional style
    list_of_persons = list(map(lambda i: Person(**i), DATA))

    # The same with list comprehension
    list_of_persons = [Person(**i) for i in DATA]

    # Same with generator (e.g. reading from file/socket from line to line)
    def get_person_data():
        for d in DATA:
            yield d

    list_of_persons = [Person(**i) for i in get_person_data()]

    # Print result
    for person in list_of_persons:
        # Due to magic method
        print(person)
