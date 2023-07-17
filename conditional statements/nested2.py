#ATM code and pin value is 2222
pin = int(input("enter your pin:"))
balance = 902345
if pin==2222:
    print("Welcome to python bank")
    print("1.balance enquiry")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.help")
    option = int(input("enter the option:"))
    if option == 1:
        print("your current balance is:",balance,"rs/-")
    elif option == 2:
        w_amount = int(input("enter withdraw amount:"))
        if w_amount<=balance:
            balance = balance - w_amount
            print("Your updated balance is:",balance)
            max_withdrawal_amount = 10000
            daily_withdrawal_limit = 10000
            if balance >= daily_withdrawal_limit:
                print("max amount limit cross")
            else:
                print("balance")
        else:
            print("Insufficient balance")
    elif option == 3:
        deposit = int(input("enter deposit amount:"))
        balance = balance + deposit
        print("Your updated balance is:",balance)
    elif option == 4:
        help = (input("how can i help you:"))
        print("how can i help you")
    else:
        print("invalid option")

else:
    print("Invalid pin")
# 5. Mobile number change need new contact information (enter old mobile and enter new mobile)
# 6. PIN number change 

