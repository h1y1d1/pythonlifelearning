
"""def sum_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result

print(sum_numbers(1,2,3,4))
print(sum_numbers(5,10,15))
print(sum_numbers(1,23,44,55,66,77,889,9776,5,54,5))"""

def details(**kwargs):
    for key, value in kwargs.items():
        print(key,value)

details(name="venkat", age=44, city="toronto",profession="tester")

#name="venkat"
#print(f"my name is:","venkat")

