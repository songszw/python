import random
val = random.randint(1,10)
num=3
while num > 0:
    num -= 1
    temp = input('please enter any number:')
    number = int(temp)
    if number == val :
        print('wahoo, got it')
        num=0
        break
    else :
        if number > val :
            print('your number is bigger than mine')
        else :
            
            print ('your number is smiller than mine')

print('game over')
        
