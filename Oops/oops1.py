class child:
    age=5
    place = "toronto"
    country = "canada"
    def details(self,name,age,place):
        self.name = name
        self.age = age
        self.page = place
        print("hello",name,"age:",age,"place:",place)

#print(child.age)
raki = child()
panduu = child()
sidhu = child()
laddu = child()
lucky = child()

print(raki.age)
print(raki.place)
print(raki.country)

raki.details("ammugadu",12,"vizag")
print(raki.place)