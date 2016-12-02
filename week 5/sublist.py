def sublist(L):
    New=[]
    new=[]
    
    for i in range (len(L)):
        if i <len(L)-1 and L[i]<=L[i+1]:
            new.append(L[i])
        
        else:
            new.append(L[i])


            if len(new)>len(New):
                New=new
            new=[] #reset new
    print("The longest sub-sequence is: ", New)



L=[1,2,3,4,1,5,1,6,7]
print (sublist(L))
