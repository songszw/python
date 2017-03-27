class Ball:
    def __init__(self,name):
        self.name = name
    def say(self):
        print('你好，世界，我是%s'%self.name)

a = Ball('songzhiwen')
a.say()
