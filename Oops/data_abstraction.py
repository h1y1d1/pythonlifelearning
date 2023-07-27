"""
Data abstraction - is a process of hiding the implementation details of an object and exposing only the relevant information
In python, abstraction can be achieved using abstract classes and 
"""

from abc import ABC, abstractmethod

"""class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
c = circle(5)
print(c.area())"""

class database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self,query):
        pass

class mysql(database):
    def connect(self):
        pass

    def execute_query(self,query):
        pass

class postgresql(database):
    def connect(self):
        pass

    def execute_query(self,query):
        pass