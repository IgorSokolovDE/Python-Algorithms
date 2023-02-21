def f(n,kUmn):
    global kPr 
    if n>11: return
    if n==11:
        if kUmn==1:
            kPr+=1
        return
    else:
        f(n+1,kUmn)
        f(n+2,kUmn)
        f(n*2,kUmn+1)
        f(n*3,kUmn+1)
kPr=0
f(1,0)
print(kPr)
