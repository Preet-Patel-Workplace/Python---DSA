# Taking Inputs of Basic Personal Information

Name  = input("Enter your name:  " )
Age = input("Enter your age: ")
Mobile = input("Enter your mobile number : ")
Email = input("Enter your Email : ")

print("\n Your Entered Details ")
print(type(Name) , Name)
print(type(Age), Age)
print(type(Mobile), Mobile)
print(type(Email) , Email)


#Now Taking Inputs With Specified Datatype 
print("\n Inputs With Typecasting With Specified Datatype")
Name  = input("\n Enter your name:  " )
Age = int(input("Enter your age: "))
Mobile = int(input("Enter your mobile number : "))
Email = input("Enter your Email : ")

print(type(Name) , Name)
print(type(Age), Age)
print(type(Mobile), Mobile)
print(type(Email) , Email)