'''
class Student:
    """ THIS IS JUST AN EXAMPLE"""
    name = "ram"
    identy = 101
    address = "ktm"
    def __init__(self,name,identy,address):
        self.name = name
        self.identy = identy
        self.address = address
        print('NEXT')
    def Student_Data(self):
        print('NAME: ', self.name)
        print('IDENTY: ',  self.identy)
        print('LOCATION: ', self.address)

object1 = Student('shyam', 202, 'pokhara')        # Creating an object named 'okect1' in the class Student
object1.Student_Data()

object2 = Student('hari', 303, 'golfutar')
object2.Student_Data()

object3 = Student('shaswot', 777, 'dhapasi')
object3.Student_Data()

print(Student.__doc__)    # Printing the doc string

print(Student.name)        # PRinting the default data... LOC 3 and 4
print(Student.identy)
'''

'''
class Nepal:
    def ktm_city(self):
        print('ktm==valley')

capital = Nepal()
capital.ktm_city()
'''
'''
class Celebs:
    def __init__(self, n, j):
        self.name = n
        self.job = j

    def work(self):
        if self.job == "wrestling":
            print(self.name, "works as a wrestler")
        elif self.job == "Movies":
            print(self.name, "is a fabulous actor")

    def speak(self):
        print(self.name + " says, how are you??")


human = Celebs("Kevin Hart", "Movies")
human.work()
human.speak()
'''

'''
#Class Method 
class Nepal:
    @classmethod
    def ktm(cls):
        print("ktm is a valley")


capital = Nepal()
Nepal.ktm()
'''


'''
class Cars:
    m1 = "Ford"
    m2 = "Audi"
    p1 = 50000
    p2 = 60000

    @classmethod
    def car_model(cls, M):
        cls.type = M
        print("The 1st model is: ", cls.m1)
        print("The another model is:", cls.m2)

    @classmethod
    def car_price(cls, P):
        cls.price = P
        print("The price of Ford is:", cls.p1)
        print("The price of Audi is:", cls.p2)


automobile = Cars()
Cars.car_model("m1, m2")
Cars.car_price("p1,p2")
'''

# lst = []
# for i in range(3):
#     name = input("enter student name: ")
#     lst.append(name)
#
# for i in lst:
#     print(i)



