from array import *
arr=[101,20,30,40,33,42,123,45]
print(arr)
max=arr[0]
n=len(arr)
for i in range(0,n):
    if arr[i]>max:
        max=arr[i]
print("The largest number is",(max))