num=int(input("Enter the  num"))
first=0
second=1
print(first)
print(second)
fibo=first+second
for i in range(2,num):  
    third=first+second
    first=second
    second=third
    print(third)
