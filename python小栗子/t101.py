def digui(i):
    if i == 1:
        return 1
    else:
        return i * digui(i-1)

number = int(input('please type a number:'))
result = digui(number)
print('%d 的阶乘是 %d',(number,result))