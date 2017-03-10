import random
secret = random.randint(1,10)

try:
    temp = input('请输入一个数字：')
    num = int(temp)
except (ValueError,EOFError):

    print('那是啥玩意，我特么要一个数字')
    num = secret

while num!=secret:
    if secret == num:
        print('哦哟哟哟哟，猜对啦')
    else:
        if secret>num:
            print('哦哟哟哟哟，小了')
        else:
            print('哦哟哟哟哟，大了')

    try:
        temp = input('猜错啦，重新猜一下：')
        num = int(temp)
    except (ValueError, EOFError):
        print('那是啥玩意，我特么要一个数字')
        num = secret


print('Game over')