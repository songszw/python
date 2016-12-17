def newbin(num):
    result = ''
    if num:
        result = newbin(num//2)
        return result+str(num%2)
    else:
        return result

print(newbin(10))
