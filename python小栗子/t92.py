guess=0
while guess!=8:
    temp = input('please type a number:')
    guess = int(temp)

    if guess == 8:
        print('Bingo')
    else:
        if guess >8:
            print('bigger than mine')
        else:
            print('smiller than mine')