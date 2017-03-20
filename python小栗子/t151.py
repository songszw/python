class Ball:
    def ballName(self,name):
        self.name = name
    def clickBall(self):
        print('我叫%s,你好'% self.name)

a = Ball()
a.ballName('dami')
b = Ball()
b.ballName('xiaomi')
a.clickBall()
b.clickBall()