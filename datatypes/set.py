# we use { } for set

bikes = {"Honda","Avenger","Duke","Yamaha","Royal Enfield","Glamour","Hero"}
print(bikes)
bikes.add("tvs")
print(bikes)
print(type(bikes))


rangabali = {"white shirt","rangabali center","village"}
print(rangabali)
rangabali.add("social worker")
print(rangabali)
rangabali.add("bomb")
print(rangabali)

#index value [ ], method (), print(), type(), add()

rangabali.clear()
print(rangabali)

odd_num = {1,3,5,7,9,11,13,15,17}
prime_num = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
diff = prime_num.symmetric_difference(odd_num)
print(odd_num)
print(prime_num)
print(diff)

odd_num = {1,3,5,7,9,11,13,15,17}
prime_num = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
diff = prime_num.intersection(odd_num)
print(odd_num)
print(prime_num)
print(diff)

odd_num = {1,3,5,7,9,11,13,15,17}
prime_num = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
diff = prime_num.union(odd_num)
print(odd_num)
print(prime_num)
print(diff)

sports_channel = {"ten sports","sony six","sony live",
                  "star sports","dd sports","espn"}
print(sports_channel)
sports_channel.remove("ten sports")
print(sports_channel)
surya = sports_channel.copy()
print(surya)
#ten = {1,2,3,{1.1,2.2},4}
#print(ten)"""

#frozen set
l3 = ["item1","item2","item3",45,76,23,76]

#type conversion --->set
s3 = set(l3)
print(s3)


#froz_s3 = frozenset(l3)
#print(froz_s3)
#print(froz_s3)
#froz_s3.add("surya")

s3.pop()
print(s3)



print(bikes)
bikes.add("r15")
print(bikes)
bikes.add("jawa")
print(bikes)
print(type(bikes))
bikes.clear()
print(bikes)

numbers = {1,4,5,8,1,66,34,1,65,34,90,1,22,67,98,2,1}
print(numbers)

bikes = {"Honda","Avenger","Duke","Yamaha","Royal Enfield","Glamour","Hero"}
Highend_bikes = {"Royal Enfield","Avenger","Yamaha","Duke","KTM","Pulsor","Kawasaki","NS200"}