## Dictionary Basic 
#"Key" : "Value",

##Unordered
#Mutable 
#Dont Allow duplicate keys

info = {
    "name" : "Preet Patel",
    "Age" : 16,
    "Marks" : [80, 90 , 75], 
    "Lang" : ("Java" , "C" , "Python"),
}

print(type(info))

print(info)

print(info["Age"])

info["Age"] = 19

print(info["Age"])

info["CanDrive"] = True

print(info)

Null_Dict = {}

print(Null_Dict)

## Nested Dictionary 

student = {
    "name" : "Preet Patel",

    "Subject" : {
        "phy" : 82,
        "chem" : 70,
        "math" : 80
    }
}

print(student["Subject"])
print(student["Subject"]["phy"])


# Dictionary Methods

print(student.keys())

#printing like list 

print(list(student.keys()))

#
print(student.values())

print(student.items())



 