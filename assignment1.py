# LIST : List is a collection of data in which it is of different data types
lst=["letsupgrade",'python',100,10.5]
print (lst)
#List operations are as follow in list we can add element,del element,find index ,find elemet,copy,sort
#to add a substring
#to add a string using extend which is as a character
lst.append([12,9,8])
print(lst)
lst.extend("hope")
print(lst)
#to  get an element and to get an element from the substring
print(lst[2])
print(lst[4][2])
#to get the index of the element
print(lst.index("python"))
#to delete an element the list
del lst[2]
print(lst)
#to pop an element
print(lst.pop())
print(lst.pop(6))
#to print the substring using concantenation
print(lst[1 : 4])
# to count
mlist=["assignment",100,"holiday",100]
print(mlist.count(100))
print(lst+mlist)


#DICTIONARY:Dictionary used to have key value and value and it is mutable and iwe used{ key : value} to describe the dictionary
dict ={"name" : "aaa","age":10,"location" : "chicago","phoneno":909999}
print(dict)
# used to print key and value
print (dict.keys())
print(dict.values())
print(dict.pop("location"))
print(dict.items())
print('NAME : ',dict.get("name"))


#TUPLE:Tuple is similar to list but have limited functions  which is count and indexand most importantly it is immutable
tple=("letsupgrade","python",100,10.5,100)
print(tple)
#to print the index of the element
print(tple.index("python"))
#to print the number of times the element present we use count
print(tple.count(100))


#STRING:String is a sequence of characters in which we can perform operations
str="Letupgrade is awesome and  it is very cool"
print(str)
str2='python'
#to perform concantenation
print(str+str2)
#to find using index
print(str[0])
#to perform capitalization
print(str.capitalize())
#to convert into uppercase
print(str.upper())
#to find how many time the word repeated
print(str.count("is"))
#to find whether the given word ends with given letter which returns boolen value
print(str2.endswith("n"))
#to perform casefold which is to make every element in the same case as all the letter 
print(str.casefold())
#to find where the word is present
print(str.find("p"))


#SETS:sets are unorderd collection of items most importantly every elemnt should be unique and it is also immutable
st={"hello",100,"letsugrade",200,"krish"}
print(st)
#to add an element ,update the set
st.add(109.33)
print(st)
st.update([5,99])
print(st)
#to remove an element and to pop the element
st.remove(5)
print(st)
print(st.pop())
set1={1,2,3,4,5}
set2={6,7,8,9,1,2,3}
#to perform set union
print(set1|set2)
#to perform set intersection
print(set1&set2)
#to perform set differnce
print(set1-set2)

