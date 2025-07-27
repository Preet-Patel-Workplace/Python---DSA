## Abstarction

#Hiding the implementation details of a class and only showing the essential features to user 

## Encapsulation
# Wrapping data and functions into a single unit (object)


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def Start(self):
        self.acc = True
        self.clutch = True
        print("Car Started")

car1 = Car()
car1.Start()