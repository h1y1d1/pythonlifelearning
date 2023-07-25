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