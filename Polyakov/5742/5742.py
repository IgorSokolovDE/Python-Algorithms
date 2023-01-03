#def F(n,m):
#    if m>n: return 0
#    else:
#        if n%m==0:
#            return 1+F(n,m+1)
#        else:
#            return F(n,m+1)
#print(F(107864,3))        
m=3
n=107864
F=0
while m<=n:
    if n%m==0:
        F+=1
    m+=1
print(F)    
