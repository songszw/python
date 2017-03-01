def discount(oldprice,rate):
    finalprice = oldprice*rate
    return finalprice

oldprice = float(input('请输入原价：'))
rate = float(input('请输入折扣率:'))
print('折后价是：',discount(oldprice,rate))

