"""
Private: Private attributes or methods can only be accessed within the class aND NOT VISIBLE outside of the classs
Public: Public attributes or methods can be accessed from any where
Protected: Protected attributes or methods can be accesses within the class and its subclass

"""
#private
"""class myclass:
    def __init__(self):
        self.__private_var = 10
    def __private_method(self):
        return "this is a private method"
    
obj = myclass()
print(obj.__private_method())
print(obj.__private_var)"""

"""class female:
    def __age(self):
        print("my age is:")
chandu = female()
print(chandu.__age())"""

#public
"""class myclass:
    def __init__(self):
        self.public_var = 10
    def public_method(self):
        return "this is a public method"
    
obj = myclass()
print(obj.public_method())
print(obj.public_var)"""

#protected
"""class myclass:
    def __init__(self):
        self._protected_var = 10
    def _protected_method(self):
        return "this is a protected method"

#we can use for subclass    
    
obj = myclass()
print(obj._protected_method())
print(obj._protected_var)"""

class phone:
    def _gallery(self):
        print("i have access to my gallery")
class motherphone(phone):
    def display(self):
        print(self._gallery())

photos = motherphone()
print(photos.display())








