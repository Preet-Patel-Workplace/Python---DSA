#Delcaring all the basic variables 
#And printing afterwards along with the type of variable


Age = 25
name = "Preet"
Address = " 38-99 hobinson street"
GPA = 92.33
Student = True


print(type(Age), "Age = " , Age) 
print(type(name) ,  "Name = " , name)
print(type(Address) , "Address = " , Address)
print(type(GPA) , "GPA  = " , GPA)
print(type(Student) , "Student = " , Student )



# Arithmetic Operators
#(+,-,*,/,%,**)
a = 5 
b = 4 
c = 10  

print( "Sum + ", a + b + c)
print("Subtract = ",a - b -  c)
print("Product =  ",a * b * c)
print("Division = ",( a / b ) / c)
#Making and Equation with mix match
print((a % b) * 100)


# Relational Comparision Operators 
print(a == b == c)
print(a != b != c)
print(a >= b)
print (a <= b)

# Assignment Operators
a += 5
b *= 10
c /= 5

# Logical Operators
print(not False)
print(not (a > b))

val1  = True
val2 = True

print("AND Operator: " , val1 and val2)

print("OR Operator: ", (a == b) or (b > c))


