def make_repeat(n):
        return lambda s : s * n

double = make_repeat(2)
print(double(4))
print(double('FishC'))
