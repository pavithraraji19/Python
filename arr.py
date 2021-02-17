from array import*
arr=array('i',[])
n=int(input("Enter the len"))
for i in range(n):
    x=int(input("Enter the value"))
    arr.append(x)
print(arr)
search=int(input("Enter the search val"))
count=0
for e in arr:
    if e==search:
        print (count)
        break
    count=count+1
        