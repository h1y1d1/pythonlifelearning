class Account:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def checkpassword(self,password):
        return self.password == password
    
Accounts=[]
loginaccount = None
while True:
    info = input("Enter 1 for account creation and 2 for login: ")
    if int(info) == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        Accounts.append(Account(username, password))
        print("Account created successfully")
    elif int(info)==2:
            username=input("enter username: ")
            password=input("enter password: ")
            for i in Accounts:
                if i.username == username and i.checkpassword(password):
                    loginaccount = Account
                    print(f"{username} login is successful")
                    break
            if loginaccount is None:
                print("invalid username or password")
            else:
                print("welcome to IRCTC")
                break
    else:
            print("enter wrong input")
class traininfo:
    def __init__(self,train_num,destination,avl_seats,source):
        self.train_num = train_num
        self.destination = destination
        self.avl_seats = avl_seats
        self.source = source
    def displayinfo(self):
        print("--------------------------------")
        print(f"train_num {self.train_num}")
        print(f"destination {self.destination}")
        print(f"avl_seats {self.avl_seats}")
        print(f"source {self.source}")
        print("--------------------------------")

class passengerlist():
    def __init__(self,p_name,p_age,p_mobileno):
        self.p_name=p_name
        self.p_age=p_age
        self.p_mobileno=p_mobileno
    def passengerinfo(self):
        print("******************************")
        print("                Passengerlist           ")
        print("******************************")
        print(f"passengername:          {self.p_name}")
        print(f"passengerage:          {self.p_age}")
        print(f"passengermobileno:          {self.p_mobileno} \n")
        print("******************************")

loginaccount = 1
trainlist = [13456,23456,34567]
trains = [traininfo(13456,"hyderabad","vijayawada",400),
          traininfo(23456,"vizag","vijayawada",220),
          traininfo(34567,"vijayawada","vizag",340)]
while(True):
    if loginaccount is not None:
        user_input=input("enter 1 to know about train info: \n enter 2 to exit: ")
        if int(user_input)==1:
            for i in trains:
                i.displayinfo()
            req_train = int(input("enter train number: "))
            for i in range(len(trains)):
                if req_train == trains[i].train_num:
                    print("\n available tickets for this train are: ", trains[i].avl_seats)
                    if (trains[i].avl_seats<=0):
                        print("sufficient tickets not available")
                        break
                    tickets = int(input("please enter no of tickets: "))

                    if(tickets<=trains[i].avl_seats and tickets>0):
                        p_name1 = input("enter passenger name: ")
                        p_age1 = input("enter passenger age: ")
                        p_mobileno1 = input("enter passenger mobileno: ")
                        p =passengerlist(p_name1,p_age1,p_mobileno1)
                        print("------------------------------------")
                        print(tickets,"tickets has been blocked succesfully")
                        print("------------------------------------")
                        p.passengerinfo()
                        trains[i].avl_seats = trains[i].avl_seats=tickets
                    elif(tickets > trains[i].avl_seats):
                        print("sufficient tickets not available")
                    else:
                        print("please enter valid tickets")
        elif int(user_input)==2:
            break
        else:
            print("enter valid details")




