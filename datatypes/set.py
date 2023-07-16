# we use {} for set values will populate in alphabetical order

"""bikes = {"Honda","Avenger","Duke","Yamaha","Royal Enfield","Glamour","Hero"}
print(bikes)
print(type(bikes))
#add values in set
bikes.add("r15")
print(bikes)
bikes.add("jawa")
print(bikes)
# ONLY SINGLE VALUE WE CAN ADD and indexing value will not work
#bikes.add("rx100","x1")
#print(bikes)

bikes = {"Honda","Avenger","Duke","Yamaha","Royal Enfield","Glamour","Hero"}
bikes.clear()
print(bikes)
#Duplicate values not allowed in set
numbers = {1,2,3,1,4,5,6,1,7,8,9,10}
print(numbers)
print(type(bikes))"""

"""rangabali = {"white shirt","rangabali centre","village"}
rangabali.add("social worker")
print(rangabali)
rangabali.add("bomb")
print(rangabali)

#index value kavali ante [], method (), print(), type(),add()

rangabali.clear()
print(rangabali)

# difference
odd_num = {1,3,5,7,9,11,13,15,17}
prime_num = {2,3,5,7,11,13,17,19,23,29}
diff =odd_num.difference(prime_num)
print(odd_num)
print(prime_num)
print(diff)

odd_num = {1,3,5,7,9,11,13,15,17}
prime_num = {2,3,5,7,11,13,17,19,23,29}
diff =prime_num.difference(odd_num)
print(odd_num)
print(prime_num)
print(diff)

odd_num = {"Surya","Python",5,7,9,11,13,15,17}
prime_num = {2,3,5,7,11,13,17,19,23,29,"py","life"}
diff =prime_num.difference(odd_num)
print(odd_num)
print(prime_num)
print(diff)

odd_num = {1,3,5,7,9,11,13,15,17}
prime_num = {2,3,5,7,11,13,17,19,23,29}
diff =prime_num.symmetric_difference(odd_num)
print(odd_num)
print(prime_num)
print(diff)


odd_num = {1,3,5,7,9,11,13,15,17}
prime_num = {2,3,5,7,11,13,17,19,23,29}
diff =prime_num.difference_update(odd_num)
print(odd_num)
print(prime_num)
print(diff)

odd_num = {1,3,5,7,9,11,13,15,17}
prime_num = {2,3,5,7,11,13,17,19,23,29}
diff =prime_num.intersection(odd_num)
print(odd_num)
print(prime_num)
print(diff)

odd_num = {1,3,5,7,9,11,13,15,17}
prime_num = {2,3,5,7,11,13,17,19,23,29}
diff =prime_num.union(odd_num)
print(odd_num)
print(prime_num)
print(diff)"""

#cannot use two values we can remove at a time
"""sports_channel = {"ten sports","sony six","sony live",
                  "star sports","espn","dd sports"}
#sports_channel.remove("ten sports","dd sports")
sports_channel.remove("dd sports")
print(sports_channel)
surya = sports_channel.copy()
print(surya)"""

#ten = {1,2,3,{1.1,1.2},4}
#print(ten)

#only list can run the code with indexing
#num_list = [1,2,3,[3.1,3.2,3.3],4,5,6]
#print(num_list[3][0])

#frozen set
l3 = ["item1","item2","item3",45,76,23,78]

#type conversion to set
s3 = set(l3)
print(s3)

froz_s3 = frozenset(l3)
print(froz_s3)

#we cannot add or change in frozen set
#froz_s3.add("surya")

s3.pop()
print(s3)
























