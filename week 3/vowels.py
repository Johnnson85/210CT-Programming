def remvow(string):
    vowels=["a","e","i","o","u"]
    new=""
    for c in string:
        if c not in vowels:
            new+=c
            
    
    print(new)
    
remvow("beautiful")
