def test(**canshu):
    print('有%d个参数：'% len(canshu))
    print('分别是',canshu)

test(a=1,b=2,c=3,d=4)
a = {'a':'110','b':'120','c':'130'}
test(**a)



