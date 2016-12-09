def counting(*worlds):
    length = len(worlds)
    for i in range(length):
        letters = 0
        spaces = 0
        digit = 0
        others= 0
        for each in worlds[i]:
            if each.isalpha():
                letters+=1
            elif each.isdigit():
                digit+=1
            elif each == ' ':
                spaces+=1
            else:
                others+=1
        print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，标点符号 %d 个'% (i+1, letters, digit, spaces, others))
counting('i love, lily and i want to make money','i think i need a reast for a weail')
