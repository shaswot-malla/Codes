#CALCULATOR
'''
print ("Welcome to Simple Calculator")
while True:
    a = float(input("Enter first number: "))
    operator = input(" : ")
    b = float(input("Enter second number: "))

    if operator == "+":
        addition = str(a + b)
        print ("Answer: " + addition)

    elif operator == "-":
        subtraction = str(a-b)
        print ("Answer: " + subtraction)
    
    elif operator == "*":
        multiplication = str(a*b)
        print ("Answer: " + multiplication)

    elif operator == "/":
        divison = str(a/b)
        print ("Answer: " + divison)

    else:
        print ("INVALID!!!!!!!!")
'''


#DiSCOUNT 
'''
price = int(input("Enter the price: "))
if price <= 5000:
    amount = str( price - 5/100 * price)
    print ("Your total after 5 percent discount is: " + amount)

elif price > 5000 and price <=10000:
    amount = str( price - 10/100 * price)
    print ( "Your total after 10 percent discount is: " + amount)

elif price > 10000 and price <= 15000:
    amount = str( price - 20/100 * price)
    print ( "Your total after 20 percent discount is: " + amount)

elif price > 15000:
    amount = str( price - 30/100 * price)
    print ("Your total after 30 percent discount is: " + amount)

print("THANK YOU FOR SHOPPING WITH US!!")
'''



## LEAP YEAR
''' 
year = int(input("Enter a year: "))
if year % 4 == 0:
    print ("It is leap year!!!")
else:
    print ("It is not leap year!")
'''



## ATM

print ("WELCOME TO ATM")
user = str(input("ENTER YOUR USERNAME: "))
if (user=="shaswot"):
    print("Welcome")
else:
    print("ERROR")
code = int(input("ENTER THE CODE: "))
if (code==4355):
    print ("YOU HAVE ENTERED THE MACHINE")
else:
    print("ACCESS DENIED")

print (" 1.) View Balance   2.) Withdraw   3.) Deposit   4.) EXIT " )
current_balance = 1000
while True:
    choose = int(input("Press 1,2,3 or 4 according to your wish! : "))
    if choose == 1:
        print (" Your current balance is: " + "Rs." + str(current_balance))
    elif choose == 2:
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw < current_balance:
            confirmation = str(input("Are you sure you want to withdraw the amount???"))
            if confirmation == "yes":
                print (" Please wait! Your cash is being withdrawn. ")
                current_balance=current_balance-withdraw #yo edit haneko chu 
                print("Updated balance is = ",current_balance)
            else:
                print (" CANCELLED ")
        else:
            print (" YOU DO NOT HAVE SUFFICIENT BALANCE!")      
        #removed 2 lines from here 
    
    elif choose == 3:
        deposit = int(input("Enter the amount you want to deposit: "))
        print (" You have successfully deposited " + "Rs." + str(deposit) + " in your account! ")
        current_balance=current_balance+deposit
       # upblc = str(1000 + deposit )                #Removed this line 
        print (" New balance = ", current_balance)
    
    elif choose == 4:
        print (" Transaction Complete!! ")
        print (" Transaction number : 12345678 ")
        print (" Current Interest Rate: 3.4%")
        print (" THANK YOU FOR CHOOSING OUR BANK!! ") 
        break







# FACTORIAL
'''
factorial = 1
num = int(input("Enter a number: "))
for i in range(factorial,num+1):
    factorial = factorial * i
    print (factorial)
'''



#Password Generator
'''
import random
x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*-_=+<>/?|"
password = "".join(random.sample(x,8))
print ("Random password is: " + password)
'''