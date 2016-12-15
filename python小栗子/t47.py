def fun(x,y):
    if y:
        return x*fun(x,y-1)
    else:
        return 1
print(fun(2,3))
