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
"""create = open("D:\Python training\Pythonlife\pyhtonlifelearning\Oops\pythonlife.txt",'w')
create.write("I am learning file handling today")"""

#if file not available
"""saturday = open("file_handling.txt",'w')
saturday.write("saturday is the best day")"""

#append
"""append = open("append.txt",'a')

append.write("surya is a good boy")
append.write("surya sir is not a bad boy")
append.close()"""

"""python = open("D:\Python training\Pythonlife\pyhtonlifelearning\Oops\python_intro.txt","r")

#print(python.read(25))
text = python.readlines()
for lines in text:
    word = lines.split()

print(word)"""

import csv

with open('d:\IT Training courses\SQL Server\Employee Sample Data.xlsx.csv', 'r') as csvfile:
    #csvfile.write("End of data")
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
