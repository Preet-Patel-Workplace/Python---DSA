# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n == 0):
        return 0
    else :
         return n + sum(n - 1 )


print(sum(5))










# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.

cities = ["Vadodara" , "Anand" , "Surat", "Delhi", "Amhedavad", "Rajkot", "ABC"]

def List_Print(list,n):
    print(cities[n])
    if (n == len(cities)-1):
        return
    List_Print(cities,n + 1)

List_Print(cities,0)