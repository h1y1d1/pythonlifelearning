class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    dog1 = dog("buddy",4)
    dog2 = dog("max",5)
    print(dog1.name)
    print(dog1.age)
    print(dog2.name)
    print(dog2.age)
#In Python, the if __name__ == "__main__": line is used to control the execution of code when a Python script is run as the main program. It allows you to separate the code that should be executed when the script is run directly from the code that should only be executed when the script is imported as a module in another script.
