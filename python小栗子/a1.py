class Turtle:
    color = 'green'
    weight = '10'
    legs = 4
    mouth = '大嘴'
    def climb(self):
        print('我要一直往前爬...')
    def swime(self):
        print('我能游得很快')
    def eat(self):
        print('我要吃肉')
a = Turtle()
a.climb()
print(a.color)


