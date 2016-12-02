def binarySearch(L, item, low, high):
    first = 0
    last = len(L)-1
    found=False
    while first<=last and not found:
        midpoint = (first + last)//2
        if L[midpoint] == item:
            found = True
            if True and item in range (low,high):
                print("yes it is on a list and is in an interval")
                return found
            else:
                print("on a list, but not in an interval")
                return found
                
        else:
            if item < L[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return ("not on a list")

L = [2,3,5,7,9,13]
low=10
high=14
print(binarySearch(L,13,low, high))
