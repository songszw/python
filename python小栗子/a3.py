class Turtle:
    def __init__(self,x):
        self.num = x
class Fish:
    def __init__(self,x):
        self.num = x

class pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('池子里共有乌龟%d只，鱼%d条'%(self.turtle.num,self.fish.num))

a = pool(10,9)
a.print_num()