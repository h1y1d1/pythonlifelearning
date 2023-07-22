#function
"""
def pranamam():
    print("namasthey")

print(type(pranamam))

print(pranamam())

def pranamam(name):
    print("NAMASTHEY",name)

person1 = pranamam("venkat")
person2 = pranamam("surya")
person3 = pranamam("sai")
print(person1)
print(person2)
print(person3)

def login(username,password):
    username_list = ["surya","chandu","sai","python","AI","kafka"]
    if username == "surya" and password == 1122:
        return "welcome"
    else:
        print("wrong details")
user1 = login("surya",1122)
print(user1)

print()

def add(num1,num2):
    total = num1+num2
    return total*total

print(add(3,4))"""

#boats and streams..
"""
A boat can travel with a speed of 13km/hour in still water if the speed of the stream is 4 km/hour. find the time taken by the boat to go 68 km downstream
"""

#downstream = 13+4 =17km/hour
#total time = 68/17 = 4hrs

"""def boats(speed,speed_stream,distance,stream):
    d_s = speed+speed_stream
    u_p = speed-speed_stream
    if stream == 'd':
        total_time = distance/d_s
        return total_time
    elif stream=='u':
        total_time = distance/u_p
        return total_time

print(boats(10,2,60,'d'))"""

def even(num):
    if num%2==0:
        return "even number"
    else:
        return "odd number"
    
print(even(49))

