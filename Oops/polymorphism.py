"""
Polymorphism allows objects to be treated as instance of their parents and it can take two forms: method overloading

Method Overloading: Method overloading meaNS DEFINING MULTIPLE METHODWITH the same name different paramemtrs in the same class. python does not support method directly
Method Overriding: method overriding involves redefining a method in the subclass that a in the parent class.

"""

#method overloading

"""class calculator:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return num1+num2
    
    def add(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        return num1+num2+num3
    
addition = calculator()
print(addition.add(23,33,22))"""

#method overriding

"""class husband:
    def cash(self):
        print("i have 10000 rupees")

class wife(husband):
    def cash(self):
        print("no thats not your money thats my money")

panduu = wife()
panduu.cash()"""

class movie:
    def guntur_karam(self):
        print("pooja hegde")

class updatemovie(movie):
    def guntur_karam(self):
        print("meenakshi chowdary")

heroine = updatemovie()
print(heroine.guntur_karam())