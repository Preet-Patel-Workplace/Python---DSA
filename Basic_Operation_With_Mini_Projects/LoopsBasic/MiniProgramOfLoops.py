#Printing the odd numbers to the stoping number 

for i in range(0,int(input("Enter the stoping number : ")), 2):
    print(i)


#using Counter

count = 0 

for i in range(int(input("Enter the start number: ")), int(input("Enter the stop number :"))):
    count += 1

print("Total  count is " , count)

#WAP to find the sum of first natural number

SN = int(input("Enter the number till sum is required : "))

sum = 0
for i in range(SN):
    sum += i


#WAP to find a factorial of n 

i = int(input("Enter the number of factorila is required : "))

fac = 1
j = 0
while j <= i :
    fac *= j

print("Here is the factorial : " ,j)
