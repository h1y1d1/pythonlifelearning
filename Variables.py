# What is a Variable in Python?
# A Python variable is a reserved memory location to store values. In other words, a variable in a python program gives data to the computer for processing.
# Variable Types - Every value in Python has a datatype. Different data types in Python are Numbers, List, Tuple, Strings, Dictionary, etc. Variables in Python can be declared by any name or even alphabets like a, aa, abc, etc.

a = 100
print(a)

# declare a variable
f = 0
print(f)
# re-declare variable
f = 'guru99'
print(f)

# Python String Concatenation and Variable

# undefined throw error
# a='guru'
# b=99
# print a+b

# Correct code
a = 'guru'
b = 99
print(a + str(b))

# Python Variable Types: Local & Global - There are two types of variables in Python, Global variable and Local variable. When you want to use the same variable for rest of your program or module you declare it as a global variable, while if you want to use the variable in a specific function or method, you use a local variable while Python variable declaration.
f = 101
print(f)

# Global vs Local variable in functions
# Global function:
def somefunction():
# Local variable
    f = 'I am learning Python'
    print(f)
somefunction()
print(f)
f = 101
print(f)
# Global vs.local variables in functions
def someFunction():
  global f
  print(f)
  f = "changing global variable"
someFunction()
print(f)

#Delete a variable - You can also delete Python variables using the command del “variable name”.
f=11;
print(f)


del f
print(f)

#To run without error
f=11;
print(f)
del f
print(f)