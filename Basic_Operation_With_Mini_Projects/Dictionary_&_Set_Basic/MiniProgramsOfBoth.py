##Q1  Store following word meanings in a python dictionary:
#     table: "a piece of furniture", "list of facts figures"
#     cat : "A small animal"


Dict = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "A small animal"
}


##Q2 WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

marks.update({"Phy" : int((input("Enter Phy : ")))})
marks.update({"Phy" : int((input("Enter Chem : ")))})
marks.update({"Phy" : int((input("Enter Maths : ")))})

print(marks)

## Q3 Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)

#Solution 1
values = { 9, "9.0" }

#solution 2
values2 ={ 
    ("float" , 9)
    ("Int" , 9.0)
}