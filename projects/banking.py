class Account():    
    def __init__(self, username, password, balance=0):
        self.username=username
        self.password=password
        self.balance=balance

    def checkpassword(self,password):
        self.password == password
           
    def deposit(self,depositamount):
        self.depositamount = depositamount
        print("\nAvailable Balance for Account Holder",self.username,"is",self.balance,"\n")
        self.balance = self.balance + self.depositamount
        print(self.username,"your Account is Credited with Amount of ",self.depositamount)
        print("-----------------------------------")
        print("      User Account Details       ")
        print("-----------------------------------")
        print(f"Useracount:        {self.username}")
        print(f"Available Balance: {self.balance}")
        print(f"Amount Credited:    {self.depositamount}")
        print("-----------------------------------")

    def withdrawfunds(self,withdrawfunds):
        self.withdrawfunds = withdrawfunds
        self.balance = self.balance-self.withdrawfunds
        print(self.username,"your Account is Debited with Amount of ",self.withdrawfunds)
        print("-----------------------------------")
        print("      User Account Details       ")
        print("-----------------------------------")
        print(f"Useracount:     {self.username}")
        print(f"Available Balance:  {self.balance}")
        print(f"Amount Debited:    {self.withdrawfunds}")
        print("-----------------------------------")

    def Checkbalance(self):
        print("-----------------------------------")
        print("      User Account Details       ")
        print("-----------------------------------")
        print(f"useracount: {self.username}")
        print(f"available balance: {self.balance}")
        print("-----------------------------------")

    def mini_statement(self,depositamount,withdrawfunds):
        self.depositamount=depositamount
        self.withdrawfunds = withdrawfunds
        print("-----------------------------------")
        print("         Mini Statement          ")
        print("-----------------------------------")
        print(f"Useracount:     {self.username}")
        print(f"Available Balance:      {self.balance}")
        if(self.depositamount>0):
            print(f"Amount Deposited:       {self.depositamount}")
        else:
            print("No debit transactions done")
        if(self.withdrawfunds>0):
            print(f"Amount Withdrawn:       {self.withdrawfunds}")
        else:
            print("No credit transactions done")
        print("-----------------------------------")

account = [Account("user1","password1",0),Account("user2","password2",0)]
loginaccount = None

while True:
    input1 = input("Please find below options \n1. User Account Creation \n2. Login ")
    if int(input1) == 1:
        username1 = input("please enter Username:  ")
        pwd1 = input("please enter Password: ")
        account.append(Account(username1,pwd1))
        print("\n--------------------------------")
        print("User Account Created Sucessfully")
        print("--------------------------------\n")
    elif int(input1) == 2:
        username1 = input("please enter Username:  ")
        pwd1 = input("please enter Password: ")
        for i in account:
            if i.username == username1 and i.password == pwd1:
                loginaccount = account
                print("\n--------------------------------")
                print(f"{username1} login is successfully")
                print("--------------------------------\n")
        break
    else:
        print("invalid username or password")

depositamount=0
withdraw_amount=0

while True:
    user_input=input("\nwould you like to tranasct with bank enter \ny for Yes or\nn for No ")
    if user_input.lower() == 'y': 
        print("\n--------------------------------")
        print("1. Amount deposit \n2. With draw funds \n3. Check Balance \n4. View Mini Statement")
        print("----------------------------------\n")
        transactions = input("selected required option ")
        for i in account:
            if i.username == username1 and i.password == pwd1:        
                if int(transactions) == 1:
                    depositamount = int(input("\nEnter the amount you would like to deposit: "))
                    i.deposit(depositamount)
                elif int(transactions) == 2:
                    print("\nAvailable Balance is",i.balance)
                    withdraw_amount = int(input("\nenter the amount you would like to withdraw: "))
                    i. withdrawfunds(withdraw_amount)
                elif int(transactions)==3:
                    i.Checkbalance()
                elif int(transactions) == 4:
                    i.mini_statement(depositamount,withdraw_amount)
                else:
                    print("invalid input")               
    elif user_input.lower() == 'n':
        break
    else:
        print("Enter Y or N")