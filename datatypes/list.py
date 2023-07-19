#list
user_name = ["venkat","sunita","raki"]
print(user_name)
print(type(user_name))


"""Lists are used to store multiple items in a single variable. In this section we will learn about:

1.) Creating lists
2.) Indexing and Slicing Lists
3.) Basic List Methods
4.) Nesting Lists
5.) Introduction to List Comprehensions
Lists are constructed with brackets [ ] and commas separating every element in the list.

Let's go ahead and see how we can construct lists!"""

#create a list with name of student_names
student_names=["shiva","vishwa","akhil","chandu","surya","emma","staine"]
print(student_names)
print(type(student_names))

grade = [23,2.5,3.5,44,78]
print(grade)
print(type(grade))

#name = "surya"
#print(name[2])

#Indexing and Slicing

#Indexing and slicing work just like in strings. Let's make a new list to remind ourselves of how this works:

movies = ["RRR", "KGF 2", "Radhe shyam","sita ramam","karthikeya 2","pushpa"]
print(movies)
print(movies[2])
print(movies[2:4])
print(movies[:3])
print(movies[-2])
print(movies[-5])
print(movies[-4:-3])


#list methods -- append/insert/trash/clear/
movies=["RRR", "KGF 2", "RS","sita ramam","karthikeya 2","pushpa"]
movies.append("kgf1")
movies.insert(2,"Sahoo")
movies.remove("RRR")
#movies.clear()
movies.pop(3)
print(movies)

mobiles =["Apple","linux","google","samsung",["1 plus","oppo"]]
print(mobiles)
print(mobiles.count("Apple"))

numbers = [2,5,7,8,4,7,8,9]
numbers.sort(reverse=True)
print(numbers)

list1 = [1,2,3]
list2 = [ "surya ", "python "," life "]
print(list1)
list1.extend(list2)
print(list1)
print(len(list1))