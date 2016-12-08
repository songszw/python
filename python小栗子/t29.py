def newbin(num):
    text = []
    result = ''
    while num:
        quo = num%2
        num = num//2
        text.append(quo)
    while text:
        result+=str(text.pop())
    return result
print(newbin(10))
