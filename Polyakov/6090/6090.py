a=[0,3,3,3,1,3,2,3,2,1,4,5,4,5,2,3,3]
b=[0,1,2,1,2,3,2,1,2,3,2,3,2,1,1,3,1]
c=[0,1,4,2,2,2,1,2,3,2,3,4,3,4,3,2,4]
MinE=1000000000000000000000000000000
def F(n,En):
    global MinE
    if n>16: return
    if n==16:
        MinE=min(MinE,En)
        return
    else:
        F(n+1,En+a[n])
        F(n+2,En+b[n])
        F(n*2,En+c[n])
F(1,0)
print(MinE)
        
