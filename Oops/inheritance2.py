#multiple
"""class parent1:
    def display(self):
        print("this is from the parent1 class")

class parent2:
    def display2(self):
        print("this is parent2 class")

class child(parent1,parent2):
    def display(self):
        super().display()
        super().display2()

c = child()
c.display()"""

#multilevel
class grandfather:
    def display(self):
        print("I am grand father")

class father(grandfather):
    def display(self):
        print("I am father")
        super().display()

class son(father):
    def display(self):
        super().display()
        print("I am son")

buddy = son()
buddy.display()