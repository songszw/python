def funnum(n):
    sum = n
    for i in range(1,n):
        sum *=i
    return sum

number = int(input('please enter a number:'))
lala = funnum(number)
print('%d 的阶乘是 %d' %(number,lala))
