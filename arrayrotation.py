from array import *
arr=array('i',[])
k=int(input("Enter the len of array"))
for i in range(k):
    i=int(input("Enter the val"))
    arr.append(i)
n=int(input("Enter the rotation value"))
print("Orginal array is",arr)
for i in range(0,n):
    temp=arr[0]
    for j in range(0,len(arr)-1):
        arr[j]=arr[j+1]
    arr[len(arr)-1]=temp
print(arr)
#similar to array reversal