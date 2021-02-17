list1=["go","run","for","what","you","need","run","go"]
print("list before ",list1)
n=int(input("Enter the occurence"))
word=input("Enter the word")
count=0
for i in range(0,len(list1)):
    if (list1[i]==word):
        count=count+1
        if (count==n):
            del list1[i]
print("New list will be",list1)