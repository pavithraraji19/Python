for num in range(1042000,702648265):
    order=len(str(num))
    sum=0
    temp=num
    while temp > 0:
         digit=temp%10
         sum+=digit**order
         temp//=10
         if num== sum:
             print ("The first armstrong no is ",num)
         break
        
