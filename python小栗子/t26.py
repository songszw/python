def sum(x):
    result = 0
    for each in x:
        if (type(each)==int) or (type(each)==float):
            result+=each
        else:
            continue

    return result

print(sum([1,8,5,4,3,8,'f',4,'f']))
        
