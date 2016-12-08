def getsum(*arg,base=3):
    result=0
    for i in arg:
        result+=i
    result*=base
    print('结果是:',result)
getsum(1,2,3,4,5,base=5)
