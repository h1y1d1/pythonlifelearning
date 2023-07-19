#tuple

user_name = ("ram","rahim","robert")
print(user_name)
print(type(user_name))

numbers = (2,5,7,9,5,8,9)
print(numbers)
print(type(numbers))


#tuple indication ( ) tuples
states = ("tg","Ap","tn","bihar","delhi")
print(states)
states1 = ("telangana","Ap","tamilnadu","bihar","delhi","up")
print(states1)

'''
1. Convert tuple into list.
2. Add items in the list.
3. Convert list into tuple.
'''


state_list = list(states)
print(state_list)
state_list.append("up")
print(state_list)

states = tuple(state_list)
print(states)

food = ("pani puri", "ice cream", "gobi", "pizza", "milkshake")
print(food)

food_list = list(food)
print(food_list)
food_list.insert(2,"Biryani")
print(food_list)
food = tuple(food_list)
print(food)
print(type(food))
print(food[4])
print(food[2:5])

fruits = ("apple","banana","orange","cherry","mango")
fruit1,fruit2,fruit3,fruit4,fruit5= fruits
print(fruits)
print(fruit5)

phones = ("one plus","vivo","apple","samsung","oppo","poco")
print(phones)
op,vo,ap,sg,opp,pc = phones
print(op)

id_num = (501,502, 503, 504,505)
print(id_num)
rn1,rn2,rn3,rn4,rn5=id_num
print(rn3)

#join
tuple1 = (1,2,3,6,7)
tuple2 = (5,6,7,8)
tuple3 = tuple1*3
print(tuple3)

print("eppudra "*10)