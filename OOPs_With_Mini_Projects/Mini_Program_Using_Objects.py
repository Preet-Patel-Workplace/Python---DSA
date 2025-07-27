#Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average

class Student:

    def __init__(self, name, mark1, mark2, mark3):
        
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3


    def Average(self):
        return int((self.mark1 + self.mark2 + self.mark3)/3)



s1 = Student(input("Enter the name of student : "),int(input("Enter the marks of 1st Subject : ")),int(input("Enter the marks of 2nd Subject : ")),int(input("Enter the marks of 3rd Subject : ")) )
s2 = Student(input("Enter the name of student : "),int(input("Enter the marks of 1st Subject : ")),int(input("Enter the marks of 2nd Subject : ")),int(input("Enter the marks of 3rd Subject : ")) )
s3 = Student(input("Enter the name of student : "),int(input("Enter the marks of 1st Subject : ")),int(input("Enter the marks of 2nd Subject : ")),int(input("Enter the marks of 3rd Subject : ")) )

print("Average Of marks of " , s1.name , " : " , s1.Average())
print("Average Of marks of " , s2.name , " : " , s2.Average())
print("Average Of marks of " , s3.name , " : " , s3.Average())