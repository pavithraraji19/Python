list1=['m','a','l','a','y','a','l','a','m']
print(list1)
list2=list.copy(list1)
list2.reverse()
print(list2)
if (list1==list2):
    print("Is a palindrome")
else:
    print("Is not a palindrome")