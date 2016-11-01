a = '8'
answer = input('please enter a number:')

while True:
    if answer > a:
        print('bigger')
        print('wrong, try it again')
        answer = input('please enter a number:')
    elif answer < a :
        print('small')
        print('wrong, try it again')
        answer = input('please enter a number:')
    elif answer == a :
        print('bingo')
        break
        
       
    
