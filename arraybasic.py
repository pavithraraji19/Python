from array import *
vals=array('i',[20,30,40,50])
#print(vals.buffer_info())
#new_array=array(vals.typecode, (a for a in vals))
#for e in new_array:
    #print(e)
#for e in vals:
    #print(e)
i=0
while(i<len(vals)):
    print(vals[i])
    i+=1