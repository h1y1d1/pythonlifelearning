#dict {}
nominations = {"director":"SSR","movie":"RRR",
               "Actors":"NTR.jr,Ram charan","singer":"Keravani"}
print(nominations["director"])
print(nominations)
#keys and values

#print(nominations.keys())
#print(nominations.values())

nominations["Actors"] = "Jr.NTR & Ram Charan"
print(nominations)

print(nominations.get("movie"))

nominations.pop("Actors")
print(nominations)

#ADD
nominations["costume"] = "ramadevi SS"

nominations["fighter"] = "Ramlaxman"
nominations["vfx"] ="Srinivas"


nominations.setdefault("dop")

nominations["dop"] = "senthil"
print(nominations)

nominations["light"] = "senthil"
print(nominations)

family={
    #"key":{key:value,key:value}
    #Good:{meaning1:nice,meaning2:not bad}
    "big_kid":{"name":"Kiran","age":20},
    "middle_kid":{"name":"abhiram","age":18},
    "last_kid":{"name":"raju","age":89}
}
print(family["middle_kid"]["name"])

#list1 = [1,2,3,[3.1,3.2,3.3],4,5,6]
#print(list1[3][0])"""

#user database
users = {"surya":"pass","kiran":"p234","python":1234}
print(users)
#new reg
users["chandu"] = 4545
print(users)

#grading system

marks = {"surya":32,"kiran":89,"chandana":90}

print(marks)

#Telugu trans
telugu = {"list":" pattika",
          "laptop":"sashanala grandham","tab":"palaka"}
print(telugu)
print(telugu.keys())

#inventory managment
inventory = {
    "apple": 10,
    "one plus": 5,
    "samsung": 7
}

ship = int(input("enter ship no:"))
inventory["apple"] = inventory["apple"]-ship
print(inventory)

#config
max_connections = int(input("enter connection:"))
config = {
    "debug_mode": False,
    "max_connections": max_connections,
    "log_level": "INFO"
}
print(config)

debug_mode = int(input("Enter value: "))
config = {
    "debug_mode": debug_mode,
    "max_connections": 12,
    "log_level": "INFO"
}
print(config)

name = input("Enter your name:")
pin = int(input("Enter pin:"))

user_data = {"username":name,"password":pin}

print(user_data)