def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

number = int(input('please type a number: '))
result  = factorial(number)
print("%d 的阶乘是 %d" % (number,result))
