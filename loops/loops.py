# FOR/While/Nested FOR loop

"""name = "varma"

for i in name:
    print(name)

#Write a Python program that uses a for loop to calculate and print the sum of all the even numbers between 1 and 50 (inclusive)."""
#1 -- 0, 2-- 2, 3--2, 6,
"""total = 0
for i in range(1,51):
    if 1%2!=0:
        total = total + i
        print(total)

total = 0
for i in range(1,51):
    total = total+i
print(total)

#While loop
i = 1
while i < 6:
    print(i)
    i += 1"""

#login
"""user_name = input("enter user name:")
password = input("enter password:")

while user_name!= "varma" and password != "1111":
    user_name = input("enter user name:")
    password = input("enter password:")"""

"""number = int(input("enter number:"))
total = 0
while number!=0:
    total = total + number
    print(total)
    number = int(input("enter number:"))"""

#marks
"""marks = int(input("enter marks:"))

while marks<35:
    print("try next sem")
    marks = int(input("enter marks:"))
else:
    print("passssssssssss")"""

#loops 1. statements --- break, continue, pass

"""marks = int(input("enter marks:"))
count = 1
while marks<34:
    if count<3:
        print("try again in next sem")
        count+=1
        marks = int(input("enter marks:"))
    else:
        print("out of attempts")
        break
else:
    print("passsss")"""

#prime numbers... 100 add and get sum...

"""num = 1
while num<51:
    if num%5!=0:
        print("busss")
    else:
        print(num)
        num+=1
    break"""

"""circle = int(input("Enter your circle radius: "))
count = 1
while circle !=0:
    area = (22/7)*circle**2
    print("The area of",count,"circle is:",area)
    count+=1
    circle = int(input("Enter your circle radius: "))"""

#first 10 odd numers -- 1,3,5,7,9,11,13,15,17,19
count = 0
num = 0
while count<15:
    if num%2!=0:
        print(num)
        num+=1
        count+=1
    else:
        num+=1