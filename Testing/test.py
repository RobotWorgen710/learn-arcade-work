# Is-A and has-A relationships
# --- These are attributes
# Person has a name

class Dog:
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0
        print("New Dog")


class Cat(Dog):
    super.__init__()
