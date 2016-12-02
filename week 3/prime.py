def prime(p):
    
    if p > 1:
        for i in range (2,p):
            if (p%i)==0:
                print(p, "is not a prime number")
                return p
            else:
                print(p, "is a prime number")
                return p
    else:
        print(p, "is not a prime number")
prime(16)
