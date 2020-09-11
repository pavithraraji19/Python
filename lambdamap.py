#PROGRAM1

listy1=['1','5','6','4','1','2','3','5']
listy2=['1','1','5']
result=set(x in listy1 for x in listy2)
flag=0
for ans in result:
    if ans== False:
        flag=1
if flag==0:
    print("Its a match")
else:
    print("Its gone")



#PROGRAM2
def primeno(i):
    for j in range(2,i):
        if (i%j)==0:
           break
        else:
            return i
primeNo=filter(primeno,range(1,2501))
print(list(primeNo))


#PROGRAM3
lst=["Hey  this is Pavithra from Chennai"]
print(lst)
newlst=list(map(lambda words:" ".join([word.capitalize() for word in words.split()]),lst))
print(newlst)
