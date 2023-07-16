#pass calculator
maths = 90
eng = 87
if maths>35 and eng>35:
    print("pass")
else:
    print("fail")

maths=int(input("enter math marks:"))
eng=int(input("enter eng marks"))
if maths>35 and eng>35:
    print("pass")
elif maths>100 or eng>100:
    print("please enter a value between 0 to 100")
else:
    print("fail")

sub1 = int(input("enter sub1 marks:"))
sub2 = int(input("enter sub2 marks:"))

if sub1>35 and sub2>35:
    print("pass")
elif sub1>100 or sub2>100:
    print("invalid input")
else:
    print("fail")

maths=int(input("enter math marks:"))
eng=int(input("enter eng marks"))
if (maths>35 and maths<101) and (eng>35 and eng<101):
    print("pass")
else:
    print("fail")

maths:float(input("enter name:"))
if maths>35 and maths<101:
    print("pass")
else:
    print("fail")

