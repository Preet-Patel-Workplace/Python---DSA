# In this code will take Two number as a input from user then provide some option of operations between  numbers 
# and using conditional statement working on it

print("Hello")
Name = input("Enter your Name : ")
num1 = int(input("Enter the First number : " )) 
num2 = int(input("Enter the Second number : " ))

print("\n")

Choice1 = int((input("If you want to make changes in you Name, Enter 1 \nOr you want to perform any operation on numbers, Enter 2 :")))

print("\n")
if(Choice1 == 1) :
    Choice2 = int(input("For Changes in Name following are options : \n 1.Add Another Word 2.Capitalize First Letter 3. Replace any Character or Word \nEnter Here your choice(Between 1 to 3) : "))
    print("\n")
    if(Choice2 ==  1 ) :
        Name = Name + " " + input("Enter the New Word to Add : ")
        print(" \nName Changed! \n")
        print(Name)
    elif(Choice2 == 2) :
        Name = Name.capitalize()
        print("\nName Changed! \n")
        print(Name)
    elif(Choice2 == 3):
        Name = Name.replace(input("Enter the Word/Character To Be changed : ") , input("Enter the new word/Character :"))
        print("\nName Changed! \n")
        print(Name)
    else :
        print("\n")
        print("Wrong Choice")
elif(Choice1 ==  2):
    Choices3  = int(input("You can select from following for operation : \n1.Add 2.Subtract 3.Product 4.Check for any them is multiple of other number \nYou Can enter here(From 1 to 4) :  "))
    print("\n")
    if(Choices3 == 1 ) :
        print(num1 + num2)
    elif(Choices3 ==  2 ) : 
        print(num1 - num2)
    elif(Choices3 == 3):
        print(num1 * num2)
    elif(Choices3 == 4):
        if(num1 % num2 == 0) : 
            print("Number 1 is the multiple of Number 2 ")
        elif(num2 % num1 == 0) :
            print("Number 2 is the multiple of Number 1 ")
        else :
            print("No one id multiple of each other") 
    else :
        print("wrong Chocie") 
else :
    print("Wrong Choices !")
