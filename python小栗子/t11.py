import random
times = 3
secret = random.randint(1,10)
print(secret)
guess = 0
print('guess what number you want')
while (guess!=secret) and (times>0):
    temp = input()
    guess = int(temp)
    times -=1
    if guess == secret:
        print('bingo')
        break
    else:
        if guess > secret:
            print('bigger')
            
        else:
             print('smiller')
            
print('game over')

