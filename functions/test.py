
#test1
def calculate_area_circle(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area
radius = 5
area = calculate_area_circle(radius)
print("The area of the circle with radius", "is", "area")

#test2
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime)

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#test3
def reverse_string(s):
    return s[::-1]
print(reverse_string)

#test4


def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = (find_common_elements)
print("Common elements:", common_elements)



#test5
def capitalize_words(sentence):
    return sentence.title()
sentence = input("enter a word:")
print("capitalize_words",capitalize_words(sentence))

#sentence = input("Enter a sentence: ")
#print("Capitalized sentence:", capitalize_words(sentence))
