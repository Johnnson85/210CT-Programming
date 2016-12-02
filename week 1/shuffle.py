import random

def randomList(a):
    a=[1,2,3,4,5,6,7,8,9]
    b=[]
    for i in range(len(a)):
        element=random.choice(a)
        a.remove(element)
        b.append(element)
        return(b)

randomList(a)
