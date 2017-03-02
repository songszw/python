import random
num = random.randint(1,10)
temp = input('please type your number:')
guess = int(temp)
while num!=guess:
    temp = input('wrong number, try it again:')
    guess = int(temp)
    if guess==num:
        print('Wow,bingo')
    else:
        if guess>num:
            print('bigger than what i want')
        else:
            print('smiller than what i want')
print('Game over')