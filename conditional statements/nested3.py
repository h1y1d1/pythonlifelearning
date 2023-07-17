#gratest among three numbers using nested if statement

"""
check if the number is "a" greater than b,if yes,
check if the number is "a" greater than c,if yes,
"a" ius greater number among the three.

"""
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)