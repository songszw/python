def endprice(price,rate):
    finail_price=price*rate
    return finail_price

old_price = float(input('请输入单价：'))
rate_price = float(input('请输入折扣率：'))
new_price = endprice(old_price,rate_price)
print('折后价是：',new_price)
