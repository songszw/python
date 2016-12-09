def discounts(price,rate):
    finalprice = price*rate
    oldprice = 10
    print('修改后的原价是：',oldprice)
    return finalprice
oldprice = float(input('请输入原价:'))
rate = float(input('请输入折扣率：'))
print('修改后的原价是：',oldprice)
newprice = discounts(oldprice,rate)
print('折后价格是',newprice)
