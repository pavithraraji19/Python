#PROGRAM 1
class BankAccount:
    def __init__(self):
        self.Name="R.Pavithra"
        self.balance=0
        print("YOUR ACCOUNT IS CREATED")
    def deposit(self):
        amount=int(input("\n  Enter amount to be  deposit:"))
        self.balance+=amount
        print("\n Amount deposit is=%d"%self.balance)  
    def withdrawl(self):
        amount=int(input("\n  Enter amount to be withdrawl:"))
        if amount>self.balance:
            print("INSUFFICIENT BALANCE")
        else:
            self.balance-=amount
            print("\n YOUrR REMAINING BALANCE IS%d"%self.balance)
    def enquiry(self):
        print("Your balance =%d"%self.balance)
    
print("\n           WELCOME TO THE BANK         ")
account=BankAccount()
account.deposit()
account.withdrawl()
account.enquiry()

#PROGRAM2
import math
pi=math.pi
class cone:
    def __init__(self,r,h):
        self.r=r
        self.h=h
    def  volume(self):
        result=(1/3)*pi*self.r*self.h
        print("\n volume of cone is" ,result)
    def surfacearea(self):
        result=pi*self.r*self.h+ pi * self.r*self.r
        print("\nsurface area is",result)
ra=float(input("enter the radius"))
he=float(input("enter the height"))
c=cone(ra, he)
c.volume()
c.surfacearea()


