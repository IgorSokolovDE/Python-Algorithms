def F(n):
    global kPr
    if n>16:
        return
    if n==16:
        kPr+=1
    else:
        F(n+2)
        F(n+3)
        x=n
        n4=''
        while x>0:
            n4=str(x%4)+n4
            x//=4
        n4=n4+'0'
        F(int(n4,4))
kPr=0
F(1)
print(kPr)
