#tuple indication() tuples
states = ("telangana","ap","tn","bihar","delhi")
print(states)
#cant use the below in tuples
#states.insert()
#states.clear()
# normally add value into tuple
states1 = ("telangana","ap","tn","bihar","up","delhi")
print(states1)
#1. convert tuple into list
#2. add items in the list
state_list = list(states)
print(state_list)
state_list.append("up")
print(state_list)
#convert list into tuple
states = tuple(state_list)
print(states)

#second scenario
food = ("pani puri","ice cream","gobi","pizza","chicken","milkshake")
print(food)

food_list = list(food)
print(food_list)
food_list.insert(2,"biryani")
print(food_list)

food = tuple(food_list)
print(food)

print(type(food))

#delete scenario using list and convert to tuple
food_list = list(food)
food_list.pop(3)
print(food_list)

#convert to tuple
food = tuple(food_list)
print(food)

#how to access indexing value - slicing
print(food[4])
print(food[2:])
print(food[:3])
print(food[-2:])

#unpack
fruits = ("apple","orange","banana","cherry","mango")
fruits1,fruits2,fruits3,fruits4,fruits5 = fruits
print(fruits)
print(fruits5)

phones = ("iphone","samngsung","1plus","vivo","oppo","jio")
print(phones)
ap,sg,op,vo,opp,ji = phones
print(op)

id_num = (501,502,503,504)
print(id_num)
rn1,rn2,rn3,rn4 = id_num
print(rn3)
#any index values we have to use [] square brackets
#me = (1,2,3,4)

#join
tuple1 = (1,2,3,4)
tuple2 = (5,6,7,8)
tuple3 = tuple1+tuple2
print(tuple3)
#repeat when we use multiply
tuple1 = (1,2,3,4)
tuple2 = (5,6,7,8)
tuple3 = tuple1*3
print(tuple3)

print("eppudra "*10)





















