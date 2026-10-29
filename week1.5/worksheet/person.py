# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name,birth):
        self.name= name
        self.birth = birth
        if not isinstance(name, str):
            raise TypeError(f"{name} should be a string")
        if  name == "":
            raise ValueError("name is an empty string.")
        if not isinstance(birth, date):
            raise TypeError("birth is not a `date` object.")
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def initials(self):
        names = self.name.split()
        ini = ""
        for i in names:
          ini += i[0] 
        return ini
    def is_birthday(self):
        if date.today().month == self.birth.month & self.birth.day == date.today().day :
            return True
        else:
            return False
def main ():
    p2=Person("Jack jack",date(2008,10,29))
    print(p2.initials())

    print(p2.is_birthday)
if __name__=="__main__":
    main()
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
