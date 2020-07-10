# Example: Data Abstraction:
# def calculation():
#    print("*************************CACULATOR*************************")
#    x = int(input("Enter First Value: "))
#    y = int(input("Enter Second Value: "))

#    print(
#        " Press 1 for Addition (+)\n Press 2 for Subtraction (-) \n Press 3 for Multiplication (*)\n Press 4 for Divission (/)")

#    option = int(input("==> "))

#    def add():
#       result = x + y
#        print(result)

#    def sub():
#        result = x - y
#        print(result)

#    def mul():
#        result = x * y
#        print(result)

#    def div():
#        result = x / y
#        print(result)

#    if option == 1:
#        add()
#    elif option == 2:
#        sub()
#    elif option == 3:
#        mul()
#    elif option == 4:
#        div()


# calculation()

# Example: Data Encapsulation:
"""
class Computer:
    def __init__(self):
        self.__maxspeed = 150       # Private attribute (because of 2 underscore)

    def sell(self):
        print("Maximum Speed : {}".format(self.__maxspeed))

    def setMaxSpeed(self, price):       # Setter Function
        self.__maxspeed = price


s = Computer()
s.sell()
# Changing speed:
s.__maxspeed = 200            # Since LOC 44 is private attribute, wont be updated.. Needs Setter Funtion
s.sell()

s.setMaxSpeed(250)
s.sell()
"""

# Example: Data Inheritance:
"""
class Employee:                                          # MAIN CLASS
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):                               # SUB CLASS
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):                                  # SUBCLASS

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()
"""

# Example: Polymorphism in Class:

"""
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
"""

