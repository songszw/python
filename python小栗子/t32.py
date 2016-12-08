def sxhs():
    for each in range(100,1000):
        number = each
        num = 0
        while number:
            num = num + (number%10)**3
            number = number//10

        if num == each:
            print(each,end = '\t')
print('所有的水仙花数是：',end='')
sxhs()
