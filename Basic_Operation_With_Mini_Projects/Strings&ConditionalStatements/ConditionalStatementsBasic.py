#Conditonal Statements Basic 

#if(Conditon):
#   Statement1
#elif(Condition):
#   Statement2
#else :
#   StatementN

light = "Red"

if(light == "Red"):
    print("Stop")
elif(light == "Green"):
    print("Go")
else:
    print("Error")

#If statement always Check but elif statement checks when if statement is false

## NESTING

num = 34 

if(num >= 0):
    if(num == 0):
        print("Number is zero")
    else :
        print(num)
else :
    print("Number is negative ")

