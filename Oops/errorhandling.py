"""
syntax error: mispeeled, missing column or unbalanced parathsesis
type error: int,float error
name error: variable or function not found in scope(name 'x' is not defined error is raised when the program attempts to access or use a variable that has not been defined or assigned a value. This can happen if the variable is spelled incorrectly, or if it is accessed before it has been defined.)
index error: out of range (ex:phone number more than 10 digits)
key error: when key is not found in dictionary
valueerror: value not found
attribute error: when an attribute or method not found in object
IO error: input/output operation reading,writing(file hadling error)
Zero division error: divided by zero
Import error: while importing
Indentation error: spaces or tab error
"""
"""amount = 10000
try:
    if(amount / 0):
        print("you are eligible to purchase self")
except:
    print("indentation error")"""

"""a = 10
try:
 print(a/0)
except:
 print("Zero division error")"""

"""try:
    phone_number = int(input("Enter number:"))
    print(phone_number)
except ValueError:
    print("only use numbers for phone number")"""

"""try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("Can't divided anything with zero")"""

try:
    file = open("D:\Python training\Pythonlife\pyhtonlifelearning\Oops\python.txt",'r')
    for text in file:
        print(text)
except FileNotFoundError:
    print("file is not found")

finally:
    print("Success")




