# #Q1 WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

list = []

list.append(input("Enter First Favorite Movie Name  : "))
list.append(input("Enter Second Favorite Movie Name  : "))
list.append(input("Enter Third Favorite Movie Name  : "))

print(list)

#Q2 WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
list1 = [1, 2, 3, 2, 1]
list2 = [1, "abc", "abc", 1]

list1_Reverse = list1.copy()
list2_Reverse = list2.copy()

list1_Reverse.reverse()
list2_Reverse.reverse()

if(list1 == list1_Reverse and list2 == list2_Reverse) :
    print("Both List contains palindrome of elements")
elif(list1_Reverse == list1) :
    print("First list contains palindrome of elements")
elif(list2 == list2_Reverse) :
    print("List 2 contains palindrome of elements")
else:
    print("No list contains palindrome of elements")

#Q3 WAP to count the number of students with the "A" grade in the following tuple.
grades = ("C", "D", "A", "A", "B", "B", "A")

print(grades.count("A"))



#Q4 Store the above values in a list & sort them from "A" to "D".
grades = ["C", "D", "A", "A", "B", "B", "A"]

grades.sort()
print(grades)
