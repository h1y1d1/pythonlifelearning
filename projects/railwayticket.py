class Account():
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def checkpassword(self,password):
        return self.password == password
        
accounts = [
    #Account("","")
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

    