def gcd(x,y):
    if y:
        return gcd(y,x%y)
    else:
        return x
print(gcd(4,6))
