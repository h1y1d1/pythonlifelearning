"""i = 1
while i < 6:
    print(i)
    i += 1 # i = i + 1(old form)"""

"""username = input("enter username:")
password = input("enter password:")

while username!="surya" and password != "1111":
    username = input("enter username:")
    password = input("enter password:")"""

"""num = int(input("enter number: "))
total = 0
while num!=0:
    total+num
    print(num)
    num += int(input("enter number: "))
    
print(num)"""

"""marks = int(input("enter your marks: "))

while marks<35:
    print("try again in next sem")
    marks = int(input("enter your marks: "))
else:
    print("passssss")"""

#loop 1. statement -- break, continue, pass

"""marks = int(input("enter your marks: "))
count = 1
while marks<35:
    if count<3:         
        print("try again in next sem")
        count += 1   
        marks = int(input("enter your marks: "))
    else:
        print("out of attempts")
        break
else:
    print("passssss")"""

#prime numbers...100 add and get sum...
"""num = 1
while num<51:
    if num%5==0:
        print("busssss")
        num+=1
    else:
        print(num)
        num+=1"""

"""circle = int(input("enter your circle radius: "))
count = 1
while circle !=0:
    area = (22/7)*(circle**2)
    print("the area of ",count,"circle is:",area)
    count+=1
    circle = int(input("enter your circle radius: "))"""

#first ten odd nymbers -- 1,3,5,7,9,11,13,15,17,19,21

count = 0
num = 0
while count<10:
    if num%2!=0:
        print(num)
        num+=1
        count+=1
    else:
        print("skip")
        num+=1


