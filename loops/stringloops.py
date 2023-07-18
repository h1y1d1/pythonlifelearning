#Write a Python program that uses a for loop to count and print the number of vowels (a, e, i, o, u) in a given string.

"""name = "Write a Python program that uses a for loop to count and print the number of vowels (a, e, i, o, u) in a given string."
v_count = 0
letters_count = 0
for i in name:
    if i in 'aeiou':
        v_count = v_count+1
    else:
        letters_count = letters_count+1
print(v_count)
print(letters_count)"""

name = "aadddsakfnkjsdnkjsn"
a_count = 0
for i in name:
    if i=="a":
        a_count = a_count+1
print(a_count)