name = input('请输入待查找的用户名：')
score = [["迷途",85],["黑夜",80],["小布丁",65],["福禄娃哇",95],["依婧",90]]
onoff = False

for each in score:
    if name in each[0]:
        print(name+'的的分是：',each[1])
        onoff = True
        break

if onoff == False:
    print('查找的数据不存在！')
