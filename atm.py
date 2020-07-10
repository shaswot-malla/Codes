print ("WELCOME TO THE MACHINE!!")
user = input(" Enter your username: ")
if user == "shaswot":
    print ("Hi! Shaswot")
else:
    print ("INCORRECT USERNAME!!!!!")
password = int(input(" Enter your code: "))
if password == 4355:
    print ("You have now entered the machine")
else:
    print("Access Denied")

print (" 1.) View Balance      2.) Withdraw      3.) Deposit       4.)EXIT ")
current_balance = 1000
while True:
    choose = int(input(" Press 1,2,3 or 4 as you wish: "))
    if choose == 1:
        print ("Your Current Balance is " + " Rs. " + str(current_balance))
    
    elif choose == 2:
        withdraw = int(input(" Enter the amount you want to withdraw: "))
        if withdraw < current_balance:
            confirm = input(" ARE YOU SURE YOU WANT TO WITHDRAW THE AMOUNT?? ")    
            if confirm ==  "yes":
                print(" Please wait your cash is beig withdrawn... ")
                current_balance = current_balance - withdraw
                print (" Your updated balance is " + str(current_balance))
            else:
                print ( " CANCELLED ")
        else: 
            print (" Sorry! You do not have sufficient balance! ")     

    elif choose == 3:
        deposit = int(input(" Enter the amount you want to deposit: "))
        current_balance = current_balance + deposit
        print ( " Your updated balance is " + " Rs." + str(current_balance))
    
    elif choose == 4:
        print (" Thank you for using our service!! See you soon! ")
        break
            
