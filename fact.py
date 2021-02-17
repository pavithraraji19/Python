num=int(input("Enter the num "))
fact=1
if num==0:
    print("Enter number more than 2")
elif num==1:
    print("The factorial of one is one")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial of the number",fact)