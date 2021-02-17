list1=[4,8,2,6,76,45,222,1,90]
print(list1)
#list1.sort()
#print(list1)
#print("The smallest element in the list is",list1[0])
#print("The largest element in the list is",list1[-1])
min_list1=list1[0]
max_list1=list1[0]
for i in range (1,len(list1)):
    if list1[i]<min_list1:
        min_list1=list1[i]
    if list1[i]>max_list1:
        max_list1=list1[i]
print("The min number is",min_list1)
print("The max number is",max_list1)