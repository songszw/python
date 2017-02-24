text = input('Guess which number i want to say:')
guess = int(text)


while guess != 8:
    print('wrong number')
    if guess > 8:
        print('Your number is bigger than mine')
    else:
        print('Your number is smaller than mine')
    print('Please try it again')
    text = input('Guess which number i want to say:')
    guess = int(text)
print('bingo')
print('Game over')