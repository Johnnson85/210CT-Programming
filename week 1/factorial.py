def zeros_in_factorial(x):

    if x < 5:
        return 0

    count = 0
    i = 5
    while x//i >= 1:
        count += x // i
        i *= 5
    return count
print("the number of zero's is:",zeros_in_factorial(5))


        


