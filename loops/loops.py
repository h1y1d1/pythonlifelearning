#for loop
"""
for i(iteration) in something:
    print("ok")

"""

#range-- from to to range(5) range is a method

#print(range(2,5))
"""list1 = [1,2,3,4,5,6,7,8,9,10]
for i in list1:
    if i%2==0:
        print(i,"-even number")
    else:
        print(i,"-odd number")"""

#create tables -- 2*2=4,2*3=6,2*4=8
"""table = int(input("enter table number:"))
for num in range(1,21):
    print(table,"X",num,"=",num*table)

#take a list -- [34,65,87,45,22,12,34,35,46,57,68]
# 3rd highest value should multiply

third = [34,65,87,45,22,12,34,35,46,57,68]
third.sort(reverse=True)
print (third)

for j in third:
    if j%2!=0:
        if j!=third[2]:
            print(j*third[2])
        else:
            print(j)
    else:
        print(j)"""

