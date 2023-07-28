#file handling

"""
Versatility
flexibility
user-friendly
cross-platform

r: open an existing file for read
w: open an existing file to write
a: append (add at the end) - it wont override the existing
r+: read and write, previous data in the file will be overridden
w+: write and read and overiding
a+: append and read data from file

"""
#Read file
"""text = open("D:\Python training\Pythonlife\pyhtonlifelearning\Oops\python.txt",'r')

for lines in text:
    print(lines)"""

#creating file
create = open("D:\Python training\Pythonlife\pyhtonlifelearning\Oops\pythonlife.txt",'w')
create.write("this is a session about file handling")