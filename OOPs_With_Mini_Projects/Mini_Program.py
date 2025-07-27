#Create Account class with attributes -  balance and account no.
# Create methods fr debit, credit & printing the balance 

class Account:
    balance = 0
    accountNo = 0
    def __init__(self, balance, accoutNo):
        self.balance = balance
        self.accountNo = accoutNo

        

    def Debit(self , amount):
        if self.balance == 0 :
            print("Sorry, Your balance is 0\nyou cannot debit any amount now!")
        else :
            self.balance = self.balance - amount
            print("Amount debited Successfully!")
            print("New Balance : " , self.balance)

    def Credit(self,amount):
        self.balance = self.balance + amount
        print("Amount credited Successfully!")
        print("New Balance : " , self.balance)

    def get_Balance(self):
        print("Your Current balance is :" , self.balance)


print("Hello, ")

c1 = Account(int(input("Enter the Intial Balance : ")), int(input("Enter the Accout number : ")))

choices = int(input("Menu \n1. Debit\n2. Credit\n3. View Balance \n"))

while choices > 0 and choices <= 3:
    if choices ==  1:
        c1.Debit(int(input("Enter the amount : ")))
    elif choices == 2:
        c1.Credit(int(input("Enter the amount : ")))
    elif choices ==3 :
        c1.get_Balance()
    
    choices = int(input("Menu \n1. Debit\n2. Credit\n3. View Balance \n4. Exit \n"))
else :
    print("Wrong Choice")


print("Thanks!!!")
    