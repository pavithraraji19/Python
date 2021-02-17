#list1=[1,2,3,-1,4,-5]
start=-3
end=11
pos_count=0
neg_count=0
for i in range(start,end+1):
    if i>0:
        pos_count=pos_count+1
        print("The number is positve",i)
    else:
        print("The number is negative",i)
        neg_count=neg_count+1
print("Negative count=",neg_count)
print("Positive count=",pos_count)