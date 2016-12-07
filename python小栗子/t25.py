def min(x):
    last = x[0]
    for each in x:
        if last>each:
            last=each

    return last

print(min('215646616808748465'))
