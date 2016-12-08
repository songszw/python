def sxh():
    for each in range(100,1000):
        temp = each
        sun = 0
        while temp:
            sun = sun + (temp%10) ** 3
            temp=temp//10
        if sun==each:
            print(each,end='\t')

print('所有的水仙花数是：',end='')
sxh()

