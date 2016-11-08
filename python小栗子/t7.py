def funn(n):
    if n<1:
        print ('wrong number')
        return -1
    if n==1 or n ==2:
        return 1
    else:
        return funn(n-1)+funn(n-2)

sum = int(input('please enter a number:'))
print(funn(sum))
