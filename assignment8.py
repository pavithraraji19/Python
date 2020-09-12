#PROGRAM1

def  decorators_function(input_function):
    def fibo():
           print ("hey this is a program in which we gonna find fibonnacci series with decorators")
           input_function()
           nterms=int(input("enter the ending limit"))
           n1,n2=0,1
           count=0
           if nterms<=0:
               print("Please enter a psitive integer")
           elif nterms==1:
               print("fibonnacci series upto ",nterms,":")
               print(n1)
           else:
               print("Fibonnaci sequence")
               while count<nterms:
                   print(n1)
                   nth=n1+n2
                   n1=n2
                   n2=nth
                   count+=1
    return fibo
def hello():
    print("hi,this s hello func")


modified_hello=decorators_function(hello)
modified_hello()



#PROGRAM 2

#file =open("text.txt","r")
#file.write("hi")
#file.close()

try:
    file=open("text.txt","r")
    file.write("hi")
    file.close()
#except Exception as e:
  #  print(e)
except :
    print("sorry ,it is a read file so you cannot be able to write in the file)

    
