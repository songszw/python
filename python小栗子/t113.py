try:
    int('abc')
    sum = 1+'1'
    f = open('F://iurioewrio.txt')
    print(f.read())
    f.close()
except (OSError,TypeError,ValueError) as reason:
    print('出错啦，错误原因是:'+str(reason))
