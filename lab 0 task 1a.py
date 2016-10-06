#lab0
class NumberOne:
  def __init__(self):
    a=float(5.3)
    b=float(7.6)
    c=float(10.1)
    d=float(2.6)
    
    NumberOne.SolutionOne(self,a,b,c,d)
  def SolutionOne(self,a,b,c,d):
    
    one=(a/b)
    two=(c/d)
    if one>two:
      print(round(one,3))
    else:
      print(round(two,3))

NumberOne()
