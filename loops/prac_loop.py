#Write a Python program that uses a for loop to calculate and print the sum of all the even numbers between 1 and 50 (inclusive).

#1 loop ---0,2---2,3--2,4--6 even == and odd !=
total = 0
for i in range(1,51):
    if i%2==0:
        total = total+i
print(total)
   