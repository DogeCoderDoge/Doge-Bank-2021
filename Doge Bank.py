print("Welcome to Doge Bank") 
print("How much money would you like to start with?") 
balance = int(input()) 
session_live = True

while session_live:
    print("Great! You can type DEPOSIT to DEPOSIT money, BAL to check your  BALANCE and WITHDRAW to WITHDRAW money, EXIT to exit.") 
    operation = input()
    if operation == "DEPOSIT": 
        print("You have started a deposit operation, say Y to continue") 
        confirm = input() 
        if confirm == "Y": 
            print("How much would you like to deposit?") 
            depositNum = int(input()) 
            balance = balance + depositNum
            print("You have deposited", depositNum, "| Your current balance is", balance)
    
    elif operation == "BAL":
        print("Your current balance is", balance)

    elif operation == "WITHDRAW":
        print("You have started a withdraw operation, say Y to continue")
        confirm = input()
        if confirm == "Y":
            print("How much would you like to withdraw?")
            withdrawNum = int(input())
            balance = balance - withdrawNum
            print("You have withdrawed", withdrawNum, "| Your current balance is", balance)  

    elif operation == "EXIT":
        print("Thank you for using our DOGE ATM")
        session_live = False
    