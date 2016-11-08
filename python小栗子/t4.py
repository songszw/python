def funn(n):
    if n==1:
        return 1
    else:
        return n*funn(n-1)
number = int(input('please enter a number:'))
sum = funn(number)
print("%d 的阶乘是：%d" % (number,sum))
