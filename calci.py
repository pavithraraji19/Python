print("Welcome to simple calculator")
n=int(input("Enter the option you wanna do /n1.ADDITION /n2.SUBTRACTION /n3.Multiplication /n4.DIVISION /n5.EXPONIENTIATION"))

a=int(input("Enter the first value"))
b=int(input("ENter the second value"))
if (n==1):
    result_add=a+b
    print("The result is ",result_add)
elif (n==2):
    result_sub=a-b
    print("The result is",result_sub)
elif (n==3):
    result_mul=a*b
    print("The result is",result_mul)
elif (n==4):
    result_div=a/b
    print("The result is",result_div)
elif (n==5):
    result_expo=a**b
    print("The result is",result_expo)
else:
    print("Please enter valid option")
