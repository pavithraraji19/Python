list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
total=[]
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        total.append(list1[i]+list2[i])
print(total)
