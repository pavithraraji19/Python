num=int(input("Enter the number"))
if num<=0:
    print("Enter number more than one")
elif num==1:
    print("Sorry! one is neither a prime nor a composite")
else:
    if num>2:
        for i in range(1,num):
            if (num%i==0):
                print("Is  not a prime",num)
                break 
            else:
                print("Is a prime",num)