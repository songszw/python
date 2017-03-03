answer = 'Hello,world'
world = input('please type the world:')
while True:
    if answer == world:
        break
    print('wrong world')
    world = input('please type the world again:')
print('bingo')
print(answer)
