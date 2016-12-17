def ish(n,start,end):
    if start>end:
        return 1
    else:
        return ish(n,start+1,end-1) if n[start]==n[end] else 0
string = input('please enter the world: ')
length = len(string)-1
if ish(string,0,length):
    print('\"\%s\"是回文'% string)
else:
    print('\"%s\"不是回文'% string)
