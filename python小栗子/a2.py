class Ball:
    def setName(self,name):
        self.name = name
    def world(self):
        print('我叫%s，谁不爽？'% self.name)

a = Ball()
a.setName('小土豆')
b = Ball()
b.setName('小乃求')
c = Ball()
c.setName('death')
a.world()
b.world()
c.world()