#汉诺塔游戏
def hanoi(num,x,y,z):
    if num==1:
        print(x,"-->",z)
    else:
        hanoi(num-1,x,z,y)
        print(x,'-->',z)
        hanoi(num-1,y,x,z)
num = int(input('请输入汉诺塔的层数：'))
hanoi(num,'x','y','z')
        
