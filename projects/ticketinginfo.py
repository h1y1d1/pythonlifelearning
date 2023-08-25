class account():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def checkpassword(self,password):
        return self.password == password

class traininfo():
    def __init__(self,train_num,source,destination,available_seats):
        self.train_num=train_num
        self.source=source
        self.destination=destination
        self.available_seats=available_seats
    def displayinfo(self):
        
        print(f"train_num: {self.train_num}")
        print(f"source: {self.source}")
        print(f"destination: {self.destination}")
        print(f"available_seats: {self.available_seats}")
        

class passengerlist():
    def __init__(self,p_name,p_age,p_mobileno):
        self.p_name=p_name
        self.p_age=p_age
        self.p_mobileno=p_mobileno
    def passengerinfo(self):
      
        print(f"passenger name:          {self.p_name}")
        print(f"passenger age:           {self.p_age}")
        print(f"passenger mobile number: {self.p_mobileno} \n")


accounts=[]
loginaccount = None
while(True):
    print("enter 1 for account creation\n2 for login\n")
    info = input("\n Enter Choice:  ")
    if int(info)==1:
        username=input("enter username:  ")
        password=input("enter password:  ")
        accounts.append(account(username,password))
        print("account created successfully\n")
    elif int(info)==2:
        username=input("enter username:  ")
        password=input("enter password:  ")
        for i in accounts:
            if i.username == username and i.checkpassword(password):
                loginaccount = account
                print(f"{username} login successful \n")
                break
        if loginaccount is None:
                print("Invaid username or password")
        else:
            print("welcome")
            break 
    else:
        print("entered wrong input")


trains = [traininfo(12389,"hyderabad","Vijayawada",400),
        traininfo(23405,"Guntur","Vijayawada",420),
        traininfo(12345,"hyderabad","Guntur",40)]
while(True):
    if loginaccount is not None:
        user_input= input(("enter 1 to know about train info: \nenter 2 to exit:  "))
        if int(user_input) == 1:
            print("-----------Available Train Details------------")
            for i in trains:
                print("---------------------------")
                i.displayinfo()
                print("---------------------------\n")
            req_train = int(input("enter train number: "))
            for i in range(len(trains)):
                if req_train == trains[i].train_num:
                    print("\navailable tickets for this train are : ", trains[i].available_seats)
                    if(trains[i].available_seats<=0):
                        print("sufficent tickets not avaiable")
                        break
                    tickets = int(input("please enter number of tickets : "))

                    if(tickets <= trains[i].available_seats and tickets>0):
                        p_name1 = input("enter passenger name:  ")
                        p_age1 = input("enter passenger age:  ")
                        p_mobileno1 = input("enter passenger mobileno:  ")
                        p =passengerlist(p_name1,p_age1,p_mobileno1)
                        print("------------------------------")
                        print(tickets,"tickets have been booked successfully")
                        print("------------------------------")
                        print("*******************************")
                        print("       Your Ticket Details         ")
                        print("********************************")
                        print("Train Number:        ",trains[i].train_num)
                        print("Source:              ",trains[i].source)
                        print("Destination:         ",trains[i].destination)
                        p.passengerinfo()
                        print("**************************")
                        trains[i].available_seats = trains[i].available_seats-tickets
                    elif(tickets > trains[i].available_seats):
                        print("sufficient tickets not available")
                    else:
                        print("please enter valid tickets")
        elif int(user_input) == 2:
            break
        else:
            print("enter valid details")
