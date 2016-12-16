def pwer(x,y):
    if y:
        return x*pwer(x,y-1)
    else:
        return 1
print(pwer(2,3))
