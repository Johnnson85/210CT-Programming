def sq(s):
  
  x=int(0)
  if s>0:
    while x*x < s:
      x=int( x+1)
    if x * x != s:  
        print (s, "is not a perfect square")
        s=(s-1)
        sq(s)
    else:
      print (s, "is a highest perfect square cause :", x, "*", x, "=",s)
      return x
  else:
    print ("not a good input, sorry")
    return None
  	
sq(189)  
