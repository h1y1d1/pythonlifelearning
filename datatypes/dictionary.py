#dictionary access
"""nominations = {"director":"SSR","movie":"RRR","actors":"NTR.jr,Ram charan","singer":"keervani"}
print(nominations)
print(nominations["director"])
print(nominations)
#keys and values
print(nominations.keys())
print(nominations.values())
#change
nominations["actors"] = "jr.ntr & Ram charan"
print(nominations)
print(nominations.get("movie"))
#pop
nominations.pop("actors")
print(nominations)
#add new value
nominations["costume"] = "Ramadevi SS"
print(nominations)

nominations["vfx"] = "srinivas"
print(nominations)

nominations.setdefault("dop")
print(nominations)
nominations["dop"] = "senthil"
print(nominations)

nominations["light"] = "senthil"
print(nominations)"""

"""#{"key":value{key:value,key:value}}
#good:{meaning1:nice,meaning2:no bad}
family ={"big_kid":{"name":"kiran","age":20},"middle_kid":{"name":"abhiram","age":18},"last_kid":{"name":"raju","age":89}}
print(family["big_kid"]["name"])
print(family["middle_kid"]["name"])
#print(family["middle_kid"]["name"]["age"])
#example for list
#list1 = [1,2,3,[3.3,3.2,3.1],4,5,6]
#print(list1[3][0])

#user database
users = {"surya":"pass","kiran":"p234","python":1234}
print(users)
#new registration
users["chandu"] = 4545
print(users)

#grading system
marks = {"surya":32,"kiran":89,"chandana":90}
print(marks)

#transalation"
telugu = {"list":"patika","laptop":"sashanala grandham","tab":"palaka"}
print(telugu)
print(telugu.keys())

#inventory mgmt
inventory = {"apple":10,"one plus":7,"samgsung":5}
print(inventory)

inventory["apple"] = inventory["apple"]-2
print(inventory)

ship = int(input("enter ship no:"))
inventory["apple"] = inventory["apple"]-ship
print(inventory)

#configuration
max_connections = int(input("enter connections: "))
config = {"debug_mode":False,"max_connections":max_connections,"log_level":"INFO"}
print(config)

debug_mode = int(input("enter value: "))
config = {"debug_mode":debug_mode,"max_connections":12,"log_level":"INFO"}
print(config)"""

"""name = input("Enter your name:")
pin = int(input("Enter pin:"))
user_data = {"username":name,"password":pin}
print(user_data)
"""

#2nd highest value
list1 = [2, 7, 34, 98, 3, 23, 56, 83, 12, 45, 98, 12, 102, 456]
sorted_list = sorted(list1, reverse=True)
second_highest = sorted_list[1]
print("The second highest value is:", second_highest)

tuple1 = {2, 7, 34, 98, 3, 23, 56, 83, 12, 45, 98, 12, 102, 456}
sorted_list = sorted(tuple1, reverse=True)
second_highest = sorted_list[2]
print("The second highest value is:", second_highest)









