def showSuShu(num):
    count = num//2
    while count>1:
        if num % count == 0:
            print('%d的最大公约数是%d'%(num,count))
            break
    else:
        print('%d是素数'% num)
anum = int(input('请输入一个数字：'))
showSuShu(anum)