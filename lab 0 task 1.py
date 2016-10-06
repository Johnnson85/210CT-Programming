#Lab 0
#task 1

class NumberOne:
    def __init__(self):
        
        a=input("enter float number for a: ")
        b=input("enter float number for b: ")
        c=input("enter float number for c: ")
        d=input("enter float number for d: ")

        a=float(a)
        b=float(b)
        c=float(c)
        d=float(d)

        NumberOne.SolutionOne(self,a,b,c,d)

    def SolutionOne(self,a,b,c,d):
        first=(a/b)
        second=(c/d)

        if first>second:
            print(round(first,3))
        else:
            print(round(second,3))
        
NumberOne()

        





