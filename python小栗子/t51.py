def fab(n):
    if n<1:
        print('wrong number')
        return -1
    if n==1 or n ==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
result = fab(20)
if result!= -1:
    print('共有%d对小兔崽子'% result)
