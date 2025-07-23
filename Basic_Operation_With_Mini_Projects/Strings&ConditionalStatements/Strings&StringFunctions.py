#Strings with Basic Operations 
str1 = "Hello"
str2 = "World"

#Concatenation
FinalStr = str1 + " " + str2
print(FinalStr)

#Length of strs
print(len(str1))
print(len(str2))
print(len(FinalStr))

#indexing 
print(str1[0], " " , str1[1], " " , str1[2], " " , str1[3], " ", str1[4] )

#Slicing 
print(FinalStr[0:4])
print(FinalStr[0:])
print(FinalStr[:8])

#Slicing with negative index
print(FinalStr[-8:-1])

## String Functions

str = "i am Preet Patel"

#EndsWith()
print(str.endswith("el"))

#Capitalize()
print(str.capitalize())
#saving 
str  = str.capitalize()

#Replace()
print(str.replace("Preet" , "Prit"))

#Find()
print(str.find("Preet")) #returns 6
print(str.find("Q")) #returns -1

#Count()
print(str.count("e")) # returns 3



