#creating list
student_name = ["ram","krishna","dhoni","shiva"]
print(student_name)
print(type(student_name))

ms_dhoni = [23,24,25]
print(ms_dhoni)
print(type(ms_dhoni))

students_total = ["ram",34,34.5,True,False,1982,"krishna"]
print(students_total)
print(type(students_total))

surya = list([1,2,3,4])
print(surya)

#indexing and slicing

#name = "surya"
#print(name[0])

movies = ["RRR","Sitaramam","Radhesyam","KGF","Puspha"]
print(movies)

#particularly print KGF
print(movies[3])
print(movies[4])
#slicing
print(movies[1:4]) #python will accept n-1 last values need to add plus one
print(movies[3:5])
print(movies[3:]) 
print(movies[:5])
print(movies[2:4])

#negative slicing
print(movies[-1]) # coms from last values
print(movies[-3])

print(movies[-1:-4]) #reverse
print(movies[-7:1])
print(movies[-7:])

#list methods
movies.append("Salaar") #add in end
movies.append("spy")
movies.append(["surya","chandana"]) # called nested list
print(movies)

movies.append("RRR") # it will add and list allow duplicate values

#insert
movies.insert(2,"project k") #inside brakets called arguements and should give index value to insert
movies.insert(3,"khaleja")
print(movies)

#remove and clear
movies.remove("RRR") #first occurance
movies.remove("RRR")
#movies.remove("rrr") #not in list
movies.remove("spy")
print(movies)

#movies.clear() #delete completely
#print(movies)
#trash
trash_bin = movies.pop(3) #pop will work on indexing
print(movies)
print(trash_bin)
#pop
list1=["surya",2,3,4.5] #this is append opposite and pop will store value
list1.pop() 
print(list1)
#sort - ascending to decending
numbers = [3,5,5,6,4,2,"surya","python","AI"] #sort can do for int or string it will not support both
numbers = ["surya","raja","python","AI","powerBI"]
numbers.sort()
numbers.sort(reverse=True)
print(numbers)

mobiles=["1 plus","Samgsung","oppo","Apple"]
mobiles = ["Apple","Samngsung",["1 plus","oppo"]] #nested list into list
print(mobiles[1])
print(mobiles[2][0])

#count
print(mobiles.count("Apple"))

#extend we can keep string and Intiger
list1=[1,2,3]
list2=[4,5,6]
list3=["surya","ram","krishna"]
print(list1)
list1.extend(list2+list3)
print(list1)
print(len(list1))

















