class Account:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def checkpassword(self,password):
        return self.password == password
    
class traininfo:
    def __init__(self,train_num,destination,avl_seats,source):
        self.train_num = train_num
        self.destination = destination
        self.avl_seats = avl_seats
        self.source = source
    def displayinfo(self):
        print(f"train_num {self.train_num}")
        print(f"destination {self.destination}")
        print(f"avl_seats {self.avl_seats}")
        print(f"source {self.source}")
        
        
accounts = [
    Account("user1","password")
]
loginaccount = None
while True:
    print("1.create an account:\n 2.login")
    choice=int(input("enter choice: "))
    if choice == 1:
        username=input("enter username: ")
        password=input("enter password: ")
        accounts.append(Account(username,password))
        print("account created successful")
    elif choice == 2:
        username=input("enter username: ")
        password=input("enter password: ")
        for account in accounts:
            if account.username == username and account.checkpassword(password):
                loginaccount=account
                print(f"{username} is login successful")
                break
        if loginaccount is None:
            print("invalid username or password")
        else:
            print("Welcome to IRCTC")
            break
    else:
        print("enter valid details")
#print("search ur destination")
if loginaccount is not None:
    trains=[traininfo("12345","hyderabad","130","vijayawada"),
            traininfo("12345","vja","110","vizag")]
    for train in trains:
        train.displayinfo()



    # train_details = []
    # print("1. Vizag:\n 2. Vijayawada:\n 3. hyderabad:\n")
    # destiny = int(input("choose ur option: "))
    # if destiny == 1:
    #     train_num = "12345"
    #     destination = "Vijayawada"
    #     avl_seats = "120"
    #     print("train_num",train_num,"destination",destination,"avl_seats",avl_seats)
    # elif destiny==2:
    #     train_num = "67891"
    #     destination = "Vizag"
    #     avl_seats = "115"
    #     print("train_num",train_num,"destination",destination,"avl_seats",avl_seats)
    # elif destiny==3:
    #     train_num = "78901"
    #     destination = "Hyderabad"
    #     avl_seats = "120"
    #     print("train_num",train_num,"destination",destination,"avl_seats",avl_seats)
    # else:
    #     print("Please select ur destination")


    