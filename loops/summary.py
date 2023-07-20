"""
FOR loop - For loop is used to iterate over set/range.list of values
WHILE loop - While loop is a Run until break/condition false/pass
"""

"""10*1 20*1 30*1
10*2 20*2 30*2
10*3 20*3 30*3
10*4 20*4 30*4
10*5 20*5 30*5..."""

#nested FOR and WHILE

"""list1 = [1,2,3,4,5]
list2 = [10,20,30,40,50]

for i in list2:
    for j in list1:
        print(i,i*j)
        #print("_____")
    print("_____")"""

#Scenario - hi _______, welcome to our company... 100 members

#names = ["surya","chandana","varma","rajeswari","sai prasad","bhanu prakash","rudra","sanju"]
#e_id = [50201,50202,50203,50205,50206,50207,50208]
"""details = []
for i in names:
     for j in e_id:
        if i==j:    
            print("hi",i,"Welcome to our company","your emp id is: ",j)"""

"""for i in range(7):
    print("hi",names[i],"Welcome to our company","your emp id is:",e_id[i])"""


"""exam = input("enter input y/n:")

if exam.lower()=="y":
    exam = True
elif exam.lower() =="n":
    exam=False
else:
    print("invalid input (y/n)")

while exam==True:
    for i in range(1,6):
        print(i,"subject",i)
    subject = int((input("enter subjetc number:")))
    if subject ==1:
        print("sub1 exam")
    elif subject ==2:
        print("sub2 exam")
    elif subject ==3:
        print("sub3 exam")
    elif subject ==4:
        print("sub4 exam")
    elif subject ==5:
        print("sub5 exam")
    else:
        print("wrong input")
    break"""

users = {"surya":"1122","chandana":"1123","varma":"1124","rajeswari":"1125","sai prasad":"1126","bhanu prakash":"1127","rudra":"1128","sanju":"1129"}
print(users.keys())

user_name = input("enter username:")
password = input("enter password:")

#print(users.keys())
#print(users.values())

for i in range(len(users)):
    for j in range(2):
        if user_name in  users.keys() and password == users[user_name]:
            print("welcome to insta")
            print(users[user_name])
            break
        else:
            print("wrong details")
            user_name = input("enter username:")
            password = input("enter password:")
    break
