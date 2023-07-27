"""
Private: Private attributes or methods can only be accessed within the class aND NOT VISIBLE outside of the classs
Public: Public attributes or methods can be accessed from any where
Protected: Protected attributes or methods can be accesses within the class and its subclass

"""
class myclass:
    def __init__(self):
        self.__private_var = 10
    def __private_method(self):
        return "this is a private method"
    
obj = myclass()
print(obj.__private_method())
print(obj.__private_var)