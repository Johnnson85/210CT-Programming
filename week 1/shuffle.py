import random

def randomList(a):
    
    b=[]
    for i in range(len(a)):
        element=random.choice(a)
        a.remove(element)
        b.append(element)
        if len(a)==0:
            print(b)
a=[1,2,3,4,5,6,7,8,9]
randomList(a)
