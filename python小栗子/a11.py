import time as t
class Timer():
    #reseting
    def __init__(self):
        self.unit = ['年','月','日','时','分','秒']
        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0
        self.end = 0

    #let the times be the end of the function
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    #add
    def add(self,other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt+=(str(result[index])+str(self.unit[index]))
        return prompt

    #start
    def start(self):
        self.begin = t.localtime()
        print('开始计时')
    #stop
    def stop(self):
        if not self.begin:
            print('请先调用start（）')
        else:
            self.end = t.localtime()
            print('停止计时')
            self._calc()
    #get times
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt+=(str(self.lasted[index])+str(self.unit[index]))

