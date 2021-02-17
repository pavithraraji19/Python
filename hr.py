#for i in range(ord('F'),ord('P')):
    #q=chr(a)
    #print(q)
#n=input(int())
#x,y,a,b=input().split()
#x,y,a,b=int (x) ,int (y) ,int (a) , int (b)
#for i in range(4):
#if x*y==a+b:
#	print ("yes")
#else:
#	print("no")
for i in range(int(input())):

    x,y,a,b = map(int,input().split())

    if(x*y == a+b):

        print("Yes")

    else:

        print("No")