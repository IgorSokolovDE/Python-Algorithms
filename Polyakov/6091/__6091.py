RE1=[0,3,3,3,1,3,2,3,2,1,4,5,4,5,2,3,3]
RE2=[0,1,4,2,7,2,1,2,3,2,3,4,3,4,3,2,4]
MinEn=10000000000000000000000000000000
KolP1=0
def F(n,k1,En):
    global MinEn
    global KolP1
    if n>16: return
    if n==16:
        if En<MinEn:
            MinEn=En
            KolP1=k1
        return
    else:
       F(n+1,k1+1,En+RE1[n])
       F(n*2,k1,En+RE2[n])
F(1,0,0)
print(KolP1)
        
    
