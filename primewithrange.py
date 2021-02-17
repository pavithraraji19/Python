start=int(input("Enter thr start range"))
end=int(input("Enter the end range"))
for num in range(start,end+1):
    flag=0
    for i in range(2,num):
        if (num%i)==0:
            flag=1
            break
    if (flag==0):
        print(num)
        
    
            