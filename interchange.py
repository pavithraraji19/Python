list1=['a','p','p','l','e']
print (list1)
#length=len(list1)
#print(length)
#temp=list1[1]
#list1[1]=list1[-1]
#list1[-1]=temp
#print(list1)
new1=list1.pop(1)
new2=list1.pop(-1)
list1.insert(1,new2)
list1.insert(-1,new1)
print(list1)
#list1[0],list1[-1]=list1[-1],list1[0]
#print(list1)
