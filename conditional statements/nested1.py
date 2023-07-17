marks=int(input("enter math marks:"))
#-- avg,topper,above avg,distinction
if marks>35:
    print("pass")
    if marks>35 and marks<45:
        print("avg")
    elif marks>45 and marks<65:
        print("above avg")
    elif marks>65 and marks<90:
        print("Topper")
    elif marks>90 and marks<100:
        print("Distinction")
else:
    print("fail")