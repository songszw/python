def hannuota(n,x,y,z):
    if n ==1:
        print(x,'-->',z)
    else:
        hannuota(n-1,x,z,y)
        print(x,'-->',z)
        hannuota(n-1,y,x,z)
n = int(input('please type a number:'))
hannuota(n,"X","Y","Z")
