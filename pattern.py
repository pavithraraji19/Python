lines=int(input("Enter the lines"))
for i in range(lines,0,-1):
    for j in range(0,i):
        print("%",end=" ")
    print("\r")
for i in range(1,lines):
    for j in range(0,i+1):
        print("%",end=" ")
    print("\r")
