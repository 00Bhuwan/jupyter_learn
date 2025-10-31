#def add(firstName, lastName):        # without types doesn't suggest types for firstName
def add(firstName: str | list, lastName: str = None):     # types included in firstName thus suggests str methods
    firstName = firstName.capitalize()
    return firstName + " " + lastName

fname = "john"
lname = ""

name = add(fname, lname)
print(name)