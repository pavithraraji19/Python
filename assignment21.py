start=int(input("Enter the starting no:"))
end=int(input("Enter the ending no:"))
for num in range(start,end+1):
    if num>1:
        for  i in range(2,num):
            if(num%i) == 0:
                break
        else:
             print("the prime no is",num)
