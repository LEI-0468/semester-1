# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name,birth):
        if not isinstance(name, str):
            raise TypeError("name should be a string")
        if  isinstance(name, None):
            raise ValueError("name is an empty string.")
        if not isinstance(birth, date):
            raise TypeError("birth is not a `date` object.")
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
