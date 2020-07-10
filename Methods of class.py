# Methods in class:

# (A) Instance Method:

# "syntax"
#    def method_name(self):          #Instance Method without parameters
#        function body
#    def method_name(self,f1,f2):    #Instance Methos with parameters/Formal Arguments
#        function body

# Instance Method without Parameters:

# class Mobile:
#   def show_model(self):           #Instance Method
#       print('Nokia')
# nokia = Mobile()
# nokia.show_model()                    #cAlling


# Example:
# class Mobile:
#    def __init__(self):
#        self.model = 'Nokia'        #Instance Variable
#    def show_model(self):           #Instance Method
#        print(self.model)           #Accessing Instance variable inside Instance Method
# nokia = Mobile()
# Calling Instance Method without Argument:
# nokia.show_model()                 #object_name.method_name()

# Example: Instance Method with Parameter:

# class Mobile:
#    def __init__(self):            #Constructor Method
#        self.model = 'Nokia'       #Instance Variable
#    
#    def show_model(self,p):        # Instance method with parameters
#        self.price = p             # self.price == Instance Variable && p == parameter "Formal Argument"
#        print(self.model,self.price)
# nokia = Mobile()
# Calling
# nokia.show_model(1000)         # Call Method with Argument == syntax: object_name.method_name(Actual_Argument)

# 2 objects "nokia && samsung"
# nokia = Mobile()
# samsung = Mobile()
# nokia.show_model(1000)
# samsung.show_model(2000)

# Example: Instance Method without Parameter:
# class Coventry:
# Instance Method
#    def college_name(self):
#        print('My college name is Softwarica')
# softwarica = Coventry()
# softwarica.college_name()

# (B) Class Method

# Class Method without parameters

# class Mobile:
#    @classmethod  # Decorator
#    def show_model(cls):  # Class Method
#        print('Nokia SR')


# nokia = Mobile()
# nokia.show_model()


# Example 1: Class Method without parameter
# class Mobile:
#    fp = 'Yes'
#    @classmethod
#    def show_model(cls):
#        print("Fingerprint:",cls.fp)
# nokia = Mobile()
# Mobile.show_model()

# Example 2: Class Method with parameter
# class Mobile:
#    fp = 'Yes'
#    pr = 20000
#
#   @classmethod
#    def show_model(cls, r):
#        cls.ram = r
#        print("Fingerprint:", cls.fp)
#        print("RAM:", cls.ram)

#    @classmethod
#    def show_price(cls, pr):
#        cls.price = pr
#        print("Price is: ", cls.pr)


# nokia = Mobile()
# Mobile.show_model("32 GB")
# Mobile.show_price(20000)


# Static method with parameters

"""
class Nepal:
    @staticmethod
    def kathmandu(k, t, m):
        ward_number_one = k
        ward_number_two = t
        ward_number_three = m
        print(ward_number_one, ward_number_two, ward_number_three)


country = Nepal()
Nepal.kathmandu(1, 2, 3)
"""

"""
class Vehicle:
    @staticmethod
    def auto_mobile(a, b, c, p_1, p_2, p_3):
        type1 = a
        type2 = b
        type3 = c
        price_a = p_1
        price_b = p_2
        price_c = p_3
        print(" The Price of", type1 + " is", p_1)
        print(" The price of", type2 + " is", p_2)
        print(" The price of", type3 + " is", p_3)


cars = Vehicle()
Vehicle.auto_mobile("BMW", "AUDI", "MerCEDEZ", 200, 600, 800)
"""





