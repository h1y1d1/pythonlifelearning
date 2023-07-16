
maths=int(input("enter math marks:"))
eng=int(input("enter eng marks"))
if (maths>34 and maths<101) and (eng>34 and eng<101):
    print("pass")
elif (maths<35 and maths>-1) and (eng<35 and eng>-1):
    print("fail")
else:
    print("input invalid")
