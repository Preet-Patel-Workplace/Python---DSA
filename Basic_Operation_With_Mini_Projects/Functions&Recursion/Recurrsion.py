## Recurrsion means function calls itself 

# def show(n):
#     print(n)
#     if(n != 0):
#         show(n-1)
    

# show(5) # 5 4 3 2 1

## Factorial 
def factorial(n):
    if(n == 0 or n ==1):
        return 1
    elif(n > 1):
        return n * factorial(n - 1)
    else :
        print("Wrong number")


print(factorial(5))
