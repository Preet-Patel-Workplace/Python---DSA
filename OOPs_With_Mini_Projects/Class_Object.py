## Class And Object

class car:
    color = "blue"

car1 = car()
print(car1.color)

car2 = car()
print(car2.color)


# __init__ Function

class Student:
    
    def __init__(self, name):
        self.name = name 

s1 = Student("karan")
s2 = Student("Preet")
print(s1.name)  
print(s2.name)

# Methods

class Student:
    
    def __init__(self, name):
        self.name = name 
    
    def Hello(self):
        print("Hello " , self.name)
    
    def get_name(self):
        return self.name


s1 = Student("Karan")
s1.Hello()
print(s1.get_name())

# Static Method 

class student:
    @staticmethod #decorator 
    def hello():
        print ("hello")