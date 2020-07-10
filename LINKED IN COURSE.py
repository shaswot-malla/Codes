'''
q = int(input("Enter a number"))
if q%2 == 0:
    print (f"q is an even number")
else:
    print (f"it is odd")
'''

'''
def main():
    print ("HELLO WORLD")
if __name__ == "__main__":
    main()
'''    
'''
f = 0
print (f)
f = "abc"
print (f)
print ("this is a string "  + str(123))

def someFunction ():
    global f   
    f = "def"
    print (f)
someFunction ()
print (f)
'''
'''
def func1():
    print ("I am a function")
func1 ()
print (func1())
print (func1)
'''
#CONDITIONAL STRUCTURES:
'''
x, y = 10, 100
if (x<y):
    st = "x is less than y"
elif (x==y):
    st = "both of them are equal"
else:
    st = "x is greater than y"
print (st)
#you can also write a one line program like below if you have only two conditions if and else#
st = "x is less than y" if (x<y) else"x is greater or equal to y"
print (st)
'''

#LOOPS
'''
x = 0
while (x<6):
    print (x)
    x = x + 2
'''
'''
x = 0
for x in range (2, 8):

    print (x)
'''
#use a loop over a collection
'''
days = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY")
for d in days:
    print (d) 
'''
#break 
'''
for x in range (5, 10):
    if (x == 7): break
    print (x)
'''

#CONTINUE
'''
for x in range (5, 10):
    if (x % 2 == 0): continue
    print (x)
'''

#ENUMERATE
'''
days = ("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY")
for i,d in enumerate(days):
    print (i, d)
'''
'''
def inc(a,b=1):
    return(a+b)
a=inc(1)
a=inc(a,a)
print (a)
'''
#DATE and TIME
'''
from datetime import date
from datetime import time
from datetime import datetime
today = date.today()
print ("Todays date is", today)
print ("Date's component", today.day, today.month, today.year)
print ("Todays weekday # is: ", today.weekday())
'''
'''
print ("WELCOME TO MY COMPUTER!!")
name = input("Whats your name?")
if name == "Softwarica":
    print ("HEY THATS MY NAME TOO!!")
print ("Hi" + name)
'''
'''
print("""
Helllo 
its me
I was wondering""")
'''
'''
print ("Hello\nWorld!")
'''

#CONCATENATION
'''
You can add (concatenate) strings to strings.
You can add numbers to numbers.
If you try to add a string to a number, you get an error.
If it's in quotes, it's a string. If it's not in quotes, it's not a string.

You get the same result if you use variables :
return 
a = "cat"
b = "dog"
c = 2
d = 3

print(a + b) # 'catdog'
print(a +  "bird") # 'catbird'
print(a + c) # error
print(c + d) # 5
print(c + 4) # 6
'''
#exercice 1 ko number 3
'''
height = int(input(" Enter your height in meter: "))
weight = int(input (" Enter your weight in kgs: "))
BMI = (int(weight) / int(height**2))
print ("Your BMI is..")
print (BMI)
'''

#exer 1 ko number 8
'''
import random
i = 0
while i < 10:
    number_odd = (random.randint(0,1000))*2 + 1
    print (number_odd)
    i = i + 1
'''
'''
a = str(input("ENTER YOUR FIRST NAME :"))
b = str(input("ENTER YOUR SECOND NAME :"))
print (" YOUR FULL NAME IS " + a + b)

'''
#EXERCISE 2 Assignmentttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
m = a*b
print (m)
'''
'''
x = float(input("Enter your number: "))
r = round(x,2)
print (r)
'''

'''
a = 2.56985
x = "{:.2f}".format(a)
print (x)
''' # OR #
'''
print ("%.2f" % 2.56789)
'''
'''
n = 4
for i in range (1,11):
    print (n, 'x', i, '=', n*i)
'''
'''
num = int(input("ENTER A NUMBER: "))
if num > 1:
    for i in range(2, num):
        if (num % i == 0):
            print ("The given number is not a prime number")
else:
    print ("Yes, the number you entered is a prime number")
'''
'''
num = int(input("ENTER A NUMBER: "))
if num % 2 == 0:
    print ("YES THE NUMBER YOU ENTERED IS AN EVEN NUMBER")
else:
    print (num, " IS NOT AN EVEN NUMBER ")
'''
'''
list1 = [8,17,39,48,73,83,98,111,120,153,202]
for item in list1:
    if item > 100:
        break
    if item % 2 == 0:
        print (item)
'''
'''
num = 4
for i in range (1,11):
    print (num, "X", i, "=",  num*i )
'''
#8
'''
lowest = 1
highest = 100
print ("Prime numbers between", lowest, "and", highest, "are: ")
for num in range (lowest, highest):
    if num > 1:
        for i in range (2, num):
            if (num % i == 0):
                break
        else:
            print (num)
'''
               #ORRR#
'''
for num in range (2,101):
    prime = True
    for i in range (2, num):
        if (num%i==0):
            prime = False
    if prime:
        print(num)
'''
'''
num = int(input("ENTER A NUMBER: "))
factorial = 1
for i in range(1,num + 1):
    factorial = factorial*i
print (factorial)
'''
 #TO BE CONTINUED atm
'''
print ("WELCOME TO THE MACHINE")
user = str(input("ENTER YOUR USERNAME: "))
if (user=="shaswot"):
    print("enter the code")
else:
    print("ERROR")
code = int(input("ENTER THE CODE: "))
if (code==4355):
    print ("YOU HAVE ENTERED THE MACHINE")
else:
    print("ACCESS DENIED")
'''
'''
a = str(input("Are you a girl or a boy ?\n"))
b = int(input("How old are you ?\n"))
if (a == "girl" and b >= 18) :
  print("Hello beautiful\n")
else :
  print("Goodbye !!\n")
  '''
#12
'''
n=5
for num in range(n+1):
    for i in range(num):
        print(num,end = " ")
    print("\n")
'''

#13
'''
x = int(input(" Enter a number: "))
y= str(x)
reverse = y[::-1]
result = y == reverse
print("The original and the reverse number is same = ",result)

'''
#pattern 
'''
x=1
while x<=40:
    print("*"*x)
    x+=1
    
x=39
while x>=1:
    print("*"*x)
    x-=1
'''
#WHILE SOLOLEARN
'''
x = 1
while x <= 10:
    print("*"*x)
    x = x + 1
x = 9
while x>=1:
    print("*"*x)
    x = x - 1
'''
'''
a = int(input("enter a number: "))
b = 1
while b<=10:
    print (str(a) + "X" + str(b) + " = " , (a*b))
    b = b + 1
'''
'''
i = 0
while 1 == 1:
    i = i + 1
    print (i)
    if i >= 13:
        print("THE CODE IS BREAKING")
        break
'''
'''
madman = 20
aaa = 1
fighting = True
while fighting:
    madman = madman - aaa
    print("HIT HIM MORE!!! Health is:")
    print (madman)
    if (madman == 5):
        print ("FINISH HIM AND WIN")
        break
'''
##### LIST
'''
places = [ "KATHMANDU", "POKHARA", "BIRATNAGAR", "HETAUDA", "DARJEELING", "HUMLA"]
print (places[1][2])
'''
'''
list = ["A", "B", "C", "D", "E", "F", "G"]
i = 0
while i <=6:
    print (list[i])
    i = i + 1
    if i == 5:
        print ("5th element cannot be printed", list[5])
'''
####TIP for LIST .split()
''' 
Some types, such as strings, can be indexed like lists.
Indexing strings behaves as though you are indexing a list....'

For example:

if you got a list of words in a string, intead of listing them
like this: ["a", "b", "c", "d", "e", "f", "g", "h"];
which can be boring, alot of typing and very long, you can do
something like this:

words = "I love learning Python using Sololearn!".split()
print(words)

Output:
['I', 'love', 'learning', 'Python', 'using', 'Sololearn!']

The .split() converts the entire string into a list and separates each word.
You can then use [ ] to grab an item from the index...

print(words[3])

Output:
Python
'''
'''
sen = "I really love you Muskaan".split()
print (sen)
print (sen[4])
'''
#### RE-ASSIGNING IN LIST
''' 
list1 = ["abc", "def", "ghi", "jkl", "mno", "pqr"]
list1[2] = "shas"
list1[5] = "musk"
print (list1)
'''
## OR
'''
nums = [7, 7, 7, 7, 7]
x = 0
while x < len(nums):
    nums[x] = 5
    x += 1
print(nums)
'''
'''
nums = [1,2,3,4,5,6,7,8,9,10]
nums[3] = nums[4] = nums[7]
print (nums)
'''
'''
nums = [1,2,3]
print(nums + [4,5,6])
print(nums * 2)
'''
### in helps to check if an item is in the list or not 
'''
greet = ["hi", "hello", "namaste", "hey"]
seeoff = ["bye", "adios"]
print ("hello" in greet)
print ("ciao" in seeoff)
'''
'''
college = ["SOFTWARICA", "MALPI", "NAMI", "ACE"]
enroll = input("  ENTER THE COLLEGE YOU WANT TO ENROLL IN: ")
print (enroll)
if (enroll in college):
    print ("ALLOWED")
else:
    print ("NOT POSSIBLE")
'''
###### append adds what you want to add at the end of the list
'''
num = [1,2,6,7]    
num.append("SHAS")
print (num)
'''
'''
i= int(input('Give me number!'))
x = i + 10
nums = []
while i <= x:
       nums.append(i)
       i += 1
       print(nums)
'''
#### insert is like append but you can add the element in any place you want to
''' eg1
nums = [1,2,3,4]
nums.insert(4, 5)
print (nums)
'''
'''eg2
country = ["nepal", "china", "america"]
country.insert(1, "pakistan")
print(country)
'''
'''
nat = ["geographic", "country", "whatever"]
nat.insert(0, "nation")
nat.append("a channel")
print(nat)
print(len(nat))
'''

### There are a few more useful functions and methods for lists.
### max(list): Returns the list item with the maximum value
### min(list): Returns the list item with minimum value
### list.count(obj): Returns a count of how many times an item occurs in a list
### list.remove(obj): Removes an object from a list
### list.reverse(): Reverses objects in a list

'''
words = ['hello','world','and','hello','universe']
print(max(words))
'''
'''
list = ["abc", "def", "ghi"]
print(min(list))
'''
'''
list=[1,2,3,4,5]
list.reverse()
print(list)
'''
### RANGE 
'''
Some Useful Examples..
# Note:
List is used here so it stores each number in the range in a list. without it, your output would be [0, 5] instead of [0, 1, 2, 3, 4, 5].

a = list(range(5)) 
#Outputs: [ 0, 1, 2, 3, 4 ]
# Notice it prints 5 values starting from Zero.

b = list(range(20,25))
#Outputs: [ 20, 21, 22, 23, 24 ]
# Notice it prints 20 but stops at 24.

c = list(range(6,12, 2)
#Outputs: [ 6, 8, 10 ]
# Notice the third value is the increment.
'''
'''
''''''
a = range (10, 20, 2) #creates a range from 10 to 20 every 2 steps
b = list(a)
print(a)
print (b)

OUTPUT
range(10, 20, 2)
[10, 12, 14, 16, 18]
'''
'''
x = list(range(0,10,2))
print (x)
'''
# LOOOOPS
'''
sen = ["Hi", "my", "name", "is", "Shaswot"]
a = 0
b = len(sen) - 1
while a <= b:
    c = sen[a]
    print (c)
    a = a + 1
'''
'''
for i in range(20):
    if i == 5:
        print ("Lets skip i here")
        continue
    elif i == 7:
        print ("here is our lucky number", i)
    elif i == 13:
        print ("here is a fucked up number", i)
    elif i == 18:
        print ("WE ARE STOPPING HERE")
        break
    else:
        print (i)
'''
'''
x = input(" ENTER A SYMBOL ")
for i in range (1,7):
    print (i*x)
'''
########################## JUST A SIMPLE CALCULATOR
'''
while True:
    print (" CHOOSE WHAT YOU WANNA DO ")
    print ("add ", "subtract ", "divide", "mod ", "do nothing ")
    user = input(":")

    if user == "add":
        num1 = float(input("ENTER FIRST NUMBER: "))
        num2 = float(input("ENTER SECOND NUMBER: "))
        result = str(num1 + num2)
        print ("Answer: " + result)

    if user == "subtract":
        num1 = float(input("ENTER FIRST NUMBER: "))
        num2 = float(input("ENTER SECOND NUMBER: "))
        result = str(num1 - num2)
        print ("Answer: " + result)
    
    if user == "divide":
        num1 = float(input("ENTER FIRST NUMBER: "))
        num2 = float(input("ENTER SECOND NUMBER: "))
        result = str(num1/num2)
        print ("Answer: " + result)

    if user == "mod":
        num1 = float(input("ENTER FIRST NUMBER: "))
        num2 = float(input("ENTER SECOND NUMBER: "))
        result = str(num1 % num2)
        print ("Answer: " + result)
'''
'''
i = 1
while i<100:
    print (i)
    i = i + 1
print ("TIMES UP")
'''
'''
i = 2
while True:
    if i%3 == 0:
        break
    print (i)
    i = i + 2
'''
#def 
'''
def with_exclam(word):
    print (word + "!!!")
with_exclam("HI")                   ### calling function
with_exclam("are you okay?")        ### calling function
'''
'''
def simple_addition(num1,num2):
    answer = num1 + num2 
    print ("num1 is", num1)
    print ("num2 is", num2)
    print (answer)

simple_addition(5,3)                  ### CALLING FUNCTION simple_addition
'''
'''
def twonums(x,y)
    print (x*y)
    print (x+y)
    print (x-y)
twonums (6,10)    ### calling function that you defined
'''
'''
def function(variable):
    variable += 1
    print (variable)
function (7)
'''
'''
def max(x,y):
    if x>y:
        return x
    else:
        return y
print (max(5,7))
z = max(4,2)
print(z)
'''

################# what's the difference between (return) & (print) ?
 ###  As i know, there are two differences:

 ##  1. After using (return) in a function, the next lines will be ignored. 
 # But if we use (print), all the next lines will be evaluated and run.

  ## 2. If you use (return) inside a function, you can do some operations on the result. e.g. multiply it by another value or... .
## But if we use (print),you can't do any operations on the result.
## For better understanding check this code:

## >>> def  sum(x,y):
   #              return  x+y
##>>> sum(4,5)* 2       #output:  18
     

###  >>> def  sum(x,y):
  #                print(x+y)
## >>> sum(4,5)* 2       #output: ERROR

###  because when we use (print), we can only display things.
##  but when we use (return), we can either display and sum and...
###  Just keep this in mind that you can't do operations on:  print ( )

'''
def something(x,y):
    return x * y

a = 4
b = 5
operation = something      ### assigned function something to variable operation 
print (operation (a,b))
'''
'''
def add(x,y):
    return x + y
def again(func, x,y):
    return func(func(x,y),func(x,y))

a = 5
b = 10
print(again(add,a,b))
'''
'''
def square(x):
    return x*x
def test(func,x):
    print (func(x))
##func = square ----------- helps to understand
test (square,2)
'''

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

#password random generator
'''
import random
r = "abcdefghijklmnopqrstuvwxyz1234567890"
password = "".join(random.sample(r,8))       
print (password) 
'''
#SOLOLEARN CONTINUE
'''
import random                    ## telling python to import a module named (Random)
for i in range(10):              ## tell python how many random numbers has to be generated in this case its 10
    value = random.randint(1,100) 
    print (value)
## In 3rd line we declare a variable value which stores the random numbers received by the random.randint(1,6) function
## Note: The function is already present in the module Random that we imported 
 ## a module can have n numbers of functions in it so we need to specify the name of the function that we need to import from the module

'''
'''
import math
num = 25
print(math.sqrt(num))
'''

## print(help('math'))       [ helps you to see all the fucntions in math module ]

'''
from math import pi
print (pi)
'''
'''
from math import sqrt,cos          ## from LOC 773 to 780, both give the same result. the only difference is that in the first one
print(sqrt(64))                    #   you dont have to call the module all over again                           
print(cos(0))
'''
'''
import math
print(math.sqrt(64))
print(math.cos(0))
'''
#### https://pymotw.com/3/ ## 

'''
def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(sum(10))
'''
'''
def print_nums(x):
  for i in range(x):
    print(i)
  return         ## indent of return matters alot. if its below print it returns 0. CORRECT WAY is below for
print_nums(10)
'''
#try,except and finally
'''
try:
    X = 6
    y = 10
    print(X+y)
except:
    print("Something's wrong")
'''
'''
try:
  print(1)
except:
  print(2)
finally:
  print(3)
'''
#raise
'''
print(123)
raise ValueError
print(3123)
'''
'''
password = input("Enter your password: ")
if len(password) < 6:
    raise ValueError("password must be more than 6 letters or numbers")
'''
#assert
'''
print ('hi')
assert 2+2 == 4
print ('muskaan')
assert 5+5 == 10
print ('matina')
assert 2+3 == 6                  ### False, so the next line will not be printed
print ('i dont love her')
'''
'''
temp = 5
assert (temp <= 0), "Can live atleast"
assert (temp >= 0), "Colder than fucking 0 degree"
'''
'''
def a_func():
    print("HI!!")
var = None
print(var)
a_func()
'''
#Dict
'''
age = {"Muskaan": 45, "Shaswot": 20, "Shasmu": 5}
print(age["Muskaan"])
'''
'''
my_dict = {1:"Softwarica", 2:"Malpi"}
print(my_dict[1] + " is a good college. ")
print(len(my_dict[2]))
'''
'''
cars ={"BMW":'red and luxury', "Mercedez":'black and speed'}
print(cars["BMW"])
'''
'''
List = [0,{"d":45,5:[7,8]},7]
print (List[1][5][1])           ## list[1] is {"d":45,5:[7,8]}... list[1][5] is [7,8] because its stored in 5 
'''
'''
primary = {
    "red" : [1,2,3],
    "blue" : [9,8,1],         ##commas are very imp in dict
    "green" : [7,7,7]           
}
print(primary["red"] + [4,5,6,7,8,10])
'''
'''
squares = {1:1,2:4,3:'error',4:16}
squares[3]=9
squares[2]='hi there im 2'
squares[5]=25
print(squares)
'''
'''
primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])
'''
'''
nums ={
    1: "one",
    2: "two",
    3: "three"
}
print(1 in nums)
print('three'in nums)
print(4 not in nums)
print(3 in nums)
'''
'''
#If the number before the comma is missing in the dictionary, then the number after the comma is taken as the value by default. 
## That is the reason :-
# fib.get(4,0) will give 3
# fib.get(7,5) will give 5
# Therefore 3+5 = 8
fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
'''
'''
squares = {x: x*x for x in range(7)}
print(squares)
'''
'''
odd_square = {x: x*x for x in range(11) if x%2==1 }
print(odd_square)
'''

#Tuple and Set online class         # always put comma if only one element in a tuple ('python',)
'''
tup = (10,2,"shas")
print (tup[0])
'''
'''
tup1 = 1,2,3,4,5
tup2 = ('shas','muskaan', 'nepal')
tup3 = (tup1 + tup2) * 2
tup4 = ('p,p,p,p,p,p,r,t,u')
print(tup3)
print(tup2[::-2])
print(tup4.count('p'))        #count
'''
#SET
'''
set1 = {1,2,3,4,5,6,7,8}
set2 = {'a','b','c',2,3,4}
A = {100,1,1000,10000,500,50}
B = {222,333,1,4444,5555,6666,7777}
print("The union is: " , set1|set2)
print("The intersection is: " , set1 & set2)
print('\n')
set  = A.union(B)
print(set)
common = A & B                            ## & is used for intersection
print("A intersection B is: " , common)
print(A.intersection(B)) #or
print("Only set1 is: ", set1 - set2)      #difference.. or you can also write set1.difference(set2)
print()                                   #symmetric difference pani cha
'''
#although tuples are immutable LIST inside a tuple can be changed
'''
tupe1 = (1,2,3,'shas', ['abc','shaswot']) 
tupe1[4][0] = 'muskaan'
print(tupe1)
'''
# packed and unpacked tuples
'''
fruits = ('apple','banana','grape')
f1,f2,f3 = fruits
print(f1)
print(f2)
print(f3)
'''
#LIST SLICING
'''
list1 = [1,2,3,4,5,6,7,8,9]
print(list1[::-1])           #### [::-1]PRINTS ALL THE ELEMENTS IN LIST IN REVERSE
'''
'''
s = {}
print(s)
print(type(s))    
'''
'''
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])
'''
'''
cubes = []
for i in range(0,5):
    cubes.append(i**3)
print(cubes)
'''
'''
even = [i**2 for i in range(10) if i**2 % 2==0]
print(even)
'''
'''
a = 100
def a_random_func():
    z = a + 20
    print(z)
def another_func():
    print ("the first variable is ", a)
a_random_func()
another_func()
'''
# String Formatting
'''
nums = [4,5,6]
msg = "Numbers: {0},{1},{2}".format(nums[0],nums[1],nums[2])
print(msg)
'''
'''
print("{0}{1}{0}".format("abra", "cad"))
'''
'''
a = "{x},{y}".format(x=5,y=6)
print(a)
'''
'''
from random import randint
greetings = ["Hello","Howdy","You smell funny"]
title = ["Human.", "Trump!" , "Maid."]
greeting = "{x}, {y}".format(x=greetings[randint(0,2)], y=title[randint(0,2)])
print(greeting)
'''
'''
s = "{c},{b},{a}".format(a=5,b=9,c=7)
print(s)
'''
################
################# SINCE LOC is alot, will be continued in Sololearn2.py ###################

# JUST a Random Turtle Try for first time
'''
import turtle
painter = turtle.Turtle()
painter.pencolor("red")
for i in range(50):
    painter.forward(50)
    painter.left(123)          ##lets go couterclock wise this time
painter.pencolor("blue")
for i in range(50):
    painter.forward(100)
    painter.left(123)
painter.pencolor("green")
for i in range(50):
    painter.backward(50)
    painter.forward(100)
    painter.left(50)
    painter.right(30)
    painter.forward(50)
    painter.right(55)
    painter.left(100)
'''
'''
import turtle
a = turtle.Turtle()
for i in range(10):

    a.forward(100)
    a.left(90)
    a.forward(150)
    a.left(90)
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.left(45)
    a.forward(100)
    a.dot(90)
    a.pencolor('red')
    a.dot(10)
    a.forward(90)
    a.right(90)
    a.backward(150)
    a.left(90)
    a.forward(5)
    a.left(90)
    a.stamp()
'''
