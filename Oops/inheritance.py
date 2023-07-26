"""
super keywor: in python, the super() keyword is used to caLL A METHOD the parent class is a subclass.
It allows us to extend the functionality of the parent class while reusing its method.
It is often used in inheritance to access the methods and attributes of the parent class

"""
"""class parent:
    def display(self):
        print("this is from the parent class")

class child(parent):
    def display(self):
        super().display()
        

c = child()
c.display()"""

class daddy:
    def details(self,name,sur_name,age,place):
        self.name = name
        self.sur_name = sur_name
        self.age = age
        self.place = place
        print("name:",name,"sur_name:",sur_name,"age:",age,"place:",place)



class surya(daddy):
    def details(self,name,age):
        self.name = name
        self.age = age
        super().details(name,self.sur_name,age,self.place)
        print("name:",name,"sur_name:",self.sur_name,"age:",age,"place:",self.place)

venkat = daddy()
venkat.details("venkat","chandana",65,"hyd")
name = surya()
name.details("surya",40)
