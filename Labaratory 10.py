a=10
b=100
c=100

if a > b and a > c:
    print(str(a) + " is greater than " + str(b) + " and " + str(c))
    
elif b > a and b > c:
    print(str(b) + " is greater than " + str(a) + " and " + str(c))
    
elif c > a and c > b:
    print(str(c) + " is greater than " + str(a) + " and " + str(b))
    
elif a == b and a > c:
    print(str(a) + " is equal to " + str(b) + " and greater than " + str(c))
    
elif a == c and a > b:
    print(str(a) + " is equal to " + str(c) + " and greater than " + str(b))
    
elif b == c and b > a:
    print(str(b) + " is equal to " + str(c) + " and greater than " + str(a))
    
else:
    print(" They are all equal")