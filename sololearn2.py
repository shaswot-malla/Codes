#Continue after linkedin course.py

#Functional PROGRAMMING
'''
def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 20))
'''
#PureFunction
'''
def pure_func(x,y):
   temp = x + 2*y
   return temp / (2*x + y)
print(pure_func(10,5))                  #20/25
'''
'''
def g(x, week_day):
   if week_day=="Tuesday":
       return x+1
   else:
       return x
print(g(2,"Tuesday"))
'''

'''
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
'''

'''
def softwarica():
   print('My College ')

softwarica()
'''
'''
import sys
sys.setrecursionlimit(5)
print(sys.getrecursionlimit())
'''
'''
name = 'shaswot'
print(id(name))
'''