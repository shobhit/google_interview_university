def euc(a,b):
    if b==0:
        return a
    else:
       return euc(b,a%b)

print euc(0,1)