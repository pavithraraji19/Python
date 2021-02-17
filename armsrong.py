num=int(input("Enter the number"))
copy=num
result=0
while copy>0:
    remainder=copy%10
    result+=remainder**3
    copy//=10
if num==result:
    print("The entered number is armstong",num)
else:
    print("The entered number is not a armstrong",num)
